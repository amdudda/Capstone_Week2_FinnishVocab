#Vocabulary Quizzer: Finnish/English

## Introduction

This project was inspired by my desire to attend WorldCon 75.  This will take place in Helsinki, Finland, in August of 2017.  I would like to have at least a minimal vocabulary for simple navigation, so I designed this application to help practice my vocabulary.

## Requirements

This code uses UTF-8 characters (those umlauts, natch).  Consequently, this code needs to be compiled with Python version 3.x to run properly.

## Features

Vocabulary terms will be stored in a simple database.  Initially it will consist of a single table holding a Finnish word and its English translation.  I'm going to ignore the possibility of homophones in Finnish, on the assumption that these are unlikely in beginner vocabulary.

I might eventually add a phrase dictionary to quiz myself on tourist phrases.

## Side Notes

Finnish is syntactically very different from English.  It features heavily suffixing agglutinative morphology and numerous case endings.  Prosody is also markedly different; almost all words have stress on the first syllable, and questions are identified lexically rather than through intonation.

This tutor does not cover grammar, prosody, or phonology.  It assumes you already know how to read and pronounce Finnish words, and you're on your own for figuring out how to construct syntactially valid statements.

## Future updates/fixes

* The database does not check whether new entries already exist.
* Store a difficulty rating, or assign textbook-style chapters to vocabulary items, so that users can set a difficulty rating for the words they are asked about.
* A table of useful tourist phrases users can practice.

## Credits
vocab1.txt is gleaned from http://sssscomic.com/comic.php?page=195
