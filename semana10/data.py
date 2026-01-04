import csv
import os

File = "students.csv"

def export_to_csv(students):
    if not students:
        print('No students to export.')
        return
    try:
        with open(File, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)
        print('Students exported to CSV successfully.')
    except Exception as e:
        print(f'Error exporting to CSV: {e}')

def import_from_csv(students):
    if not os.path.exists(File):
        print('No CSV file found.')
        return
    try:
        with open(File, 'r') as f:
            reader = csv.DictReader(f)
            students.clear()
            for row in reader:
                row['spanish'] = float(row['spanish'])
                row['english'] = float(row['english'])
                row['social'] = float(row['social'])
                row['science'] = float(row['science'])
                row['average'] = float(row['average'])
                students.append(row)
        print('Students imported from CSV successfully.')

    except Exception as e:
        print(f'Error importing from CSV: {e}')