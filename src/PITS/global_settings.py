"""
包含应用程序设置、配置和最终Streamlit的部署需要的密钥等。
它将参数集中管理，方便调整和更新
"""
__all__ = ["LOG_FILE", "SESSION_FILE","CACHE_FILE","CONVERSATION_FILE","QUIZ_FILE",
        "SLTDES_FILE","STORAGE_PATH","INDES_STORAGE","QUIZ_SIZE","INDES_STORAGE"]

from pathlib import Path
project_root_path = Path(__file__).parent.parent.parent
PITS_RUNTIME_ROOT_PATH = project_root_path / 'pits_run'

LOG_FILE = PITS_RUNTIME_ROOT_PATH / "session_data" /  "user_action.log"
SESSION_FILE = PITS_RUNTIME_ROOT_PATH / "session_data" / "user_session_state.json"
CACHE_FILE = PITS_RUNTIME_ROOT_PATH / "cache" / "pipeline_cache.json"
CONVERSATION_FILE = PITS_RUNTIME_ROOT_PATH / "cache"/ "chat_history.json"
QUIZ_FILE = PITS_RUNTIME_ROOT_PATH / "cache" / "quiz.csv"
SLTDES_FILE = PITS_RUNTIME_ROOT_PATH / "cache" / "slides.json"
STORAGE_PATH = PITS_RUNTIME_ROOT_PATH / "ingestion_storage"
INDES_STORAGE = PITS_RUNTIME_ROOT_PATH / "index_storage"
QUIZ_SIZE = 5
ITEMS_ON_SLIDE = 4