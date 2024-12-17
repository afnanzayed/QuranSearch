from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams
from transformers import AutoTokenizer, AutoModel
import requests
import torch



# Load the model directly from Hugging Face (requires an active internet connection)
model_name = "CAMeL-Lab/bert-base-arabic-camelbert-mix"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# If you face any issues with downloading the model, it is recommended to download it locally
# and use the following code to load the model from your device:

# Dynamically load the path to the 'models' directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(current_dir, "models")
# tokenizer = AutoTokenizer.from_pretrained(model_path)
# model = AutoModel.from_pretrained(model_path, from_tf=False)

# Function to generate embeddings
def generate_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the last hidden state as the embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding

# Connect to Qdrant (in-memory for now)
client = QdrantClient(":memory:")

# Create a collection in Qdrant
client.recreate_collection(
    collection_name="Al-Kahf",
    vectors_config=VectorParams(size=768, distance="Cosine")  # Adjust size to match your model's embedding size
)

# Fetch Surah Al-Kahf verses in English
response = requests.get("https://api.alquran.cloud/v1/surah/18/en")
data = response.json()

if response.status_code == 200:
    verses = data['data']['ayahs']

    # Prepare points for Qdrant
    points = []
    for verse in verses:
        # Generate embedding for each verse
        embedding = generate_embedding(verse['text'])

        # Add the verse to Qdrant
        points.append(PointStruct(
            id=verse['number'],
            vector=embedding,
            payload={
                "text": verse['text'],
                "surah": "Al-Kahf",
                "ayah_number": verse['numberInSurah']
            }
        ))

    # Insert points into Qdrant
    client.upsert(collection_name="Al-Kahf", points=points)
    print("Surah Al-Kahf has been stored successfully!")
else:
    print("Failed to fetch Surah Al-Kahf data.")


def semantic_search(query):
    # Generate embedding for the query
    query_embedding = generate_embedding(query)

    # Search in Qdrant
    results = client.search(
        collection_name="Al-Kahf",
        query_vector=query_embedding
        # ,limit=5  # Number of results to retrieve
    )

    # Display results
    print("Search Results:")
    for result in results:
        print(f"Ayah {result.payload['ayah_number']}: {result.payload['text']}")


if __name__ == "__main__":
    query = input("Enter your query: ")
    semantic_search(query)


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Generate embeddings using the model
def generate_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the last hidden state as the embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding
