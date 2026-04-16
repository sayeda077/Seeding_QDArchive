#!/usr/bin/env python3
"""
Seeding QDArchive - Part 1 Acquisition Pipeline

This script:
- creates the SQLite database using the 5-table schema
- searches DataverseNO using repository queries
- downloads all files from matching datasets
- stores metadata in SQLite
- supports manual project entry for Murray Archive

Folder structure created:
downloads/
  dataverse_no/
    <project_id>/
  murray_archive/
    <project_id>/

Database file:
<student_id>-seeding.db
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote
from requests.exceptions import RequestException, Timeout

import requests


# ----------------------------
# Configuration
# ----------------------------

DATAVERSE_NO_BASE = "https://dataverse.no"
DATAVERSE_NO_SEARCH_API = f"{DATAVERSE_NO_BASE}/api/search"
DATAVERSE_NO_DATASET_API = f"{DATAVERSE_NO_BASE}/api/datasets/:persistentId"

REPOSITORIES = {
    6: {
        "name": "dataverse_no",
        "url": "https://dataverse.no/",
        "download_method": "API",
    },
    18: {
        "name": "murray_archive",
        "url": "https://www.murray.harvard.edu/",
        "download_method": "MANUAL",
    },
}

DEFAULT_QUERIES = [
    "qdpx",
    "maxqda",
    "interview study",
]

SKIP_EXTENSIONS = {
    ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".m4v", ".webm",
    ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a",
}

QDA_EXTENSIONS = {
    ".qdpx",
    ".qdc",
    ".mx",
    ".mx24",
    ".mx22",
    ".mx20",
    ".nvp",
    ".nvpx",
    ".atlproj",
    ".hpr7",
    ".qda",
    ".rqda",
    ".qdp",
    ".qel",
    ".ppj",
    ".pprj",
    ".qlt",
    ".f4p",
}


# ----------------------------
# Data classes
# ----------------------------

@dataclass
class ProjectRecord:
    query_string: str
    repository_id: int
    repository_url: str
    project_url: str
    version: Optional[str]
    title: str
    description: Optional[str]
    language: Optional[str]
    doi: Optional[str]
    upload_date: Optional[str]
    download_date: str
    download_repository_folder: str
    download_project_folder: str
    download_version_folder: Optional[str]
    download_method: str


@dataclass
class FileRecord:
    project_id: int
    file_name: str
    file_type: str
    download_result: str


# ----------------------------
# Utility helpers
# ----------------------------

def now_timestamp() -> str:
    return datetime.now().isoformat(timespec="seconds")


def safe_filename(value: str, max_length: int = 150) -> str:
    value = value.strip().replace("/", "_").replace("\\", "_")
    value = re.sub(r"[^\w\-. ]+", "_", value)
    value = re.sub(r"\s+", "_", value)
    value = value[:max_length].strip("._")
    return value or "untitled"


def extension_of(filename: str) -> str:
    return Path(filename).suffix.lower().lstrip(".")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def request_json(url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


# ----------------------------
# Database layer
# ----------------------------

class MetadataDB:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.create_tables()

    def create_tables(self) -> None:
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query_string TEXT NOT NULL,
                repository_id INTEGER NOT NULL,
                repository_url TEXT NOT NULL,
                project_url TEXT NOT NULL UNIQUE,
                version TEXT,
                title TEXT NOT NULL,
                description TEXT,
                language TEXT,
                doi TEXT,
                upload_date TEXT,
                download_date TEXT NOT NULL,
                download_repository_folder TEXT NOT NULL,
                download_project_folder TEXT NOT NULL,
                download_version_folder TEXT,
                download_method TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                file_name TEXT NOT NULL,
                file_type TEXT NOT NULL,
                download_result TEXT NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS keywords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                keyword TEXT NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS person_role (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS licenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                license TEXT NOT NULL,
                FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
            );
        """)

        self.conn.commit()

    def project_exists(self, project_url: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM projects WHERE project_url = ?", (project_url,))
        return cursor.fetchone() is not None

    def insert_project(self, record: ProjectRecord) -> int:
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO projects (
                query_string, repository_id, repository_url, project_url, version,
                title, description, language, doi, upload_date, download_date,
                download_repository_folder, download_project_folder,
                download_version_folder, download_method
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record.query_string,
            record.repository_id,
            record.repository_url,
            record.project_url,
            record.version,
            record.title,
            record.description,
            record.language,
            record.doi,
            record.upload_date,
            record.download_date,
            record.download_repository_folder,
            record.download_project_folder,
            record.download_version_folder,
            record.download_method,
        ))
        self.conn.commit()
        return int(cursor.lastrowid)

    def insert_file(self, record: FileRecord) -> None:
        self.conn.execute("""
            INSERT INTO files (project_id, file_name, file_type, download_result)
            VALUES (?, ?, ?, ?)
        """, (
            record.project_id,
            record.file_name,
            record.file_type,
            record.download_result,
        ))
        self.conn.commit()

    def insert_keyword(self, project_id: int, keyword: str) -> None:
        if not keyword:
            return
        self.conn.execute("""
            INSERT INTO keywords (project_id, keyword)
            VALUES (?, ?)
        """, (project_id, keyword))
        self.conn.commit()

    def insert_person_role(self, project_id: int, name: str, role: str) -> None:
        if not name:
            return
        self.conn.execute("""
            INSERT INTO person_role (project_id, name, role)
            VALUES (?, ?, ?)
        """, (project_id, name, role))
        self.conn.commit()

    def insert_license(self, project_id: int, license_name: str) -> None:
        if not license_name:
            return
        self.conn.execute("""
            INSERT INTO licenses (project_id, license)
            VALUES (?, ?)
        """, (project_id, license_name))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()


# ----------------------------
# DataverseNO client
# ----------------------------

class DataverseNOClient:
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session or requests.Session()

    def search_datasets(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        params = {
            "q": query,
            "type": "dataset",
            "per_page": max_results,
        }
        response = self.session.get(DATAVERSE_NO_SEARCH_API, params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()
        return payload.get("data", {}).get("items", [])

    def get_dataset_metadata(self, persistent_id: str) -> Dict[str, Any]:
        params = {"persistentId": persistent_id}
        response = self.session.get(DATAVERSE_NO_DATASET_API, params=params, timeout=30)
        response.raise_for_status()
        return response.json().get("data", {})

    def extract_citation_fields(self, dataset_data: Dict[str, Any]) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "title": None,
            "description": None,
            "keywords": [],
            "authors": [],
            "license": None,
            "doi": None,
            "language": None,
            "upload_date": None,
            "version": None,
        }

        latest = dataset_data.get("latestVersion", {})
        out["version"] = str(latest.get("versionNumber")) if latest.get("versionNumber") is not None else None
        out["upload_date"] = latest.get("releaseTime") or dataset_data.get("publicationDate")

        if dataset_data.get("persistentUrl"):
            out["doi"] = dataset_data.get("persistentUrl")

        metadata_blocks = latest.get("metadataBlocks", {})
        citation = metadata_blocks.get("citation", {})
        fields = citation.get("fields", [])

        for field in fields:
            field_name = field.get("typeName")

            if field_name == "title":
                out["title"] = field.get("value")

            elif field_name == "dsDescription":
                values = field.get("value", [])
                descriptions = []
                for item in values:
                    subfields = item.get("dsDescriptionValue", {}).get("value", "")
                    if isinstance(subfields, str) and subfields.strip():
                        descriptions.append(subfields.strip())
                out["description"] = "\n".join(descriptions) if descriptions else None

            elif field_name == "keyword":
                for item in field.get("value", []):
                    kw = item.get("keywordValue", {}).get("value")
                    if kw:
                        out["keywords"].append(kw)

            elif field_name == "author":
                for item in field.get("value", []):
                    name = item.get("authorName", {}).get("value")
                    if name:
                        out["authors"].append(name)

            elif field_name == "language":
                value = field.get("value")
                if isinstance(value, str):
                    out["language"] = value
                elif isinstance(value, list) and value:
                    out["language"] = ", ".join(v for v in value if isinstance(v, str))

        license_info = latest.get("license", {})
        if isinstance(license_info, dict):
            out["license"] = license_info.get("name") or license_info.get("uri")

        if not out["title"]:
            out["title"] = dataset_data.get("latestVersion", {}).get("datasetPersistentId", "Untitled Dataset")

        return out

    def get_files_from_dataset(self, dataset_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        files: List[Dict[str, Any]] = []
        latest = dataset_data.get("latestVersion", {})
        for file_entry in latest.get("files", []):
            data_file = file_entry.get("dataFile", {})
            label = data_file.get("filename") or file_entry.get("label") or "unknown_file"
            file_id = data_file.get("id")
            files.append({
                "id": file_id,
                "filename": label,
                "download_url": f"{DATAVERSE_NO_BASE}/api/access/datafile/{file_id}" if file_id else None,
            })
        return files


# ----------------------------
# Download logic
# ----------------------------

def download_file(
    url: str,
    target_path: Path,
    retries: int = 3,
    max_total_seconds: int = 60,
    max_file_size_mb: int = 200,
) -> str:
    """
    Download one file with:
    - connect/read timeout
    - retry protection
    - total per-file time limit
    - optional max file size limit

    Returns one of:
    - SUCCEEDED
    - FAILED_SERVER
    - FAILED_TIMEOUT
    - FAILED_TOO_LARGE
    """
    max_bytes = max_file_size_mb * 1024 * 1024

    for attempt in range(1, retries + 1):
        start_time = time.time()
        bytes_written = 0

        try:
            with requests.get(url, stream=True, timeout=(10, 15)) as response:
                response.raise_for_status()

                content_length = response.headers.get("Content-Length")
                if content_length:
                    try:
                        if int(content_length) > max_bytes:
                            print(f"Skipping too-large file: {url}")
                            return "FAILED_TOO_LARGE"
                    except ValueError:
                        pass

                with open(target_path, "wb") as file_obj:
                    for chunk in response.iter_content(chunk_size=8192):
                        # hard total-time cutoff
                        if time.time() - start_time > max_total_seconds:
                            raise Timeout(f"Download exceeded {max_total_seconds} seconds")

                        if chunk:
                            file_obj.write(chunk)
                            bytes_written += len(chunk)

                            # hard size cutoff during stream
                            if bytes_written > max_bytes:
                                raise RequestException(
                                    f"File exceeded size limit of {max_file_size_mb} MB"
                                )

            return "SUCCEEDED"

        except Timeout:
            print(f"Timeout while downloading {url} (attempt {attempt}/{retries})")
            if target_path.exists():
                target_path.unlink(missing_ok=True)
            if attempt == retries:
                return "FAILED_TIMEOUT"
            time.sleep(2)

        except RequestException as exc:
            print(f"Server error while downloading {url} (attempt {attempt}/{retries}): {exc}")
            if target_path.exists():
                target_path.unlink(missing_ok=True)

            # if size limit triggered, mark as too large
            if "size limit" in str(exc).lower():
                return "FAILED_TOO_LARGE"

            if attempt == retries:
                return "FAILED_SERVER"
            time.sleep(2)

        except OSError as exc:
            print(f"File write error for {target_path}: {exc}")
            if target_path.exists():
                target_path.unlink(missing_ok=True)
            return "FAILED_SERVER"

    return "FAILED_SERVER"
    


# ----------------------------
# Pipeline commands
# ----------------------------

def cmd_init_db(args: argparse.Namespace) -> None:
    db = MetadataDB(Path(args.db))
    db.close()
    print(f"Database created: {args.db}")


def cmd_search_dataverse(args: argparse.Namespace) -> None:
    db = MetadataDB(Path(args.db))
    client = DataverseNOClient()

    repo = REPOSITORIES[6]
    queries = [args.query] if args.query else DEFAULT_QUERIES
    base_download_dir = Path(args.download_root) / repo["name"]
    ensure_dir(base_download_dir)

    total_projects_added = 0
    total_files_added = 0

    for query in queries:
        print(f"\nSearching DataverseNO for query: {query}")
        try:
            search_results = client.search_datasets(query=query, max_results=args.max_results)
        except Exception as exc:
            print(f"Search failed for query '{query}': {exc}")
            continue

        print(f"Found {len(search_results)} dataset(s)")

        for item in search_results:
            persistent_id = item.get("global_id")
            project_url = item.get("url") or item.get("persistentUrl")

            if not persistent_id or not project_url:
                continue

            if not project_url.startswith("http"):
                project_url = DATAVERSE_NO_BASE + project_url

            if db.project_exists(project_url):
                print(f"Skipping existing project: {project_url}")
                continue

            try:
                dataset_data = client.get_dataset_metadata(persistent_id)
                citation = client.extract_citation_fields(dataset_data)
                files = client.get_files_from_dataset(dataset_data)
            except Exception as exc:
                print(f"Failed to fetch dataset metadata for {persistent_id}: {exc}")
                continue

            project_folder_name = safe_filename(persistent_id.replace("/", "_").replace(":", "_"))
            project_dir = base_download_dir / project_folder_name
            ensure_dir(project_dir)

            project_record = ProjectRecord(
                query_string=query,
                repository_id=6,
                repository_url=repo["url"],
                project_url=project_url,
                version=citation.get("version"),
                title=citation.get("title") or "Untitled Dataset",
                description=citation.get("description"),
                language=citation.get("language"),
                doi=citation.get("doi"),
                upload_date=citation.get("upload_date"),
                download_date=now_timestamp(),
                download_repository_folder=repo["name"],
                download_project_folder=project_folder_name,
                download_version_folder=f"v{citation['version']}" if citation.get("version") else None,
                download_method=repo["download_method"],
            )

            project_id = db.insert_project(project_record)
            total_projects_added += 1

            for keyword in citation.get("keywords", []):
                db.insert_keyword(project_id, keyword)

            for author in citation.get("authors", []):
                db.insert_person_role(project_id, author, "AUTHOR")

            if citation.get("license"):
                db.insert_license(project_id, citation["license"])

            print(f"\nProject: {citation.get('title')}")

            for file_info in files:
                filename = safe_filename(file_info["filename"])
                ext = Path(filename).suffix.lower()

                if ext in SKIP_EXTENSIONS:
                   print(f"Skipping media: {filename}")
                   continue
                target_path = project_dir / filename

                if args.download and file_info.get("download_url"):
                   print(f"  Downloading: {filename}")
                   result = download_file(file_info["download_url"], target_path)
                else:
                   result = "SUCCEEDED" if file_info.get("download_url") else "FAILED_SERVER"

                db.insert_file(FileRecord(
                    project_id=project_id,
                    file_name=filename,
                    file_type=extension_of(filename),
                    download_result=result,
                ))
                total_files_added += 1

            print(f"Added project: {citation.get('title')}")

    db.close()
    print("\nDone.")
    print(f"Projects added: {total_projects_added}")
    print(f"Files recorded: {total_files_added}")


def cmd_add_murray_manual(args: argparse.Namespace) -> None:
    """
    Manual entry for Murray Archive.

    Example:
    python main.py add-murray \
      --db 12345-seeding.db \
      --title "Interview Study on ..." \
      --project-url "https://www.murray.harvard.edu/..." \
      --description "..." \
      --license "CC BY" \
      --author "John Doe" \
      --keyword "interview" \
      --keyword "qualitative" \
      --file "transcript1.pdf" \
      --file "notes.txt"
    """
    db = MetadataDB(Path(args.db))
    repo = REPOSITORIES[18]

    if db.project_exists(args.project_url):
        print("This Murray project already exists in the database.")
        db.close()
        return

    project_folder_name = safe_filename(args.local_folder or args.title)
    project_dir = Path(args.download_root) / repo["name"] / project_folder_name
    ensure_dir(project_dir)

    project_record = ProjectRecord(
        query_string=args.query_string or "",
        repository_id=18,
        repository_url=repo["url"],
        project_url=args.project_url,
        version=args.version,
        title=args.title,
        description=args.description,
        language=args.language,
        doi=args.doi,
        upload_date=args.upload_date,
        download_date=now_timestamp(),
        download_repository_folder=repo["name"],
        download_project_folder=project_folder_name,
        download_version_folder=args.version_folder,
        download_method=repo["download_method"],
    )

    project_id = db.insert_project(project_record)

    for keyword in args.keyword or []:
        db.insert_keyword(project_id, keyword)

    for author in args.author or []:
        db.insert_person_role(project_id, author, "AUTHOR")

    if args.uploader:
        db.insert_person_role(project_id, args.uploader, "UPLOADER")

    for license_name in args.license or []:
        db.insert_license(project_id, license_name)

    for file_name in args.file or []:
        clean_name = safe_filename(file_name)
        # This just records the file in DB.
        # You manually place the real file in the project folder.
        db.insert_file(FileRecord(
            project_id=project_id,
            file_name=clean_name,
            file_type=extension_of(clean_name),
            download_result="SUCCEEDED",
        ))

    db.close()
    print("Murray project added successfully.")
    print(f"Place the actual files inside: {project_dir}")


def cmd_stats(args: argparse.Namespace) -> None:
    conn = sqlite3.connect(args.db)
    cursor = conn.cursor()

    queries = {
        "projects": "SELECT COUNT(*) FROM projects",
        "files": "SELECT COUNT(*) FROM files",
        "keywords": "SELECT COUNT(*) FROM keywords",
        "person_role": "SELECT COUNT(*) FROM person_role",
        "licenses": "SELECT COUNT(*) FROM licenses",
    }

    print("Database statistics:")
    for label, query in queries.items():
        cursor.execute(query)
        count = cursor.fetchone()[0]
        print(f"- {label}: {count}")

    print("\nProjects by repository:")
    cursor.execute("""
        SELECT repository_id, COUNT(*)
        FROM projects
        GROUP BY repository_id
        ORDER BY repository_id
    """)
    for repository_id, count in cursor.fetchall():
        repo_name = REPOSITORIES.get(repository_id, {}).get("name", f"repo_{repository_id}")
        print(f"- {repo_name}: {count}")

    conn.close()


# ----------------------------
# CLI
# ----------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Seeding QDArchive - Part 1 pipeline"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init-db
    parser_init = subparsers.add_parser("init-db", help="Create the SQLite database")
    parser_init.add_argument("--db", required=True, help="Database file path, e.g. 12345-seeding.db")
    parser_init.set_defaults(func=cmd_init_db)

    # search-dataverse
    parser_search = subparsers.add_parser("search-dataverse", help="Search DataverseNO and record/download datasets")
    parser_search.add_argument("--db", required=True, help="Database file path")
    parser_search.add_argument("--query", help="Single query string; if omitted uses default queries")
    parser_search.add_argument("--max-results", type=int, default=10, help="Max datasets per query")
    parser_search.add_argument("--download", action="store_true", help="Download files immediately")
    parser_search.add_argument("--download-root", default="downloads", help="Root download folder")
    parser_search.set_defaults(func=cmd_search_dataverse)

    # add-murray
    parser_murray = subparsers.add_parser("add-murray", help="Manually add a Murray Archive project")
    parser_murray.add_argument("--db", required=True, help="Database file path")
    parser_murray.add_argument("--title", required=True, help="Project title")
    parser_murray.add_argument("--project-url", required=True, help="Full Murray project URL")
    parser_murray.add_argument("--description", help="Project description")
    parser_murray.add_argument("--language", help="Primary language, e.g. en-US")
    parser_murray.add_argument("--doi", help="DOI or DOI URL")
    parser_murray.add_argument("--upload-date", help="Upload date, e.g. 2026-03-01")
    parser_murray.add_argument("--version", help="Version string")
    parser_murray.add_argument("--version-folder", help="Version folder name")
    parser_murray.add_argument("--query-string", help="Search query that led to this project")
    parser_murray.add_argument("--local-folder", help="Local project folder name")
    parser_murray.add_argument("--download-root", default="downloads", help="Root download folder")
    parser_murray.add_argument("--license", action="append", help="License value; can be passed multiple times")
    parser_murray.add_argument("--author", action="append", help="Author name; can be passed multiple times")
    parser_murray.add_argument("--uploader", help="Uploader name")
    parser_murray.add_argument("--keyword", action="append", help="Keyword; can be passed multiple times")
    parser_murray.add_argument("--file", action="append", help="File name; can be passed multiple times")
    parser_murray.set_defaults(func=cmd_add_murray_manual)

    # stats
    parser_stats = subparsers.add_parser("stats", help="Show simple DB statistics")
    parser_stats.add_argument("--db", required=True, help="Database file path")
    parser_stats.set_defaults(func=cmd_stats)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()