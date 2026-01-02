msg1 = input("Enter :")
msg2 = input("Enter :")


def process(string):
    pun = ""
    for char in string:
        if char.isalnum() or char.isspace():
            pun += char
    return pun


cleanTxt = process(msg1)
tokens1 = cleanTxt.lower().split()
cleanTxt = process(msg2)
tokens2 = cleanTxt.lower().split()

#common = set(tokens1).union(set(tokens2))
#print("Common words:", common)

# BOW model for words to vectors
def bow():
    vocab = set(tokens1 + tokens2)
    vector1 = [tokens1.count(word) for word in vocab]
    vector2 = [tokens2.count(word) for word in vocab]
    return vocab,vector1, vector2

vocab,vec1, vec2 = bow()
print("Vocabulary:", vocab)
print("Vector 1:", vec1)
print("Vector 2:", vec2)