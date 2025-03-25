"""
생성형 AI란 무엇인가 실습 모듈

Part 0 - 섹션 0.1.1 실습 코드: 생성형 AI의 개념, 작동 원리 및 주요 특징을 탐구합니다.
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
GENERATIVE_AI_TOPICS = {
    "1": {"name": "기본 개념", "topic": "생성형 AI의 기본 개념과 정의", "output_format": "개념 설명"},
    "2": {"name": "작동 원리", "topic": "생성형 AI의 기술적 작동 원리", "output_format": "단계별 설명"},
    "3": {"name": "주요 기술", "topic": "생성형 AI의 핵심 기술(트랜스포머, LLM 등)", "output_format": "기술 가이드"},
    "4": {"name": "발전 역사", "topic": "생성형 AI의 발전 역사와 주요 이정표", "output_format": "타임라인"},
    "5": {"name": "한계와 도전", "topic": "생성형 AI의 현재 한계와 도전 과제", "output_format": "분석 보고서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용자 정보 제공: 초보자 학습자로 자신을 설정",
        "상세한 요청사항: 핵심 개념, 쉬운 예시, 전문 용어 설명 등 요청",
        "출력 형식 지정: 학습하기 쉬운 구조와 시각적 요소 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "생성형 AI는 입력에 기반해 새로운 콘텐츠를 생성하는 머신러닝 시스템입니다",
    "기본 작동 원리는 패턴 학습, 확률 모델링, 그리고 생성적 추론에 기반합니다",
    "트랜스포머 아키텍처와 언어 모델은 현대 생성형 AI의 핵심 기술입니다",
    "맥락과 목적을 구체적으로 제공하면 AI가 더 관련성 높은 응답을 생성할 수 있습니다"
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
        "기술적 개념을 비전문가도 쉽게 이해할 수 있도록 설명하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 컴퓨터 공학을 전공하지 않은 대학생으로, {topic}에 대해 처음 배우고 있습니다. "
        f"프롬프트 엔지니어링 수업을 위해 {purpose}에 대한 기초 지식이 필요합니다. "
        f"전문 용어가 나오면 바로 풀어서 설명해주시고, 실생활에서 볼 수 있는 예시를 들어주세요."
    )
    
    # 구체적인 지시사항 추가
    if "기본 개념" in topic:
        builder.add_instructions([
            "생성형 AI의 정의와 기본 개념을 이해하기 쉽게 설명해주세요",
            "일반 AI와 생성형 AI의 주요 차이점을 비교해주세요",
            "실생활에서 접할 수 있는 생성형 AI의 예시를 최소 3가지 알려주세요",
            "생성형 AI가 가능한 일과 불가능한 일을 구분해주세요",
            "생성형 AI를 처음 접하는 사람이 알아두면 좋을 기본 용어 5개를 설명해주세요"
        ])
    elif "작동 원리" in topic:
        builder.add_instructions([
            "생성형 AI의 기본 작동 원리를 비전문가도 이해할 수 있게 설명해주세요",
            "학습, 추론, 생성 과정을 단계별로 설명해주세요",
            "복잡한 기술적 개념은 일상적인 비유를 사용해 설명해주세요",
            "텍스트 생성이 어떻게 이루어지는지 간단한 예시로 보여주세요",
            "작동 과정에서 발생할 수 있는 오류나 한계도 함께 설명해주세요"
        ])
    elif "핵심 기술" in topic or "주요 기술" in topic:
        builder.add_instructions([
            "생성형 AI의 핵심 기술들을 쉽게 이해할 수 있게 설명해주세요",
            "각 기술의 기본 개념과 중요성을 설명해주세요",
            "트랜스포머와 언어 모델이 어떻게 작동하는지 간단히 설명해주세요",
            "기술 발전의 주요 이정표가 된 모델들을 간략히 소개해주세요",
            "각 기술이 실제로 어떻게 적용되는지 예시를 들어주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 정보를 비전문가도 이해할 수 있게 설명해주세요",
            "중요한 개념과 용어를 쉽게 풀어서 설명해주세요",
            "실제 사례나 예시를 포함해 이해를 돕고 실습에 활용할 수 있게 해주세요",
            "이 주제에 관한 일반적인 오해나 잘못된 정보가 있다면 바로잡아 주세요",
            "추가로 학습하면 좋을 관련 주제나 자원을 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"전문 용어는 괄호 안에 간단한 설명을 추가해주세요. "
        f"이해를 돕기 위해 표, 비유, 예시 등을 적절히 활용해주세요. "
        f"내용은 초보자가 이해할 수 있는 수준으로 작성하되, 핵심 개념은 정확하게 전달해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="생성형 AI란 무엇인가",
        topic_options=GENERATIVE_AI_TOPICS,
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