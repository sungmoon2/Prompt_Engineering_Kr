"""
프롬프트 저장소 구축 실습 모듈

Part 3 - 섹션 3.3.1 실습 코드: 효과적인 프롬프트 저장소를 구축하고 
관리하는 방법을 학습합니다.
"""

import os
import sys
import json
import datetime
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
PROMPT_REPOSITORY_TOPICS = {
    "1": {"name": "저장소 구조", "topic": "효과적인 프롬프트 저장소 구조와 설계 원칙", "output_format": "설계 가이드"},
    "2": {"name": "저장 템플릿", "topic": "프롬프트를 체계적으로 저장하기 위한 템플릿과 메타데이터", "output_format": "템플릿 시스템"},
    "3": {"name": "플랫폼 선택", "topic": "다양한 프롬프트 저장소 플랫폼 옵션과 선택 기준", "output_format": "비교 가이드"},
    "4": {"name": "검색 전략", "topic": "프롬프트 라이브러리에서 효율적으로 검색하고 찾는 방법", "output_format": "검색 전략"},
    "5": {"name": "관리 워크플로우", "topic": "일상적 워크플로우에 프롬프트 저장소를 통합하는 방법", "output_format": "워크플로우 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프롬프트 저장소의 구축 목적과 활용 상황 설정",
        "구체적 요청: 저장소 구조, 템플릿, 관리 방법에 대한 상세 지침 요청",
        "맞춤화 요소: 사용자 역할과 AI 활용 목적에 맞는 맞춤형 접근법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 프롬프트 저장소는 반복 작업 효율성을 높이고 프롬프트 품질을 지속적으로 개선할 수 있게 합니다",
    "효과적인 메타데이터와 템플릿 시스템은 프롬프트의 재사용성과 검색 가능성을 크게 향상시킵니다",
    "사용자의 필요와 워크플로우에 맞는 저장소 플랫폼과 구조를 선택하는 것이 중요합니다",
    "지속 가능한 관리 습관을 통합하면 시간이 지남에 따라 프롬프트 라이브러리의 가치가 증가합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 관리 전문가", 
        "AI 프롬프트를 체계적으로 저장, 분류, 관리하고 효과적으로 활용하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI를 학업, 연구, 창작 등 다양한 목적으로 활용하면서 개발한 프롬프트를 "
        f"체계적으로 저장하고 관리하는 효과적인 시스템을 구축하고 싶습니다. "
        f"이를 통해 효율성을 높이고, 프롬프트를 지속적으로 개선하며, "
        f"유사한 작업에 기존 프롬프트를 쉽게 재활용하고자 합니다."
    )
    
    # 구체적인 지시사항 추가
    if "저장소 구조" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 저장소의 핵심 구성 요소와 구조 설계 원칙을 설명해주세요",
            "다양한 목적(학업, 연구, 창작, 개발 등)에 적합한 저장소 구조 예시를 제공해주세요",
            "프롬프트 저장소의 계층적 구성, 주요 카테고리와 하위 카테고리를 어떻게 설계할지 제안해주세요",
            "저장소 구조가 시간이 지남에 따라 확장하고 진화할 수 있도록 하는 전략을 설명해주세요",
            "개인 사용자와 소규모 팀에 각각 최적화된 저장소 구조의 차이점도 포함해주세요"
        ])
    elif "저장 템플릿" in topic:
        builder.add_instructions([
            "프롬프트를 체계적으로 저장하기 위한 효과적인 템플릿과 메타데이터 구조를 설명해주세요",
            "프롬프트 항목에 포함해야 할 핵심 정보 필드와 그 목적을 상세히 설명해주세요",
            "다양한 유형의 프롬프트(역할 기반, 지시형, 창작형 등)에 맞춘 템플릿 변형을 제안해주세요",
            "메타데이터를 일관되게 작성하고 유지하는 모범 사례와 팁을 제공해주세요",
            "프롬프트 성능과 사용 이력을 추적하기 위한 메타데이터 필드도 포함해주세요"
        ])
    elif "플랫폼 선택" in topic:
        builder.add_instructions([
            "프롬프트 저장소로 활용할 수 있는 다양한 플랫폼과 도구의 장단점을 비교 분석해주세요",
            "파일 시스템, 문서 도구(노션, 옵시디언 등), 데이터베이스, 전용 AI 도구, 코드 저장소 등 주요 옵션을 평가해주세요",
            "각 플랫폼이 제공하는 기능과 한계, 그리고 어떤 사용 사례에 적합한지 설명해주세요",
            "플랫폼 선택 시 고려해야 할 핵심 요소(접근성, 검색 기능, 확장성, 협업 지원 등)를 설명해주세요",
            "개인 사용자와 학생에게 가장 적합한 무료 또는 저비용 옵션도 추천해주세요"
        ])
    elif "검색 전략" in topic:
        builder.add_instructions([
            "구축한 프롬프트 라이브러리에서 필요한 프롬프트를 효율적으로 검색하고 찾는 방법을 설명해주세요",
            "효과적인 검색 인덱스와 메타데이터 활용 전략을 제안해주세요",
            "다양한 검색 조건(목적, 유형, 도메인, 성능 등)을 조합하는 방법을 설명해주세요",
            "문맥과 상황에 기반한 직관적인 프롬프트 발견 인터페이스 설계 원칙을 제시해주세요",
            "플랫폼별 최적화된 검색 기법과 단축키, 검색 패턴도 포함해주세요"
        ])
    elif "관리 워크플로우" in topic:
        builder.add_instructions([
            "프롬프트 저장소 관리를 일상적인 AI 사용 워크플로우에 효과적으로 통합하는 방법을 설명해주세요",
            "프롬프트 캡처, 저장, 태깅, 검색, 활용, 개선의 전체 사이클을 체계화하는 워크플로우를 제안해주세요",
            "일관된 프롬프트 관리 습관을 개발하기 위한 실용적인 팁과 전략을 제공해주세요",
            "효율적인 관리를 위한 자동화 가능성과 도구 활용법을 설명해주세요",
            "관리 워크플로우를 학업, 연구, 창작 등 다양한 상황에 맞게 조정하는 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "기본 원칙과 모범 사례를 명확하게 설명해주세요",
            "다양한 상황과 요구에 맞게 조정할 수 있는 유연한 프레임워크를 제공해주세요",
            "초보자도 쉽게 시작할 수 있는 단계별 가이드를 포함해주세요",
            "구체적인 예시와 템플릿으로 실용적인 적용을 지원해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 템플릿과 예시는 코드 블록으로 제시해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"다양한 사용 사례와 니즈에 맞는 여러 옵션을 제시하되, 실용적인 권장사항도 함께 제공해주세요. "
        f"모든 내용은 대학생이 AI 프롬프트 관리를 시작하는 데 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 저장소 구축 방법",
        topic_options=PROMPT_REPOSITORY_TOPICS,
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
