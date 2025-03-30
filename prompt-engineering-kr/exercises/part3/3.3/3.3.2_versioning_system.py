"""
프롬프트 분류 및 태그 시스템 실습 모듈

Part 3 - 섹션 3.3.2 실습 코드: 프롬프트를 효과적으로 분류하고 
태그 시스템을 개발하는 방법을 학습합니다.
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
CLASSIFICATION_TOPICS = {
    "1": {"name": "분류 체계", "topic": "효과적인 프롬프트 분류 체계 구축 원칙과 방법", "output_format": "분류 가이드"},
    "2": {"name": "태그 전략", "topic": "체계적인 프롬프트 태그 시스템 설계 및 관리 전략", "output_format": "태그 시스템"},
    "3": {"name": "다차원 분류", "topic": "다차원 프롬프트 분류 프레임워크 개발 방법", "output_format": "프레임워크 가이드"},
    "4": {"name": "통제 어휘", "topic": "프롬프트 관리를 위한 통제 어휘와 용어 표준화", "output_format": "용어 가이드"},
    "5": {"name": "분류 진화", "topic": "시간에 따른 분류 체계 발전 및 관리 전략", "output_format": "관리 전략"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프롬프트 분류 및 태그 시스템의 필요성과 목표 설정",
        "구체적 요청: 체계적인 분류 프레임워크와 태그 시스템 요청",
        "맞춤화 요소: 프롬프트 유형과 사용 목적에 맞는 맞춤형 접근법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 분류와 태그 시스템은 프롬프트의 검색성과 재사용성을 크게 향상시킵니다",
    "다차원 분류 프레임워크는 다양한 관점에서 프롬프트를 조직화하고 접근할 수 있게 합니다",
    "통제된 어휘와 표준화된 태그는 일관성 있는 프롬프트 관리의 핵심입니다",
    "분류 체계는 시간이 지남에 따라 진화할 수 있도록 유연하게 설계되어야 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "정보 분류 전문가", 
        "복잡한 정보를 체계적으로 분류하고 효과적인 태그 시스템을 설계하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI 프롬프트 라이브러리를 구축하면서 프롬프트를 효과적으로 분류하고 "
        f"태그를 지정하는 체계적인 시스템이 필요합니다. "
        f"이를 통해 필요할 때 적절한 프롬프트를 쉽게 찾고, "
        f"프롬프트 컬렉션을 효율적으로 관리하고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "분류 체계" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 분류 체계를 구축하기 위한 핵심 원칙과 접근법을 설명해주세요",
            "프롬프트 분류를 위한 주요 카테고리와 하위 카테고리의 논리적 구조를 제안해주세요",
            "목적, 유형, 도메인, 복잡성 등 다양한 분류 차원을 설명하고 예시를 제공해주세요",
            "학생의 다양한 AI 사용 상황(학습, 연구, 창작, 문제 해결 등)에 적합한 분류 구조를 설명해주세요",
            "분류 체계의 유연성과 확장성을 유지하는 방법도 포함해주세요"
        ])
    elif "태그 전략" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 태그 시스템을 설계하고 관리하는 전략을 설명해주세요",
            "프롬프트 태깅을 위한 다양한 태그 유형(주제, 기능, 품질, 상태 등)과 그 목적을 설명해주세요",
            "일관된 태그 적용을 위한 규칙과 가이드라인을 제안해주세요",
            "효율적인 태그 관리를 위한 도구와 기법을 소개해주세요",
            "시간이 지남에 따라 태그 시스템을 유지하고 개선하는 방법도 포함해주세요"
        ])
    elif "다차원 분류" in topic:
        builder.add_instructions([
            "프롬프트를 다양한 차원에서 분류할 수 있는 다차원 분류 프레임워크를 설명해주세요",
            "목적, 형식, 도메인, 복잡성 등 주요 분류 차원과 각 차원의 세부 카테고리를 상세히 설명해주세요",
            "다차원 분류 프레임워크를 실제로 구현하고 시각화하는 방법을 제안해주세요",
            "다차원 분류를 통해 프롬프트에 접근하고 검색하는 효과적인 방법을 설명해주세요",
            "다차원 분류 프레임워크의 장단점과 최적의 활용 방법도 포함해주세요"
        ])
    elif "통제 어휘" in topic:
        builder.add_instructions([
            "프롬프트 관리를 위한 통제 어휘와 용어 표준화의 중요성과 방법을 설명해주세요",
            "효과적인 통제 어휘 목록을 개발하고 관리하는 프로세스를 제안해주세요",
            "동의어, 상위어, 하위어 등 용어 간의 관계를 관리하는 방법을 설명해주세요",
            "용어 표준화를 통해 검색 효율성을 향상시키는 전략을 제시해주세요",
            "통제 어휘 시스템의 진화와 유지 관리를 위한 모범 사례도 포함해주세요"
        ])
    elif "분류 진화" in topic:
        builder.add_instructions([
            "시간이 지남에 따라 프롬프트 분류 체계를 진화시키고 관리하는 전략을 설명해주세요",
            "프롬프트 컬렉션의 성장에 따른 분류 체계 확장 방법을 제안해주세요",
            "새로운 프롬프트 유형이나 사용 패턴에 맞게 분류 체계를 조정하는 방법을 설명해주세요",
            "분류 체계의 일관성을 유지하면서 개선하는 프로세스를 설명해주세요",
            "분류 체계 변경을 효과적으로 관리하고 문서화하는 방법도 포함해주세요"
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
        f"실제 사용 가능한 분류 체계와 태그 시스템 예시를 시각적으로 제시해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"다양한 사용 사례에 맞는 여러 옵션을 제시하되, 실용적인 권장사항도 함께 제공해주세요. "
        f"모든 내용은 대학생이 프롬프트 분류 시스템을 구축하는 데 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="효과적인 분류 및 태그 시스템",
        topic_options=CLASSIFICATION_TOPICS,
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
