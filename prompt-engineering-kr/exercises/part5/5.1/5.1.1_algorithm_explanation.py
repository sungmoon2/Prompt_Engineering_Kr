"""
프로그래밍 개념 이해 실습 모듈

Part 5 - 섹션 5.1.1 실습 코드: 프로그래밍 개념을 효과적으로 이해하고 설명받는 방법을 학습합니다.
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
PROGRAMMING_CONCEPT_TOPICS = {
    "1": {"name": "객체지향 개념", "topic": "객체지향 프로그래밍의 핵심 개념과 원칙", "output_format": "개념 가이드"},
    "2": {"name": "함수형 프로그래밍", "topic": "함수형 프로그래밍의 주요 패러다임과 기법", "output_format": "학습 가이드"},
    "3": {"name": "비동기 프로그래밍", "topic": "비동기 프로그래밍의 개념과 실제 구현 방법", "output_format": "개념 설명서"},
    "4": {"name": "디자인 패턴", "topic": "소프트웨어 디자인 패턴의 이해와 적용", "output_format": "패턴 가이드"},
    "5": {"name": "알고리즘과 자료구조", "topic": "핵심 알고리즘과 자료구조의 이해", "output_format": "학습 로드맵"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 맥락 제공: 현재 지식 수준과 학습 목표 명시",
        "멀티모달 설명 요청: 비유, 시각화, 코드 예제 등 다양한 형태의 설명 요청",
        "단계적 복잡성: 기본 개념부터 고급 응용까지 단계별 접근 요청",
        "실제 활용 사례: 실무 적용 맥락과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프로그래밍 개념 학습은 자신의 지식 수준과 학습 스타일에 맞는 설명을 요청하는 것이 중요합니다",
    "복잡한 개념은 비유, 시각화, 코드 예제 등 다양한 방식으로 접근하면 이해가 더 깊어집니다",
    "기본 개념부터 실제 응용까지 단계적 복잡성을 통해 체계적으로 학습하는 것이 효과적입니다",
    "개념이 실제로 어떻게 활용되는지 맥락을 이해하면 더 의미 있는 학습이 가능합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "프로그래밍 교육 전문가", 
        "복잡한 프로그래밍 개념을 학습자의 수준과 맥락에 맞게 명확하고 이해하기 쉽게 설명하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프로그래밍을 배우고 있는 학생이며, {topic}에 대해 체계적으로 이해하고 싶습니다. "
        f"프로그래밍 기초는 있지만 {topic}에 대해서는 초보 수준입니다. "
        f"단순히 개념 정의만이 아니라, 실제로 어떻게 동작하고 어떤 상황에서 활용되는지 "
        f"실용적인 측면에서 이해하고 싶습니다. 비유, 예시, 시각적 설명과 함께 "
        f"단계적으로 심화되는 설명이 있으면 더 효과적으로 학습할 수 있을 것 같습니다."
    )
    
    # 주제별 맞춤 지시사항 추가
    if "객체지향" in topic:
        builder.add_instructions([
            "객체지향 프로그래밍의 핵심 개념(캡슐화, 상속, 다형성, 추상화)을 실생활 비유와 함께 설명해주세요",
            "각 개념을 보여주는 간단한 코드 예제와 시각적 다이어그램을 함께 제공해주세요",
            "객체지향 설계의 주요 원칙(SOLID)을 각각 설명하고 이를 어길 때의 문제점도 설명해주세요",
            "객체지향 프로그래밍의 장단점과 언제 사용하는 것이 적합한지 설명해주세요",
            "초보자가 객체지향 프로그래밍을 학습할 때 흔히 겪는 오해와 실수, 그리고 이를 극복하는 방법도 알려주세요"
        ])
    elif "함수형 프로그래밍" in topic:
        builder.add_instructions([
            "함수형 프로그래밍의 핵심 개념(순수 함수, 불변성, 고차 함수, 합성 등)을 실생활 비유로 설명해주세요",
            "각 개념을 보여주는 간단한 코드 예제를 JavaScript나 Python으로 제공해주세요",
            "함수형 프로그래밍이 객체지향 프로그래밍과 어떻게 다른지 비교해주세요",
            "함수형 프로그래밍의 장점과 어떤 문제 해결에 특히 효과적인지 설명해주세요",
            "함수형 프로그래밍을 배울 때의 학습 로드맵과 추천 자료도 제안해주세요"
        ])
    elif "비동기 프로그래밍" in topic:
        builder.add_instructions([
            "비동기 프로그래밍의 기본 개념과 동기 프로그래밍과의 차이점을 실생활 비유로 설명해주세요",
            "비동기 처리의 다양한 패턴(콜백, Promise, async/await 등)을 단계적으로 설명하고 코드 예제를 제공해주세요",
            "비동기 프로그래밍에서 흔히 겪는 문제(콜백 지옥, 경쟁 상태 등)와 해결 방법을 설명해주세요",
            "비동기 코드의 디버깅 및 테스트 전략을 제안해주세요",
            "다양한 상황에서의 비동기 패턴 선택 가이드와 모범 사례도 공유해주세요"
        ])
    elif "디자인 패턴" in topic:
        builder.add_instructions([
            "소프트웨어 디자인 패턴의 기본 개념과 목적을 설명해주세요",
            "주요 디자인 패턴 카테고리(생성, 구조, 행위 패턴)를 분류하고 각 카테고리의 대표적인 패턴 3-4개를 설명해주세요",
            "각 패턴의 설명에는 문제 상황, 해결책, UML 다이어그램, 그리고 간단한 코드 예제를 포함해주세요",
            "패턴을 과도하게 사용할 때의 위험성과 안티패턴에 대해서도 설명해주세요",
            "실제 개발에서 패턴을 인식하고 적용하는 방법과 학습 순서를 제안해주세요"
        ])
    elif "알고리즘" in topic:
        builder.add_instructions([
            "핵심 자료구조(배열, 연결 리스트, 스택, 큐, 트리, 그래프, 해시 테이블)의 특성과 사용 상황을 비교해주세요",
            "주요 알고리즘 패러다임(분할 정복, 동적 계획법, 탐욕 알고리즘 등)을 실생활 비유와 함께 설명해주세요",
            "기본적인 정렬 및 검색 알고리즘의 작동 방식을 시각적으로 설명하고 시간/공간 복잡도를 비교해주세요",
            "알고리즘 문제 해결 접근법과 효과적인 학습 전략을 단계별로 제안해주세요",
            "실제 소프트웨어 개발에서 알고리즘과 자료구조 지식이 어떻게 활용되는지 실제 사례를 들어 설명해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 핵심 개념을 실생활 비유와 함께 설명해주세요",
            "개념을 이해하는 데 도움이 되는 시각적 다이어그램과 코드 예제를 제공해주세요",
            "기본 개념부터 고급 활용까지 단계적으로 설명해주세요",
            "이 개념이 실제 프로그래밍에서 어떻게 활용되는지 구체적인 사례를 들어 설명해주세요",
            "흔한 오해와 실수, 그리고 효과적인 학습 방법도 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록, 코드 블록 등을 명확히 구분해주세요. "
        f"텍스트 다이어그램이나 그림을 ASCII 아트로 표현하여 시각적 이해를 돕는 요소를 포함해주세요. "
        f"코드 예제는 실행 가능하고 명확한 주석이 포함되도록 작성해주세요. "
        f"각 개념의 설명은 기본 개념 → 작동 원리 → 실제 예시 → 응용 방법 순으로 구성하여 체계적으로 이해할 수 있게 해주세요. "
        f"학습 후 다음 단계로 나아갈 수 있는 자료나 연습 문제도 제안해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프로그래밍 개념 이해",
        topic_options=PROGRAMMING_CONCEPT_TOPICS,
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