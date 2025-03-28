"""
큰 과제를 작은 조각으로 나누기 실습 모듈

Part 2 - 섹션 2.1.1 실습 코드: 효과적인 과제 분해 기법과 도구를 학습합니다.
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
TASK_DECOMPOSITION_TOPICS = {
    "1": {"name": "WBS 기법", "topic": "작업 분할 구조(WBS)를 활용한 과제 분해 방법", "output_format": "가이드"},
    "2": {"name": "마인드맵", "topic": "마인드맵을 활용한 과제 분해 및 구조화 기법", "output_format": "실습 가이드"},
    "3": {"name": "MECE 원칙", "topic": "MECE(Mutually Exclusive, Collectively Exhaustive) 원칙을 활용한 체계적 분해 방법", "output_format": "방법론 가이드"},
    "4": {"name": "애자일 방식", "topic": "애자일 방법론의 스토리 분해 및 태스크 관리 기법", "output_format": "실용 가이드"},
    "5": {"name": "디자인 사고", "topic": "디자인 사고(Design Thinking)를 활용한 문제 분해 접근법", "output_format": "프로세스 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 효과적인 과제 분해의 필요성과 목적 설명",
        "구체적 요청: 단계별 접근법과 실용적인 기법 요청",
        "구조화된 출력: 실습 예시와 시각적 자료 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 과제 분해는 복잡한 과제를 관리 가능한 단위로 변환하는 핵심 기술입니다",
    "다양한 분해 기법은 과제의 성격과 목적에 따라 선택적으로 활용할 수 있습니다",
    "체계적인 분해는 과제의 모든 측면을 포괄하고 중복이나 누락을 방지합니다",
    "시각화 도구는 과제의 구조와 구성 요소 간의 관계를 명확히 이해하는 데 도움이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "과제 관리 전문가", 
        "복잡한 과제와 프로젝트를 효과적으로 분해하고 관리하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"종종 큰 과제나 프로젝트를 어떻게 시작해야 할지 몰라 어려움을 겪습니다. "
        f"효과적으로 큰 과제를 관리 가능한 작은 조각으로 나누는 체계적인 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "WBS 기법" in topic:
        builder.add_instructions([
            "작업 분할 구조(WBS)의 개념과 핵심 원칙을 명확히 설명해주세요",
            "WBS를 활용하여 과제를 체계적으로 분해하는 단계별 프로세스를 제시해주세요",
            "효과적인 WBS 작성을 위한 실용적인 팁과 주의사항을 공유해주세요",
            "학업 프로젝트, 연구 과제 등 대학생에게 적합한 WBS 적용 사례와 템플릿을 제공해주세요",
            "WBS를 디지털 도구를 활용하여 작성하고 관리하는 방법도 소개해주세요"
        ])
    elif "마인드맵" in topic:
        builder.add_instructions([
            "마인드맵의 기본 개념과 과제 분해에 활용하는 원리를 설명해주세요",
            "마인드맵을 사용하여 복잡한 과제를 체계적으로 분해하는 단계별 방법을 제시해주세요",
            "효과적인 마인드맵 작성을 위한 구체적인 기법과 팁을 공유해주세요",
            "학업 과제, 논문 작성, 프로젝트 계획 등 다양한 상황에서의 마인드맵 활용 예시를 보여주세요",
            "디지털 마인드맵 도구 추천과 효과적인 활용법도 포함해주세요"
        ])
    elif "MECE 원칙" in topic:
        builder.add_instructions([
            "MECE(Mutually Exclusive, Collectively Exhaustive) 원칙의 개념과 중요성을 설명해주세요",
            "MECE 원칙을 적용하여 과제를 체계적으로 분해하는 단계별 접근법을 제시해주세요",
            "일반적인 MECE 분류 프레임워크와 그 활용법을 설명해주세요",
            "학업 및 연구 상황에서 MECE 원칙을 적용한 구체적인 사례와 예시를 포함해주세요",
            "MECE 적용 시 흔히 발생하는 오류와 그 해결 방법도 알려주세요"
        ])
    elif "애자일 방식" in topic:
        builder.add_instructions([
            "애자일 방법론의 사용자 스토리와 태스크 분해 개념을 설명해주세요",
            "복잡한 기능이나 요구사항을 작은 스토리와 태스크로 분해하는 단계별 방법을 제시해주세요",
            "효과적인 스토리 작성과 태스크 분해를 위한 실용적인 기법과 도구를 소개해주세요",
            "팀 프로젝트나 학업 과제에 애자일 분해 방식을 적용하는 구체적인 예시를 보여주세요",
            "애자일 태스크 관리를 위한 도구(Trello, Jira 등) 활용법도 간략히 안내해주세요"
        ])
    elif "디자인 사고" in topic:
        builder.add_instructions([
            "디자인 사고(Design Thinking)의 개념과 문제 분해에서의 역할을 설명해주세요",
            "디자인 사고를 활용하여 복잡한 문제를 체계적으로 분해하는 프로세스를 단계별로 설명해주세요",
            "공감, 정의, 발상, 프로토타입, 테스트 단계에서의 분해 기법을 구체적으로 소개해주세요",
            "학업 및 연구 프로젝트에 디자인 사고를 적용한 실제 사례와 예시를 포함해주세요",
            "디자인 사고를 지원하는 워크숍 형식이나 도구도 함께 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 개념과 원리를 명확하게 설명해주세요",
            "이 방법을 활용하여 복잡한 과제를 체계적으로 분해하는 단계별 접근법을 제시해주세요",
            "효과적인 활용을 위한 구체적인 기법과 팁을 공유해주세요",
            "대학생의 학업 및 프로젝트 상황에 적용할 수 있는 실제 사례와 예시를 포함해주세요",
            "이 방법을 지원하는 유용한 도구나 템플릿도 함께 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"단계별 접근법과 과정을 체계적으로 구성하고, 시각적 예시(다이어그램, 표 등)를 포함해 이해를 돕습니다. "
        f"실제 대학 과제나 프로젝트 예시를 통해 적용 방법을 구체적으로 보여주세요. "
        f"각 단계와 기법에 대한 설명은 이론뿐만 아니라 실용적인 적용 팁을 포함해주세요. "
        f"마지막에는 '실습 활동' 섹션을 추가하여 독자가 직접 시도해볼 수 있는 간단한 연습을 제안해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="큰 과제를 작은 조각으로 나누기",
        topic_options=TASK_DECOMPOSITION_TOPICS,
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