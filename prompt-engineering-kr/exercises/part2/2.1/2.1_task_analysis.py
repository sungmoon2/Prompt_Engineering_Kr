"""
과제 분석과 분해 전략 실습 모듈

Part 2 - 섹션 2.1 실습 코드: 복잡한 과제를 작은 단위로 분해하고 체계적으로 분석하는 방법을 학습합니다.
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
TASK_ANALYSIS_TOPICS = {
    "1": {"name": "연구 프로젝트", "topic": "복잡한 연구 프로젝트의 분해 및 분석 전략", "output_format": "분석 프레임워크"},
    "2": {"name": "비즈니스 과제", "topic": "비즈니스 문제 분석 및 해결 접근법", "output_format": "문제 분해 가이드"},
    "3": {"name": "학술 에세이", "topic": "학술 에세이 작성을 위한 체계적 분석 방법", "output_format": "단계별 가이드"},
    "4": {"name": "기술 개발", "topic": "기술 개발 프로젝트의 효과적인 분해 전략", "output_format": "프로젝트 계획 체계"},
    "5": {"name": "복잡한 의사결정", "topic": "복잡한 의사결정을 위한 분석 프레임워크", "output_format": "의사결정 매트릭스"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 과제의 복잡성과 분해 필요성 설명",
        "구체적 요청: 체계적 분석과 단계별 접근법 요청",
        "구조화된 출력: 재사용 가능한 프레임워크와 시각적 요소 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "복잡한 과제는 작은 구성 요소로 분해하면 더 효과적으로 접근할 수 있습니다",
    "체계적인 분석 프레임워크를 사용하면 과제의 모든 측면을 포괄적으로 고려할 수 있습니다",
    "5W1H(누가, 무엇을, 언제, 어디서, 왜, 어떻게) 접근법은 과제 분석의 기본 도구입니다",
    "작은 단위로 분해된 과제는 우선순위를 정하고 체계적으로 접근하기가 더 용이합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "과제 분석 전문가", 
        "복잡한 문제와 과제를 체계적으로 분석하고 분해하는 전략을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"복잡한 과제를 앞두고 압도감을 느끼고 있으며, 어디서부터 시작해야 할지 혼란스럽습니다. "
        f"과제를 체계적으로 분석하고 관리 가능한 작은 부분으로 분해하는 효과적인 접근법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "연구 프로젝트" in topic:
        builder.add_instructions([
            "복잡한 연구 프로젝트를 체계적으로 분석하고 분해하는 방법을 설명해주세요",
            "연구 질문 설정, 문헌 검토, 방법론 선택, 데이터 수집/분석, 결과 해석 등 주요 단계별 접근법을 제시해주세요",
            "각 단계를 더 작은 작업으로 분해하는 구체적인 전략과 도구를 추천해주세요",
            "일반적인 연구 프로젝트 진행 시 발생하는 장애물과 이를 극복하기 위한 방법도 포함해주세요",
            "연구 진행 상황을 추적하고 관리하는 효과적인 방법도 제안해주세요"
        ])
    elif "비즈니스 과제" in topic:
        builder.add_instructions([
            "비즈니스 문제와 과제를 체계적으로 분석하고 분해하는 방법을 설명해주세요",
            "문제 정의, 원인 분석, 대안 생성, 의사결정, 실행 계획 등 주요 단계별 접근법을 제시해주세요",
            "SWOT, PEST, 5 Forces, 가치 사슬 분석 등 유용한 비즈니스 분석 프레임워크의 활용법을 설명해주세요",
            "복잡한 비즈니스 과제를 작은 단위로 분해하고 우선순위를 정하는 방법을 제시해주세요",
            "팀 프로젝트로 진행할 때의 역할 분담과 협업 전략도 포함해주세요"
        ])
    elif "학술 에세이" in topic:
        builder.add_instructions([
            "학술 에세이 작성 과제를 체계적으로 분석하고 접근하는 방법을 설명해주세요",
            "주제 선정, 리서치, 개요 작성, 초안 작성, 편집/수정 등 주요 단계별 접근법을 제시해주세요",
            "효과적인, 논리적인 구조를 설계하는 방법과 논증 구성 전략을 설명해주세요",
            "각 단계를 더 작은 작업으로 분해하고 진행하는 구체적인 방법을 제안해주세요",
            "일반적인 학술 에세이 작성 시 발생하는 어려움과 이를 극복하기 위한 전략도 포함해주세요"
        ])
    elif "기술 개발" in topic:
        builder.add_instructions([
            "기술 개발 프로젝트를 체계적으로 분석하고 분해하는 방법을 설명해주세요",
            "요구사항 분석, 설계, 개발, 테스트, 배포 등 주요 단계별 접근법을 제시해주세요",
            "각 단계를 더 작은 작업과 기능 단위로 분해하는 효과적인 전략을 설명해주세요",
            "애자일, 스크럼, 칸반 등 프로젝트 관리 방법론을 활용한 작업 분해 및 추적 방법을 포함해주세요",
            "기술 개발 과정에서 발생하는 일반적인 문제와 이를 예방/해결하기 위한 접근법도 제안해주세요"
        ])
    elif "복잡한 의사결정" in topic:
        builder.add_instructions([
            "복잡한 의사결정 상황을 체계적으로 분석하고 접근하는 방법을 설명해주세요",
            "문제 정의, 대안 생성, 평가 기준 설정, 대안 평가, 결정 및 실행 등 주요 단계별 접근법을 제시해주세요",
            "의사결정 매트릭스, 결정 트리, 비용-편익 분석 등 유용한 의사결정 도구와 프레임워크를 소개해주세요",
            "복잡한 요소가 많은 의사결정을 작은 하위 결정으로 분해하는 전략을 설명해주세요",
            "불확실성과 리스크를 고려한 의사결정 접근법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}을 체계적으로 분석하고 작은 구성 요소로 분해하는 방법을 설명해주세요",
            "주요 단계와 구성 요소를 식별하고 분류하는 접근법을 제시해주세요",
            "복잡한 과제를 관리 가능한 작은 작업으로 분해하는 구체적인 전략과 도구를 추천해주세요",
            "5W1H, 마인드맵, 로직 트리 등 유용한 분석 프레임워크의 활용법을 설명해주세요",
            "일반적으로 발생하는 어려움과 이를 극복하기 위한 방법도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"단계별 접근법과 분해 전략을 체계적으로 구성하고, 가능한 경우 시각적 요소(표, 다이어그램 등)를 포함해주세요. "
        f"실제 사례나 예시를 통해 설명하여 이해를 돕고, 실용적인 팁과 도구도 함께 제안해주세요. "
        f"대학생이 즉시 활용할 수 있는 실용적인 내용으로 구성하되, 지속적으로 참고할 수 있는 리소스로 활용할 수 있게 만들어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="과제 분석과 분해 전략",
        topic_options=TASK_ANALYSIS_TOPICS,
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
