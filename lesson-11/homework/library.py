import sqlite3

with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)
    
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ])
    
    cursor.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))
    
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
    print(cursor.fetchall())
    
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ])
    
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print(cursor.fetchall())
