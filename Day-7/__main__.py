import math

# -------- LOAD CORPUS --------
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

# -------- PREPROCESS --------
def preprocess(text):
    clean = ""

    for ch in text:
        if ch.isalnum() or ch.isspace():
            clean = clean + ch

    clean = clean.lower()
    return clean.split()

doc_tokens = []

for doc in docs:
    doc_tokens.append(preprocess(doc))

# -------- BUILD VOCAB --------
vocab = []

for doc in doc_tokens:
    for word in doc:
        if word not in vocab:
            vocab.append(word)

# -------- TF --------
def compute_tf(tokens):
    tf = {}
    total_words = len(tokens)

    for word in tokens:
        if word in tf:
            tf[word] += 1
        else:
            tf[word] = 1

    for word in tf:
        tf[word] = tf[word] / total_words

    return tf

tf_docs = []

for doc in doc_tokens:
    tf_docs.append(compute_tf(doc))

# -------- IDF --------
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

# -------- TF-IDF --------
def compute_tfidf(tf, idf):
    tfidf = {}

    for word in tf:
        if word in idf:
            tfidf[word] = tf[word] * idf[word]

    return tfidf

def vectorize(tfidf, vocab):
    vector = []

    for word in vocab:
        if word in tfidf:
            vector.append(tfidf[word])
        else:
            vector.append(0)

    return vector

# -------- COSINE SIMILARITY --------
def cosine(v1, v2):
    dot = 0
    mag1 = 0
    mag2 = 0

    for i in range(len(v1)):
        dot += v1[i] * v2[i]
        mag1 += v1[i] * v1[i]
        mag2 += v2[i] * v2[i]

    mag1 = math.sqrt(mag1)
    mag2 = math.sqrt(mag2)

    if mag1 == 0 or mag2 == 0:
        return 0

    return dot / (mag1 * mag2)

# -------- SEARCH --------
THRESHOLD = 0.15

while True:
    query = input("\nEnter Query: ")

    if query.lower() == "exit":
        break

    query_tokens = preprocess(query)
    query_tf = compute_tf(query_tokens)
    query_tfidf = compute_tfidf(query_tf, idf)
    query_vec = vectorize(query_tfidf, vocab)

    scores = []

    for tf_doc in tf_docs:
        doc_tfidf = compute_tfidf(tf_doc, idf)
        doc_vec = vectorize(doc_tfidf, vocab)
        scores.append(cosine(query_vec, doc_vec))

    best_score = max(scores)
    best_index = scores.index(best_score)

    if best_score < THRESHOLD:
        print("Result: I don't know ❌")
    else:
        print("Result:", docs[best_index])
