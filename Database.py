# database setup code - use with caution!
# most of this is modelled on the practice exercise done in class.
import sqlite3, traceback
dev = True  # so we can print stacktrace in dev environment

def CreateDB():
    try:
        # create the database and insert records into it.
        # connection string to tell it what database to connect to.  If DNE, it creates a new db.
        conn = sqlite3.connect('FinnVocab.db')

        print ("Opened database successfully");

        # this sends the create table string to the database so it can run it
        # INTEGER PRIMARY KEY creates an alias for ROWID in sqlite3 and is analogous to an autoincrement field:
        # https://sqlite.org/autoinc.html
        conn.execute('''CREATE TABLE VOCABULARY
        (ID INTEGER PRIMARY KEY,
        FINNISH TEXT NOT NULL,
        ENGLISH TEXT NOT NULL);''')
        print("Table created successfully");
    except sqlite3.Error as e:
        # error handling
        print("Something went wrong trying to set up the database or its table")
        # display traceback - would not appear in production versions of this app
        if dev: traceback.print_exc()
        # and roll back changes
        conn.rollback()
    finally:
        # housekeeping: and don't forget to close our connection
        conn.close()
# end CreateDB

def InsertVocabulary(filename):
    try:
        # connection string to tell it what database to connect to.  If DNE, it creates a new db.
        conn = sqlite3.connect('FinnVocab.db')
        # Python does not send string data natively, have to tell it to do so explicitly -
        # see http://stackoverflow.com/questions/10268518/python-string-to-unicode
        conn.text_factory = str

        # takes a flat file and inserts records into the database
        fin = open(filename)

        for line in fin:
            vocab = line.split(",")
            finn = vocab[0].strip()
            eng = vocab[1].strip()
            # debugging: this works...
            # print(finn + ":" + eng)

            # We're going to let the database autoassign record id numbers
            result = conn.execute("INSERT INTO VOCABULARY (FINNISH,ENGLISH) \
              VALUES (?,?);", (finn,eng));

        conn.commit()

        print("records inserted from " + filename)

    except sqlite3.Error as e:
        # error handling
        print("Rolling back changes due to error")
        # display traceback - would not appear in production versions of this app
        if dev: traceback.print_exc()
        # and roll back changes
        conn.rollback()
    finally:
        # close the connection
        conn.close()
# end InsertRecords

def PrintAllRecords():
    try:
        # connection string to tell it what database to connect to.  If DNE, it creates a new db.
        conn = sqlite3.connect('FinnVocab.db')
        # conn.text_factory = str

        # set our cursor at the beginning of the result set.
        cursor = conn.execute("SELECT * FROM VOCABULARY;")

        # print out the records
        for row in cursor:
            print("ID = " + str(row[0]))
            print("FINNISH = " + row[1])
            print("ENGLISH = " + row[2])

        print("All records printed!")
    except sqlite3.Error as e:
        print("Unable to access or print the records in the Vocabulary table.")
        # print out the stack trace
        if dev: traceback.print_exc()
        # NB: no changes should have happened, but let's be paranoid and rollback just in case our code truly borks something.
        conn.rollback()
    finally:
        # close the connection
        conn.close()
# end PrintAllRecords

def AddVocab(s,e):
    # this lets users add new vocabulary to the database
    try:
        # connection string to tell it what database to connect to.  If DNE, it creates a new db.
        conn = sqlite3.connect('FinnVocab.db')
        # make absolutely sure it can handle unicode strings
        conn.text_factory = str

        # insert the record into the database
        conn.execute("INSERT INTO VOCABULARY (FINNISH, ENGLISH) VALUES(?,?);", (s,e))
        # don't forget to commit your changes!!!
        conn.commit()
        print("Successfully added '%s' to the dictionary as '%s'."% (s,e))
    except sqlite3.Error as e:
        # in case of error, notify user and roll back changes
        print("Unable to add %s, %s to dictionary."% (s,e))
        if dev: traceback.print_exc()
        conn.rollback()
    finally:
        # close the connection
        conn.close()
# end AddVocab

'''
MISC VOCABULARY-RELATED METHODS
'''

def getVocabByID(ID):
    from Vocabulary import Vocabulary
    try:
        #theData = ""
        # this returns a Vocabulary item based on the record ID in the database
        conn = sqlite3.connect('FinnVocab.db')

        num2use = str(ID)
        # debugging: print(num2use)
        # need to pass a tuple; if you pass a plain string, the query breaks on anything >=10
        # see http://stackoverflow.com/questions/4409539/pythonsqlite-the-like-query-with-wildcards#4409584
        # for where I found the answer (while working on team project & looking for something totally unrelated, of course! :D )
        cursor = conn.execute("SELECT ID, FINNISH, ENGLISH FROM VOCABULARY WHERE ID = ?;", (num2use,))

        # there should be exactly one result returned
        record = cursor.fetchone()
        theID = record[0]
        theFinn = record[1].strip()
        theEngl = record[2].strip()
        theData = Vocabulary(theID,theFinn,theEngl)
    except sqlite3.Error as e:
        print("Unable to retrieve record number " + str(ID) + ".")
        traceback.print_exc()
        # set theData to None so the program can fail gracefully.
        theData = None
    finally:
        # close the connection
        conn.close()
        return theData
# end getByID

def getLastID(table_name):
    # method to get the last ID number in the database so we can set a random range for pulling record IDs.
    lastID = 0
    try:
        conn = sqlite3.connect('FinnVocab.db')
        cursor = conn.execute("SELECT MAX(ID) FROM " + table_name + ";")
        lastID = cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("Unable to identify last record in db")
        traceback.print_exc()
    finally:
        # always close the connection when we're done with it.
        conn.close()

    return lastID
# end getLastID