# PharmPuls – Automated Pharmacy Stock & Inventory Management

## Project Overview

PharmPuls is a Python-based pharmacy inventory monitoring system designed to help track pharmaceutical product quantities and identify items with low stock levels.

The application uses a command-line interface (CLI) to manage inventory information and stores data in a JSON file. It helps users monitor stock levels and detect products that need restocking.

## Features

- **Inventory Management:** Stores product names, quantities, stock thresholds, and categories.
- **JSON Data Persistence:** Saves inventory information in a JSON file.
- **Stock Monitoring:** Checks product quantities against their defined thresholds.
- **Critical Stock Alerts:** Identifies products whose quantities are below the specified threshold.
- **Command-Line Interface:** Allows users to check, update, and display inventory information through terminal commands.

## Technologies Used

- Python
- JSON
- Argparse
- Operating System (os) module

## Project Structure

```text
PharmPuls/
│
├── main.py
├── README.md
└── data/
    └── inventory.json
```

The `data/inventory.json` file is created automatically when the application runs if it does not already exist.

## Installation

1. Make sure Python is installed on your computer.
2. Clone the repository:

```bash
git clone https://github.com/sudesirinn/pharmpuls-.git
```

3. Navigate to the project directory:

```bash
cd pharmpuls-
```

## Usage

Run the application using Python.

### 1. Display Inventory Status

```bash
python main.py --status
```

Displays the current inventory information, including product names, quantities, thresholds, and categories.

### 2. Check Critical Stock

```bash
python main.py --check
```

Checks the inventory and displays a warning for products whose quantities are below their stock thresholds.

### 3. Update Product Quantity

```bash
python main.py --update "Parol" --qty 12
```

Updates the quantity of the specified product in the inventory file.

## Example Inventory

The application starts with an example product:

| Product | Quantity | Threshold | Category |
|---|---:|---:|---|
| Parol | 3 | 5 | Medication |

Since the quantity of Parol is below its threshold, the system identifies it as a critical stock item.

## How It Works

1. The user runs a command through the CLI.
2. The application processes the command-line arguments using `argparse`.
3. The inventory manager loads the stored data from the JSON file.
4. The stock monitor checks product quantities when requested.
5. Updated inventory information is saved to the JSON file.

## Project Objective

The main objective of PharmPuls is to provide a simple and practical solution for pharmacy stock monitoring. By identifying products with low quantities and maintaining inventory data, the application aims to support more organized inventory management and reduce the risk of stock shortages.

## Team Members

- Ayşe Sude Şirin
- Bilgesu Karakurum
- Arda Duman
- Arian Haidary
- Abderraouf Achour

---

**PharmPuls – Smarter Pharmacy Stock Monitoring.**
