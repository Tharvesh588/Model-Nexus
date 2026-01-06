import math

_file = input("Enter corpus file path: ")

def load_docs(path):
    docs = []
    f = open(path, 'r', encoding='utf-8')

    for line in f:
        line = line.strip()
        if line != "":
            docs.append(line)

    f.close()
    return docs

docs = load_docs(_file)

def preprocess(text):
    clean = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            clean += ch
    return clean.lower().split()

doc_tokens = []
for doc in docs:
    doc_tokens.append(preprocess(doc))

vocab = []
for doc in doc_tokens:
    for word in doc:
        if word not in vocab:
            vocab.append(word)

def compute_tf(tokens):
    tf = {}
    total = len(tokens)

    for word in tokens:
        tf[word] = tf.get(word, 0) + 1

    for word in tf:
        tf[word] = tf[word] / total

    return tf

tf_docs = []
for doc in doc_tokens:
    tf_docs.append(compute_tf(doc))

def compute_idf(doc_tokens, vocab):
    idf = {}
    total_docs = len(doc_tokens)

    for word in vocab:
        count = 0
        for doc in doc_tokens:
            if word in doc:
                count += 1

        idf[word] = math.log((total_docs + 1) / (count + 1))

    return idf

idf = compute_idf(doc_tokens, vocab)

def compute_tfidf(tf, idf):
    tfidf = {}
    for word in tf:
        if word in idf:
            tfidf[word] = tf[word] * idf[word]
    return tfidf

def vectorize(tfidf, vocab):
    vec = []
    for word in vocab:
        vec.append(tfidf.get(word, 0))
    return vec

def cosine(v1, v2):
    dot = 0
    mag1 = 0
    mag2 = 0

    for i in range(len(v1)):
        dot += v1[i] * v2[i]
        mag1 += v1[i] ** 2
        mag2 += v2[i] ** 2

    mag1 = math.sqrt(mag1)
    mag2 = math.sqrt(mag2)

    if mag1 == 0 or mag2 == 0:
        return 0

    return dot / (mag1 * mag2)

# -------- MEMORY --------
last_topic = None
THRESHOLD = 0.15

while True:
    query = input("\nUser: ")

    if query.lower() == "exit":
        break

    if len(query.split()) <= 2 and last_topic:
        query = last_topic + " " + query

    query_tf = compute_tf(preprocess(query))
    query_vec = vectorize(compute_tfidf(query_tf, idf), vocab)

    scores = []

    for tf_doc in tf_docs:
        doc_vec = vectorize(compute_tfidf(tf_doc, idf), vocab)
        scores.append(cosine(query_vec, doc_vec))

    best = max(scores)
    index = scores.index(best)

    if best < THRESHOLD:
        print("Bot: I don't know 🤷")
    else:
        print("Bot:", docs[index])
        last_topic = query
