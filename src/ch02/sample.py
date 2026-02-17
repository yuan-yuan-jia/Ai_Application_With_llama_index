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

files_path = Path(__file__).parent / 'files'

documents = SimpleDirectoryReader(input_dir=files_path).load_data()
index = VectorStoreIndex.from_documents(documents=documents)
query_engine = index.as_query_engine()

response = query_engine.query("summarize each document in a few sentences")
print(response)