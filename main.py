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

def turning_letter_dictionaries_to_lists(mydictionary):
    try:
        dictioanries_list = []
        for key in mydictionary:
            if key.isalpha() == True:
                temp_dictionary = {}
                temp_dictionary[key] = mydictionary[key]
                dictioanries_list.append(temp_dictionary)
        return dictioanries_list
    except Exception:
        error = "Not a dicionary"
        return error

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        character_list = turning_letter_dictionaries_to_lists(count_characters(file_contents))
        print(character_list)
if __name__ == "__main__":
    main()