"""
생성형 AI와 프롬프트 엔지니어링 이해하기 실습 모듈

Part 0 - 섹션 0.1 실습 코드: 생성형 AI의 기초 개념과 프롬프트 엔지니어링의 중요성을 이해합니다.
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
AI_INTRO_TOPICS = {
    "1": {"name": "생성형 AI 개념", "topic": "생성형 AI의 기본 개념과 작동 원리", "output_format": "개요 설명"},
    "2": {"name": "프롬프트 엔지니어링 소개", "topic": "프롬프트 엔지니어링의 개념과 중요성", "output_format": "안내서"},
    "3": {"name": "AI 모델 비교", "topic": "주요 생성형 AI 모델(ChatGPT, Claude, Gemini 등)의 특징과 차이점", "output_format": "비교표"},
    "4": {"name": "활용 사례", "topic": "다양한 분야에서의 생성형 AI 활용 사례", "output_format": "사례 모음"},
    "5": {"name": "미래 전망", "topic": "생성형 AI와 프롬프트 엔지니어링의 미래 발전 방향", "output_format": "전망 분석"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 초보자 관점과 학습 목적 명시",
        "구체적 지시사항: 핵심 개념, 예시, 응용법 등 요청",
        "구조화된 형식 요청: 명확한 섹션 구분과 시각적 요소 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "생성형 AI는 입력받은 프롬프트를 기반으로 새로운 콘텐츠를 생성하는 AI 시스템입니다",
    "프롬프트 엔지니어링은 AI에게 효과적으로 지시하는 기술로, 출력 품질에 큰 영향을 미칩니다",
    "명확한 맥락과 목적을 제공하면 더 관련성 높은 응답을 얻을 수 있습니다",
    "다양한 AI 모델은 각각 고유한 특성과 장단점을 가지고 있어 목적에 맞게 선택해야 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 교육 전문가", 
        "초보자도 쉽게 이해할 수 있도록 생성형 AI와 프롬프트 엔지니어링을 설명하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 처음 배우는 대학생입니다. "
        f"프롬프트 엔지니어링 수업을 위해 {purpose}에 대한 기초 지식이 필요합니다. "
        f"가능한 쉽게 설명해주시고, 실제 예시를 포함해 이해를 돕고 실습에 활용할 수 있게 해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "기본 개념" in topic or "개념" in topic:
        builder.add_instructions([
            "생성형 AI의 기본 원리를 비전문가도 이해할 수 있게 설명해주세요",
            "중요한 용어와 개념을 명확히 정의해주세요",
            "일상생활에서 볼 수 있는 친숙한 비유나 예시를 들어주세요",
            "이 주제를 이해하기 위한 사전 지식이 있다면 간략히 알려주세요",
            "실제 활용 방법에 대한 간단한 팁도 포함해주세요"
        ])
    elif "비교" in topic:
        builder.add_instructions([
            "각 모델의 핵심 특징을 3-5가지로 요약해주세요",
            "모델별 강점과 약점을 명확히 비교해주세요",
            "각 모델이 특히 뛰어난 사용 사례나 분야를 알려주세요",
            "초보자가 처음 시작하기에 가장 적합한 모델과 그 이유를 제안해주세요",
            "이 비교가 2024년 현재 기준임을 명시하고, 모델이 계속 발전하고 있다는 점도 알려주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 가장 중요한 핵심 개념 5가지를 명확하게 설명해주세요",
            "실제 응용 사례와 예시를 포함해주세요",
            "초보자가 흔히 겪는 오해나 실수를 알려주세요",
            "추가 학습을 위한 단계별 접근 방법을 제안해주세요",
            "마지막에 요약과 핵심 포인트를 다시 정리해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"가능하면 표, 예시 박스 등 시각적 요소를 포함하여 이해하기 쉽게 만들어주세요. "
        f"전체 길이는 초보자가 부담 없이 읽을 수 있는 정도로 조절해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="생성형 AI와 프롬프트 엔지니어링 이해하기",
        topic_options=AI_INTRO_TOPICS,
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