from stats import wordCount
from stats import characterData
import sys



def get_book_text(filePath):
    with open(filePath) as f:
        fileText = f.read()
        return fileText
# print(haha)



def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
    filePath = sys.argv[1]
        
    bookText = get_book_text(filePath)
    no_of_words  = wordCount(bookText)
    # print(f"{no_of_words} words found in the document")
    chardicks  = characterData(bookText)
    # print(chardick)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {no_of_words} total words")
    print("--------- Character Count -------")
    for dik in chardicks :
        character = dik["char"]
        characterCount = dik["num"]
        print(f"{character}: {characterCount}")
    print("============= END ===============")
    # print(sys.argv)


main()
