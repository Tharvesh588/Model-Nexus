START

INPUT multiple sentences (documents)

STEP 1: Preprocess each sentence
    - remove punctuation
    - convert to lowercase
    - tokenize into words

STEP 2: Build Vocabulary
    - combine all tokens from all documents
    - remove duplicates
    - store as VOCAB list

STEP 3: Calculate Term Frequency (TF)
    FOR each document:
        FOR each word in VOCAB:
            count = number of times word appears in document
            tf = count / total words in that document
            store TF value

STEP 4: Calculate Inverse Document Frequency (IDF)
    total_docs = number of documents
    FOR each word in VOCAB:
        doc_count = number of documents containing that word
        idf = log(total_docs / doc_count)
        store IDF value

STEP 5: Calculate TF-IDF
    FOR each document:
        FOR each word in VOCAB:
            tfidf = TF(word, document) * IDF(word)
            store TF-IDF vector

OUTPUT TF-IDF vectors for all documents

END
