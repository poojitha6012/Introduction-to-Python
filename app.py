 import csv
import os
from datetime import datetime

FILE_NAME = "grievances.csv"

# Initialize CSV file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "GrievanceID", "Name", "RegNo", "Department",
                "Category", "Description", "Date", "Status"
            ])

# Generate Grievance ID

def generate_id():
    return "GRV" + datetime.now().strftime("%Y%m%d%H%M%S")

# Add Grievance
def add_grievance():
    name = input("Enter Student Name: ")
    reg = input("Enter Registration Number: ")
    dept = input("Enter Department: ")

    print("\nCategories: Academic / Exam / Hostel / Transport / Admin / Others")
    category = input("Enter Category: ")

    desc = input("Enter Grievance Description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gid = generate_id()
    status = "Submitted"

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([gid, name, reg, dept, category, desc, date, status])

    print(f"\n✅ Grievance Submitted Successfully! ID: {gid}")

# View All Grievances
def view_grievances():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Search Grievance
def search_grievance():
    gid = input("Enter Grievance ID to search: ")
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == gid:
                print("\n🔍 Grievance Found:")
                print(row)
                found = True
                break

    if not found:
        print("❌ Grievance not found!")


# Update Status

def update_status():
    gid = input("Enter Grievance ID to update: ")
    updated_rows = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == gid:
                print("Current Status:", row[7])
                new_status = input("Enter New Status: ")
                row[7] = new_status
                found = True
            updated_rows.append(row)

    if found:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("✅ Status Updated Successfully!")
    else:
        print("❌ Grievance ID not found!")

# MAIN MENU
def main():
    initialize_file()

    while True:
        print("\n===== SGRS MENU =====")
        print("1. Add Grievance")
        print("2. View All Grievances")
        print("3. Search Grievance")
        print("4. Update Status")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_grievance()
        elif choice == '2':
            view_grievances()
        elif choice == '3':
            search_grievance()
        elif choice == '4':
            update_status()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice! Try again.")
