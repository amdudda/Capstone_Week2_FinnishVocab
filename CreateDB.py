# database setup code - use with caution!

import sqlite3

def CreateDB():
    # create the database and insert records into it.
    # connection string to tell it what database to connect to.  If DNE, it creates a new db.
    conn = sqlite3.connect('FinnVocab.db')

    print ("Opened database successfully");

    # this sends the create table string to the database so it can run it
    conn.execute('''CREATE TABLE VOCABULARY
    (ID INT PRIMARY KEY NOT NULL,
    FINNISH TEXT NOT NULL,
    ENGLISH TEXT NOT NULL);''')
    print("Table created successfully");

    # housekeeping: and don't forget to close our connection
    conn.close()
# end CreateDB

def InsertRecords(filename):
    # connection string to tell it what database to connect to.  If DNE, it creates a new db.
    conn = sqlite3.connect('FinnVocab.db')
    # takes a flat file and inserts records into the database
    fin = open(filename)

    for line in fin:
        vocab = line.split("\t")
        finn = vocab[0]
        eng = vocab[1]
        # We're going to let the database autoassign record id numbers
        conn.execute("INSERT INTO VOCABULARY (FINNISH,ENGLISH) \
          VALUES (?,?)", (finn,eng));

    # close the connection
    conn.close()
# end InsertRecords

def PrintAllRecords():
    # connection string to tell it what database to connect to.  If DNE, it creates a new db.
    conn = sqlite3.connect('FinnVocab.db')

    # set our cursor at the beginning of the result set.
    cursor = conn.execute("SELECT * FROM VOCABULARY")

    for row in cursor:
        print("ID = " + str(row[0]))
        print("FINNISH = " + row[1])
        print("ENGLISH = " + row[2])

    print("All records printed!")

    # close the connection
    conn.close()