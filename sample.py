Sample Data Script
Creates a small sample dataset and saves it to sample_data.csv.
Run with: python sample_data.py
"""

import csv
from pathlib import Path

DATA = [
    {"id": 1, "name": "Abebe", "age": 21, "department": "Computer Science"},
    {"id": 2, "name": "Sara", "age": 22, "department": "Information Systems"},
    {"id": 3, "name": "Miki", "age": 20, "department": "Software Engineering"},
    {"id": 4, "name": "Dawit", "age": 23, "department": "Computer Science"},
    {"id": 5, "name": "Liya", "age": 21, "department": "Data Science"},
]

def main():
    output_file = Path(__file__).with_name("sample_data.csv")
    fieldnames = ["id", "name", "age", "department"]

    with output_file.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(DATA)

    print(f"Created {output_file.name} with {len(DATA)} records.")

if __name__ == "__main__":
    main()
