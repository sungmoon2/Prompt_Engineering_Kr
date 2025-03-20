"""
주제 범위와 깊이 최적화 전략

챕터 1의 세부 내용을 다루는 실습 코드
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import write_file, save_markdown

def main():
    """
    실습 코드 메인 함수
    """
    print(f"===== 주제 범위와 깊이 최적화 전략 =====")
    
    # 사용자 입력 받기
    topic = input("주제를 입력하세요: ")
    
    # 프롬프트 구성
    prompt_builder = PromptBuilder()
    # TODO: 적절한 프롬프트 템플릿 구성
    
    # 실행 로직 구현
    
    print("\n실행 완료!")

if __name__ == "__main__":
    main()
