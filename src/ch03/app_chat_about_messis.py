from llama_index.core import Document,SummaryIndex,Settings
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.readers.wikipedia import WikipediaReader
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

loader = WikipediaReader()
documents = loader.load_data(pages=["Messi Lionel"])
parser = SimpleNodeParser.from_defaults()
nodes = parser.get_nodes_from_documents(documents)
index = SummaryIndex(nodes)
query_engine = index.as_query_engine()
print("Ask me anything about Lionel Messi!")

while True:
    question = input("Your question: ")
    if question.lower() == "exit":
        break
    response = query_engine.query(question)
    print(response)