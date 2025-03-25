"""
무지를 인정하는 질문의 힘 실습 모듈

Part 1 - 섹션 1.2.1 실습 코드: 자신의 지식 부족을 인정하고 기초부터 배우는 접근법의 효과를 학습합니다.
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
ADMIT_IGNORANCE_TOPICS = {
    "1": {"name": "블록체인 기술", "topic": "블록체인 기술의 기본 원리", "output_format": "초보자 가이드"},
    "2": {"name": "머신러닝", "topic": "머신러닝의 핵심 개념과 원리", "output_format": "입문 설명"},
    "3": {"name": "천체물리학", "topic": "우주와 천체물리학의 기초", "output_format": "개념 소개"},
    "4": {"name": "게임 이론", "topic": "경제학의 게임 이론 기초", "output_format": "기본 가이드"},
    "5": {"name": "신경과학", "topic": "뇌와 신경계의 기본 작동 원리", "output_format": "기초 설명"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "무지 인정: '아무것도 모릅니다'라고 명시적으로 인정",
        "기초 요청: 가장 기본적인 개념부터 설명 요청",
        "학습 지원 요청: 전문 용어 설명과 실생활 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "자신의 무지를 인정하면 AI가 기초 수준에 맞춰 설명해주어 학습이 용이해집니다",
    "무지 인정은 전문가에게도 효과적인 학습 전략입니다",
    "기초부터 배우는 접근법은 복잡한 주제의 근본적 이해를 돕습니다",
    "지식 수준을 솔직하게 공유하면 AI가 맞춤형 설명을 제공할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "인내심 있는 교육자", 
        f"{topic}에 대해 완전한 초보자에게 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 정말 아무것도 모릅니다. 이 분야의 가장 기본적인 개념조차 생소합니다. "
        f"마치 5살 아이에게 설명하듯이 가장 기초적인 것부터 설명해주세요. "
        f"저는 이 주제에 관련된 어떤 전문 용어도 이해하지 못하니, 모든 개념을 풀어서 설명해주시면 감사하겠습니다."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        "가장 기본적인 개념과 원리부터 설명해주세요",
        "모든 전문 용어는 일상적인 언어로 풀어서 설명해주세요",
        "가능하면 일상생활에서 볼 수 있는 예시나 비유를 사용해주세요",
        "기본 개념을 이해한 후 물어볼 수 있는 다음 단계의 질문을 제안해주세요",
        "복잡한 개념은 더 작은 부분으로 나누어 단계적으로 설명해주세요",
        "시각적으로 상상할 수 있는 설명을 포함해주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"설명은 최대한 간결하고 이해하기 쉽게 작성해주세요. "
        f"중요한 개념이나 용어는 처음 등장할 때 굵은 글씨로 강조하고 간단히 설명해주세요. "
        f"단계별로 점진적으로 설명하고, 각 단계가 끝날 때마다 간략히 요약해주세요. "
        f"실생활 예시나 비유는 별도의 박스나 섹션으로 구분하여 제시해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="무지를 인정하는 질문의 힘",
        topic_options=ADMIT_IGNORANCE_TOPICS,
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