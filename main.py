
import os


#word count function
def count_words(text):
    
    words = text.split()
    
    return len(words)

def main():
    #getting the book
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    
    #taking out jus the name from the path, has to include .txt?
    book_name = os.path.basename(book_path)

    #taking out the .txt
    book_name = os.path.splitext(book_name)[0]

    #counting the words
    word_count = count_words(text)
    
    print(f"--- Report of: {book_name} ---")
    print(f"{word_count} words found in the document")
    
    #counting the letters
    character_count = character_counter(text)
    
    sorted_character_count = convertdict_and_sort(character_count)

    for item in sorted_character_count:
        print(f"The '{item['character']}' character was found {item['num']} times")

    print("Job done B)")


#inputting book text
def get_book_text(path):
    with open(path) as f:
    
        return f.read()
    
#character counting function    
def character_counter(text):
    
    lower_text = text.lower()
    
    character_list = {}
    
    for character in lower_text:
        if character.isalpha():
            if character in character_list:
                character_list[character] += 1 
            else:
                character_list[character] = 1

    return character_list

#converting current dictionary into multiple, and then sorting all fo the individuals

def convertdict_and_sort(character_list):
    
    character_count_list = [{"character": char, "num": count} for char, count in character_list.items()]
    
    sorted_list = sorted(character_count_list, key=lambda x: x["num"], reverse=True)
    
    return sorted_list


main()