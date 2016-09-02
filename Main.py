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
    options = "1. Quiz: Finnish to English\n" + \
        "2. Quiz: English to Finnish\n" +  \
        "3. Add Vocabulary\n" +  \
        "4. Quit\n"
    print(options)
# end showmenu

def quizme():
    while True:
        showmenu()
        userinput = raw_input("> ")
        if userinput == OPTION_F2E:
            # quiz on Finnish recognition
            quizVocab("Finnish")
        elif userinput == OPTION_E2F:
            quizVocab("English")
        elif userinput == OPTION_ADD:
            print("not impelemented yet")
        elif userinput == OPTION_QUIT:
            print("Kiitos!")
            # exit the program
            exit()
            break   # just being cautious - no endless loops, please
        else:
            # tell the user they made an invalid choice and have them try again
            print("You have not made a valid selection. Please try again.")
    # end while loop
# End quizme

def quizVocab(language):
    # asks a player to type in the translation of a word
    # language tells the computer whether to display finnish words or english words as prompts.
    print(language + " vocab recognition not impelemented yet")
    # TODO pick a random vocabulary item and see if the user can give the correct answer.
    print(str(getLastID()))

'''
BODY OF CODE
'''
quizme()
# myWord = getVocabByID(5)
# if myWord != None:
#     print(myWord)