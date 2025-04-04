"""
실제 코드 예제 요청 실습 모듈

Part 5 - 섹션 5.1.2 실습 코드: 효과적인 코드 예제 요청 전략을 학습합니다.
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
CODE_EXAMPLE_TOPICS = {
    "1": {"name": "자료구조 구현", "topic": "다양한 자료구조의 효과적인 구현 예제", "output_format": "코드 가이드"},
    "2": {"name": "알고리즘 시각화", "topic": "알고리즘 동작 과정의 시각적 설명과 코드 예제", "output_format": "튜토리얼"},
    "3": {"name": "디자인 패턴 적용", "topic": "실용적인 디자인 패턴 코드 예제와 활용법", "output_format": "패턴 가이드"},
    "4": {"name": "API 활용 사례", "topic": "주요 라이브러리와 API의 실용적 코드 예제", "output_format": "코드 레시피"},
    "5": {"name": "성능 최적화 기법", "topic": "코드 성능 최적화를 위한 실용적 예제", "output_format": "최적화 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 코드 예제 요청"],
    "enhanced": [
        "난이도 요청: 입문부터 고급까지 단계별 코드 예제 요청",
        "설명 요청: 자세한 주석과 실행 과정 설명 포함 요청",
        "비교 요청: 다양한 구현 방식의 코드 예제 비교 요청",
        "실용 요청: 실제 프로젝트에 적용 가능한 현실적 예제 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 코드 학습을 위해서는 다양한 난이도와 접근법의 예제를 요청하는 것이 중요합니다",
    "코드의 작동 원리를 이해하기 위해 상세한 주석과 단계별 설명을 포함한 예제를 요청하세요",
    "같은 문제를 해결하는 다양한 방법의 코드 예제를 비교하면 더 깊은 이해를 얻을 수 있습니다",
    "실제 사용 맥락을 반영한 실용적인 코드 예제가 실무 적용에 더 유용합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대한 코드 예제를 보여주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "프로그래밍 교육 전문가", 
        "복잡한 프로그래밍 개념을 명확한 코드 예제와 시각적 설명을 통해 효과적으로 전달하는 전문 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대해 학습하고 있는 중급 개발자입니다. "
        f"개념은 대략적으로 이해하고 있지만, 실제 코드로 구현하는 방법과 다양한 활용 패턴을 배우고 싶습니다. "
        f"단순히 동작하는 코드보다는 모범 사례와 실용적인 접근법을 보여주는 잘 설명된 예제가 필요합니다. "
        f"입문 수준부터 고급 수준까지 단계적으로 학습할 수 있는 예제와 각 코드의 작동 원리에 대한 "
        f"명확한 설명이 포함되면 좋겠습니다."
    )
    
    # 주제별 맞춤 지시사항 추가
    if "자료구조" in topic:
        builder.add_instructions([
            "다음 자료구조의 Python 구현 예제를 난이도별로 제공해주세요: 연결 리스트, 이진 검색 트리, 해시 테이블",
            "각 자료구조에 대해 기본 구현부터 시작하여 고급 기능(예: 균형 트리, 충돌 해결 전략)까지 단계적으로 코드를 보여주세요",
            "각 코드 예제에 상세한 주석과 작동 원리 설명을 포함해주세요",
            "각 자료구조의 주요 연산(삽입, 검색, 삭제 등)의 시간 복잡도 분석도 포함해주세요",
            "실제 프로젝트에서 이러한 자료구조를 활용하는 실용적인 사례와 패턴도 코드로 보여주세요"
        ])
    elif "알고리즘" in topic:
        builder.add_instructions([
            "다음 알고리즘의 시각적 설명과 Python 구현 예제를 제공해주세요: 퀵 정렬, 다익스트라 최단 경로, 동적 프로그래밍",
            "각 알고리즘의 실행 과정을 단계별로 시각화하여 보여주세요(텍스트 기반 다이어그램 사용)",
            "입력 크기와 패턴에 따른 성능 특성을 설명하고, 최적화 기법도 함께 제시해주세요",
            "같은 문제를 해결하는 다양한 알고리즘 접근법을 비교하는 코드 예제도 포함해주세요",
            "실제 상황에서 알고리즘 선택 시 고려해야 할 트레이드오프를 설명하고, 적합한 사용 시나리오를 제시해주세요"
        ])
    elif "디자인 패턴" in topic:
        builder.add_instructions([
            "다음 디자인 패턴의 실용적인 구현 예제를 Python 또는 JavaScript로 제공해주세요: 싱글톤, 옵저버, 팩토리, 전략 패턴",
            "각 패턴의 기본 구조와 핵심 구성 요소를 설명하고, UML 다이어그램(텍스트 기반)으로 시각화해주세요",
            "각 패턴이 해결하는 문제와 적용 시나리오를 실제 코드 예제와 함께 설명해주세요",
            "패턴의 장단점과 잠재적인 오용 사례도 설명해주세요",
            "여러 패턴을 조합하여 더 복잡한 문제를 해결하는 고급 예제도 포함해주세요"
        ])
    elif "API" in topic:
        builder.add_instructions([
            "다음 영역의 주요 라이브러리/API 활용을 위한 실용적인 코드 예제를 제공해주세요: HTTP 요청, 데이터베이스 접근, 비동기 처리",
            "각 예제는 기본 사용법부터 시작하여 오류 처리, 최적화, 보안 고려사항까지 단계적으로 발전시켜주세요",
            "실제 프로젝트에서 자주 마주치는 시나리오(인증, 페이지네이션, 트랜잭션 등)에 대한 코드 패턴을 포함해주세요",
            "각 API/라이브러리의 일반적인 함정과 이를 피하는 모범 사례를 코드로 보여주세요",
            "테스트 가능하고 유지보수하기 쉬운 API 통합 코드 작성법도 설명해주세요"
        ])
    elif "성능 최적화" in topic:
        builder.add_instructions([
            "다음 영역의 코드 성능 최적화 기법과 실제 예제를 제공해주세요: 메모리 사용, 실행 시간, I/O 작업",
            "각 최적화 기법에 대해 최적화 전/후의 코드를 비교하고 개선 원리를 설명해주세요",
            "데이터 구조 선택, 알고리즘 개선, 캐싱 등 다양한 최적화 전략을 다루세요",
            "성능 병목 지점을 식별하고 측정하는 방법과 도구도 코드 예제와 함께 설명해주세요",
            "최적화와 코드 가독성/유지보수성 사이의 트레이드오프를 다루고, 균형 잡힌 접근법을 제시해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 다양한 난이도(입문, 중급, 고급)의 코드 예제를 제공해주세요",
            "각 코드 예제에 상세한 주석과 작동 원리 설명을 포함해주세요",
            "다양한 접근법과 구현 방식을 비교하고 각각의 장단점을 분석해주세요",
            "실제 프로젝트에서 활용할 수 있는 실용적인 패턴과 모범 사례를 포함해주세요",
            "흔한 실수와 함정, 그리고 이를 피하는 방법도 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 코드 블록, 설명 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요:\n\n"
        f"1. 개요: 주제 소개 및 학습 목표\n"
        f"2. 기본 예제: 핵심 개념을 보여주는 간단한 코드\n"
        f"3. 중급 예제: 실용적인 활용법과 패턴\n"
        f"4. 고급 예제: 최적화 및 고급 기법\n"
        f"5. 비교 분석: 다양한 접근법의 장단점\n"
        f"6. 실제 적용: 실무에서의 활용 사례\n\n"
        f"코드 예제는 실행 가능하고 잘 주석 처리된 완전한 형태로 제공해주세요. "
        f"가능한 경우 텍스트 기반 다이어그램이나 시각자료를 포함하여 이해를 돕고, "
        f"단계별 실행 과정도 설명해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="실제 코드 예제 요청 전략",
        topic_options=CODE_EXAMPLE_TOPICS,
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