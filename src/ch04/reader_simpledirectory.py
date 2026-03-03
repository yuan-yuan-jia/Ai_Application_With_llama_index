from common.config import setup
from llama_index.core import SimpleDirectoryReader
from pathlib import Path

file_path = Path(__file__).parent / 'files'
reader = SimpleDirectoryReader(
    input_dir=file_path,
    recursive=True,
)
documents = reader.load_data()

for doc in documents:
    print(doc.metadata)