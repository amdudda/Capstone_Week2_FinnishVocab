from Database import *
from Vocabulary import *
import random
'''
nb: this project requires python 3.x to handle utf-8 characters properly.
'''

# some static values
OPTION_F2E = '1'
OPTION_E2F = '2'
OPTION_ADD = '3'
OPTION_QUIT = '4'
LANG_EN = "English"
LANG_FI = "Finnish"

'''
DATABASE SETUP BLOCK - IGNORE UNLESS YOU NEED TO SET UP THE DB OR MODIFY DATA.
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
            addVocab()
        elif userinput == OPTION_QUIT:
            print("Kiitos! (Thanks!)")
            # exit the program
            exit()
            break   # just being cautious - no endless loops, please
        else:
            # tell the user they made an invalid choice and have them try again
            print("You have not made a valid selection. Please try again.")
    # end while loop
# End quizme

def quizVocab(source_lang):
    # source_lang is the language the user will be presented with - target is what they have to translate it into
    target_lang = LANG_FI
    if source_lang == LANG_FI: target_lang = LANG_EN
    # wrap in a while loop until player says not to continue
    playagain = "y"
    while playagain != "n":
        # asks a player to type in the translation of a word
        # language tells the computer whether to display finnish words or english words as prompts.
        # pick a random vocabulary item and see if the user can give the correct answer.
        # generate a random integer in the range 1..lastID
        vocabID = random.randint(1,getLastID("VOCABULARY"))
        # print out the selected item
        word = getVocabByID(vocabID)
        question = "What is '" + word.getVocab(source_lang) + "' in " + target_lang + "?\n"
        xlate = word.getTranslation(source_lang)
        response = input(question).lower()  # let's be kind and not demand case sensitivity in responses
        if (response == xlate):
            print("You are correct!")
        else:
            print("Sorry, the correct answer is '" + xlate + "'.")
        playagain = input("Would you like to try another word?  Enter 'y' for yes or 'n' for no.\n").lower()
# end quizVocab

def addVocab():
    # we're going to store data in lowercase to maintain consistency
    suomi = input("What is the Finnish word you wish to add?\n").lower()
    englanti = input("What is the English translation for '" + suomi + "'?\n").lower()
    ok2insert = input("Are you sure you want to add '%s' as '%s' to the dictionary? Enter y for 'yes' or 'n' for no.\n"% (suomi,englanti))
    if ok2insert == 'y':
        AddVocab(suomi,englanti)
    else:
        print("You entered something other than 'y', so I did not add your information to the database.")
    # debugging
    #PrintAllRecords()
# end addVocab

'''
BODY OF CODE
'''
# PrintAllRecords()
# print(getVocabByID(12))
quizme()
