# PRINTING-TRACKER
A modular Python CLI tool to track and calculate campus printing &amp; stationery expenses using JSON persistence.
# Smart Campus Stationery & Printing Tracker (PrintHub CLI)

A modular, object-oriented Command Line Interface (CLI) application built in Python to record, calculate, and log printing services and stationery expenses in campus environments.

## Features
- **Rate Catalog Management:** Read, view, and dynamically update printing and stationery rates persisted locally via JSON storage.
- **Interactive Order Tracker:** Log multiple order items, convert custom entries on-the-fly, and enforce numerical input validation.
- **Dynamic Receipt Engine:** Auto-compute item subtotals, grand total bill amount, and print structured ASCII receipts.
- **Automated Unit Tests:** Built-in test suite using Python's standard `unittest` library.

## Project Structure
```text
printhub-tracker/
│
├── data/
│   └── catalog.json
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── catalog_manager.py
│   └── tracker.py
├── tests/
│   ├── __init__.py
│   └── test_tracker.py
├── main.py
├── README.md
└── statement.md
