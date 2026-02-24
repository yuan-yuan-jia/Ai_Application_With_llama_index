from typing import List
from llama_index.core import Document,SummaryIndex
from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,Settings
from pathlib import Path
from llama_index.llms.dashscope import DashScope,DashScopeGenerationModels
from llama_index.embeddings.dashscope import DashScopeEmbedding,DashScopeTextEmbeddingModels
from dotenv import load_dotenv
import os

load_dotenv()
api_key = "DASHSCOPE_API_KEY"
# 设置嵌入模型
Settings.embed_model = DashScopeEmbedding(model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,api_key=os.getenv(api_key))


# 配置 LLM 模型
llm = DashScope(model_name=DashScopeGenerationModels.QWEN_PLUS,api_key=os.getenv(api_key))
Settings.llm = llm

nodes: List[TextNode] = [
    TextNode(
        text="Lionel Messi is a football player from Argentina."
        ),
    TextNode(
        text="He has won the Ballon d'Or trophy 7 times."
        ),
    TextNode(text="Lionel Messi's hometown is Rosario."),
    TextNode(text="He was born on June 24, 1987.")
]

index = SummaryIndex(nodes)

query_engine = index.as_query_engine()
response = query_engine.query(
    "What is Messi's hometown?"
)

print(response)
