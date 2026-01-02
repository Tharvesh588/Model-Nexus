#~ TF IDF Concept
# TF-IDF stands for Term Frequency-Inverse Document Frequency, a method used in information retrieval and text mining to evaluate the importance of a term in a document relative to a collection of documents.

# TF = (Number of times term t appears in a document) / (Total number of terms in the document)
# IDF = log_e(Total number of documents / Number of documents with term t in it)
# TF-IDF = TF * IDF


import math

docs = ["I Love NLP and AI !",
       "NLP is the best 🥳",
       "python is good 🔥 for NLP development"]

# _file = input("Enter file path: ")
# def docData(fileName):
#     with open(fileName, 'r') as f:
#         data = f.readlines()
#     return data
# docs = docData(_file)


print(f"Original text:{docs}")
def preProcess(msg):
    txt = ""
    for words in msg:
        if words.isalnum() or words.isspace():
            txt+=words
    return txt.lower().split()

token=[]

for doc in docs:
    words = preProcess(doc)
    token.append(words)

print("\n Docs Token:")
for i,t in enumerate(token):
    print(i+1," = ",t)

vocab = set()
for words in token:
    for word in words:
        vocab.add(word)

vocab = list(vocab)

print("\n Vocabulary: ",vocab)

def TF(tokens):
    tf={}
    total = len(tokens)

    for word in tokens:
        tf[word]=tf.get(word,0) +1

    for word in tf:
        tf[word] = tf[word]/total

    return tf

tf_doc=[]

for words in token:
    val = tf_doc.append(TF(words))

def idf(tokens,vocab):
    idf={}
    total = len(tokens)

    for word in vocab:
        dCount=0
        for words in token:
            if word in words:
                dCount+=1

        idf[word] = math.log(total/(1+dCount))
    
    return idf


idf_values = idf(token,vocab)

print("\n IDF Values:")
for word, value in idf_values.items():
    print(word,":",round(value,3))

def tf_idf(tf,idf):
    tfidf={}
    for word in tf:
        tfidf[word] = tf[word]*idf[word]
    return tfidf

print("\n TF-IDF Values:")
for i in range(len(tf_doc)):
    tfidf = tf_idf(tf_doc[i],idf_values)
    print(f"Doc {i+1} TF-IDF:",tfidf)

    for word, value in tfidf.items():
        print(word, ":", round(value, 3))
