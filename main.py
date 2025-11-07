# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
from problem_set1 import problem1
#call the function
problem1()
#an abstract representation of the function 
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
from advanced_slicing import advance_slice
advance_slice()
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
from extracting_info import extract_info
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
from manipulating_words import manipluate_word
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
from string_methods import string_method
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
from string_joiningandspliting import join_split
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.




info = "Python is fun. Fun is good. Good is subjective."
print(info.rfind('subjective'))
subjective_wrd = info[36:]
print(subjective_wrd)
every_third = info.split()[::3]
reversed_words = ' '.join(info.split()[::-1])

text = "MAY THE FORCE BE WITH YOU."
lower_text = text.lower()

motto = ["Make", "haste", "slowly."]
joined_motto = ' '.join(motto)
split_on_a = joined_motto.split('a')

sentence = "Life is what happens when you are busy making other plans."
replaced_busy = sentence.replace("busy", "distracted")
replaced_plans = sentence.replace("plans", "mistakes")

word = "Iteration"
repeated_word = word * 7

quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
has_moonlight = "moonlight" in quote2

phrase = "Supercalifragilisticexpialidocious"
num_chars = len(phrase)
count_i = phrase.count('i')

# refactoring means to restructure code without changing its external behavior
# this helps improve code readability and maintainablitlty 