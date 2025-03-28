"""
낯선 주제 단계적 이해 실습 모듈

Part 1 - 섹션 1.4.2 실습 코드: 전문 지식이 없는 낯선 주제를 단계적으로 이해하는 방법을 학습합니다.
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
    "1": {"name": "양자 컴퓨팅", "topic": "양자 컴퓨팅의 기본 개념과 원리", "output_format": "학습 가이드"},
    "2": {"name": "생물정보학", "topic": "생물정보학의 핵심 원리와 응용", "output_format": "개념 설명"},
    "3": {"name": "블록체인", "topic": "블록체인 기술의 작동 원리와 활용", "output_format": "단계별 가이드"},
    "4": {"name": "기후 모델링", "topic": "기후 변화 예측 모델의 기본 원리", "output_format": "이해 프레임워크"},
    "5": {"name": "행동경제학", "topic": "행동경제학의 주요 개념과 실생활 적용", "output_format": "학습 로드맵"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 맥락 제공: 초보자 관점과 단계적 학습 목표 설정",
        "구체적 요청: 기초 개념부터 심화 개념까지의 체계적 설명 요청",
        "학습 구조화: 내용의 계층적 구성과 시각적 요소 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "낯선 주제는 처음부터 깊이 이해하려 하기보다는 단계적으로 접근하는 것이 효과적입니다",
    "기초 개념과 용어를 먼저 이해하는 것이 복잡한 개념을 학습하는 데 중요한 기반이 됩니다",
    "비유와 친숙한 예시를 활용하면 복잡한 개념을 직관적으로 이해하는 데 도움이 됩니다",
    "주제를 여러 계층으로 나누어 접근하면 복잡성을 관리하고 체계적으로 이해할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "교육 전문가", 
        "복잡한 주제를 초보자도 이해하기 쉽게 설명하는 전문 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 전혀 배경 지식이 없는 대학생입니다. "
        f"이 주제에 관심이 생겨서 기초부터 차근차근 이해하고 싶습니다. "
        f"전문 용어와 복잡한 개념 때문에 진입 장벽을 느끼고 있어, 단계적으로 접근할 수 있는 안내가 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "양자 컴퓨팅" in topic:
        builder.add_instructions([
            "양자 컴퓨팅의 가장 기본적인 개념부터 시작하여 단계적으로 설명해주세요",
            "일반 컴퓨팅과 양자 컴퓨팅의 핵심 차이점을 비유와 예시를 통해 설명해주세요",
            "큐비트, 중첩, 얽힘 등 핵심 용어를 비전문가도 이해할 수 있게 풀어서 설명해주세요",
            "양자 컴퓨팅의 가능성과 현재 기술적 한계에 대해 균형 있게 설명해주세요",
            "더 깊이 학습하기 위한 단계별 로드맵과 접근 방법을 제안해주세요"
        ])
    elif "생물정보학" in topic:
        builder.add_instructions([
            "생물정보학의 기본 개념과 목적을 비전문가도 이해할 수 있게 설명해주세요",
            "DNA, 단백질 서열 분석 등 핵심 분야를 쉬운 비유와 예시로 설명해주세요",
            "생물학과 컴퓨터 과학/정보학이 어떻게 융합되는지 설명해주세요",
            "생물정보학에서 사용되는 기본적인 알고리즘과 도구의 원리를 간단히 소개해주세요",
            "이 분야를 단계적으로 학습하기 위한 접근법과 필수 기초 지식을 안내해주세요"
        ])
    elif "블록체인" in topic:
        builder.add_instructions([
            "블록체인의 기본 개념과 작동 원리를 비유와 예시를 통해 쉽게 설명해주세요",
            "해시 함수, 분산 원장, 합의 알고리즘 등 핵심 개념을 단계적으로 설명해주세요",
            "블록체인의 주요 특성(투명성, 불변성, 탈중앙화 등)과 그 의미를 설명해주세요",
            "암호화폐와 블록체인의 관계, 그리고 블록체인의 다양한 활용 사례를 소개해주세요",
            "블록체인을 더 깊이 이해하기 위한 학습 경로와 필수 배경 지식을 안내해주세요"
        ])
    elif "기후 모델링" in topic:
        builder.add_instructions([
            "기후 모델링의 기본 개념과 목적을 비전문가도 이해할 수 있게 설명해주세요",
            "날씨 예보와 기후 모델링의 차이점을 명확하게 설명해주세요",
            "기후 모델에 포함되는 주요 요소(대기, 해양, 육지 등)와 그 상호작용을 설명해주세요",
            "기후 변화 시나리오와 예측이 어떻게 생성되는지 기본 원리를 설명해주세요",
            "기후 모델링의 한계와 불확실성, 그리고 이 분야를 단계적으로 학습하는 방법을 안내해주세요"
        ])
    elif "행동경제학" in topic:
        builder.add_instructions([
            "행동경제학의 기본 개념과 전통적 경제학과의 차이점을 쉽게 설명해주세요",
            "인간의 비합리적 행동 패턴과 그것이 경제적 의사결정에 미치는 영향을 예시와 함께 설명해주세요",
            "휴리스틱, 편향, 프레이밍 효과 등 주요 개념을 일상생활 사례와 함께 설명해주세요",
            "행동경제학의 주요 연구와 발견, 그리고 실생활 및 정책에의 적용 사례를 소개해주세요",
            "행동경제학을 단계적으로 학습하기 위한 접근법과 필수 배경 지식을 안내해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 가장 기본적인 개념과 원리를 비전문가도 이해할 수 있게 설명해주세요",
            "핵심 용어와 개념을 일상적인 비유와 예시를 통해 설명해주세요",
            "해당 분야의 중요성과 실제 응용 사례를 소개해주세요",
            "이 주제를 이해하기 위해 필요한 배경 지식과 단계적 학습 경로를 안내해주세요",
            "초보자가 흔히 겪는 어려움과 그 극복 방법도 함께 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"내용을 난이도에 따라 '입문 단계', '기초 단계', '심화 단계'로 구분하여 구성해주세요. "
        f"핵심 용어는 처음 등장할 때 굵은 글씨로 강조하고 간단한 정의를 함께 제공해주세요. "
        f"복잡한 개념은 일상생활의 비유나 예시를 통해 직관적으로 이해할 수 있게 설명해주세요. "
        f"가능하면 내용을 시각화할 수 있는 다이어그램이나 표를 포함해주세요. "
        f"마지막에는 '다음 학습 단계'를 제안하여 심화 학습 방향을 안내해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="낯선 주제 단계적 이해",
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