"""
프롬프트 기록과 관리 시스템 실습 모듈

Part 3 - 섹션 3.3 실습 코드: 프롬프트를 체계적으로 저장, 분류, 관리하는 
방법을 학습합니다.
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
PROMPT_MANAGEMENT_TOPICS = {
    "1": {"name": "관리 시스템", "topic": "효과적인 프롬프트 관리 시스템의 구성 요소와 설계 원칙", "output_format": "시스템 가이드"},
    "2": {"name": "관리 워크플로우", "topic": "프롬프트 관리를 일상 워크플로우에 통합하는 방법", "output_format": "워크플로우 가이드"},
    "3": {"name": "개인 vs 팀", "topic": "개인과 팀 환경에서의 프롬프트 관리 전략 비교", "output_format": "비교 가이드"},
    "4": {"name": "통합 프레임워크", "topic": "저장, 분류, 버전 관리를 통합한 종합적 관리 프레임워크", "output_format": "프레임워크 가이드"},
    "5": {"name": "자동화 전략", "topic": "프롬프트 관리 작업 자동화를 위한 도구와 전략", "output_format": "자동화 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프롬프트 관리 시스템의 목표와 활용 상황 설정",
        "구체적 요청: 효과적인 프롬프트 관리를 위한 체계적 접근법 요청",
        "맞춤화 요소: 사용자 환경과 요구사항에 맞는 실용적 전략 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 프롬프트 관리 시스템은 AI 활용의 일관성, 효율성, 품질을 크게 향상시킬 수 있습니다",
    "저장, 분류, 버전 관리의 통합적 접근은 프롬프트 자산의 가치를 극대화합니다",
    "관리 워크플로우를 일상 업무에 자연스럽게 통합하는 것이 시스템의 지속가능성을 위해 중요합니다",
    "개인과 팀 환경에 맞는 맞춤형 접근법으로 프롬프트 관리의 효과를 최적화할 수 있습니다"
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
        "AI 프롬프트를 체계적으로 저장, 분류, 버전 관리하고 효과적으로 활용하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI를 다양한 학업 및 개인 프로젝트에 활용하고 있으며, 개발한 프롬프트를 "
        f"체계적으로 관리하는 효과적인 시스템과 워크플로우를 구축하고 싶습니다. "
        f"이를 통해 프롬프트 재사용성을 높이고, 지속적인 개선을 추적하며, "
        f"장기적으로 AI 활용 역량을 강화하고자 합니다."
    )
    
    # 구체적인 지시사항 추가
    if "관리 시스템" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 관리 시스템의 핵심 구성 요소와 설계 원칙을 설명해주세요",
            "저장소 구조, 분류 체계, 버전 관리 등 주요 시스템 구성 요소 간의 관계와 통합 방법을 설명해주세요",
            "다양한 유형의 프롬프트(학술, 창작, 기술 등)를 효과적으로 관리할 수 있는 유연한 시스템 아키텍처를 제안해주세요",
            "관리 시스템 설계 시 고려해야 할 주요 트레이드오프와 의사결정 포인트를 설명해주세요",
            "장기적으로 확장 가능하고 지속 가능한 관리 시스템을 위한 핵심 원칙도 포함해주세요"
        ])
    elif "관리 워크플로우" in topic:
        builder.add_instructions([
            "프롬프트 관리를 일상적인 AI 사용 워크플로우에 효과적으로 통합하는 방법을 설명해주세요",
            "프롬프트 캡처, 정리, 활용, 개선의 전체 사이클을 효율적으로 관리하는 워크플로우를 제안해주세요",
            "학업 활동(연구, 글쓰기, 문제 해결 등) 과정에서 프롬프트 관리 습관을 자연스럽게 통합하는 전략을 설명해주세요",
            "관리 오버헤드를 최소화하면서 프롬프트 자산의 가치를 극대화하는 균형 전략을 제시해주세요",
            "다양한 상황과 활동에 맞게 조정할 수 있는 유연한 워크플로우 템플릿도 포함해주세요"
        ])
    elif "개인 vs 팀" in topic:
        builder.add_instructions([
            "개인 환경과 팀 환경에서의 프롬프트 관리 전략의 주요 차이점과 유사점을 비교 분석해주세요",
            "개인 사용자를 위한 간소화된 관리 시스템과 팀 협업을 위한 확장된 시스템의 특징을 설명해주세요",
            "개인 환경에서 시작하여 팀 환경으로 확장할 때 고려해야 할 핵심 변화와 전환 전략을 제안해주세요",
            "팀 환경에서 일관성, 품질, 접근성을 유지하면서 다양한 팀원의 요구를 수용하는 방법을 설명해주세요",
            "개인과 팀 각각의 상황에 최적화된 도구와 플랫폼 추천도 포함해주세요"
        ])
    elif "통합 프레임워크" in topic:
        builder.add_instructions([
            "프롬프트 저장, 분류, 버전 관리를 효과적으로 통합한 종합적 관리 프레임워크를 설명해주세요",
            "STORE 또는 유사한 프레임워크를 활용한 체계적인 프롬프트 관리 접근법을 상세히 설명해주세요",
            "통합 프레임워크의 각 구성 요소 간 상호작용과 정보 흐름을 설명해주세요",
            "다양한 프롬프트 관리 목표(재사용성, 개선 추적, 지식 공유 등)를 균형 있게 달성하는 방법을 제시해주세요",
            "통합 프레임워크를 실제로 구현하기 위한 단계별 로드맵과 모범 사례도 포함해주세요"
        ])
    elif "자동화 전략" in topic:
        builder.add_instructions([
            "프롬프트 관리 작업을 효과적으로 자동화하기 위한 도구와 전략을 설명해주세요",
            "메타데이터 추출, 분류 제안, 성능 추적 등을 자동화할 수 있는 방법을 제안해주세요",
            "스크립트, API, 기존 도구 등을 활용한 실용적인 자동화 솔루션을 설명해주세요",
            "자동화의 적절한 수준과 수동 관리가 여전히 중요한 영역을 구분해주세요",
            "기술적 지식이 제한적인 사용자도 적용할 수 있는 접근 가능한 자동화 전략도 포함해주세요"
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
        f"프로세스와 워크플로우는 시각적 다이어그램이나 단계별 목록으로 설명해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"모든 내용은 대학생이 AI 프롬프트 관리를 시작하는 데 바로 적용할 수 있도록 "
        f"실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 기록과 관리 시스템",
        topic_options=PROMPT_MANAGEMENT_TOPICS,
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
