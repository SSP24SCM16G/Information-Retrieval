import sys
from indexermain.indexer2 import TextData, TextVectorizer

def print_cosine_similarity(query):
    data_directory = '/Users/gourusamhitha/Downloads/IR_Project/indexermain'

    data = TextData(data_directory)
    data.load_data()

    vectorizer = TextVectorizer(data.preprocessed_data)
    vectorizer.fit()

    preprocessed_query = data.preprocess_text(query)
    results = vectorizer.query(preprocessed_query)

    print("Query Results based on Cosine Similarity (score > 0.00):")
    for result in results:
        print(f"Article: {result['article']}")
        print(f"Link: {result['link']}")
        print(f"Cosine Similarity Score: {result['score']:.4f}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If command line arguments are provided, take the query from them
        query = " ".join(sys.argv[1:])
        print_cosine_similarity(query)
    else:
        # If no command line arguments are provided, prompt the user to enter the query
        query = input("Enter your query: ")
        print_cosine_similarity(query)
