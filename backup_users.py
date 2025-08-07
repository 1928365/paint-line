import sqlite3
import json
import os

DATABASE = 'applications.db'
BACKUP_DIR = 'backup'

def backup_data():
    if not os.path.exists(DATABASE):
        print(f"數據庫文件 '{DATABASE}' 不存在，無需備份。")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 備份 users 表
        cursor.execute("SELECT id, username, password, name, is_admin FROM users")
        users_data = [dict(row) for row in cursor.fetchall()]
        users_backup_path = os.path.join(BACKUP_DIR, 'users_backup.json')
        with open(users_backup_path, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, ensure_ascii=False, indent=4)
        print(f"用戶數據已備份到: {users_backup_path}")

        # 備份 login_records 表
        cursor.execute("SELECT id, user_id, username, ip_address, login_time FROM login_records")
        login_records_data = [dict(row) for row in cursor.fetchall()]
        login_records_backup_path = os.path.join(BACKUP_DIR, 'login_records_backup.json')
        with open(login_records_backup_path, 'w', encoding='utf-8') as f:
            json.dump(login_records_data, f, ensure_ascii=False, indent=4)
        print(f"登入記錄已備份到: {login_records_backup_path}")

    except sqlite3.Error as e:
        print(f"數據庫備份錯誤: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    backup_data()
