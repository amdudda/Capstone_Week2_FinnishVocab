''' nb: this project requires python 3.x to handle utf-8 characters properly.'''
from CreateDB import *
from Vocabulary import *
import random

# some static values
OPTION_F2E = '1'
OPTION_E2F = '2'
OPTION_ADD = '3'
OPTION_QUIT = '4'
LANG_EN = "English"
LANG_FI = "Finnish"

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
        userinput = input("> ")
        if userinput == OPTION_F2E:
            # quiz on Finnish recognition
            quizVocab(LANG_FI)
        elif userinput == OPTION_E2F:
            quizVocab(LANG_EN)
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
    # pick a random vocabulary item and see if the user can give the correct answer.
    # TODO generate a random integer in the range 1..lastID once bug is fixed.
    vocabID = random.randint(1,9) # ,getLastID())
    # print out the selected item
    word = getVocabByID(vocabID)
    question = "What is '" + word.getVocab(language) + "' in " + language + "?"
    xlate = word.getTranslation(language)
    response = input(question)
    if (response == xlate):
        print("You are correct!")
    else:
        print("Sorry, the correct answer is " + xlate + ".")

'''
BODY OF CODE
'''
#PrintAllRecords()
# print(getVocabByID(9))
quizme()
