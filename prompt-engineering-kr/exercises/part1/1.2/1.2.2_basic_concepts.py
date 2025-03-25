"""
단계적으로 지식 쌓기 실습 모듈

Part 1 - 섹션 1.2.2 실습 코드: 기초 개념부터 시작하여 단계적으로 지식을 쌓는 방법을 학습합니다.
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
STEP_BY_STEP_TOPICS = {
    "1": {"name": "통계학 기초", "topic": "통계학의 기본 개념과 원리", "output_format": "단계별 가이드"},
    "2": {"name": "프로그래밍 입문", "topic": "컴퓨터 프로그래밍의 기초", "output_format": "학습 로드맵"},
    "3": {"name": "경제학 원리", "topic": "기본 경제학 원리와 개념", "output_format": "학습 단계"},
    "4": {"name": "화학 기초", "topic": "화학의 기본 원리와 개념", "output_format": "단계별 학습"},
    "5": {"name": "음악 이론", "topic": "기초 음악 이론과 작곡 원리", "output_format": "학습 경로"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "단계적 접근 요청: 기초부터 점진적으로 학습하는 구조 요청",
        "선수 지식 확인: 필요한 사전 지식 요청",
        "학습 로드맵 요청: 체계적인 단계별 학습 경로 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "복잡한 주제는 단계적으로 접근하면 이해하기 쉬워집니다",
    "각 단계에서 필요한 지식을 확인하면 학습 목표가 명확해집니다",
    "체계적인 학습 로드맵은 효율적인 지식 습득에 도움을 줍니다",
    "단계별 질문 체인을 구성하면 점진적으로 깊이 있는 이해가 가능합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학습 코치", 
        f"{topic}을 체계적으로 가르치는 교육 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}을 처음부터 체계적으로 배우고 싶은 학생입니다. "
        f"완전한 초보자 수준에서 시작하여 단계적으로 지식을 쌓아가고 싶습니다. "
        f"각 단계별로 필요한 개념과 기술을 명확히 이해하고, 다음 단계로 넘어가기 전에 습득해야 할 핵심 내용을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        "완전 초보자를 위한 기초 개념부터 시작해주세요",
        "학습 단계를 명확히 구분하고, 각 단계별 학습 목표를 설명해주세요",
        "각 단계에서 습득해야 할 핵심 개념과 기술을 구체적으로 알려주세요",
        "한 단계에서 다음 단계로 넘어가기 위한 선행 조건이나 이해 수준을 설명해주세요",
        "각 단계에서 활용할 수 있는 학습 자료나 연습 방법을 제안해주세요",
        "초보자가 흔히 겪는 어려움과 이를 극복하는 팁도 함께 알려주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"학습 단계는 명확히 번호를 매겨 구분하고, 각 단계의 시작과 끝을 명확히 표시해주세요. "
        f"각 단계별 핵심 개념은 굵은 글씨로 강조하고, 중요한 용어는 처음 등장할 때 간단히 설명해주세요. "
        f"시각적으로 학습 경로를 이해할 수 있도록 단계별 진행 구조를 표현해주세요. "
        f"각 단계를 마스터했는지 확인할 수 있는 간단한 체크포인트나 질문도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="단계적으로 지식 쌓기",
        topic_options=STEP_BY_STEP_TOPICS,
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