import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'production_schedule.db')

def add_column_to_db():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 檢查欄位是否已存在，避免重複添加導致錯誤
        cursor.execute("PRAGMA table_info(production_schedule)")
        columns = [col[1] for col in cursor.fetchall()]
        if 'created_by_user_id' not in columns:
            cursor.execute("ALTER TABLE production_schedule ADD COLUMN created_by_user_id INTEGER;")
            conn.commit()
            print("'created_by_user_id' 欄位已成功新增到 production_schedule 表。")
        else:
            print("'created_by_user_id' 欄位已存在，無需新增。")

    except sqlite3.Error as e:
        print(f"資料庫操作錯誤: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    add_column_to_db()