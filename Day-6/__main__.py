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

def preProcess(msg):
    txt = ""
    for words in msg:
        if words.isalnum() or words.isspace():
            txt+=words
    return txt.lower().split()

docToken=[]

for doc in docs:
    docToken.append(preProcess(doc))

vocab = set()
for words in docToken:
    for word in words:
        vocab.add(word)

vocab = list(vocab)

def compute_tf(tokens):
    tf={}
    total = len(tokens)

    for word in tokens:
        tf[word]=tf.get(word,0) +1

    for word in tf:
        tf[word] = tf[word]/total

    return tf

tf_doc=[]

for words in docToken:
    val = tf_doc.append(compute_tf(words))

def compute_idf(docTokens,vocab):
    idf={}
    total = len(docTokens)

    for word in vocab:
        dCount=0
        for words in docToken:
            if word in words:
                dCount+=1

        idf[word] = math.log(total/(1+dCount))
    
    return idf


idf_values = compute_idf(docToken,vocab)

def compute_tfidf(tf, idf):
    tfidf = {}
    for word in tf:
        if word in idf:           # handle unknown key fix
            tfidf[word] = tf[word] * idf[word]
    return tfidf


def vector(tfidf,vocab):
    vec = []
    for word in vocab:
        vec.append(tfidf.get(word,0))
    return vec

def cos(vec1,vec2):
    dot=0
    mag1=0
    mag2=0

    for i in range(len(vec1)):
        dot+= vec1[i]*vec2[i]
        mag1+= vec1[i]**2
        mag2+= vec2[i]**2

    mag1 = math.sqrt(mag1)
    mag2 = math.sqrt(mag2)

    if mag1==0 or mag2==0:
        return 0

    return dot/(mag1*mag2)

while True:

    query = input("Enter Query: ")
    if query.lower()=='exit':
        break
    queryToken = preProcess(query)
    query_tf = compute_tf(queryToken)
    query_tfidf = compute_tfidf(query_tf,idf_values)
    query_vec = vector(query_tfidf,vocab)
    if sum(query_vec) == 0:
        print("No relevant knowledge found in documents.")
        continue
    
    score = []

    for i in range(len(tf_doc)):
        doc_tfidf = compute_tfidf(tf_doc[i],idf_values)
        doc_vec = vector(doc_tfidf,vocab)
        similarity = cos(query_vec,doc_vec)
        score.append(similarity)

        print(f"\nDocument {i+1} Similarity Score: ",round(similarity,3))

    doc_score = score.index(max(score))
    print(f"\nMost Relevant Document",docs[doc_score])