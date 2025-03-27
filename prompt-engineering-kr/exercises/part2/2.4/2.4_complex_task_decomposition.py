"""
낯선 주제 탐색하기 실습 모듈

Part 2 - 섹션 2.4 실습 코드: 낯선 주제를 단계적으로 이해하고 체계적으로 탐색하는 방법을 실습합니다.
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
UNFAMILIAR_TOPICS = {
    "1": {"name": "양자 컴퓨팅", "topic": "양자 컴퓨팅의 기본 원리와 응용", "output_format": "개념 설명"},
    "2": {"name": "게임 이론", "topic": "경제학과 의사결정에서의 게임 이론", "output_format": "입문 가이드"},
    "3": {"name": "신경언어학", "topic": "신경언어학적 프로그래밍(NLP)의 핵심 개념", "output_format": "개념 지도"},
    "4": {"name": "블록체인", "topic": "블록체인 기술의 작동 원리와 응용 분야", "output_format": "기술 개요"},
    "5": {"name": "행동경제학", "topic": "행동경제학의 주요 이론과 실생활 적용", "output_format": "학습 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["낯선 주제에 대한 직접적인 설명 요청"],
    "enhanced": [
        "단계적 접근: 초보자 관점에서 점진적 이해 요청",
        "구조화된 탐색: 핵심 개념과 관계 체계적 분석",
        "실용적 적용: 실생활 예시와 응용 사례 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "낯선 주제 탐색은 기본 개념과 용어부터 시작하여 점진적으로 이해를 넓혀가는 것이 효과적입니다",
    "복잡한 주제는 더 작은 하위 개념으로 분해하여 구조적으로 접근하는 것이 중요합니다",
    "다양한 비유와 실제 예시를 통해 추상적인 개념을 직관적으로 이해할 수 있습니다",
    "개념 간의 관계와 맥락을 파악하는 것이 단편적 지식보다 깊은 이해를 가능하게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "전문 교육자", 
        "복잡한 개념을 초보자도 이해할 수 있게 명확하고 체계적으로 설명하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 처음 배우는 대학생입니다. "
        f"이 주제는 저에게 완전히 생소하지만, 학기 과제를 위해 빠르게 기본 개념을 이해해야 합니다. "
        f"전문 용어가 많아 혼란스러우며, 어디서부터 공부를 시작해야 할지 모르겠습니다. "
        f"기초부터 체계적으로 이해할 수 있도록 도와주세요."
    )
    
    # 구체적인 지시사항 추가
    if "양자 컴퓨팅" in topic:
        builder.add_instructions([
            "양자 컴퓨팅의 가장 기초적인 개념부터 시작하여 단계적으로 설명해주세요",
            "기존 고전적 컴퓨팅과 양자 컴퓨팅의 핵심 차이점을 쉬운 비유로 설명해주세요",
            "큐비트, 양자 중첩, 양자 얽힘 등 핵심 용어를 초보자도 이해할 수 있게 설명해주세요",
            "양자 컴퓨팅의 실제 응용 분야와 현재 발전 상황을 간략히 소개해주세요",
            "더 깊이 학습하기 위한 단계적 접근법과 초보자에게 적합한 자료를 추천해주세요"
        ])
    elif "게임 이론" in topic:
        builder.add_instructions([
            "게임 이론의 기본 개념과 의미를 일상적인 예시를 통해 설명해주세요",
            "내시 균형, 지배 전략, 죄수의 딜레마 등 핵심 개념을 단계적으로 소개해주세요",
            "게임 이론이 경제학, 정치학, 생물학 등 다양한 분야에 어떻게 적용되는지 예시를 들어주세요",
            "간단한 게임 이론 문제를 통해 실제 분석 방법을 보여주세요",
            "게임 이론적 사고방식을 일상 의사결정에 적용할 수 있는 방법을 제안해주세요"
        ])
    elif "신경언어학" in topic:
        builder.add_instructions([
            "신경언어학적 프로그래밍(NLP)의 기본 정의와 목적을 명확히 설명해주세요",
            "NLP의 핵심 원리와 기본 가정을 초보자 관점에서 이해하기 쉽게 설명해주세요",
            "앵커링, 리프레이밍, 라포 등 주요 기법과 개념을 구체적 예시와 함께 소개해주세요",
            "NLP가 의사소통, 심리치료, 교육, 비즈니스 등에 어떻게 적용되는지 설명해주세요",
            "NLP에 대한 과학적 평가와 비판적 시각도 균형 있게 포함해주세요"
        ])
    elif "블록체인" in topic:
        builder.add_instructions([
            "블록체인 기술의 기본 개념과 작동 원리를 일상적 비유를 통해 설명해주세요",
            "분산 원장, 합의 메커니즘, 암호화 해시 등 핵심 개념을 단계적으로 소개해주세요",
            "블록체인이 어떻게 데이터의 무결성과 신뢰성을 보장하는지 설명해주세요",
            "암호화폐를 넘어선 다양한 블록체인 응용 분야와 사례를 소개해주세요",
            "블록체인 기술의 한계와 과제, 미래 전망에 대해서도 언급해주세요"
        ])
    elif "행동경제학" in topic:
        builder.add_instructions([
            "전통 경제학과 행동경제학의 핵심 차이점을 쉽게 설명해주세요",
            "제한된 합리성, 휴리스틱, 프레이밍 효과 등 주요 개념을 일상 예시와 함께 설명해주세요",
            "노벨상 수상자인 대니얼 카너먼과 리처드 탈러의 주요 연구 내용을 간략히 소개해주세요",
            "행동경제학 원리가 마케팅, 공공정책, 개인 재무 결정 등에 어떻게 적용되는지 보여주세요",
            "행동경제학적 통찰을 활용하여 더 나은 의사결정을 할 수 있는 실용적인 팁을 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 가장 기초적인 개념과 원리를 초보자 관점에서 설명해주세요",
            "핵심 용어와 개념을 일상적인 비유나 예시를 통해 직관적으로 이해할 수 있게 해주세요",
            "주제를 논리적인 하위 영역으로 분류하여 체계적으로 설명해주세요",
            "실제 응용 사례와 현실적 예시를 통해 이론과 실제의 연결성을 보여주세요",
            "더 심화된 학습을 위한 단계적 접근법과 추천 자료를 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"개념을 단계적으로 구성하여 쉬운 내용에서 점차 심화된 내용으로 진행해주세요. "
        f"핵심 용어는 굵은 글씨로 표시하고 간결한 정의를 제공해주세요. "
        f"가능한 경우 비유, 예시, 시각적 설명을 활용하여 추상적 개념을 구체화해주세요. "
        f"개념 간의 관계와 연결성이 드러나도록 구조화해주세요. "
        f"초보자가 다음 단계로 학습을 진행할 수 있는 로드맵도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="낯선 주제 탐색하기",
        topic_options=UNFAMILIAR_TOPICS,
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
