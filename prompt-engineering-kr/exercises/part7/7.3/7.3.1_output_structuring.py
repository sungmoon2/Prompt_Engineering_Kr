"""
구조화된 출력 요청 마스터하기 실습 모듈

Part 7 - 섹션 7.3.1 실습 코드: 다양한 구조화된 출력 형식 요청 방법과 효과적인 정보 조직화 전략을 학습합니다.
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
STRUCTURED_OUTPUT_TOPICS = {
    "1": {"name": "비교 분석 표", "topic": "여러 항목을 체계적으로 비교하는 표 형식 설계", "output_format": "비교 매트릭스"},
    "2": {"name": "계층적 목록", "topic": "정보의 계층 구조를 표현하는 목록 형식 설계", "output_format": "중첩 목록"},
    "3": {"name": "단계별 가이드", "topic": "프로세스를 명확하게 전달하는 단계별 지침 설계", "output_format": "프로세스 가이드"},
    "4": {"name": "FAQ 형식", "topic": "질문과 답변 형식으로 정보를 구조화하는 방법", "output_format": "FAQ 문서"},
    "5": {"name": "의사결정 프레임워크", "topic": "체계적인 선택과 평가를 위한 구조화된 프레임워크", "output_format": "의사결정 도구"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 일반적인 정보 요청"],
    "enhanced": [
        "구체적 구조: 명확한 섹션과 계층 지정",
        "포맷 지침: 모든 요소의 정확한 형식 요구",
        "관계 표현: 정보 간 연결과 흐름 정의",
        "일관성 규칙: 동일한 패턴 적용 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "구조화된 출력을 요청하면 복잡한 정보를 더 쉽게 이해하고 활용할 수 있습니다",
    "다양한 구조화 형식(표, 목록, 단계별 가이드 등)은 각기 다른 유형의 정보 전달에 최적화되어 있습니다",
    "명확한 구조 지침을 포함한 프롬프트는 일관되고 예측 가능한 결과를 제공합니다",
    "효과적인 정보 구조화는 핵심 내용을 강조하고 관계를 명확히 하는 데 도움이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 맞춤 역할 및 맥락 설정
    if "비교 분석 표" in topic:
        builder.add_role(
            "정보 시각화 전문가", 
            "복잡한 정보를 명확한 표 형식으로 구조화하여 비교 분석을 용이하게 하는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"다양한 항목, 제품, 개념 등을 체계적으로 비교할 수 있는 효과적인 표 형식을 설계하고 싶습니다. "
            f"특히 복잡한 정보를 한눈에 비교할 수 있는 매트릭스 구조와 시각적 요소 활용법에 대한 지침이 필요합니다."
        )
        
        builder.add_instructions([
            "효과적인 비교 분석을 위한 표 구조의 다양한 형식과 각각의 적합한 사용 상황을 설명해주세요",
            "비교 항목과 비교 기준을 명확하게 구성하는 방법과 최적의 배치 전략을 제시해주세요",
            "복잡한 정보를 표 안에서 계층화하고 강조하는 효과적인 기법을 설명해주세요",
            "표 내 데이터를 시각적으로 구분하고 패턴을 강조하는 방법(기호, 색상 참조, 포맷팅 등)을 제안해주세요",
            "재사용 가능한 비교 분석 표 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
        
    elif "계층적 목록" in topic:
        builder.add_role(
            "정보 구조화 전문가", 
            "복잡한 정보를 논리적 계층 구조로 조직화하여 이해와 탐색을 용이하게 하는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"복잡한 개념, 분류 체계, 조직 구조 등을 명확한 계층 구조로 표현하고 싶습니다. "
            f"특히 정보 간의 관계와 종속성을 시각적으로 명확하게 전달하는 중첩 목록 형식이 필요합니다."
        )
        
        builder.add_instructions([
            "효과적인 계층적 목록 구조의 다양한 형식(번호 매기기, 글머리 기호, 중첩, 트리 등)과 각각의 적합한 사용 상황을 설명해주세요",
            "정보의 논리적 계층과 관계를 명확하게 표현하는 최적의 구조화 전략을 제시해주세요",
            "복잡한 계층 구조를 시각적으로 명확하게 표현하는 들여쓰기, 기호, 포맷팅 기법을 설명해주세요",
            "목록 내 항목을 그룹화하고 관계를 강조하는 효과적인 방법을 제안해주세요",
            "재사용 가능한 계층적 목록 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
        
    elif "단계별 가이드" in topic:
        builder.add_role(
            "프로세스 설계 전문가", 
            "복잡한 과정과 절차를 명확하고 따라하기 쉬운 단계별 지침으로 변환하는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"다양한 프로세스, 절차, 방법론을 사용자가 쉽게 따라할 수 있는 단계별 가이드로 구조화하고 싶습니다. "
            f"특히 복잡한 과정을 논리적 순서로 분해하고 각 단계를 명확하게 전달하는 구조가 필요합니다."
        )
        
        builder.add_instructions([
            "효과적인 단계별 가이드의 다양한 구조 형식과 각각의 적합한 사용 상황을 설명해주세요",
            "복잡한 프로세스를 명확한 단계로 분해하고 논리적 흐름을 구성하는 전략을 제시해주세요",
            "각 단계의 정보를 일관되고 이해하기 쉽게 구조화하는 방법을 설명해주세요",
            "단계 간 관계, 분기점, 선택 사항 등을 명확하게 표현하는 기법을 제안해주세요",
            "재사용 가능한 단계별 가이드 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
        
    elif "FAQ 형식" in topic:
        builder.add_role(
            "지식 관리 전문가", 
            "복잡한 정보를 질문과 답변 형식으로 구조화하여 접근성과 이해도를 높이는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"제품 설명, 정책 안내, 문제 해결 가이드 등을 사용자 중심의 FAQ 형식으로 구조화하고 싶습니다. "
            f"특히 사용자의 관점에서 정보를 조직화하고 쉽게 찾을 수 있는 효과적인 FAQ 구조가 필요합니다."
        )
        
        builder.add_instructions([
            "효과적인 FAQ 문서의 다양한 구조 형식과 각각의 적합한 사용 상황을 설명해주세요",
            "자주 묻는 질문을 식별하고 논리적으로 그룹화하는 전략을 제시해주세요",
            "질문과 답변을 명확하고 일관된 형식으로 구성하는 방법을 설명해주세요",
            "FAQ 내 정보 탐색을 용이하게 하는 구조적 요소(목차, 카테고리, 검색 키워드 등)를 제안해주세요",
            "재사용 가능한 FAQ 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
        
    elif "의사결정 프레임워크" in topic:
        builder.add_role(
            "의사결정 설계 전문가", 
            "복잡한 선택 과정을 체계적이고 객관적인 구조로 변환하여 더 나은 결정을 돕는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"다양한 옵션 평가, 위험 분석, 우선순위 설정 등을 위한 체계적인 의사결정 프레임워크를 설계하고 싶습니다. "
            f"특히 복잡한 요소들을 고려하여 객관적이고 일관된 결정을 내릴 수 있는 구조화된 도구가 필요합니다."
        )
        
        builder.add_instructions([
            "효과적인 의사결정 프레임워크의 다양한 구조 형식과 각각의 적합한 사용 상황을 설명해주세요",
            "의사결정 요소(기준, 가중치, 옵션, 점수 등)를 체계적으로 구성하는 방법을 제시해주세요",
            "정량적/정성적 평가를 균형있게 통합하는 구조화 전략을 설명해주세요",
            "의사결정 과정을 시각적으로 명확하게 표현하는 매트릭스, 표, 차트 등의 활용법을 제안해주세요",
            "재사용 가능한 의사결정 프레임워크 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
        
    else:
        builder.add_role(
            "정보 구조화 전문가", 
            "복잡한 정보를 명확하고 효과적인 구조로 조직화하여 이해와 활용을 높이는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있습니다. "
            f"다양한 유형의 정보를 효과적으로 구조화하는 방법과 명확한 형식으로 전달하는 전략을 알고 싶습니다. "
            f"특히 정보의 본질과 목적에 맞는 최적의 구조화 형식을 선택하고 적용하는 방법이 필요합니다."
        )
        
        builder.add_instructions([
            "다양한 정보 구조화 형식(표, 목록, 다이어그램 등)과 각각의 적합한 사용 상황을 설명해주세요",
            "정보의 특성과 목적에 따라 최적의 구조를 선택하는 기준을 제시해주세요",
            "복잡한 정보를 명확하고 접근하기 쉽게 조직화하는 원칙과 전략을 설명해주세요",
            "구조화된 정보의 일관성과 가독성을 높이는 형식 지침을 제안해주세요",
            "재사용 가능한 정보 구조화 템플릿을 마크다운 형식으로 제공하고, 효과적인 활용법을 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 다음 요소를 효과적으로 활용해주세요:\n\n"
        f"1. 명확한 제목 계층 구조 (##, ###, ####)\n"
        f"2. 글머리 기호와 번호 매기기를 적절히 활용한 목록\n"
        f"3. 표를 사용한 정보 비교 및 구조화\n"
        f"4. 인용문(>)을 활용한 중요 포인트 강조\n"
        f"5. 코드 블록을 활용한 예시 및 템플릿 표현\n"
        f"6. 굵은 글씨와 기울임체를 활용한 강조\n\n"
        f"다음 섹션을 포함해주세요:\n"
        f"1. 개요: 해당 구조화 형식의 목적과 적합한 사용 상황\n"
        f"2. 핵심 원칙: 효과적인 구조화를 위한 기본 원칙과 지침\n"
        f"3. 구조화 방법: 단계별 구성 및 포맷팅 방법\n"
        f"4. 템플릿: 재사용 가능한 구체적 예시 및 변형\n"
        f"5. 활용 팁: 효과적인 사용을 위한 실용적 조언\n\n"
        f"각 섹션은 일관된 구조와 형식을 유지하고, 실제 사용 가능한 예시와 템플릿에 중점을 두어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="구조화된 출력 요청 마스터하기",
        topic_options=STRUCTURED_OUTPUT_TOPICS,
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