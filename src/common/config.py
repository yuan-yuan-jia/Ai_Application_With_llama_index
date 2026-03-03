"""
配置自定义的LLM模型和嵌入模型
"""
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,Settings
from llama_index.llms.dashscope import DashScope,DashScopeGenerationModels
from llama_index.embeddings.dashscope import DashScopeEmbedding,DashScopeTextEmbeddingModels
from dotenv import load_dotenv
import os

__all__=["setup"]

def setup() -> None:
    load_dotenv()
    api_key = "DASHSCOPE_API_KEY"
    # 设置嵌入模型
    Settings.embed_model = DashScopeEmbedding(model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,api_key=os.getenv(api_key))


    # 配置 LLM 模型
    llm = DashScope(model_name=DashScopeGenerationModels.QWEN_PLUS,api_key=os.getenv(api_key))
    Settings.llm = llm
