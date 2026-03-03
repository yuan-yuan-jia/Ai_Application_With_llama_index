from common.config import setup
from llama_index.readers.database import DatabaseReader
from pathlib import Path

db_path = Path(__file__).parent 

setup()

reader = DatabaseReader(
    uri="sqlite:///" + db_path.name
)
query = "SELECT * FROM products"
documents = reader.load_data(query=query)
for doc in documents:
    print(doc)