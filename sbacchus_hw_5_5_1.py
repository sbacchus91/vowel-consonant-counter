"""
Shane Bacchus
Class: CS 521 - Fall 1
Date:10/10
Homework Problem # 1
Description of Problem (just a 1-2 line summary!):
Counts total number of vowels and consonants from English sentence
"""

def vc_counter(english_sentence):
    """Counts total number of vowels and consonants from English sentence"""
    print (vc_counter.__doc__)
    upper_sentence = english_sentence.upper() #  turns to Uppercase
    numbers = '1234567890' #  Removes numbers

    for x in upper_sentence:
        if x in numbers:
            upper_sentence = upper_sentence.replace(x, "")  
    
    vowels = 0
    consonants = 0

    for i in upper_sentence: #  Determines counts
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            vowels = vowels + 1
        else:
            consonants = consonants + 1
 
   
    count_dictionary = {"total_vowels": vowels, "total_consonants": consonants}
    return count_dictionary

if __name__ == "__main__":
    while True: #  Validation
        english_sentence = input("Enter an English sentence: ") 
        sentence_no_spaces = english_sentence.replace(" ", "")
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~''' #  Removes punctuation

        for x in sentence_no_spaces:  
            if x in punc:  
                sentence_no_spaces = sentence_no_spaces.replace(x, "") 

        if sentence_no_spaces.isdigit() == True: #  Checks if only numbers are entered
            print("Please enter a sentence, not a number")
            continue
        elif sentence_no_spaces.isalpha() == False: #  Checks if characters are entered
            print("Please enter a sentence, not just random characters or characters with numbers")
            continue
        elif len(sentence_no_spaces) < 2: #  Checks if input is too small
            print("Please enter a larger sentence (minimum of 2 characters)")
            continue
        else:
            break

    returned_dictionary = vc_counter(sentence_no_spaces)
    print("Total # of vowels in sentence: " + str(returned_dictionary.get('total_vowels')))
    print("Total # of consonants in sentence: " + str(returned_dictionary.get('total_consonants')))
    

    
    