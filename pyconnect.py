import os
import mysql.connector
from dotenv import load_dotenv   

#Loading environment variables
load_dotenv()

#initiating Try BLOCK
try:
    mydb=mysql.connector.connect (
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        passwd=os.getenv("DB_PASSWD"),
        database=os.getenv("DB_DATABASE")
    )

    auto_Increment_Count = 5
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO cats (name,owner,birth) VALUES (%s,%s,%s)",("Putru","Nalayak","2015-01-03"))
    mycursor.execute("DELETE FROM cats where id=%s", (auto_Increment_Count,))
    mycursor.execute("ALTER TABLE cats AUTO_INCREMENT=%s",(auto_Increment_Count-1,))

    mydb.commit()

    mycursor.execute("Select * from cats")

    for x in mycursor:
        print(x)

#initiating exception BLOCK
except mysql.connector.Error as error:
    print("Query failed {}".format(error))

#initiating final closure BLOCK
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")

