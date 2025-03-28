"""
기초 정보에서 심화 정보로 실습 모듈

Part 1 - 섹션 1.3.3 실습 코드: 기초 수준의 정보에서 시작하여 
단계적으로 심화된 정보를 요청하는 방법을 학습합니다.
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
ADVANCED_INFORMATION_TOPICS = {
    "1": {"name": "단계적 심화", "topic": "기초에서 심화 정보로 발전하는 단계적 정보 요청 전략", "output_format": "가이드"},
    "2": {"name": "계층적 접근", "topic": "복잡한 주제를 위한 계층적 학습 접근법", "output_format": "프레임워크"},
    "3": {"name": "전문 정보 요청", "topic": "전문적 수준의 심화 정보를 요청하는 효과적인 방법", "output_format": "전략 가이드"},
    "4": {"name": "다차원 탐색", "topic": "주제의 다양한 차원을 심층적으로 탐색하는 방법", "output_format": "접근법"},
    "5": {"name": "정보 통합", "topic": "다양한 수준과 차원의 정보를 통합하는 전략", "output_format": "통합 방법론"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 단계적/심화 학습 목표 설정",
        "구체적 요청: 지식 수준별 정보 요청 전략 요청",
        "실용적 구성: 템플릿과 적용 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "단계적으로 정보를 심화시키는 접근법은 효과적인 학습과 지식 구축에 핵심입니다",
    "자신의 현재 지식 수준에 맞는 정보 요청 전략을 선택하면 학습 효율성이 높아집니다",
    "복잡한 주제는 계층적 구조로 접근하면 더 체계적으로 이해할 수 있습니다",
    "다양한 차원(이론적, 실용적, 비판적, 학제간 등)에서 주제를 탐색하면 종합적 이해가 가능합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "심화 학습 전략가", 
        "기초 지식에서 전문적 수준으로 효과적으로 발전하는 학습 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"처음에는 기초적인 개념을 익히고, 점진적으로 더 심화된 지식으로 나아가는 효과적인 방법을 배우고 싶습니다. "
        f"AI와의 대화에서 체계적으로 지식을 심화시키고 복잡한 주제를 효과적으로 탐색하는 전략이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "단계적 심화" in topic:
        builder.add_instructions([
            "기초에서 심화 정보로 발전하는 단계적 접근법의 핵심 원칙과 이점을 설명해주세요",
            "초보자, 중급자, 고급자 수준별로 적합한 정보 요청 전략과 템플릿을 제공해주세요",
            "각 단계에서 효과적으로 정보를 요청하는 구체적인 프롬프트 예시를 포함해주세요",
            "단계별 진행 과정에서 이해도를 평가하고 다음 단계로 넘어가는 기준을 제시해주세요",
            "단계적 정보 요청 전략을 실제 학습 상황에 적용하는 방법과 예시를 제공해주세요"
        ])
    elif "계층적 접근" in topic:
        builder.add_instructions([
            "복잡한 주제를 계층적 구조로 접근하는 방법과 이점을 설명해주세요",
            "지식을 기초, 중간, 심화 층위로 구조화하는 구체적인 방법을 제시해주세요",
            "계층적 정보 요청을 위한 단계별 전략과 프롬프트 템플릿을 제공해주세요",
            "주제의 전체 구조를 파악하고 하위 영역 간의 관계를 이해하는 방법을 설명해주세요",
            "계층적 접근법을 다양한 학문 분야(과학, 인문학, 사회과학 등)에 적용하는 예시를 제공해주세요"
        ])
    elif "전문 정보 요청" in topic:
        builder.add_instructions([
            "전문적 수준의 심화 정보를 효과적으로 요청하는 방법과 전략을 설명해주세요",
            "학술 연구, 기술/전문 분야, 분석적/비판적 접근 등 다양한 측면에서의 전문 정보 요청 기법을 제시해주세요",
            "전문가 수준의 지식에 접근하기 위한 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "심화 정보를 요청할 때 흔히 발생하는 장애물과 이를 극복하기 위한 전략을 설명해주세요",
            "전문적 심화 정보 요청 기법을 실제 연구나 프로젝트에 적용하는 예시를 포함해주세요"
        ])
    elif "다차원 탐색" in topic:
        builder.add_instructions([
            "주제의 다양한 차원(이론적, 실용적, 비판적, 학제간, 역사적 등)을 심층적으로 탐색하는 방법을 설명해주세요",
            "각 차원별 탐색을 위한 구체적인 질문 전략과 프롬프트 템플릿을 제공해주세요",
            "다차원적 이해를 위한 체계적인 접근법과 단계를 제시해주세요",
            "다양한 차원의 탐색을 통해 얻을 수 있는 고유한 통찰과 이점을 분석해주세요",
            "다차원 탐색 접근법을 실제 학습이나 연구에 적용하는 사례와 예시를 포함해주세요"
        ])
    elif "정보 통합" in topic:
        builder.add_instructions([
            "다양한 수준과 차원에서 수집한 정보를 효과적으로 통합하는 방법과 전략을 설명해주세요",
            "심화 정보를 조직화하고 구조화하는 다양한 방법(계층적 지식 맵, 개념 연결망, 통합 프레임워크 등)을 제시해주세요",
            "통합적 이해를 형성하기 위한 체계적인 접근법과 단계를 설명해주세요",
            "다양한 관점과 정보를 비교, 대조, 종합하는 구체적인 기법을 제공해주세요",
            "정보 통합 전략을 실제 학습이나 연구 상황에 적용하는 사례와 예시를 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 효과적인 접근법을 설명해주세요",
            "기초 정보에서 심화 정보로 발전하는 자연스러운 진행 과정과 전략을 제시해주세요",
            "다양한 수준과 차원에서 정보를 요청하고 통합하는 방법을 설명해주세요",
            "효과적인 심화 학습을 위한 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "이러한 전략을 실제 학습 상황에 적용하는 방법과 사례를 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"주요 전략과 접근법을 체계적으로 분류하고, 각 접근법별 구체적인 예시와 템플릿을 제공해주세요. "
        f"실제 활용 가능한 프롬프트 템플릿은 코드 블록으로 구분하여 명확히 제시해주세요. "
        f"단계별 접근법이나 프레임워크는 시각적으로 이해하기 쉽게 표나 다이어그램 형태로 표현해주세요. "
        f"모든 내용은 대학생이 바로 적용할 수 있도록 실용적이고 명확하게 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="기초 정보에서 심화 정보로",
        topic_options=ADVANCED_INFORMATION_TOPICS,
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