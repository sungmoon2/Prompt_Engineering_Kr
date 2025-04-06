"""
효과적인 역할 설정의 원칙 실습 모듈

Part 7 - 섹션 7.1.1 실습 코드: 효과적인 역할 설정 원칙을 학습하고 
다양한 역할 구체화 및 최적화 기법을 실습합니다.
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
ROLE_SETTING_TOPICS = {
    "1": {"name": "역할 구체화", "topic": "일반적 역할의 단계별 구체화", "output_format": "구체화 가이드"},
    "2": {"name": "역할-과제 정합성", "topic": "과제에 최적화된 역할 설정", "output_format": "역할 매핑 가이드"},
    "3": {"name": "역할 신뢰성", "topic": "신뢰할 수 있는 역할 설정 원칙", "output_format": "신뢰성 체크리스트"},
    "4": {"name": "맥락 풍부화", "topic": "역할에 맥락 정보 추가 방법", "output_format": "맥락화 프레임워크"},
    "5": {"name": "역할 설정 함정", "topic": "흔한 역할 설정 오류와 개선 방법", "output_format": "문제 해결 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["역할 설정에 대한 일반적인 정보 요청"],
    "enhanced": [
        "전문가 역할 설정: 프롬프트 엔지니어링 전문가 페르소나 부여",
        "구체적 요청: 체계적인 가이드라인과 실용적 예시 요청",
        "구조화 요소: 원칙, 방법론, 예시, 실습 활동 등 명확한 구조 지정",
        "맥락 설정: 교육 및 실습 목적과 대상 청중 명시"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 역할 설정은 프롬프트 응답의 품질과 관련성을 크게 향상시킵니다",
    "역할의 구체성, 정합성, 신뢰성, 맥락화는 효과적인 역할 설정의 핵심 원칙입니다",
    "과제와 직접적으로 관련된 전문성을 가진 역할을 선택하는 것이 중요합니다",
    "과도한 과장, 모호함, 불일치 등의 함정을 피해야 효과적인 역할 설정이 가능합니다",
    "역할을 단계적으로 구체화하고 맥락 정보를 추가하면 더 풍부하고 맞춤화된 응답을 얻을 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 엔지니어링 전문가", 
        "AI와의 효과적인 커뮤니케이션을 위한 프롬프트 최적화와 역할 설정에 특화된 전문가로, 다양한 분야의 AI 응용 프로젝트에서 고품질 결과를 이끌어내는 프롬프팅 전략을 개발하고 가르쳐온 경험이 있습니다. 특히 역할 기반 프롬프팅 기법의 효과적인 적용과 최적화에 깊은 전문성을 갖추고 있습니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우고 있는 학생으로, 특히 {topic}에 관심이 있습니다. "
        f"AI와의 상호작용에서 더 효과적인 결과를 얻기 위한 역할 설정 원칙과 방법을 체계적으로 "
        f"이해하고 실제로 적용해보고 싶습니다. 이론적 원칙뿐만 아니라 실용적인 가이드라인과 "
        f"구체적인 예시, 그리고 직접 실습해볼 수 있는 활동이 포함된 종합적인 안내가 필요합니다."
    )
    
    # 주제별 구체적인 지시사항 추가
    if "구체화" in topic:
        builder.add_instructions([
            "일반적인 역할을 단계적으로 구체화하는 체계적인 방법을 설명해주세요",
            "구체화에 필요한 핵심 요소(경력, 전문 영역, 성과, 맥락 등)를 상세히 설명해주세요",
            "다양한 분야(교육, 기술, 의료, 비즈니스 등)의 역할 구체화 예시를 제공해주세요",
            "일반적 역할과 구체화된 역할의 효과 차이를 보여주는 비교 예시를 포함해주세요",
            "역할 구체화를 위한 단계별 워크플로우와 실습 활동도 제안해주세요"
        ])
    elif "정합성" in topic:
        builder.add_instructions([
            "과제 유형별 최적화된 역할 설정을 위한 체계적인 접근법을 설명해주세요",
            "과제-역할 정합성의 중요성과 부적합한 역할 선택의 영향을 설명해주세요",
            "다양한 과제 유형(정보 제공, 분석, 창작, 교육, 문제 해결 등)에 적합한 역할 매핑 가이드를 제공해주세요",
            "역할-과제 정합성을 평가하는 프레임워크나 체크리스트를 개발해주세요",
            "과제 요구사항을 분석하여 최적의 역할을 선택하는 실습 활동도 제안해주세요"
        ])
    elif "신뢰성" in topic:
        builder.add_instructions([
            "역할 설정에서 신뢰성의 중요성과 신뢰성 있는 역할의 특성을 설명해주세요",
            "신뢰성을 높이는 구체적인 방법과 기법을 단계별로 안내해주세요",
            "과장과 신뢰성 사이의 적절한 균형을 찾는 방법을 설명해주세요",
            "다양한 분야에서 신뢰할 수 있는 역할 설정의 예시와 반례를 제공해주세요",
            "역할 설정의 신뢰성을 평가하고 개선하기 위한 체크리스트와 실습 활동도 포함해주세요"
        ])
    elif "맥락 풍부화" in topic:
        builder.add_instructions([
            "역할에 맥락 정보를 추가하는 중요성과 효과를 설명해주세요",
            "역할 맥락화에 포함할 수 있는 다양한 요소(청중, 목적, 환경, 제약 등)를 상세히 설명해주세요",
            "다양한 상황과 목적에 맞는 맥락 정보 추가 예시를 제공해주세요",
            "맥락이 없는 역할과 풍부한 맥락이 있는 역할의 효과 차이를 보여주는 비교 예시를 포함해주세요",
            "효과적인 맥락 정보 추가를 위한 프레임워크와 실습 활동도 제안해주세요"
        ])
    elif "함정" in topic:
        builder.add_instructions([
            "역할 설정에서 흔히 범하는 실수와 함정을 유형별로 분류하고 설명해주세요",
            "각 함정 유형(과장, 모호함, 불일치, 복잡화 등)의 구체적인 사례와 그 영향을 분석해주세요",
            "각 함정을 피하고 개선하는 구체적인 방법과 지침을 제공해주세요",
            "문제가 있는 역할 설정과 개선된 역할 설정을 비교하는 before/after 예시를 포함해주세요",
            "자신의 역할 설정에서 함정을 식별하고 개선하는 실습 활동도 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 체계적이고 실용적인 가이드를 제공해주세요",
            "핵심 원칙과 개념을 명확히 설명해주세요",
            "다양한 실제 예시를 통해 개념을 구체화해주세요",
            "효과적인 적용을 위한 단계별 접근법을 제시해주세요",
            "실습해볼 수 있는 활동이나 연습도 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"이론적 설명과 실용적 응용을 균형 있게 포함하고, 다양한 분야의 구체적인 예시를 통해 개념을 명확히 해주세요. "
        f"표나 비교 차트를 활용하여 정보를 시각적으로 구조화하고, 단계별 적용 방법을 명확히 제시해주세요. "
        f"마지막에는 '실습 활동' 섹션을 포함하여 배운 개념을 직접 적용해볼 수 있는 1-2개의 구체적인 연습 활동을 제안해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="효과적인 역할 설정의 원칙",
        topic_options=ROLE_SETTING_TOPICS,
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