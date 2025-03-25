"""
대화 모델로 접근하기 실습 모듈

Part 0 - 섹션 0.2 실습 코드: AI와의 대화를 통한 직관적 이해와 프롬프트 작성 기초를 학습합니다.
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
CONVERSATION_TOPICS = {
    "1": {"name": "대화적 접근", "topic": "AI와의 대화를 통한 직관적 이해 방법", "output_format": "가이드"},
    "2": {"name": "레시피 관점", "topic": "'요리 레시피' 관점으로 프롬프트 구성하기", "output_format": "방법론"},
    "3": {"name": "실험 마인드셋", "topic": "시도와 오류를 통한 프롬프트 학습 방법", "output_format": "학습 가이드"},
    "4": {"name": "대화 예시", "topic": "효과적인 AI 대화 예시와 분석", "output_format": "예시 모음"},
    "5": {"name": "자연스러운 대화", "topic": "AI와 자연스러운 대화 기법", "output_format": "기술 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "대화 맥락 설정: 학습자로서의 상황과 목적 명시",
        "구체적 요청: 사례, 방법론, 단계별 접근법 등 구체적 요소 요청",
        "구조화된 형식: 학습과 적용이 용이한 구조 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "AI는 단순한 정보 검색 도구가 아닌 대화 파트너로 접근하면 더 효과적입니다",
    "프롬프트는 '재료'와 '조리법'이 있는 요리 레시피처럼 구성하면 이해하기 쉽습니다",
    "반복적인 시도와 오류를 통해 프롬프트 작성 기술을 개선할 수 있습니다",
    "대화의 맥락과 의도를 명확히 전달하면 AI가 더 관련성 높은 응답을 제공합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 대화 전문가", 
        "생성형 AI와의 효과적인 대화 방법을 가르치는 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 처음 배우는 대학생입니다. {topic}에 대해 배우고 싶습니다. "
        f"기술적인 복잡성보다는 실용적이고 직관적인 접근 방법을 알고 싶습니다. "
        f"실제로 적용할 수 있는 구체적인 방법과 예시를 포함해 설명해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "대화적 접근" in topic:
        builder.add_instructions([
            "AI를 대화 파트너로 바라보는 관점과 그 이점을 설명해주세요",
            "대화적 접근법의 핵심 원칙 5가지를 설명해주세요",
            "일반적인 질문과 대화적 질문의 차이를 구체적인 예시와 함께 보여주세요",
            "대화를 통해 점진적으로 정보를 얻는 방법을 단계별로 설명해주세요",
            "초보자가 시작할 수 있는 대화 템플릿이나 구조를 3가지 제안해주세요"
        ])
    elif "레시피 관점" in topic:
        builder.add_instructions([
            "'요리 레시피' 비유가 프롬프트 이해에 어떻게 도움이 되는지 설명해주세요",
            "레시피 관점에서 프롬프트의 '재료'와 '조리법'에 해당하는 요소들을 설명해주세요",
            "레시피 형식으로 작성된 프롬프트 예시 3가지를 다양한 목적(정보 검색, 창작, 분석 등)에 맞춰 제공해주세요",
            "레시피 접근법을 사용할 때의 장점과 주의할 점을 설명해주세요",
            "일반 프롬프트를 '레시피 형식'으로 변환하는 단계별 방법을 알려주세요"
        ])
    elif "실험 마인드셋" in topic:
        builder.add_instructions([
            "프롬프트 학습에 실험 마인드셋이 중요한 이유를 설명해주세요",
            "효과적인 프롬프트 실험 방법과 접근 전략을 단계별로 설명해주세요",
            "프롬프트 변형에 따른 결과 차이를 추적하고 분석하는 방법을 알려주세요",
            "실패한 프롬프트에서 배우는 방법과 개선 전략을 설명해주세요",
            "초보자를 위한 간단한 프롬프트 실험 연습과 그 목적을 3-5가지 제안해주세요"
        ])
    elif "대화 예시" in topic:
        builder.add_instructions([
            "다양한 목적(정보 검색, 창작, 문제 해결 등)에 맞는 효과적인 AI 대화 예시를 최소 3가지 제공해주세요",
            "각 대화 예시에서 특히 효과적인 부분과 그 이유를 분석해주세요",
            "대화 흐름 유지와 맥락 관리가 잘 된 예시를 보여주세요",
            "일반적인 대화 실수와 그것을 개선한 버전을 비교해서 보여주세요",
            "다양한 대화 스타일(직접적, 탐색적, 단계적 등)의 사례와 각각의 장단점을 분석해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 원칙과 방법론을 명확하게 설명해주세요",
            "개념을 이해하기 쉽도록 구체적인 예시와 사례를 포함해주세요",
            "초보자가 단계별로 적용할 수 있는 실용적인 가이드를 제공해주세요",
            "흔히 발생하는 어려움이나 실수와 그 해결책을 포함해주세요",
            "실제 적용을 위한 템플릿이나 구체적인 접근법을 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"핵심 개념이나 원칙은 굵은 글씨로 강조하고, 실용적인 팁이나 예시는 별도로 구분해주세요. "
        f"대화 예시는 실제 대화 형식으로 표현하여 이해하기 쉽게 만들어주세요. "
        f"내용은 이론보다 실제 적용에 중점을 두고, 초보자도 바로 활용할 수 있게 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="대화 모델로 접근하기",
        topic_options=CONVERSATION_TOPICS,
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