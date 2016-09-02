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
            finn = vocab[0]
            eng = vocab[1]
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