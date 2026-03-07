"""
配置自定义的LLM模型和嵌入模型
"""
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,Settings
from llama_index.llms.dashscope import DashScope,DashScopeGenerationModels
from llama_index.embeddings.dashscope import DashScopeEmbedding,DashScopeTextEmbeddingModels
from dotenv import load_dotenv
import os

__all__=["setup","embed_model"]
load_dotenv()
api_key = "DASHSCOPE_API_KEY"
embed_model = DashScopeEmbedding(model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2,api_key=os.getenv(api_key))
def setup() -> None:
    # 设置嵌入模型
    Settings.embed_model =  embed_model


    # 配置 LLM 模型
    llm = DashScope(model_name=DashScopeGenerationModels.QWEN_PLUS,api_key=os.getenv(api_key))
    Settings.llm = llm
