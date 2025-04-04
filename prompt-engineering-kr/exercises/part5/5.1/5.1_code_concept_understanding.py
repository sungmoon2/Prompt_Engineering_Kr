"""
프로그래밍 개념 이해와 적용 실습 모듈

Part 5 - 섹션 5.1 실습 코드: 프로그래밍 개념을 효과적으로 이해하고 적용하는 방법을 학습합니다.
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
PROGRAMMING_CONCEPTS_TOPICS = {
    "1": {"name": "프로그래밍 패러다임", "topic": "객체지향, 함수형, 절차적 프로그래밍 패러다임 비교", "output_format": "개념 가이드"},
    "2": {"name": "데이터 구조", "topic": "주요 데이터 구조의 개념과 활용", "output_format": "학습 가이드"},
    "3": {"name": "알고리즘 설계", "topic": "알고리즘 설계 패턴과 최적화 전략", "output_format": "개념 튜토리얼"},
    "4": {"name": "동시성과 병렬성", "topic": "동시성 및 병렬 프로그래밍의 기초와 패턴", "output_format": "개념 설명서"},
    "5": {"name": "디자인 패턴", "topic": "소프트웨어 디자인 패턴의 이해와 활용", "output_format": "학습 로드맵"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 맥락 명시: 현재 지식 수준과 학습 목표 제공",
        "다중 표현 요청: 비유, 시각화, 코드 예제 등 다양한 설명 방식 요청",
        "개념 간 연결: 관련 개념들의 비교 및 관계 설명 요청",
        "실용적 적용: 실제 사용 사례와 활용 방법 포함 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프로그래밍 개념을 효과적으로 이해하려면 자신의 지식 수준에 맞는 설명을 요청하는 것이 중요합니다",
    "복잡한 개념은 비유, 시각화, 코드 예제 등 다양한 방식으로 접근할 때 더 깊이 이해할 수 있습니다",
    "관련 개념들을 비교하고 연결하면 더 포괄적인 이해를 구축할 수 있습니다",
    "개념의 실제 적용 사례와 맥락을 이해하면 더 실용적인 지식을 얻을 수 있습니다"
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
        "복잡한 프로그래밍 개념을 명확하고 이해하기 쉽게 설명하는 능력을 가진 교육자로, 다양한 학습 스타일과 배경을 가진 학생들을 위한 맞춤형 설명 접근법을 사용합니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프로그래밍 개념을 깊이 이해하고 싶은 학생으로, {topic}에 대해 배우고 있습니다. "
        f"기본적인 프로그래밍 지식은 있지만 이 주제에 대해서는 초중급 수준입니다. "
        f"개념을 단순히 암기하는 것이 아니라 실질적으로 이해하고 적용할 수 있기를 원합니다. "
        f"복잡한 아이디어를 실생활 비유, 시각적 표현, 실제 코드 예제와 함께 설명해주시면 "
        f"이해하는 데 큰 도움이 될 것 같습니다."
    )
    
    # 주제별 맞춤 지시사항 추가
    if "패러다임" in topic:
        builder.add_instructions([
            "객체지향, 함수형, 절차적 프로그래밍의 핵심 원칙과 철학을 비교해주세요",
            "각 패러다임의 장단점과 적합한 사용 상황을 실제 예시와 함께 설명해주세요",
            "동일한 문제를 세 가지 패러다임으로 각각 해결하는 코드 예제를 보여주세요",
            "실생활 비유를 통해 각 패러다임의 사고방식의 차이를 설명해주세요",
            "패러다임 간의 상호 보완적 관계와 현대 프로그래밍에서의 혼합 접근법도 설명해주세요"
        ])
    elif "데이터 구조" in topic:
        builder.add_instructions([
            "배열, 링크드 리스트, 스택, 큐, 트리, 그래프, 해시 테이블 등 주요 데이터 구조의 개념을 시각적으로 설명해주세요",
            "각 데이터 구조의 시간/공간 복잡도와 연산 특성을 비교해주세요",
            "각 데이터 구조가 특히 효과적인 문제 유형과 실제 활용 사례를 제시해주세요",
            "데이터 구조 선택 시 고려해야 할 트레이드오프와 결정 기준을 설명해주세요",
            "실제 코드로 각 데이터 구조의 기본 구현과 활용 방법을 보여주세요"
        ])
    elif "알고리즘" in topic:
        builder.add_instructions([
            "문제 해결을 위한 주요 알고리즘 설계 패턴(분할 정복, 동적 계획법, 탐욕 알고리즘 등)을 비교 설명해주세요",
            "각 설계 패턴의 적용 가능한 문제 유형과 접근 방식을 실생활 비유와 함께 설명해주세요",
            "시간 및 공간 복잡도 분석 방법과 알고리즘 최적화 전략을 설명해주세요",
            "같은 문제에 대해 서로 다른 알고리즘 접근법을 비교하는 실제 코드 예제를 제공해주세요",
            "알고리즘 설계 시 주요 고려사항과 일반적인 함정을 설명해주세요"
        ])
    elif "동시성" in topic:
        builder.add_instructions([
            "동시성과 병렬성의 차이점과 각각의 핵심 개념을 실생활 비유를 통해 설명해주세요",
            "스레드, 프로세스, 비동기 프로그래밍, 이벤트 루프 등의 개념을 시각적으로 설명해주세요",
            "경쟁 조건, 교착 상태, 기아 상태 등 일반적인 동시성 문제와 해결 방법을 설명해주세요",
            "다양한 프로그래밍 언어에서 동시성을 처리하는 방식과 패턴을 비교해주세요",
            "실제 동시성 코드 예제와 함께 디버깅 및 성능 최적화 방법을 설명해주세요"
        ])
    elif "디자인 패턴" in topic:
        builder.add_instructions([
            "주요 디자인 패턴 카테고리(생성, 구조, 행위 패턴)와 대표적인 패턴들을 설명해주세요",
            "각 패턴의 목적, 구조, 적용 시나리오를 실생활 비유와 함께 설명해주세요",
            "패턴 간의 관계와 함께 사용되는 일반적인 조합을 설명해주세요",
            "다양한 프로그래밍 언어로 각 패턴의 구현 예제를 보여주세요",
            "안티패턴과 디자인 패턴의 오용 사례도 함께 설명해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 핵심 개념과 원칙을 실생활 비유와 시각적 설명을 통해 설명해주세요",
            "관련된 주요 개념들을 비교하고 관계를 설명해주세요",
            "다양한 프로그래밍 언어에서의 구현 방식과 차이점을 코드 예제와 함께 보여주세요",
            "실제 적용 사례와 사용 패턴을 설명해주세요",
            "흔한 오해와 함정, 그리고 이를 피하는 방법을 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록, 코드 블록, 표 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요:\n\n"
        f"1. 개요: 핵심 개념과 중요성 소개\n"
        f"2. 주요 개념: 상세 설명과 비유, 시각적 표현 포함\n"
        f"3. 비교 및 관계: 관련 개념들과의 비교 및 연결\n"
        f"4. 코드 예제: 다양한 언어와 상황의 실제 코드\n"
        f"5. 실제 활용: 현업에서의 사용 사례와 패턴\n"
        f"6. 학습 자원: 추가 학습을 위한 자료 및 연습 문제\n\n"
        f"실생활 비유, 다이어그램(텍스트 기반), 표, 코드 예제 등을 풍부하게 사용하여 "
        f"다양한 학습 스타일에 맞게 개념을 설명해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프로그래밍 개념 이해와 적용",
        topic_options=PROGRAMMING_CONCEPTS_TOPICS,
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