from CreateDB import *
from Vocabulary import *

# some static values
OPTION_F2E = '1'
OPTION_E2F = '2'
OPTION_ADD = '3'
OPTION_QUIT = '4'

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
def showmenu():
    options = "1. Test Finnish to English\n" + \
        "2. Test English to Finnish\n" +  \
        "3. Add Vocabulary\n" +  \
        "4. Quit\n"
    print(options)
# end showmenu

def quizme():
    while True:
        showmenu()
        userinput = raw_input("> ")
        if userinput == "1":
            print("not impelemented yet")
        elif userinput == "2":
            print("not impelemented yet")
        elif userinput == "3":
            print("not impelemented yet")
        elif userinput == "4":
            print("Kiitos!")
            # exit the program
            exit()
            break   # just being cautious - no endless loops, please
        else:
            # tell the user they made an invalid choice and have them try again
            print("You have not made a valid selection. Please try again.")
    # end while loop
# End quizme

'''
BODY OF CODE
'''
quizme()
# myWord = getVocabByID(5)
# if myWord != None:
#     print(myWord)