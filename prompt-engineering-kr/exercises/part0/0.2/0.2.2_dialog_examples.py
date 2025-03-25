"""
요리 레시피 관점으로 프롬프트 구성하기 실습 모듈

Part 0 - 섹션 0.2.2 실습 코드: 프롬프트 작성을 요리 레시피에 비유하여 직관적으로 이해하는 방법을 학습합니다.
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
RECIPE_APPROACH_TOPICS = {
    "1": {"name": "레시피 구조", "topic": "프롬프트를 레시피처럼 구성하는 기본 구조", "output_format": "구조 가이드"},
    "2": {"name": "재료와 조리법", "topic": "프롬프트의 '재료'와 '조리법' 요소 이해하기", "output_format": "개념 설명"},
    "3": {"name": "레시피 예시", "topic": "다양한 목적에 맞는 프롬프트 레시피 예시", "output_format": "예시 모음"},
    "4": {"name": "레시피 변형", "topic": "기본 프롬프트 레시피의 목적별 변형 방법", "output_format": "변형 가이드"},
    "5": {"name": "레시피 최적화", "topic": "프롬프트 레시피의 최적화와 개선 방법", "output_format": "최적화 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "비유적 맥락 설정: 요리 레시피 비유를 활용한 학습 목적 명시",
        "구체적 요청사항: 구조, 예시, 실용적 적용법 등 세부 요소 요청",
        "시각적 형식 지정: 요리 레시피 형식을 활용한 프롬프트 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트를 요리 레시피처럼 구성하면 직관적으로 이해하고 작성하기 쉬워집니다",
    "프롬프트의 '재료'는 맥락, 정보, 예시 등이며, '조리법'은 지시사항과 원하는 결과의 형식입니다",
    "목적에 따라 레시피의 구조와 요소를 조정하면 다양한 프롬프트를 체계적으로 구성할 수 있습니다",
    "레시피 관점은 프롬프트의 구성 요소와 흐름을 시각화하는 데 도움이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 셰프", 
        "프롬프트 작성을 요리 레시피에 비유하여 이해하기 쉽게 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 처음 배우는 대학생입니다. {topic}에 대해 배우고 있습니다. "
        f"요리를 좋아하는 초보자로서, 프롬프트 작성을 요리 레시피에 비유하여 이해하고 싶습니다. "
        f"이론적인 설명보다는 요리 레시피 비유를 통해 직관적으로 이해할 수 있게 도와주세요."
    )
    
    # 구체적인 지시사항 추가
    if "레시피 구조" in topic:
        builder.add_instructions([
            "프롬프트를 레시피처럼 구성하는 기본 구조를 명확히 설명해주세요",
            "레시피의 구성 요소(재료, 준비물, 조리 단계 등)와 프롬프트 요소의 연관성을 설명해주세요",
            "실제 요리 레시피 구조를 활용한 프롬프트 템플릿을 제공해주세요",
            "레시피 구조를 사용했을 때와 그렇지 않았을 때의 결과 차이를 비교 예시로 보여주세요",
            "초보자가 바로 활용할 수 있는 간단한 프롬프트 레시피 템플릿 3가지를 제공해주세요"
        ])
    elif "재료와 조리법" in topic:
        builder.add_instructions([
            "프롬프트의 '재료'에 해당하는 요소들을 구체적으로 설명해주세요",
            "프롬프트의 '조리법'에 해당하는 요소들을 구체적으로 설명해주세요",
            "재료(맥락, 정보, 예시 등)와 조리법(지시사항, 형식 요청 등)의 균형을 맞추는 방법을 알려주세요",
            "다양한 유형의 프롬프트에 필요한 핵심 '재료'와 '조리법'을 유형별로 설명해주세요",
            "재료와 조리법 관점에서 좋은 프롬프트와 부족한 프롬프트의 예시를 비교해주세요"
        ])
    elif "레시피 예시" in topic:
        builder.add_instructions([
            "다양한 목적(정보 요청, 창작, 분석, 요약 등)에 맞는 프롬프트 레시피 예시를 최소 4가지 제공해주세요",
            "각 레시피 예시에서 '재료'와 '조리법'에 해당하는 부분을 명확히 구분하고 설명해주세요",
            "실제 요리 레시피 형식(재료 목록, 준비 시간, 조리 단계 등)을 활용하여 프롬프트 예시를 구성해주세요",
            "레시피 예시마다 기대할 수 있는 '요리 결과'(AI 응답)의 특징도 설명해주세요",
            "초보자가 자신의 목적에 맞게 레시피를 선택하고 응용할 수 있는 가이드라인을 제공해주세요"
        ])
    elif "레시피 변형" in topic:
        builder.add_instructions([
            "기본 프롬프트 레시피를 다양한 목적에 맞게 변형하는 방법을 설명해주세요",
            "하나의 기본 레시피를 3-4가지 다른 용도로 변형한 예시를 보여주세요",
            "레시피 변형 시 고려해야 할 핵심 요소와 변형 원칙을 설명해주세요",
            "'재료' 변경과 '조리법' 변경이 결과에 미치는 영향을 구체적인 예시와 함께 설명해주세요",
            "자신만의 프롬프트 레시피 변형을 개발하는 단계별 접근법을 제시해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 개념을 요리 레시피 비유를 활용해 이해하기 쉽게 설명해주세요",
            "실제 요리 레시피의 구성 요소와 프롬프트 요소를 연결하는 비유를 구체적으로 제시해주세요",
            "초보자가 바로 적용할 수 있는 실용적인 예시와 템플릿을 제공해주세요",
            "흔한 실수와 그 해결책을 '요리 실패와 해결법' 관점에서 설명해주세요",
            "이 접근법의 장점과 한계도 함께 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"요리 레시피 형식(재료 목록, 준비 시간, 조리 단계 등)을 활용하여 프롬프트 구성 요소를 시각화해주세요. "
        f"프롬프트 예시는 실제 레시피 형식으로 제시하고, 각 부분이 어떤 역할을 하는지 설명해주세요. "
        f"시각적 명확성을 위해 표, 구분선, 강조 표시 등을 적절히 활용해주세요. "
        f"초보자가 재미있게 이해할 수 있도록 친근하고 직관적인 표현을 사용해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="요리 레시피 관점으로 프롬프트 구성하기",
        topic_options=RECIPE_APPROACH_TOPICS,
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