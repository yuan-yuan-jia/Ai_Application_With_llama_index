"""
包含应用程序设置、配置和最终Streamlit的部署需要的密钥等。
它将参数集中管理，方便调整和更新
"""

LOG_FILE = "session_data/user_action.log"
SESSION_FILE = "session_data/user_session_state.json"
CACHE_FILE = "cache/pipeline_cache.json"
CONVERSATION_FILE = "cache/chat_history.json"
QUIZ_FILE = "cache/quiz.csv"
SLTDES_FILE = "cache/slides.json"
STORAGE_PATH = "ingestion_storage"
INDES_STORAGE = "index_storage"
QUIZ_SIZE = 5
ITEMS_ON_SLIDE = 4