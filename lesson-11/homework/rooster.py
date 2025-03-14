import sqlite3

with sqlite3.connect("roster.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)
    
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])
    
    cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
    
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    print(cursor.fetchall())
    
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])
    
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print(cursor.fetchall())