"""
Write a command line script using sys.argv in Python that takes in a file name and prints the number of words in the file.

First, modify the function num_words to return the number of words in a string based on whitespace.

Next, modify __main__ to use your function and to print the number of words in the file.

To use your script, you should be able to go to the Shell tab on the right and type

python main.py FILENAME

The test is for file1.txt, provided in this replit.
"""

def num_words(string):
  """Split a string into words using whitespace."""
  words = string.split()

if __name__ == "__main__":
  

  # This line is for testing. 
  print(f"The file has {num_words(text)} words.")