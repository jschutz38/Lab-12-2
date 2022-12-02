#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
#imports a new module called string and allows us to split strings later
# open the text file:
f = open('relativity.txt')
# read the file and create a list of words (google split function in python):
# Split Function: it splits a string into a list
# line 6 opens the text file
words = f.read().split()
f.close()
# Line 10 goes through the text file that we opened and reads through it and splits it into a list
# line 11 closes the open file
# calculate how many time each word is repeated (using dictionary):
word_counts = {}
# this line creates an empty dictionary
for word in words:
# This line loops over every word in the relativity text file which we split into a list above
    word_counts[word] = word_counts.get(word, 0) + 1
# This line creates a key in our new dictionary and assigns a value to it or changes the value of an already existing key in the dictionary
# The right part of the assignment statement (line 19) with the get function works as follows: If the word we are on in the for loop is already a key, the function will get the value of that word in the dictionary and add 1 to the value. If the word is not a key in the dictionary already, the default, which is 0, will be the value of that given key.
# create a list of all words:
word_list = list(word_counts.keys())
# line 23 creates a list of all of our keys in word_counts
# sort the list of all words based on how many times they are repeated:
def dict_val(x):
# line 26 creates a function called dict_val which has parameter x
    return word_counts[x]
# line 28 returns the values of the keys in the dictionary word_counts
word_list.sort(key = dict_val, reverse = True)
# .sort sorts a list in a certain way we tell it to
# line 30 takes our list of keys and puts them in descending order based on their values because of line 28
# print the top 10 most frequently used words:
print("List of top 10 most frequently used words: ")
# line 33 prints this string
print(word_list[ : 10])
# line 35 prints the first 10 words in our new sorted list because the index tells it to print the first 10 words
###this doesn't provide much information about the text because all of these are stop words


###second attempt###
#contents = open('relativity.txt').read()
#translation_table = {ord(ch) : None  for ch in string.punctuation}
#contents = contents.translate(translation_table)
#words = contents.split()

# create a list of all words in lower case:
lowercase_words = [word.lower() for word in words]
# line 48 is looping through all the words in the list and putting all of the words in word into lowercase
# .lower returns a string in all lower case
# open the file containing all of the stop words in English language:
f = open('stopWords.txt')
# line 52 opens the text file called stopWords.txt
# read the file create the list of all stop words in English language:
stop_words = f.read().split()
# line 55 says to read f and split the string into a list

###remove stop words###
# create the list of non stop words by filtering out the stop words:
non_stop_words = [word for word in lowercase_words if word not in stop_words]
# line 60 checks all of the words in the lowercase_words and if the word is not in the list stop_ words, then...
# now calculate the frequency of the non stop words:
word_counts = {}
# this creates an empty dictionary
# then... we take the words from line 60 and add them to this new dictionary called word_counts
for word in non_stop_words:
#loops through words in non_stop_words
    word_counts[word] = word_counts.get(word, 0) + 1
# This line creates a key in our new dictionary word_counts and assigns a value to it or changes the value of an already existing key in the dictionary
# The right part of the assignment statement with the get function works as follows: If the word we are on in the for loop is already a key, the function will get the value of that word in the dictionary and add 1 to the value. If the word is not a key in the dictionary already, the default, which is 0, will be the value of that given key.
word_list = list(word_counts.keys())
# line 71 creates a list with all of the keys in word_counts
# sort the words again:
word_list.sort(key = dict_val, reverse = True)
# line 74 puts the keys with the highest frequencies (values) in descending order starting with the keys with the highest frequencies
# prin the top 10 most frequently used words:
print("\nList of top 10 most frequently used non stop words: ")
print(word_list[ : 10])
# line 77 prints the string
# line 78 prints the first 10 words in our new sorted list that is in descending order based on highest to lowest frequency
