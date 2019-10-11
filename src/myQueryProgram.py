#!/usr/bin/env python3
# date: 1 March 2019
# Christopher Cook

import sqlite3



# Modify this code to handle database support. For this, get the database code from class and add it to this file to connect to your database file. The below code is to help you keep track of how many attributes here are in each table. Remember, for an INSERT, you will need to know each piece of information for each attribute of a table.

# Connecting to Database
sqlite3Filename ="proteinDB.sqlite3"
#open my database connection
#conn = sqlite3.connect("proteinDB.sqlite3")
conn = sqlite3.connect(sqlite3Filename)
print(" My database has been loaded")

# use a dictionary to keep track of how many attributes there are per table.
tables_dict = {"park": 7,
"apop": 7,
"alz": 7,
"asthma": 7,
"celiac": 7,
"liver": 7,
"lupus": 7
}

def query1(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Park"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query2(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Apop"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query3(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Alz"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query4(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Asthma"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query5(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Celiac"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query6(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Liver"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def query7(): # function in python3
    """shows the tables of the database"""
    sqlCommand1 = "SELECT * FROM Lupus"
    print("My command is: ", sqlCommand1)
    # run my query
    result = conn.execute(sqlCommand1)
    print("  Result is:", result)
    # collect my results and parse them
    tables = result.fetchall()
    # print the content to the screen
    # print("  Raw tables data :", tables)
    for i in tables: # i is the index of the object ("list")
        print(" i=", i)
# end of query1()

def createTaskPark(conn, task):
    """Creating task"""
    sql='''insert into Park (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskApop(conn, task):
    """Creating task"""
    sql='''insert into Apop (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskAlz(conn, task):
    """Creating task"""
    sql='''insert into Alz (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskAsthma(conn, task):
    """Creating task"""
    sql='''insert into Asthma (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskCeliac(conn, task):
    """Creating task"""
    sql='''insert into Celiac (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskLiver(conn, task):
    """Creating task"""
    sql='''insert into Liver (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def createTaskLupus(conn, task):
    """Creating task"""
    sql='''insert into Lupus (protID, entryName, Status, ProteinName, GeneName, Organism, Length) values(?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

############################################################################################

def insert1():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskPark(conn, task1)
# end of insert1()

def insert2():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskApop(conn, task1)
# end of insert2()

def insert3():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskAlz(conn, task1)
# end of insert3()

def insert4():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskAsthma(conn, task1)
# end of insert3()

def insert5():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskCeliac(conn, task1)
# end of insert3()

def insert6():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskLiver(conn, task1)
# end of insert3()

def insert7():
    """Inserting function for Database"""
    protID = input("Enter protID value           :")
    entryName = input("Enter entryName value        :")
    Status = input("Enter Status value           :")
    ProteinName = input("Enter ProteinName value      :")
    GeneName = input("Enter GeneName value         :")
    Organsim = input("Enter Organism value         :")
    Length = input("Enter Length value           :")

    task1=(protId, entryName, Status, ProteinName, GeneName, Organism, Length)

    createTaskLupus(conn, task1)
# end of insert3()




#######################################################################################
def updateTask1(conn, task):
    """Updating task Park"""
    sql = ''' UPDATE Park
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask2(conn, task):
    """Updating task Apop"""
    sql = ''' UPDATE Apop
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask3(conn, task):
    """Updating task Alz"""
    sql = ''' UPDATE Alz
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask4(conn, task):
    """Updating task Asthma"""
    sql = ''' UPDATE Asthma
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask5(conn, task):
    """Updating task Celiac"""
    sql = ''' UPDATE Celiac
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask6(conn, task):
    """Updating task Liver"""
    sql = ''' UPDATE Liver
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

def updateTask7(conn, task):
    """Updating task Lupus"""
    sql = ''' UPDATE Lupus
              SET protID = ? ,
                  entryName = ? ,
                  Status = ?,
                  ProteinName = ?,
                  GeneName = ?,
                  Organism = ?,
                  Length = ?
              WHERE protID = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)

###############################################################################

def updateQuery1():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask1(conn, taskA)

def updateQuery2():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask2(conn, taskA)

def updateQuery3():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask3(conn, taskA)

def updateQuery4():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask4(conn, taskA)

def updateQuery5():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask5(conn, taskA)

def updateQuery6():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask6(conn, taskA)

def updateQuery7():
    """Updating function for Database"""
    protID = input("Enter protID value               :")
    entryName = input("Enter entryName value            :")
    Status = input("Enter Status value               :")
    ProteinName = input("Enter ProteinName value          :")
    GeneName = input("Enter GeneName value             :")
    Organism = input("Enter Organism value             :")
    Length = input("Enter Length value               :")
    chooseID = input("Enter protID you want to change  :")

    taskA=(protID, entryName, Status, ProteinName, GeneName, Organism, Length, chooseID)

    updateTask7(conn, taskA)

######################################################################################

# define a function to get user-in put for the name of the table
def getTableName():
    """Function to get the table name from the user"""
    prmpt = " Enter table name (park, apop, alz, asthma, celiac, liver, or lupus): "
    tableToEdit = input(prmpt) # enter input
    tableToEdit = tableToEdit.lower() # put text in to lower case
    while(tableToEdit not in tables_dict):
        print("The entered table does not exist in the dictionary. Please re-enter the name")
        tableToEdit = input(prmpt) # enter input
        tableToEdit = tableToEdit.lower() # put text in to lower case
    return tableToEdit
# end of getTableName()

def chooseAct():
    """Function to choose Insert or Update"""
    prmpt = " Enter insert, update, or show: "
    action = input(prmpt)
    action = action.lower()
    return action

# the program actually starts here. The dictionary and the function have already been read and are in memory.
print(" Welcome to Protein Database automation program!")

action1 = chooseAct()

if action1 == "insert":
    myTable_str = getTableName()
    print(" + Note: There are <", tables_dict[myTable_str],"> attributes associated with table <",myTable_str,">.")

    # Before insert function
    if myTable_str == "park":
        query1()
    elif myTable_str == "apop":
        query2()
    elif myTable_str == "alz":
        query3()
    elif myTable_str == "asthma":
        query4()
    elif myTable_str == "celiac":
        query5()
    elif myTable_str == "liver":
        query6()
    elif myTable_str == "lupus":
        query7()
    else:
        print("this did not work")

    #Calling insert function
    if myTable_str == "park":
        insert1()
    elif myTable_str == "apop":
        insert2()
    elif myTable_str == "alz":
        insert3()
    elif myTable_str == "asthma":
        insert4()
    elif myTable_str == "celiac":
        insert5()
    elif myTable_str == "liver":
        insert6()
    elif myTable_str == "lupus":
        insert7()
    else:
        print("this did not work")

    # After insert function
    if myTable_str == "park":
        query1()
    elif myTable_str == "apop":
        query2()
    elif myTable_str == "alz":
        query3()
    elif myTable_str == "asthma":
        query4()
    elif myTable_str == "celiac":
        query5()
    elif myTable_str == "liver":
        query6()
    elif myTable_str == "lupus":
        query7()
    else:
        print("this did not work")
    print("  -- End of program --")
elif action1 == "update":
    myTable_str = getTableName()
    print(" + Note: There are <", tables_dict[myTable_str],"> attributes associated with table <",myTable_str,">.")
    if myTable_str == "park":
        query1()
    elif myTable_str == "apop":
        query2()
    elif myTable_str == "alz":
        query3()
    elif myTable_str == "asthma":
        query3()
    elif myTable_str == "celiac":
        query3()
    elif myTable_str == "liver":
        query3()
    elif myTable_str == "lupus":
        query3()
    else:
        print("this did not work")

    #Calling update function
    if myTable_str == "park":
        updateQuery1()
    elif myTable_str == "apop":
        updateQuery2()
    elif myTable_str == "alz":
        updateQuery3()
    elif myTable_str == "asthma":
        updateQuery4()
    elif myTable_str == "celiac":
        updateQuery5()
    elif myTable_str == "liver":
        updateQuery6()
    elif myTable_str == "lupus":
        updateQuery7()
    else:
        print("this did not work")

    if myTable_str == "park":
        query1()
    elif myTable_str == "apop":
        query2()
    elif myTable_str == "alz":
        query3()
    elif myTable_str == "asthma":
        query4()
    elif myTable_str == "celiac":
        query5()
    elif myTable_str == "liver":
        query6()
    elif myTable_str == "lupus":
        query7()
    else:
        print("this did not work")
    print("  -- End of program --")
elif action1 == "show":
    myTable_str = getTableName()
    if myTable_str == "park":
        query1()
    elif myTable_str == "apop":
        query2()
    elif myTable_str == "alz":
        query3()
    elif myTable_str == "asthma":
        query4()
    elif myTable_str == "celiac":
        query5()
    elif myTable_str == "liver":
        query6()
    elif myTable_str == "lupus":
        query7()
    else:
        print("This did not work")
else:
    print("You did not type insert or update!")
