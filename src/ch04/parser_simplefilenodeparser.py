from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
file_path = Path(__file__).parent / 'files' / 'sample_document1.txt' 
document = reader.load_data(file_path)

print(f"Metadata: {document[0].metadata}")
print(f"Text: {document[0].text}")