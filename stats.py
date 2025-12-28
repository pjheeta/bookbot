
##Function first calls lowercaseText to convert all text in the string to lowercase
##The calls then splits the text into a list of words and counts the total number of words
def get_num_words(splitText):
    lowerText = lowercaseText(splitText)
    wordCount = lowerText.split()
    #print (f"{wordCount}")
    countText (wordCount)

    return (len(wordCount))

#Function to lowers all text in the string splitText
def lowercaseText(splitText):
    return splitText.lower()

##go through each character in the string lowercaseText
##passing the # of times a character appears into wordDict

def countText(modText):
    wordDict = {}
    for lowerWord in modText:
        for char in lowerWord:
            wordDict[char] = wordDict.get(char, 0) + 1
            #Get Char is the heart of this problem
    print (wordDict)


            