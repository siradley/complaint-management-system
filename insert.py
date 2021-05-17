import sqlite3

#insert record
def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('complaintDB.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO complainTable
                          (id, firstname, lastname, address, gender, comment) 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into complainTable table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

recordsToInsert = [(4, 'david', 'beckham', 'Jalan Bobby, Ulu Klang', 'Female', 'Nak join liverpool tapi bapak tak bagi')]

insertMultipleRecords(recordsToInsert)