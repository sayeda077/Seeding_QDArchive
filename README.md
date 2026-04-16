# Seeding_QDArchive

## Overview

This project implements a data acquisition pipeline for collecting and organizing **Qualitative Data Analysis (QDA)** datasets from multiple research repositories.

The pipeline:

* Searches repositories for relevant datasets
* Extracts and stores metadata
* Downloads dataset files
* Organizes files into a structured folder system

---

## Dataset Summary

| Repository     | Projects | Files     |
| -------------- | -------- | --------- |
| DataverseNO    | 95       | 25650     |
| Murray Archive | 5        | 5         |
| **Total**      | **100**  | **25655** |

---

## Database

The SQLite database used in this project:

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

## 📁 Folder Structure

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

## 🔗 Dataset Access

Due to large file size (~87GB), datasets are stored externally.

Access datasets here:
 **[(https://faubox.rrze.uni-erlangen.de/getlink/fiLyHzLbH2cKweyYLbvF7t/)]**

---

## ▶️ How to Run

```bash
python main.py stats --db 23308310-seeding.db
```

---

## 🛠️ Technologies Used

* Python
* SQLite
* Dataverse API
* PowerShell (for file handling)

---

## 📌 Notes

* Dataverse datasets were collected automatically using API queries
* Murray Archive datasets were added manually
* File counts are based on actual downloaded files in each repository

---


