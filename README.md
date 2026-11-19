# PyClean – CSV Data Cleaner

A beginner-friendly Python project that cleans, formats, and organizes messy CSV datasets.

## Overview

PyClean is a lightweight CSV cleaning tool built using Python's built-in `csv` library. It helps turn inconsistent customer records into cleaner, more organized data.

## Features

- Removes duplicate records based on email addresses
- Removes leading and trailing whitespace
- Standardizes names and cities using title case
- Converts email addresses to lowercase
- Detects rows containing missing values
- Exports cleaned data to a new CSV file
- Displays a summary of the cleaning process

**Note:** Missing values are detected and reported, but they are not automatically filled in.

## Project Structure

```text
PyClean-CSV-Data-Cleaner/
├── clean_csv.py
├── messy_customers.csv
├── cleaned_customers.csv
└── README.md
```

## How to Run

**1.** Download or clone this repository.

**2.** Make sure Python 3 is installed.

**3.** Open a terminal in the project folder.

**4.** Run:

```bash
python clean_csv.py
```

**5.** Open `cleaned_customers.csv` to view the results.

No additional Python packages are required.

## Example

### Before Cleaning

| Name | City | Email |
|---|---|---|
| john silva | colombo | JOHN@example.com |
| JOHN SILVA | COLOMBO | john@example.com |
| sara perera | kandy | SARA@example.com |

### After Cleaning

| Name | City | Email |
|---|---|---|
| John Silva | Colombo | john@example.com |
| Sara Perera | Kandy | sara@example.com |

The duplicate John Silva record is removed because both records use the same email address after standardization.

## Technologies Used

- Python 3
- Python CSV module
- Git and GitHub

## Limitations

- Designed for CSV files with `Name`, `City`, and `Email` columns.
- Duplicate detection uses email addresses.
- Rows with missing email addresses are preserved.
- Missing values are not automatically replaced.
- Original input data remains unchanged.

## About This Project

This project demonstrates practical Python programming, file handling, data cleaning, and basic automation skills.

It was developed as a portfolio project to demonstrate CSV data processing capabilities.
