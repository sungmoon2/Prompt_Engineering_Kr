"""
명확한 지시문 작성하기 실습 모듈

Part 1 - 섹션 1.1 실습 코드: 기본 프롬프트와 향상된 프롬프트의 차이 비교를 통해
효과적인 지시문 작성법을 학습합니다.
"""

import os
import sys
import re
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
INSTRUCTION_TOPICS = {
    "1": {"name": "여행 계획", "topic": "3박 4일 제주도 여행 계획", "output_format": "일정표"},
    "2": {"name": "레시피 요청", "topic": "초보자를 위한 파스타 레시피", "output_format": "단계별 가이드"},
    "3": {"name": "개념 설명", "topic": "블록체인 기술의 기본 원리", "output_format": "초보자용 설명"},
    "4": {"name": "기술 비교", "topic": "Python과 JavaScript의 주요 차이점", "output_format": "비교표"},
    "5": {"name": "역사 요약", "topic": "산업혁명의 주요 영향과 결과", "output_format": "시간순 요약"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용 맥락 제공: 목적과 활용 방법 명시",
        "구체적 지시사항: 5가지 세부 요청 추가",
        "출력 형식 지정: 원하는 형식과 구조 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "명확한 맥락과 목적을 제공하면 더 관련성 높은 응답을 얻을 수 있습니다",
    "구체적인 지시사항이 모호한 요청보다 훨씬 효과적입니다",
    "원하는 출력 형식을 명시하면 응답의 구조가 개선됩니다",
    "실제 사용 목적을 공유하면 AI가 더 적합한 정보를 제공할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 사용 맥락 정보 추가
    builder.add_context(
        f"저는 {purpose}을 위해 {topic}에 대한 정보가 필요합니다. "
        f"이 정보는 {output_format} 형식으로 정리되면 가장 유용할 것 같습니다."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        f"{topic}에 대한 핵심 정보를 명확하고 구체적으로 제공해주세요",
        "중요한 요소나 고려사항을 빠짐없이 포함해주세요",
        "가능한 단계별로 구분하여 체계적으로 설명해주세요",
        "실제 예시나 사례를 포함해주면 더 이해하기 쉬울 것 같습니다",
        "일반적인 내용보다는 구체적이고 실용적인 정보에 중점을 두어주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 체계적으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    result = run_exercise(
        title="명확한 지시문 작성하기",
        topic_options=INSTRUCTION_TOPICS,
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