def wordCount(bookText):
    wordList = bookText.split()
    no_of_words = len(wordList)
    return no_of_words


def characterData(bookText):
    chardiks = []
    charData = {}
    for character in bookText:
        character = character.lower()
        charData[character] = 0 
    for character in bookText:
        character = character.lower()
        charData[character]+=1
    
    for key in charData:
        if(key.isalpha()):
            keyDik = {"char" : key , "num": charData[key]}
            chardiks.append(keyDik)
    chardiks.sort(key=lambda dik: dik["num"])


    return chardiks
