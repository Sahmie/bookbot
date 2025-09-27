from stats import count_words
from stats import num_chars
from stats import sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if(len(sys.argv) > 1):
        path = sys.argv[1]
        book_text = get_book_text(path)
        word_count = count_words(book_text)
        char_counts = num_chars(book_text)
        sorted_chars = sort_dict(char_counts)
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
    
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
    
        print("--------- Character Count -------")
        for char_data in sorted_chars:
            char = char_data["char"]
            count = char_data["num"]

            if char.isalpha():
                print(f"{char}: {count}")
    
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # book_text = get_book_text(path)
    # word_count = count_words(book_text)
    # char_counts = num_chars(book_text)
    # sorted_chars = sort_dict(char_counts)
    
    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {path}...")
    
    # print("----------- Word Count ----------")
    # print(f"Found {word_count} total words")
    
    # print("--------- Character Count -------")
    # for char_data in sorted_chars:
    #     char = char_data["char"]
    #     count = char_data["num"]

    #     if char.isalpha():
    #         print(f"{char}: {count}")
    
    # print("============= END ===============")

main()