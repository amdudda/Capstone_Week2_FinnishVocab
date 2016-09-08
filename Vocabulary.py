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

