import sys
from stats import get_num_words, pretty_sort

def main ():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    num_words_msg, contents = get_num_words(f"./{sys.argv[1]}")
    print(num_words_msg)

    print("--------- Character Count -------")
    pretty_sort(contents)

if __name__ == "__main__":
  main()
