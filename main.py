from stats import get_num_words, countText
import sys

#print (sys.argv)

### Function to Read Book Text from a File
def get_book_text(bookLocation):
    wordCount=""
    with open(bookLocation) as f:
        file_contents = f.read()
    return (file_contents)

##Main function
def main():
   # bookPath = 'books/frankenstein.txt'

    if len(sys.argv) >1:
        bookPath = sys.argv[1]
        print("============ BOOKBOT ============")
        print (f"Analyzing book found at {bookPath}...") 
        bookApplied = get_book_text(bookPath)
        NumWords = get_num_words(bookApplied)
        print ("----------- Word Count ----------")
        print (f"Found {NumWords} total words")
        print("--------- Character Count -------")
        countText(bookApplied)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()