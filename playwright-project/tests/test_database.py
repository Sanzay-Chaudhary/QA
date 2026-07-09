from database.db_helper import Database

def test_database():
    db= Database()
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    print("total users:", result[0])
    cursor.close()
    conn.close()
