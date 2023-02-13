# NLP-Examples
A set of NLP examples I created for CS 4395 - Human Language Technologies.

An [Overview of NLP](Overview_of_NLP.pdf) is available as a quick explanation of these NLP examples.

## Program 1
This program does basic text processing in Python. It will do the following:
1. Read a provided CSV file
2. Process the CSV file and adjust the formatting of each section as necessary
3. Save the file as a Pickle
4. Read the Pickle file and display the contents of the Pickle file

In order to run the program, run the following command in the directory:
> python main.py {csv_file}

In order to use the sample data provided, run the following command in the directory:
> python main.py data/data.csv

I think Python can be used effectively for text processing since it is readable. Certain functions such as "String.capitalize()" are built-in and used. Being able to use regex.match() to match Strings with regex is also extremely beneficial. The only weakness I can observe with Python is speed. If this were a CSV file with hundreds of millions of entries, a faster language may be preferred.

In this assignment, I learned how to read a CSV file in Python. I also learned some basic regex so that I could ensure that the Employee's ID and Phone Number matched the formatting needed. Finally, I learned about Pickle Files and how to effectively utilize Pickle Files.

I was able to review how to create Objects in Python and how to effectively utilize the Objects. I was also able to review how to read and write files in Python. I would like to improve in my code readability and organization. I feel like I could better organize my code so that it is easier to read.

The code is provided [here](/Program%201/)

## Program 2
This program does basic word processing utilizing NLTK. It begins by processing a text file, then proceeds to create a word guessing game from the 50 most common nouns from the text file. It will do the following:
1. Read the provided text file
2. Process the text file to create a list of the 50 most common nouns in the file
3. Play a game with the user where the user must guess the word

In order to run the program, run the following command in the directory:
> python main.py file.txt

In order to utilize the sample data provided, use:
> python main.py data/anat19.txt

In order to play the game, please input a 1 letter guess to the terminal. For example:
> e

is a valid guess for the letter "e"

The code is provided [here](/Program%202/)