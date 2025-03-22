"""
Effectiveness_evaluation 실습 모듈

Part 8 - 섹션 8.1.2 실습 코드: 기본 프롬프트와 향상된 프롬프트의 차이 비교
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.ui_helpers import (
    print_header, print_step, get_user_input, 
    display_results_comparison, print_prompt_summary,
    print_learning_points
)
from utils.example_data import get_examples_by_category
# from utils.prompt_templates import get_basic_effectiveness_evaluation_prompt, get_enhanced_effectiveness_evaluation_prompt

def main():
    """메인 함수"""
    print_header(f"Effectiveness_evaluation")
    
    # 1. 주제/과제 선택 또는 입력
    print_step(1, "주제 선택")
    # TODO: 예제 데이터 및 사용자 입력 구현
    
    # 2. 기본 프롬프트 생성 및 실행
    print_step(2, "기본 프롬프트로 질문하기")
    # TODO: 기본 프롬프트 생성 및 실행
    
    # 3. 향상된 프롬프트 생성 및 실행
    print_step(3, "향상된 프롬프트로 질문하기")
    # TODO: 향상된 프롬프트 생성 및 실행
    
    # 4. 결과 비교 및 저장
    print_step(4, "결과 비교 및 저장")
    # TODO: 결과 비교 및 저장
    
    # 5. 학습 내용 정리
    print_step(5, "학습 내용 정리")
    # TODO: 학습 내용 정리

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")
