msg = input("Enter a message: ")

#Clean Punctuation
# cleaned_msg = ''.join(char for char in msg if char.isalnum() or char.isspace())
def process(string):
    pun = ""
    for char in string:
        if char.isalnum() or char.isspace():
            pun += char

    return pun

cleanTxt = process(msg)
# print("Processed Message:", cleanTxt)

tokens = cleanTxt.lower().split()
#print("Tokens:", tokens)

stopWords = ['i','am','is','are','the','a','an','to','of','for','in','on','and']

def clean (stopList, token):
    text = " "
    for words in token:
        if words not in stopList:
            text += words+" "
    return text.split()

print(clean(stopWords, tokens))