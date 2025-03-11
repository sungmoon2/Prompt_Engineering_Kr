# utils/config_utils.py
import os
from dotenv import load_dotenv

# 기본 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# 디렉토리 없으면 생성
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# 환경 변수 로드
load_dotenv()

# 설정 정보 가져오기
def get_api_key(service="openai"):
    """API 키 가져오기"""
    if service == "openai":
        return os.getenv("OPENAI_API_KEY")
    elif service == "gemini":
        return os.getenv("GOOGLE_API_KEY")
    # 필요에 따라 다른 서비스 추가