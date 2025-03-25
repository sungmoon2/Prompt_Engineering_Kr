"""
배경 지식 없이 질문하기 실습 모듈

Part 1 - 섹션 1.2 실습 코드: 배경 지식이 없는 상태에서 효과적으로 질문하는 방법을 학습합니다.
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
NO_BACKGROUND_TOPICS = {
    "1": {"name": "양자 컴퓨팅", "topic": "양자 컴퓨팅의 기본 개념", "output_format": "초보자 가이드"},
    "2": {"name": "행동경제학", "topic": "행동경제학의 핵심 원리", "output_format": "개념 설명"},
    "3": {"name": "CRISPR 기술", "topic": "CRISPR 유전자 편집 기술", "output_format": "기초 설명"},
    "4": {"name": "분산 시스템", "topic": "분산 컴퓨팅 시스템의 기초", "output_format": "입문 가이드"},
    "5": {"name": "철학적 사고실험", "topic": "주요 철학적 사고실험", "output_format": "개념 소개"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "지식 부족 명시: 배경 지식이 없음을 명확히 전달",
        "단계적 학습 요청: 기초부터 차근차근 설명 요청",
        "이해 지원 요청: 전문 용어 설명과 예시 포함 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "배경 지식 부족을 명시하면 AI가 설명 수준을 적절히 조정할 수 있습니다",
    "기초 개념부터 단계적으로 설명을 요청하면 복잡한 주제도 이해하기 쉬워집니다",
    "전문 용어에 대한 설명을 요청하면 내용 이해가 크게 향상됩니다",
    "실생활 예시나 비유를 요청하면 추상적 개념을 더 직관적으로 이해할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "전문 교육자", 
        f"{topic}에 대해 초보자에게 설명해주는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 아무것도 모릅니다. 이 분야의 기본 개념부터 차근차근 이해하고 싶습니다. "
        f"전문 지식이 없는 초보자의 관점에서, 가장 기초적인 개념부터 설명해주세요."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        "가장 기초적인 개념부터 설명해주세요",
        "전문 용어가 나올 경우 바로 풀어서 설명해주세요",
        "실생활에서 볼 수 있는 비유나 예시를 들어주세요",
        "이 주제를 이해하기 위한 사전 지식이 있다면 알려주세요",
        "처음 접하는 초보자도 이해할 수 있는 수준으로 설명해주세요",
        "더 알아보기 위해 물어볼 수 있는 후속 질문 3개를 제안해주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"단계별로 명확하게 설명해주세요. 복잡한 개념은 더 작은 부분으로 나누어 설명해주세요. "
        f"전문 용어는 괄호 안에 간단한 설명을 추가해주세요. "
        f"중요한 개념은 굵은 글씨로 강조하고, 예시는 별도로 구분해주세요. "
        f"초보자가 차근차근 배울 수 있도록 내용을 논리적인 순서로 구성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="배경 지식 없이 질문하기",
        topic_options=NO_BACKGROUND_TOPICS,
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