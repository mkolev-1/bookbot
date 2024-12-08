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


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        test_count_words = "Project Gutenberg-tm eBooks are often"
        print(count_number_of_words(file_contents))
if __name__ == "__main__":
    main()