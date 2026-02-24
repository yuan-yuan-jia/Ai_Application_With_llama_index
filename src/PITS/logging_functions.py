"""
记录用户和应用程序的每一次交互。
写入描述性日志语句并带有时间戳以跟踪用户在整个应用程序的动作。
本地存储和检索应用程序日志-最终在云端
"""
from datetime import datetime
from PITS.global_settings import LOG_FILE
import os

def log_action(action,action_type) -> None:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp}: {action_type} : {action}\n"
    with open(LOG_FILE,'a') as file:
        file.write(log_entry)

def reset_log():
    with open(LOG_FILE,'w') as file:
        file.truncate(0)