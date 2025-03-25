"""
AI와의 대화를 통한 직관적 이해 실습 모듈

Part 0 - 섹션 0.2.1 실습 코드: AI를 단순한 도구가 아닌 대화 파트너로 접근하는 방법을 학습합니다.
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
CONVERSATION_APPROACH_TOPICS = {
    "1": {"name": "대화 원칙", "topic": "AI와의 효과적인 대화 원칙", "output_format": "원칙 가이드"},
    "2": {"name": "질문 방식", "topic": "AI에게 효과적으로 질문하는 방법", "output_format": "질문 가이드"},
    "3": {"name": "대화 흐름", "topic": "AI와의 자연스러운 대화 흐름 구성하기", "output_format": "대화 전략"},
    "4": {"name": "초보자 접근법", "topic": "AI 초보자를 위한 대화적 접근법", "output_format": "입문 가이드"},
    "5": {"name": "대화 패턴", "topic": "효과적인 AI 대화 패턴과 구조", "output_format": "패턴 분석"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 맥락 설정: 초보자 관점과 직관적 이해 목적 명시",
        "구체적 요청사항: 원칙, 사례, 단계별 접근법 등 세부 요소 요청",
        "실용적 형식 지정: 실제 적용 가능한 예시와 구조 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "AI는 단순한 질의응답 도구가 아닌 지식을 함께 탐색하는 대화 파트너로 접근하면 더 효과적입니다",
    "대화적 접근에서는 맥락 설정, 명확한 의도 전달, 후속 질문 활용이 중요합니다",
    "AI 응답을 바탕으로 질문을 발전시키며 대화를 확장하는 방식이 더 깊은 이해를 가능하게 합니다",
    "직관적 이해란 이론적 설명보다 실제 상호작용을 통해 AI 능력과 한계를 체감하는 것입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 대화 교육 전문가", 
        "생성형 AI와의 효과적인 대화 방법을 쉽고 직관적으로 설명하는 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링 수업을 처음 듣는 대학생입니다. {topic}에 대해 배우고 있습니다. "
        f"기술적인 개념보다는 실제로 적용할 수 있는 실용적인 방법을 알고 싶습니다. "
        f"AI를 도구가 아닌 대화 파트너로 접근하는 직관적인 방법을 이해하고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "대화 원칙" in topic:
        builder.add_instructions([
            "AI와의 효과적인 대화를 위한 핵심 원칙 5-7가지를 명확히 설명해주세요",
            "각 원칙별로 구체적인 적용 예시를 대화 형태로 보여주세요",
            "일반적인 질문과 대화적 접근의 질문을 비교하는 사례를 최소 3가지 제시해주세요",
            "대화 원칙을 적용했을 때와 그렇지 않았을 때의 결과 차이를 설명해주세요",
            "초보자가 바로 실천할 수 있는 간단한 대화 원칙 체크리스트를 제공해주세요"
        ])
    elif "질문 방식" in topic:
        builder.add_instructions([
            "AI에게 효과적으로 질문하는 다양한 방식을 유형별로 분류하고 설명해주세요",
            "좋은 질문과 덜 효과적인 질문의 구체적인 예시를 최소 5쌍 제시해주세요",
            "질문의 구성 요소(맥락, 목적, 구체성 등)를 분석하고 각각의 중요성을 설명해주세요",
            "질문을 점진적으로 발전시키는 방법과 실제 대화 흐름 예시를 보여주세요",
            "다양한 학습 목적(개념 이해, 문제 해결, 창작 등)에 맞는 질문 템플릿을 제공해주세요"
        ])
    elif "대화 흐름" in topic:
        builder.add_instructions([
            "AI와의 자연스러운 대화 흐름을 구성하는 방법을 단계별로 설명해주세요",
            "효과적인 대화 시작, 전개, 마무리 방법을 구체적인 예시와 함께 설명해주세요",
            "대화 중 AI의 응답을 바탕으로 후속 질문을 발전시키는 기법을 알려주세요",
            "목적에 따른 다양한 대화 구조(탐색형, 문제해결형, 창작형 등)의 예시를 제공해주세요",
            "대화 흐름이 끊겼을 때 다시 연결하는 방법과 대화 맥락을 효과적으로 유지하는 방법을 알려주세요"
        ])
    elif "초보자 접근법" in topic:
        builder.add_instructions([
            "AI를 처음 사용하는 사람을 위한 대화적 접근법을 단계별로 설명해주세요",
            "초보자가 흔히 범하는 실수와 이를 개선하는 방법을 예시와 함께 알려주세요",
            "처음부터 바로 실천할 수 있는 간단한 대화 연습 3-5가지를 제안해주세요",
            "초보자의 수준에서 점차 대화 기술을 발전시키는 단계별 학습 경로를 제시해주세요",
            "AI와의 대화에서 실패하거나 오해가 생겼을 때 대처하는 방법도 알려주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 내용을 명확하고 실용적으로 설명해주세요",
            "개념 설명보다는 구체적인 예시와 사례를 통해 이해를 돕고 실제 적용할 수 있게 해주세요",
            "초보자가 단계별로 시도해볼 수 있는 실천 방법을 제시해주세요",
            "흔한 어려움이나 실수와 그 해결책을 포함해주세요",
            "직관적 이해를 돕는 비유나 시각적 설명도 추가해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 대화 예시는 '사용자:'와 'AI:' 형식으로 구분하여 표시해주세요. "
        f"핵심 포인트는 굵은 글씨로 강조하고, 실용적인 팁은 별도 박스로 구분해주세요. "
        f"단계별 적용 방법은 번호를 매겨 순서대로 설명해주세요. "
        f"전체 내용은 초보자가 바로 실천할 수 있도록 쉽고 직관적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="AI와의 대화를 통한 직관적 이해",
        topic_options=CONVERSATION_APPROACH_TOPICS,
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