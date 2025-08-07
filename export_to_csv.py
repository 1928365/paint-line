
import sqlite3
import csv

DB_PATH = 'production_schedule.db'
CSV_PATH = 'production_schedule.csv'

def export_to_csv():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM production_schedule")
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)

    conn.close()
    print(f"Data exported to {CSV_PATH}")

if __name__ == '__main__':
    export_to_csv()
