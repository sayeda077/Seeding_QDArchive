# Seeding_QDArchive

- **Student:** Sayeda Fatema Tuj Zohura  
- **Student ID:** 23308310  
- **Project:** Applied Software Engineering Master's Project  
- **Supervisor:** Prof. Dr. Dirk Riehle  
- **University:** Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)

## Project Overview

This project implements a data acquisition pipeline for collecting and organizing **Qualitative Data Analysis (QDA)** datasets from multiple research repositories.

The pipeline:

* Searches repositories for relevant datasets
* Extracts and stores metadata
* Downloads dataset files
* Organizes files into a structured folder system

It includes:

- **Multi-repository data acquisition** using APIs (DataverseNO) and manual collection (Murray Archive)  
- **Metadata extraction and storage** in a structured SQLite database  
- **SQLite database (23308310-seeding.db)** containing **100 projects and 25,655 files**  
- **Automated download pipeline** for retrieving dataset files from Dataverse repositories  
- **Manual dataset integration** for repositories without API support (Murray Archive)  
- **Organized folder structure** for efficient dataset storage and access  
- **Scalable pipeline design** for extending to additional repositories

## Repositories

| ID | Name            | URL |
|----|-----------------|-----|
| 1  | DataverseNO     | [https://dataverse.no](https://dataverse.no) |
| 2  | Murray Archive  | [https://www.murray.harvard.edu](https://www.murray.harvard.edu) |

---
## Pipeline Diagram

```
+---------------------+
|  User Input Query   |
|  (e.g., "maxqda")   |
+----------+----------+
           |
           v
+-----------------------------+
|   Dataverse API Search      |
|   (dataverse.no)            |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Metadata Extraction        |
|  (title, DOI, author, etc.)|
+-------------+---------------+
              |
              v
+-----------------------------+
|  Store in SQLite Database   |
|  (projects, files, etc.)    |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Download Dataset Files     |
|  (organized in folders)     |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Manual Input (Murray)      |
|  (metadata + files)         |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Final Structured Archive   |
|  (clean folder system)      |
+-----------------------------+
```

## Database Summary

| Repository     | Projects | Files     |
| -------------- | -------- | --------- |
| DataverseNO    | 95       | 25650     |
| Murray Archive | 5        | 5         |
| **Total**      | **100**  | **25655** |

---

The project uses an SQLite database to store all collected metadata in a structured format:

```
23308310-seeding.db
```

It contains:

* Projects metadata
* Files information
* Keywords
* Licenses
* Person roles

---

## Folder Structure

```
QDArchive/
├── main.py
├── 23308310-seeding.db
├── downloaded/
│   ├── dataverse_no/
│   │   ├── doi_.../
│   │   └── ...
│   └── murray_archive/
│       ├── Baltimore_Longitudinal_Study_...
│       └── ...
```

---

## Dataset Access

Due to large file size (~87GB), datasets are stored externally.

Access datasets here:
 **[(https://faubox.rrze.uni-erlangen.de/getlink/fiLyHzLbH2cKweyYLbvF7t/)]**

---

## How to Run

```bash
python main.py stats --db 23308310-seeding.db
```

---

## Technologies Used

* Python
* SQLite
* Dataverse API
* PowerShell (for file handling)

---



---


