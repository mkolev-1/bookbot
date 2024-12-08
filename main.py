def count_number_of_words(mystring):
    try:
        words_list = mystring.split()
        count = 0
       
        for word in words_list:
            count += 1
        return count
    except Exception:
         error = "Not a string"
         return error

def count_characters(mystring):
    try:
        lowered_mystring = mystring.lower()
        character_dict = {}
        for character  in lowered_mystring:
            if character not in character_dict:
                character_dict[character] = 1
            else:
                character_dict[character] += 1
        return character_dict
    except Exception:
         error = "Not a string"
         return error

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        test_count_char = "Projectttt"
        print(count_characters(file_contents))
if __name__ == "__main__":
    main()