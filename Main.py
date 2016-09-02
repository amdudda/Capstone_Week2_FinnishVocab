from CreateDB import *
from Vocabulary import *

'''
DATABASE SETUP BLOCK - IGNORE UNLESS YOU NEED TO MODIFY DATA.
'''
# create the database and its table
#CreateDB()
# insert records
#InsertVocabulary("vocab1.txt")
# and try printing them
#PrintAllRecords()

'''
FUNCTIONS USED BY MAIN MODULE
'''



'''
BODY OF CODE
'''
myWord = getVocabByID(99)
if myWord != None:
    print(myWord)