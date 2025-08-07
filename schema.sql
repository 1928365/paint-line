DROP TABLE IF EXISTS production_schedule;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS login_records;

CREATE TABLE production_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_order TEXT NOT NULL,
    model_name TEXT,
    part_name TEXT NOT NULL,
    customer TEXT,
    creation_date TEXT NOT NULL,
    material_arrival_date TEXT,
    request_date TEXT,
    painting_date TEXT,
    status TEXT NOT NULL DEFAULT '待排程',
    priority TEXT NOT NULL DEFAULT '中',
    notes TEXT,
    created_by_user_id INTEGER,
    FOREIGN KEY (created_by_user_id) REFERENCES users(id)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    is_admin INTEGER DEFAULT 0
);

CREATE TABLE login_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    login_time TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
