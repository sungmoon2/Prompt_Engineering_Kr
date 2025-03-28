"""
첫 번째 실습: 낯선 주제 탐색하기 실습 모듈

Part 1 - 섹션 1.4 실습 코드: 지금까지 배운 기법을 활용하여
전혀 생소한 주제를 체계적으로 탐색하는 방법을 실습합니다.
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
    "1": {"name": "IR 자료 분석", "topic": "투자자 관계(IR) 자료 분석 방법", "output_format": "단계별 가이드"},
    "2": {"name": "학술 주제 탐색", "topic": "낯선 학술 주제를 체계적으로 탐색하는 방법", "output_format": "탐색 프레임워크"},
    "3": {"name": "기술 트렌드 이해", "topic": "생소한 기술 트렌드를 빠르게 이해하는 방법", "output_format": "접근 전략"},
    "4": {"name": "산업 분석", "topic": "새로운 산업 분야를 종합적으로 분석하는 방법", "output_format": "분석 템플릿"},
    "5": {"name": "맞춤형 탐색 방법", "topic": "자신의 학습 스타일에 맞는 주제 탐색 방법 개발", "output_format": "개발 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "단계적 접근: 초기 탐색부터 통합적 이해까지의 단계 명시",
        "구체적 요청: 각 단계별 세부 정보와 구조화된 형식 요청",
        "실용적 템플릿: 실제 적용 가능한 프롬프트 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "낯선 주제를 탐색할 때는 단계적 접근이 효과적입니다: 기본 개념 → 심화 탐색 → 통합적 이해",
    "명시적 무지(explicit ignorance) 표현은 AI가 적절한 수준으로 설명하도록 돕습니다",
    "구체적이고 구조화된 정보 요청은 체계적인 이해 구축에 도움이 됩니다",
    "다양한 관점과 비판적 분석 요청은 균형 잡힌 이해를 형성하는 데 중요합니다",
    "맞춤형 탐색 템플릿은 자신의 학습 스타일과 목표에 최적화된 접근을 가능하게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "주제 탐색 전문가", 
        "낯선 주제를 체계적으로 탐색하고 이해하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"지금까지 배운 프롬프트 작성법과 정보 수집 기법을 활용하여 "
        f"생소한 주제를 체계적으로 탐색하는 방법을 배우고 싶습니다. "
        f"실제 상황에서 바로 적용할 수 있는 구체적인 전략과 템플릿이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "IR 자료" in topic:
        builder.add_instructions([
            "IR 자료(투자자 관계 보고서)의 기본 구성 요소와 목적을 초보자도 이해할 수 있게 설명해주세요",
            "IR 자료를 체계적으로 분석하기 위한 단계별 접근법을 제시해주세요(기업 개요/사업 모델 이해, 재무 성과 분석, 전략 방향 파악, 통합적 평가 등)",
            "각 단계에서 사용할 수 있는 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "초보자가 흔히 범하는 IR 자료 분석의 실수와 이를 피하는 방법도 포함해주세요",
            "분석 결과를 효과적으로 정리하고 활용하는 방법과 템플릿도 제안해주세요"
        ])
    elif "학술 주제" in topic:
        builder.add_instructions([
            "전혀 배경 지식이 없는 학술 주제를 효과적으로 탐색하기 위한 체계적인 접근법을 설명해주세요",
            "초기 탐색, 심화 탐색, 통합적 이해 형성으로 이어지는 단계별 전략을 제시해주세요",
            "각 단계에서 활용할 수 있는 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "특히 학술적 개념이나 이론을 쉽게 이해하기 위한 요청 방법(비유 요청, 실생활 예시 요청 등)을 포함해주세요",
            "전체 학습 과정을 체계적으로 기록하고 평가하는 방법과 템플릿도 제안해주세요"
        ])
    elif "기술 트렌드" in topic:
        builder.add_instructions([
            "빠르게 변화하는 새로운 기술 트렌드를 효율적으로 이해하기 위한 접근 전략을 설명해주세요",
            "기술의 기본 원리, 현재 상태, 응용 분야, 영향력, 향후 전망 등을 체계적으로 파악하는 방법을 제시해주세요",
            "기술에 대한 다양한 관점(기술적, 사업적, 사회적, 윤리적 측면 등)을 균형 있게 탐색하는 프롬프트 전략을 제안해주세요",
            "복잡한 기술 개념을 이해하기 쉽게 설명해달라고 요청하는 효과적인 방법을 포함해주세요",
            "빠르게 기술 트렌드의 핵심을 파악하고 이를 실용적으로 활용하는 방법과 템플릿을 제공해주세요"
        ])
    elif "산업 분석" in topic:
        builder.add_instructions([
            "전혀 경험이 없는 새로운 산업 분야를 체계적으로 분석하는 종합적인 접근법을 설명해주세요",
            "산업 구조, 시장 역학, 주요 기업, 가치 사슬, 경쟁 요소, 트렌드 등을 효과적으로 파악하는 단계별 전략을 제시해주세요",
            "각 분석 단계에서 활용할 수 있는 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "다양한 관점에서 산업을 분석하고 평가할 수 있는 균형 잡힌 접근법을 포함해주세요",
            "분석 결과를 종합하여 산업에 대한 통합적 이해를 형성하는 방법과 템플릿을 제안해주세요"
        ])
    elif "맞춤형 탐색" in topic:
        builder.add_instructions([
            "자신의 학습 스타일과 목표에 최적화된 주제 탐색 전략을 개발하는 방법을 설명해주세요",
            "다양한 학습 스타일(시각적, 청각적, 읽기/쓰기, 체험적 등)과 목표(빠른 개요, 심층 이해, 실용적 응용 등)에 맞는 탐색 접근법을 제시해주세요",
            "맞춤형 탐색 템플릿을 개발하기 위한 단계별 가이드와 고려 사항을 제공해주세요",
            "학습 스타일별로 효과적인 프롬프트 구조와 요소의 예시를 포함해주세요",
            "개발한 맞춤형 템플릿을 테스트하고 개선하는 방법과 실제 적용 예시를 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}을 위한 체계적이고 효과적인 접근법을 설명해주세요",
            "초기 탐색에서 통합적 이해 형성까지의 단계별 전략을 제시해주세요",
            "각 단계에서 활용할 수 있는 구체적인 프롬프트 템플릿과 예시를 제공해주세요",
            "다양한 관점과 측면에서 주제를 탐색하는 균형 잡힌 접근법을 포함해주세요",
            "전체 탐색 과정을 기록하고 평가하는 방법과 템플릿을 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"단계별 접근법은 순차적으로 구성하고, 각 단계의 목적과 방법을 명확히 설명해주세요. "
        f"실제 사용할 수 있는 프롬프트 템플릿은 코드 블록으로 구분하여 제시해주세요. "
        f"가능한 경우 표나 다이어그램을 활용하여 개념이나 관계를 시각적으로 표현해주세요. "
        f"모든 내용은 대학생이 실제 학습 상황에서 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="첫 번째 실습: 낯선 주제 탐색하기",
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