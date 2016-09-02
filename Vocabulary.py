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

    def __str__(self):
        return str(self.ID) + ", " + self.Finnish + ", " + self.English
# end class definition for Vocabulary

'''
MISC VOCABULARY-RELATED METHODS
'''

def getVocabByID(ID):
    try:
        # this returns a Vocabulary item based on the record ID in the database
        #queryString = ("SELECT ID, FINNISH, ENGLISH FROM VOCABULARY WHERE ID = ?", ID)
        conn = sqlite3.connect('FinnVocab.db')

        cursor = conn.execute("SELECT ID, FINNISH, ENGLISH FROM VOCABULARY WHERE ID = ?", str(ID))

        # there should be exactly one result returned
        record = cursor.fetchone()
        theID = record[0]
        theFinn = record[1]
        theEngl = record[2]
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