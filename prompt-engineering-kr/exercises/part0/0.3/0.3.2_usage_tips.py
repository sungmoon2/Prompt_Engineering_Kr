"""
프롬프트 저장 및 관리 방법 실습 모듈

Part 0 - 섹션 0.3.2 실습 코드: 효과적인 프롬프트 저장, 분류, 재사용을 위한 관리 시스템을 구축하는 방법을 학습합니다.
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
    "1": {"name": "관리 시스템", "topic": "효과적인 프롬프트 관리 시스템 구축 방법", "output_format": "설계 가이드"},
    "2": {"name": "저장 도구", "topic": "프롬프트 저장 및 관리를 위한 도구와 앱 비교", "output_format": "도구 비교"},
    "3": {"name": "분류 체계", "topic": "프롬프트 분류 및 태깅 시스템 구축", "output_format": "분류 프레임워크"},
    "4": {"name": "템플릿 생성", "topic": "재사용 가능한 프롬프트 템플릿 작성 방법", "output_format": "템플릿 가이드"},
    "5": {"name": "버전 관리", "topic": "프롬프트 버전 관리와 개선 기록 방법", "output_format": "관리 전략"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용자 맥락 설정: 학습 및 재사용 목적 명시",
        "구체적 요청사항: 시스템 구축, 도구 비교, 분류 체계 등 세부 요청",
        "실용적 형식 지정: 바로 적용 가능한 방법론과 시스템 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 프롬프트 관리는 학습 효율성과 재사용성을 크게 높여줍니다",
    "목적과 상황에 맞는 적절한 저장 도구와 시스템 선택이 중요합니다",
    "효과적인 분류 체계와 태깅은 필요할 때 신속하게 프롬프트를 찾는 데 도움이 됩니다",
    "템플릿화와 버전 관리를 통해 프롬프트를 지속적으로 개선할 수 있습니다"
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
        "효율적인 프롬프트 저장, 분류, 재사용 시스템을 설계하고 구현하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우는 대학생으로, {topic}에 대한 실용적인 방법을 찾고 있습니다. "
        f"학습 과정에서 작성한 다양한 프롬프트를 체계적으로 저장하고 필요할 때 쉽게 찾아 재사용하고 싶습니다. "
        f"추가 비용 없이 바로 적용할 수 있는 실용적인 방법과 시스템을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "관리 시스템" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 관리 시스템의 핵심 구성 요소와 설계 원칙을 설명해주세요",
            "쉽게 시작할 수 있는 기본 시스템부터 고급 시스템까지 단계별 접근법을 제안해주세요",
            "관리 시스템 구축 시 고려해야 할 주요 요소(검색성, 접근성, 확장성 등)를 설명해주세요",
            "디지털 도구와 아날로그 방식을 결합한 실용적인 하이브리드 시스템도 제안해주세요",
            "학생이 무료로 구축할 수 있는 효과적인 관리 시스템 예시를 단계별로 제시해주세요"
        ])
    elif "저장 도구" in topic:
        builder.add_instructions([
            "프롬프트 저장 및 관리에 활용할 수 있는 다양한 도구와 앱을 카테고리별로 비교해주세요",
            "각 도구의 장단점, 특징, 사용 난이도, 무료/유료 기능을 객관적으로 분석해주세요",
            "노트 앱, 지식 관리 도구, 전용 프롬프트 관리 도구 등 다양한 옵션을 포함해주세요",
            "학생에게 특히 추천할 만한 무료 또는 저비용 도구와 그 이유를 설명해주세요",
            "각 도구의 프롬프트 관리 활용 예시와 기본 설정 방법도 함께 알려주세요"
        ])
    elif "분류 체계" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 분류 및 태깅 시스템 구축을 위한 원칙과 방법론을 설명해주세요",
            "목적, 주제, 복잡성 등 다양한 분류 기준과 카테고리 예시를 제안해주세요",
            "검색 효율성을 높이는 태깅 전략과 키워드 설정 방법을 구체적으로 설명해주세요",
            "분류 체계가 성장하고 진화할 수 있도록 유연성을 유지하는 방법을 알려주세요",
            "실제로 적용할 수 있는 분류 체계 템플릿과 구현 예시를 제공해주세요"
        ])
    elif "템플릿 생성" in topic:
        builder.add_instructions([
            "재사용 가능한 프롬프트 템플릿 작성을 위한 핵심 원칙과 방법을 설명해주세요",
            "다양한 목적과 상황에 맞는 템플릿 구조와 형식을 제안해주세요",
            "변수와 커스터마이징 요소를 효과적으로 포함하는 방법을 알려주세요",
            "실용적인 프롬프트 템플릿 예시를 최소 5가지 다양한 용도로 제공해주세요",
            "템플릿의 효과성을 평가하고 지속적으로 개선하는 방법도 설명해주세요"
        ])
    elif "버전 관리" in topic:
        builder.add_instructions([
            "프롬프트 개선과 진화를 추적하기 위한 버전 관리 시스템을 설명해주세요",
            "간단하면서도 효과적인 버전 명명 규칙과 변경 사항 기록 방법을 제안해주세요",
            "각 버전 간 변경 사항과 성능 차이를 비교하고 분석하는 방법을 알려주세요",
            "Git과 같은 버전 관리 도구를 프롬프트 관리에 활용하는 방법(가능하다면)도 설명해주세요",
            "프롬프트 변경 이력에서 패턴과 인사이트를 도출하는 방법을 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 개념과 방법론을 체계적으로 설명해주세요",
            "비용 효율적이고 학생이 바로 적용할 수 있는 실용적인 접근법을 제안해주세요",
            "구체적인 예시와 단계별 가이드를 통해 실제 구현 방법을 명확히 설명해주세요",
            "흔한 문제점과 해결책, 주의사항도 함께 알려주세요",
            "장기적인 관점에서 시스템을 발전시킬 수 있는 방향도 제시해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"비교 정보는 표 형식으로 제공하고, 단계별 설명은 번호를 매겨 순서대로 안내해주세요. "
        f"중요한 개념이나 팁은 강조 표시를 사용하여 눈에 띄게 해주세요. "
        f"가능하면 시각적 구조(폴더 구조, 분류 체계 등)를 ASCII 다이어그램으로 표현해주세요. "
        f"실제 예시와 템플릿은 코드 블록이나 인용구로 구분하여 바로 복사해서 사용할 수 있게 해주세요. "
        f"모든 내용은 무료 또는 최소 비용으로 구현 가능한 방법에 중점을 두어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 저장 및 관리 방법",
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