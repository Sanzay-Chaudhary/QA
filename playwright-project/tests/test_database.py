from database.db_helper import Database

def test_database():
    db= Database()
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\nEmployees Table:")
    for row in rows:
        print(row)
        
    cursor.close()
    conn.close()
