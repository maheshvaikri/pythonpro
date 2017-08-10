#!/usr/bin/env python3
"""WordLiterals is used to fetch words from the document from the URL and 
    Print it one line at a time.

 """

from urllib.request import urlopen

def fetch_words():
    """
    Fetch a list of words from a URL.abs

    Args: None

    Returns: List of words to from the Dcoument.
    """
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split() # This Splites the words and load to line of words.
            for word in line_words:
                story_words.append(word) # This appends each words into the story_words list
    return story_words

def print_items(items):
    """Print items one per line

    Args:
        Items are passed through the functions to print
    """
    for item in items:
        print(item) #prints each item from the items pass as the story words list from the fetch_words function.

def main():
    """Main Function calls the Fetch words function to fetch the words from the doc and populate it
       it into the items to print one line at a time.

       Args:
            None.  
    """
    items = fetch_words()
    print_items(items)

if __name__ == '__main__':
    main()
