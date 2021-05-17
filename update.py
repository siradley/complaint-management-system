import sqlite3

#update table
def updateSqliteTable(id, firstname, lastname):
    try:
        sqliteConnection = sqlite3.connect('complaintDB.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update complainTable set firstname = ?, lastname = ? where id = ?"""
        data = (lastname, firstname, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(1, 'Jalil', 'Hamid')