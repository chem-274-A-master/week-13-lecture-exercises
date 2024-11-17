"""
Write a command line script using argparse that takes in a file name and finds words in the file.

Modify __main__ to use argparse and to print the requested information.

To use your script, you should be able to go to the Shell tab on the right and type

python main.py FILENAME WORD

to get the number of times a word occurred. You can use the provided file file1.txt for testing.
Try using the word 'matter' as a test. The word 'matter' occurs 5 times in the file, and Matter once.
Note that you should still count the word even if it ends with punctuation (e.g. 'matter,' or 'matter.').

The test for this file counts words which are parts of other words 
(ex 'laws' will count for 'law', but "Law" would not count (case sensitive)). 
In real life, you would want to be more careful about word/character counting, 
but we aren't going that far into text processing.

Your script should have a help message and a description for each argument.
"""

if __name__ == "__main__":


  # This line is for testing. 
  print(f"The word {word} occurred {count} times in {filename}")