"""
후속 질문을 통한 심화 탐색 실습 모듈

Part 1 - 섹션 1.3.2 실습 코드: 초기 이해 후 후속 질문을 통해 
주제를 더 깊이 탐색하는 방법을 학습합니다.
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
FOLLOW_UP_QUESTIONS_TOPICS = {
    "1": {"name": "정보 격차 식별", "topic": "효과적인 후속 질문을 위한 정보 격차 식별 방법", "output_format": "가이드"},
    "2": {"name": "질문 추천 요청", "topic": "AI에게 후속 질문 추천을 요청하는 효과적인 방법", "output_format": "전략 가이드"},
    "3": {"name": "질문 체인 구성", "topic": "체계적인 이해를 위한 질문 체인 구성 방법", "output_format": "프레임워크"},
    "4": {"name": "심화 정보 요청", "topic": "기초에서 심화 정보로 발전하기 위한 질문 전략", "output_format": "단계별 가이드"},
    "5": {"name": "종합적 이해", "topic": "다양한 관점을 통합하는 후속 질문 접근법", "output_format": "통합 방법론"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 후속 질문의 목표와 활용 방법 명시",
        "구체적 요청: 다양한 유형의 후속 질문 전략 요청",
        "실용적 구성: 즉시 적용 가능한 예시와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "초기 질문 후 정보 격차를 식별하여 후속 질문을 구성하면 이해를 심화할 수 있습니다",
    "AI에게 '더 알려면 무엇을 물어야 할까요?'라고 요청하면 효과적인 후속 질문 방향을 얻을 수 있습니다",
    "체계적인 질문 체인을 구성하면 주제를 더 포괄적이고 심도 있게 이해할 수 있습니다",
    "다양한 유형의 후속 질문을 활용하면 주제의 다양한 측면을 균형 있게 탐색할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "후속 질문 전략가", 
        "효과적인 후속 질문 전략과 심화 탐색 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"초기 질문 이후에 주제를 더 깊이 이해하기 위한 효과적인 후속 질문 방법을 배우고 싶습니다. "
        f"AI와의 대화에서 단순한 정보 수집을 넘어 심화된 이해를 얻기 위한 전략적 접근법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "정보 격차 식별" in topic:
        builder.add_instructions([
            "초기 응답에서 다양한 유형의 정보 격차(개념적, 깊이, 맥락, 증거, 응용 등)를 식별하는 방법을 설명해주세요",
            "각 유형의 정보 격차에 대응하는 효과적인 후속 질문 유형과 구성 방법을 제시해주세요",
            "정보 격차 식별을 위한 체계적인 응답 분석 프레임워크나 체크리스트를 제안해주세요",
            "다양한 주제 영역(과학, 인문학, 사회과학, 비즈니스 등)에 따라 정보 격차 식별 전략이 어떻게 달라질 수 있는지 설명해주세요",
            "정보 격차 식별과 후속 질문 구성의 실제 예시를 여러 분야에서 제공해주세요"
        ])
    elif "질문 추천 요청" in topic:
        builder.add_instructions([
            "AI에게 후속 질문을 추천해달라고 요청하는 다양한 방법과 접근법을 설명해주세요",
            "다양한 목적(기초 이해, 심화 탐색, 응용 학습 등)에 맞는 질문 추천 요청 템플릿을 제공해주세요",
            "AI의 질문 추천을 최대한 활용하기 위한 전략적 접근법을 제시해주세요",
            "AI가 추천한 질문들을 효과적으로 분류, 평가, 선택하는 방법을 설명해주세요",
            "질문 추천 요청 과정에서 흔히 발생하는 문제나 한계점과 이를 극복하는 방법도 포함해주세요"
        ])
    elif "질문 체인 구성" in topic:
        builder.add_instructions([
            "주제 탐색을 위한 다양한 유형의 질문 체인(선형, 분지형, 통합형 등)을 설명하고 각각의 특징과 적합한 상황을 분석해주세요",
            "효과적인 질문 체인을 설계하기 위한 단계별 접근법과 원칙을 제시해주세요",
            "다양한 질문 유형(명확화, 깊이, 확장, 응용, 비교, 통합 질문 등)을 질문 체인에 통합하는 방법을 설명해주세요",
            "학습 목표와 주제 특성에 맞는 맞춤형 질문 체인을 구성하는 방법론을 제공해주세요",
            "질문 체인의 실제 적용 사례와 함께 각 질문이 어떻게 연결되고 이해를 심화시키는지 보여주는 예시를 포함해주세요"
        ])
    elif "심화 정보 요청" in topic:
        builder.add_instructions([
            "기초적인 이해에서 중급, 고급 수준으로 발전하기 위한 단계적 질문 전략을 설명해주세요",
            "지식 수준별(초보, 중급, 고급)로 적합한 질문 유형과 접근법을 제시해주세요",
            "복잡한 개념이나 주제를 심화 탐색할 때 활용할 수 있는 체계적인 질문 프레임워크를 제공해주세요",
            "분야별(과학기술, 인문학, 사회과학, 예술 등)로 최적화된 심화 탐색 질문 전략을 제안해주세요",
            "심화 정보 요청 시 흔히 발생하는 장애물과 이를 극복하기 위한 팁도 포함해주세요"
        ])
    elif "종합적 이해" in topic:
        builder.add_instructions([
            "다양한 관점과 측면을 통합하여 주제에 대한 종합적 이해를 형성하기 위한 질문 전략을 설명해주세요",
            "서로 다른 이론, 접근법, 관점을 비교하고 통합하는 효과적인 질문 방법을 제시해주세요",
            "복잡한 주제의 다양한 차원(이론적, 역사적, 실용적, 윤리적 측면 등)을 탐색하는 균형 잡힌 질문 프레임워크를 제안해주세요",
            "통합적 사고와 비판적 분석을 촉진하는 후속 질문 구성 방법을 설명해주세요",
            "종합적 이해 형성을 위한 질문 전략의 실제 적용 사례와 성공 요인을 분석해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 효과적인 접근법을 설명해주세요",
            "초기 질문에서 후속 질문으로 발전하는 자연스러운 진행 과정과 전략을 제시해주세요",
            "다양한 유형의 후속 질문과 각각의 목적 및 활용 방법을 설명해주세요",
            "후속 질문을 통한 심화 학습의 실제 사례와 성공 요인을 분석해주세요",
            "후속 질문 전략을 실제 학습 상황에 적용하기 위한 실용적인 팁과 가이드를 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"주요 전략과 접근법을 체계적으로 분류하고, 각 접근법별 구체적인 예시와 템플릿을 제공해주세요. "
        f"실제 대화 예시를 통해 후속 질문 전략의 적용 방법을 보여주는 것도 도움이 될 것입니다. "
        f"단계별 접근법이나 프레임워크는 시각적으로 이해하기 쉽게 표나 다이어그램 형태로 표현해주세요. "
        f"모든 내용은 대학생이 바로 적용할 수 있도록 실용적이고 명확하게 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="후속 질문을 통한 심화 탐색",
        topic_options=FOLLOW_UP_QUESTIONS_TOPICS,
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