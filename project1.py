"""
Name: Yousef Kharma
Date: 11/21/2024
Database Project

"""
# connect to database
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yousef123",
  database="menagerie"
)
mycursor = mydb.cursor()

# Code to show the databases on my system
def show_database():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


# mycursor.execute("DROP DATABASE IF EXISTS menagerie")

# Code to show the structure of the pet table
def structure_table():
    mycursor.execute("DESCRIBE pet")
    print("Structure of the pet table")
    table_structure = mycursor.fetchall()
    for x in table_structure:
        print(x)


# Code to show all the records from the pet table
def records_table():
    mycursor.execute("SELECT * FROM pet")
    print("Records of the pet table")
    table_records = mycursor.fetchall()
    for x in table_records:
        print(x)


# Code to show female dogs in pet table
def femaledog_table():
    sql = "SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Code to filter just the name and birth
def name_birth_columns():
    mycursor.execute("SELECT name, birth FROM pet")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Code to group owners and get the total of pets
def pets_per_owner():
    sql = "SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        owner = x[0]
        pet_count = x[1]
        print(f'Owner: {owner}, pet count: {pet_count}')

# Code to get name of the pets and their date of births and just the months of their births
def name_birth_month():
    sql = "SELECT name, birth, MONTH(birth) AS birth_month FROM pet"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("name            birth      birth_month")
    for x in myresult:
        name = x[0]
        birth = x[1]
        birth_month = x[2]
        print(f'{name:<10}    {birth}    {birth_month}')
