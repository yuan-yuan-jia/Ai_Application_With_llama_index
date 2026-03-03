from llama_index.readers.web import SimpleWebPageReader
from common import config

config.setup()

urls = ["https://docs.llamaindex.ai"]
documents = SimpleWebPageReader(html_to_text=True).load_data(urls=urls)

for doc in documents:
    print(doc.text)