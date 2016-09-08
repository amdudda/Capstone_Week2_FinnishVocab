'''
Work with vocabulary
'''
import sqlite3, traceback

class Vocabulary():

    def __init__(self,ID,Finn,Engl):
        # instantiates a Vocabulary item
        self.ID = ID
        self.Finnish = Finn
        self.English = Engl

    # some getters and setters
    def getID(self):
        return self.ID

    def getFinnish(self):
        return self.Finnish

    def getEnglish(self):
        return self.English

    def getVocab(self,language):
        if language == "Finnish": return self.Finnish
        elif language == "English": return self.English
        else: return None

    def getTranslation(self,language):
        if language == "Finnish": return self.English
        elif language == "English": return self.Finnish
        else: return None

    def __str__(self):
        return str(self.ID) + ", " + self.Finnish + ", " + self.English
# end class definition for Vocabulary

'''
MISC VOCABULARY-RELATED METHODS

    # in a larger database with multiple tables, I'd move these into a Database object and maybe pass a variable to
    # getLastID() for the appropriate table name.
'''

def getVocabByID(ID):
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

def getLastID():
    # method to get the last ID number in the database so we can set a random range for pulling record IDs.
    lastID = 0
    try:
        conn = sqlite3.connect('FinnVocab.db')
        cursor = conn.execute("SELECT MAX(ID) FROM VOCABULARY;")
        lastID = cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("Unable to identify last record in db")
        traceback.print_exc()
    finally:
        # always close the connection when we're done with it.
        conn.close()

    return lastID