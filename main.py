from stats import get_num_words, countText

### Function to Read Book Text from a File
def get_book_text(bookLocation):
    wordCount=""
    with open(bookLocation) as f:
        file_contents = f.read()
    return (file_contents)

##Main function
def main():
    bookPath = 'books/frankenstein.txt'
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {bookPath}...") 
    bookApplied = get_book_text(bookPath)
    NumWords = get_num_words(bookApplied)
    countText(bookApplied)
    print (f"Found {NumWords} total words")


main()