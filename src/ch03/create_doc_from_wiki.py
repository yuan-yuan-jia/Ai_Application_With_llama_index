from llama_index.readers.wikipedia import WikipediaReader

loader = WikipediaReader()
documents = loader.load_data( 
    pages=['Pythagorean theorem','fuchsia os']
)

print(f"loaded {len(documents)} documents")

for doc in documents:
    print(doc)