"""
정보 수집과 정제의 기술 실습 모듈

Part 1 - 섹션 1.3 실습 코드: 효과적으로 정보를 수집하고 정제하는 프롬프트 작성 방법을 학습합니다.
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
INFO_GATHERING_TOPICS = {
    "1": {"name": "주제 탐색", "topic": "새로운 주제 탐색을 위한 초기 질문 방법", "output_format": "질문 가이드"},
    "2": {"name": "정보 수집", "topic": "체계적인 정보 수집 전략", "output_format": "수집 프레임워크"},
    "3": {"name": "정보 정제", "topic": "수집된 정보 분석 및 정제 방법", "output_format": "정제 가이드"},
    "4": {"name": "지식 구조화", "topic": "수집된 정보의 효과적인 구조화 방법", "output_format": "구조화 템플릿"},
    "5": {"name": "후속 질문", "topic": "더 깊은 이해를 위한 후속 질문 기법", "output_format": "질문 전략"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 정보 수집과 정제 목적 설정",
        "구체적 요청: 체계적 접근법과 구조화된 방법론 요청",
        "실용적 형식: 즉시 적용 가능한 예시와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 정보 수집은 명확한 목적과 체계적인 접근법이 중요합니다",
    "초기 질문은 광범위한 탐색부터 시작하여 점차 구체화하는 것이 효과적입니다",
    "수집된 정보는 분석, 분류, 우선순위화 과정을 통해 정제해야 합니다",
    "구조화된 정보는 이해와 활용이 더 용이하며 후속 학습의 기반이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "정보 전략가", 
        "효과적인 정보 수집, 분석, 정제, 구조화 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 배우고 싶은 대학생입니다. "
        f"학술 연구와 프로젝트를 위해 효과적으로 정보를 수집하고 정제하는 방법을 알고 싶습니다. "
        f"AI를 활용해 체계적으로 정보를 수집하고 구조화하는 실용적인 전략이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "주제 탐색" in topic:
        builder.add_instructions([
            "새로운 주제를 탐색할 때 효과적인 초기 질문 방법과 원칙을 설명해주세요",
            "주제에 대한 기본 이해를 위한 5W1H 질문 프레임워크를 제시해주세요",
            "초기 질문에서 피해야 할 함정과 오류를 알려주세요",
            "다양한 분야(인문학, 과학, 기술, 사회과학 등)별로 효과적인 초기 질문 예시를 제공해주세요",
            "초기 질문에서 얻은 응답을 바탕으로 탐색 방향을 조정하는 방법도 설명해주세요"
        ])
    elif "정보 수집" in topic:
        builder.add_instructions([
            "체계적인 정보 수집을 위한 단계별 접근법을 설명해주세요",
            "다양한 유형의 정보를 효율적으로 수집하기 위한 질문 템플릿을 제공해주세요",
            "정보 수집 시 고려해야 할 정보의 다양성, 깊이, 관련성 측면을 설명해주세요",
            "복잡한 주제를 더 작은 하위 주제로 분해하여 정보를 수집하는 방법을 알려주세요",
            "정보 수집 과정에서 객관성과 다양한 관점을 유지하는 방법도 포함해주세요"
        ])
    elif "정보 정제" in topic:
        builder.add_instructions([
            "수집된 정보를 분석하고 정제하는 체계적인 방법을 설명해주세요",
            "관련성, 신뢰성, 최신성 등에 따라 정보를 평가하는 기준을 제시해주세요",
            "핵심 정보와 부가 정보를 구분하고 우선순위를 정하는 방법을 알려주세요",
            "정보 간의 관계와 패턴을 발견하는 분석 기법을 설명해주세요",
            "AI와의 대화에서 얻은 정보를 검증하고 보완하는 방법도 포함해주세요"
        ])
    elif "지식 구조화" in topic:
        builder.add_instructions([
            "수집된 정보를 효과적으로 구조화하는 다양한 방법과 템플릿을 제공해주세요",
            "마인드맵, 개념도, 매트릭스 등 다양한 구조화 도구의 장단점과 적합한 상황을 설명해주세요",
            "복잡한 정보를 계층적으로 구성하는 방법과 원칙을 알려주세요",
            "정보 간의 관계와 연결성을 시각화하는 방법을 제안해주세요",
            "구조화된 정보를 효과적으로 저장하고 검색하는 방법도 포함해주세요"
        ])
    elif "후속 질문" in topic:
        builder.add_instructions([
            "더 깊은 이해를 위한 효과적인 후속 질문 기법과 원칙을 설명해주세요",
            "초기 응답을 바탕으로 더 구체적이고 심층적인 질문을 생성하는 방법을 알려주세요",
            "다양한 질문 유형(개방형/폐쇄형, 탐색형/확인형 등)의 특징과 적절한 활용 시기를 설명해주세요",
            "질문 체인을 구성하여 점진적으로 깊이 있는 이해를 달성하는 방법을 제시해주세요",
            "다양한 학문 분야에 적합한 후속 질문 예시와 템플릿을 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "단계별 방법론과 구체적인 예시를 포함해주세요",
            "초보자가 쉽게 적용할 수 있는 템플릿이나 프레임워크를 제공해주세요",
            "일반적인 함정이나 오류와 이를 피하는 방법을 설명해주세요",
            "다양한 학문 분야에 적용할 수 있는 범용적인 전략과 특정 분야에 특화된 전략을 모두 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"핵심 개념과 원칙은 굵은 글씨로 강조하고, 예시는 인용 형식이나 별도 박스로 구분해주세요. "
        f"단계별 접근법은 번호를 매겨 명확히 구분해주세요. "
        f"적용 가능한 템플릿이나 프레임워크는 실제 사용할 수 있는 형태로 제공해주세요. "
        f"시각적 이해를 돕기 위한 표, 다이어그램 구조 등도 포함해주세요. "
        f"학생이 실제 연구나 프로젝트에 바로 적용할 수 있는 실용적인 내용을 중심으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="정보 수집과 정제의 기술",
        topic_options=INFO_GATHERING_TOPICS,
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