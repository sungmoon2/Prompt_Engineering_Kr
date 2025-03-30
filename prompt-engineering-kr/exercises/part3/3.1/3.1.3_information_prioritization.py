"""
핵심 정보 추출 및 관리 실습 모듈

Part 3 - 섹션 3.1.3 실습 코드: 대화에서 핵심 정보를 추출하고
효과적으로 관리하는 방법을 학습합니다.
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
INFORMATION_EXTRACTION_TOPICS = {
    "1": {"name": "정보 유형 분류", "topic": "대화에서 다양한 정보 유형을 식별하고 분류하는 방법", "output_format": "분류 가이드"},
    "2": {"name": "정보 추출 프레임워크", "topic": "체계적인 정보 추출을 위한 EXTRACT 프레임워크 활용법", "output_format": "실용 가이드"},
    "3": {"name": "우선순위 설정", "topic": "정보의 중요도와 관련성에 따른 우선순위 설정 방법", "output_format": "평가 시스템"},
    "4": {"name": "정보 구조화", "topic": "추출된 정보의 효과적인 구조화 및 조직화 방법", "output_format": "구조화 템플릿"},
    "5": {"name": "정보 관리 시스템", "topic": "장기 프로젝트를 위한 정보 관리 및 업데이트 시스템", "output_format": "관리 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 핵심 정보 추출 및 관리의 필요성 설정",
        "구체적 요청: 체계적인 추출 방법과 구조화 템플릿 요청",
        "실용적 형식: 즉시 적용 가능한 시스템과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "대화에서 다양한 유형의 정보를 식별하고 분류하는 능력은 효과적인 정보 관리의 기초입니다",
    "체계적인 정보 추출 프레임워크를 사용하면 핵심 정보를 일관되게 포착할 수 있습니다",
    "모든 정보가 동일하게 중요한 것은 아니므로 우선순위 설정이 필수적입니다",
    "추출된 정보는 재사용과 접근이 용이하도록 효과적으로 구조화해야 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "정보 관리 전문가", 
        "복잡한 대화와 프로젝트에서 핵심 정보를 체계적으로 추출하고 관리하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 장기적인 대화와 복잡한 프로젝트에서 중요한 정보를 효과적으로 추출하고 관리하는 방법을 배우고 싶습니다. "
        f"특히 학업과 연구에서 핵심 정보를 놓치지 않고 체계적으로 관리하는 실용적인 시스템이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "정보 유형 분류" in topic:
        builder.add_instructions([
            "대화에서 발생하는 다양한 정보 유형(사실, 개념, 결정사항, 행동 항목, 통찰 등)을 분류하는 체계를 설명해주세요",
            "각 정보 유형의 특징과 식별 방법을 구체적으로 설명해주세요",
            "정보 유형별 분류의 실제 예시와 사례를 제공해주세요",
            "정보 유형을 시각적으로 구분하는 방법(태그, 아이콘, 색상 코드 등)을 제안해주세요",
            "자동화된 정보 유형 분류를 위한 AI 프롬프트 템플릿도 제공해주세요"
        ])
    elif "정보 추출 프레임워크" in topic:
        builder.add_instructions([
            "EXTRACT 프레임워크(Evaluate purpose alignment, eXamine dependencies, Tag and categorize, Rate confidence, Arrange hierarchically, Compress redundancies, Timestamp key changes)의 각 단계를 상세히 설명해주세요",
            "프레임워크의 각 단계별 적용 방법과 구체적인 예시를 제공해주세요",
            "EXTRACT 프레임워크를 다양한 상황(연구 프로젝트, 학습 세션, 문제 해결 등)에 맞게 적용하는 방법을 설명해주세요",
            "프레임워크 적용 시 주의해야 할 점과 일반적인 함정을 피하는 방법을 알려주세요",
            "실제 대화 예시에 EXTRACT 프레임워크를 적용한 단계별 사례를 포함해주세요"
        ])
    elif "우선순위 설정" in topic:
        builder.add_instructions([
            "정보의 중요도와 관련성을 평가하기 위한 체계적인 기준을 설명해주세요",
            "우선순위 매트릭스(중요도 × 긴급성)와 같은 우선순위 설정 도구의 활용법을 설명해주세요",
            "상황과 목적에 따라 우선순위 기준을 조정하는 방법을 제시해주세요",
            "다양한 유형의 프로젝트에 맞는 맞춤형 우선순위 평가 시스템을 제안해주세요",
            "우선순위 결정에서 흔히 발생하는 편향과 이를 극복하는 방법을 설명해주세요"
        ])
    elif "정보 구조화" in topic:
        builder.add_instructions([
            "추출된 정보를 효과적으로 구조화하는 다양한 방법(계층적 구조, 네트워크 구조, 매트릭스 등)을 설명해주세요",
            "다양한 정보 구조화 템플릿과 각각의 적합한 상황을 제시해주세요",
            "정보 간의 관계와 연결성을 시각화하는 방법을 설명해주세요",
            "효과적인 태깅, 인덱싱, 참조 시스템 구축 방법을 제안해주세요",
            "구조화된 정보의 유지보수와 업데이트를 위한 실용적인 접근법도 포함해주세요"
        ])
    elif "정보 관리 시스템" in topic:
        builder.add_instructions([
            "장기 프로젝트를 위한 종합적인 정보 관리 시스템의 설계 원칙과 구성 요소를 설명해주세요",
            "정보의 수집, 추출, 구조화, 저장, 검색, 업데이트를 포괄하는 통합 워크플로우를 제시해주세요",
            "다양한 도구(노트 앱, 지식 베이스, 프로젝트 관리 도구 등)를 활용한 실용적인 시스템 구축 방법을 제안해주세요",
            "시간 경과에 따른 정보 업데이트와 버전 관리 전략을 설명해주세요",
            "정보 관리 시스템의 실제 구축 사례와 단계별 구현 가이드를 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "기본 원칙과 단계별 구현 방법을 명확하게 설명해주세요",
            "다양한 상황에 맞는 구체적인 적용 사례와 예시를 제공해주세요",
            "실제 활용할 수 있는 템플릿과 도구를 제안해주세요",
            "일반적인 문제와 해결책도 함께 설명해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 템플릿과 예시는 코드 블록으로 제시해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"핵심 개념과 원칙은 굵은 글씨로 강조하고, 중요한 팁은 인용 형식으로 표시해주세요. "
        f"모든 내용은 대학생이 학업과 연구 프로젝트에 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="핵심 정보 추출 및 관리",
        topic_options=INFORMATION_EXTRACTION_TOPICS,
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
