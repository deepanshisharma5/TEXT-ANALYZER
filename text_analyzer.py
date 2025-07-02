#project
#1. Project Idea: Text Analyzer 
#• Description: Create a program that takes a string input from the user and performs 
#various analyses such as counting the number of words, characters, and sentences. It 
#can also identify the most frequent words and display them. 
#• Features: 
#o Input a string. 
#o Count words, characters, sentences. 
#o Identify and display the most frequent words.

def text_analyzer():
    text = input("Enter a string:\n")
    
    words = text.split()
    words_count = len(words)
    
    characters_count = len(text)
    
    sentences = text.split('.')
    sentences_count = len(sentences) - sentences.count('')
    
    print(f"Number of words: {words_count}")
    print(f"Number of characters: {characters_count}")
    print(f"Number of sentences: {sentences_count}")

text_analyzer()
