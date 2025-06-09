import sys
from stats import get_num_words, get_sorted_result

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        num_words = get_num_words(filepath)
        num_chars = get_sorted_result(filepath)

        print(f"============ BOOKBOT ============\n"
            f"Analyzing book found at {filepath}...\n"
            f"----------- Word Count ----------\n"
            f"Found {num_words} total words\n"
            f"--------- Character Count -------\n"
            f"{num_chars}\n"
            f"============= END ===============\n")
    
main()