"""
해당 분야의 필수 용어 먼저 파악하기 실습 모듈

Part 1 - 섹션 1.2.3 실습 코드: 새로운 분야를 학습할 때 필수 용어와 개념을 먼저 파악하는 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
ESSENTIAL_TERMS_TOPICS = {
    "1": {"name": "금융 투자", "topic": "금융 투자 분야의 필수 용어와 개념", "output_format": "용어 사전"},
    "2": {"name": "웹 개발", "topic": "웹 개발의 핵심 용어와 기술", "output_format": "용어집"},
    "3": {"name": "인공지능", "topic": "인공지능과 머신러닝의 기본 용어", "output_format": "개념 정리"},
    "4": {"name": "법률 용어", "topic": "기본 법률 용어와 개념", "output_format": "용어 가이드"},
    "5": {"name": "의학 기초", "topic": "기초 의학 및 건강 관련 필수 용어", "output_format": "용어 요약"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "용어 요청: 필수 용어와 개념 요청",
        "용어 설명 요청: 쉬운 설명과 실제 사용 예시 요청",
        "용어 분류 요청: 체계적 분류와 관계 설명 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "새로운 분야의 용어를 먼저 파악하면 학습 속도와 이해도가 크게 향상됩니다",
    "핵심 용어의 관계와 구조를 이해하면 분야 전체를 조망할 수 있습니다",
    "실제 사용 예시와 함께 용어를 배우면 실용적인 이해가 가능합니다",
    "체계적으로 분류된 용어집은 지속적인 학습과 참조에 유용합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학습 가이드", 
        f"{topic}을 초보자에게 효과적으로 설명하는 전문 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}을 처음 배우는 학생입니다. "
        f"이 분야를 효과적으로 학습하기 위해 먼저 필수 용어와 핵심 개념을 이해하고 싶습니다. "
        f"전문가들이 자주 사용하는 용어와 그 의미를 알면 더 빠르게 학습할 수 있을 것 같습니다."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        "이 분야에서 반드시 알아야 할 20-30개 정도의 핵심 용어와 개념을 알려주세요",
        "각 용어에 대해 초보자도 이해할 수 있는 쉬운 설명을 제공해주세요",
        "가능하면 각 용어의 실제 사용 예시나 맥락도 함께 알려주세요",
        "용어들 간의 관계나 구조를 이해할 수 있도록 적절히 분류해주세요",
        "입문자가 자주 혼동하는 유사 용어들이 있다면 그 차이점도 설명해주세요",
        "이 용어들을 바탕으로 더 심화 학습을 위한 다음 단계도 제안해주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"용어는 카테고리별로 분류하여 체계적으로 정리해주세요. "
        f"각 용어는 굵은 글씨로 강조하고, 그 아래에 설명과 예시를 포함해주세요. "
        f"전체적인 용어 간의 관계나 구조를 시각적으로 이해할 수 있는 요약도 포함해주세요. "
        f"초보자가 참조하기 쉽도록 알파벳 순서나 중요도 순으로 정렬하는 것도 고려해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="해당 분야의 필수 용어 먼저 파악하기",
        topic_options=ESSENTIAL_TERMS_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")