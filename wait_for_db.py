import time
import MySQLdb
import os

while True:
    try:
        MySQLdb.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
        )
        print("✅ Database is ready!")
        break
    except MySQLdb.OperationalError:
        print("⏳ Waiting for database...")
        time.sleep(2)
