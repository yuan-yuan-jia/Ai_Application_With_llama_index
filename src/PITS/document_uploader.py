"""
和LlamaIndex交互，处理上传文档的数据导入和索引
"""
from typing import Sequence
from PITS.logging_functions import log_action
from PITS.global_settings import STORAGE_PATH,CACHE_FILE
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.core.ingestion import IngestionCache,IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.extractors import SummaryExtractor
from llama_index.core.schema import BaseNode
from common.config import embed_model


def ingest_documents() -> Sequence[BaseNode]:
    documents = SimpleDirectoryReader(STORAGE_PATH,filename_as_id=True).load_data()
    for doc in documents:
        print(doc.id_)
        log_action(f"File '{doc.id_}' uploaded user", action_type="UPLOAD")
    
    try:
        cached_hashes = IngestionCache.from_persist_path(str(CACHE_FILE))
        print("Cache file found. Running using cache ...")
    except:
        cached_hashes = None
        print("No cache file found. Running without cache...")
    pipeline = IngestionPipeline(
        transformations = [
            TokenTextSplitter(chunk_size=1024,chunk_overlap=20),
            SummaryExtractor(summaries=['self']),
            embed_model
        ],
        cache=cached_hashes
    )

    nodes = pipeline.run(documents=documents)
    pipeline.cache.persist(str(CACHE_FILE))
    return nodes

if __name__ == "__main__":
    from common.config import setup
    setup()
    embedded_nodes = ingest_documents()
    for node in embedded_nodes:
        print(node)