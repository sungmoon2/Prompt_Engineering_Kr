"""
프로젝트 맥락 관리 실습 모듈

Part 3 - 섹션 3.2.3 실습 코드: 장기 프로젝트에서 맥락의 일관성을
유지하기 위한 효과적인 맥락 관리 시스템을 구축하는 방법을 학습합니다.
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
PROJECT_CONTEXT_TOPICS = {
    "1": {"name": "맥락 문서 설계", "topic": "효과적인 프로젝트 맥락 문서의 구조와 구성 요소", "output_format": "문서 템플릿"},
    "2": {"name": "맥락 추적 시스템", "topic": "장기 프로젝트에서 중요 결정과 변화를 추적하는 시스템", "output_format": "추적 프레임워크"},
    "3": {"name": "지식 기반 구축", "topic": "프로젝트 지식을 체계적으로 축적하고 관리하는 방법", "output_format": "지식 관리 시스템"},
    "4": {"name": "맥락 업데이트", "topic": "프로젝트 진행에 따른 맥락 문서의 효과적인 업데이트 전략", "output_format": "업데이트 가이드"},
    "5": {"name": "맥락 통합 전략", "topic": "재설정과 브리지를 통합한 종합적 맥락 관리 전략", "output_format": "통합 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프로젝트 맥락 관리의 목표와 필요성 설정",
        "구체적 요청: 체계적인 맥락 관리 시스템과 도구 요청",
        "실용적 형식: 즉시 적용 가능한 템플릿과 방법론 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 맥락 관리는 장기 프로젝트의 일관성과 효율성을 크게 향상시킵니다",
    "잘 설계된 맥락 문서는 프로젝트의 핵심 정보와 결정사항을 효과적으로 보존합니다",
    "지식 기반 구축을 통해 프로젝트 지식을 점진적으로 축적하고 활용할 수 있습니다",
    "재설정과 브리지를 통합한 종합적 접근법이 복잡한 프로젝트 관리에 효과적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프로젝트 맥락 관리 전문가", 
        "복잡한 장기 프로젝트에서 맥락의 일관성을 유지하고 핵심 정보를 체계적으로 관리하는 전략과 시스템을 설계하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 장기 협업 프로젝트에서 맥락의 일관성을 유지하고, 중요한 결정사항과 정보를 "
        f"효과적으로 관리하는 체계적인 시스템을 구축하고 싶습니다. "
        f"특히 연구, 논문 작성, 창작 프로젝트, 소프트웨어 개발 등 다양한 유형의 프로젝트에 "
        f"적용할 수 있는 실용적인 방법론과 도구가 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "맥락 문서 설계" in topic:
        builder.add_instructions([
            "효과적인 프로젝트 맥락 문서의 핵심 구성 요소와 이상적인 구조를 설명해주세요",
            "다양한 프로젝트 유형에 적용할 수 있는 맥락 문서 템플릿을 제공해주세요",
            "각 섹션의 목적과 포함해야 할 정보 유형을 상세히 설명해주세요",
            "맥락 문서의 다양한 사용 방식과 효과적인 참조 방법을 제안해주세요",
            "실제 사용 가능한 맥락 문서 템플릿과 작성 예시를 포함해주세요"
        ])
    elif "맥락 추적 시스템" in topic:
        builder.add_instructions([
            "장기 프로젝트에서 중요 결정, 변화, 진행 상황을 효과적으로 추적하는 시스템을 설명해주세요",
            "결정 로그, 변경 관리, 이슈 추적 등의 구성 요소와 작동 방식을 설명해주세요",
            "시간에 따른 프로젝트 변화를 시각화하고 이해하는 방법을 제안해주세요",
            "다양한 유형의 변화와 결정(작은 조정부터 주요 방향 전환까지)을 적절히 추적하는 방법을 설명해주세요",
            "실제 구현 가능한 추적 시스템 템플릿과 사용 예시를 포함해주세요"
        ])
    elif "지식 기반 구축" in topic:
        builder.add_instructions([
            "프로젝트 지식을 체계적으로 축적하고 관리하는 지식 기반 시스템을 설명해주세요",
            "지식의 수집, 조직화, 검색, 업데이트를 위한 체계적인 접근법을 제시해주세요",
            "다양한 유형의 지식(개념, 결정, 자원, 참조 등)을 효과적으로 관리하는 방법을 설명해주세요",
            "프로젝트 진행에 따라 지식 기반을 발전시키고 활용하는 전략을 제안해주세요",
            "실제 구현 가능한 지식 관리 시스템 템플릿과 도구 추천을 포함해주세요"
        ])
    elif "맥락 업데이트" in topic:
        builder.add_instructions([
            "프로젝트 진행에 따른 맥락 문서의 효과적인 업데이트 전략과 방법론을 설명해주세요",
            "정기적인 업데이트 주기와 트리거 이벤트를 식별하는 방법을 제시해주세요",
            "무엇을 유지하고, 무엇을 변경하고, 무엇을 제거할지 결정하는 기준을 설명해주세요",
            "맥락 문서의 버전 관리와 변경 내역 추적 방법을 제안해주세요",
            "효율적인 업데이트 워크플로우와 체크리스트를 포함해주세요"
        ])
    elif "맥락 통합 전략" in topic:
        builder.add_instructions([
            "대화 재설정, 브리지, 맥락 문서를 통합한 종합적인 맥락 관리 전략을 설명해주세요",
            "각 요소(재설정, 브리지, 맥락 문서)의 역할과 상호작용 방식을 설명해주세요",
            "다양한 상황과 시점에 적합한 맥락 관리 도구 선택 기준을 제시해주세요",
            "종합적인 맥락 관리 워크플로우와 시스템 설계 방법을 설명해주세요",
            "실제 구현 가능한 통합 맥락 관리 시스템과 적용 예시를 포함해주세요"
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
        title="프로젝트 맥락 관리",
        topic_options=PROJECT_CONTEXT_TOPICS,
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
