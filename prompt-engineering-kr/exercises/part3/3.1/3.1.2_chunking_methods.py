"""
대화 요약 및 압축 기법 실습 모듈

Part 3 - 섹션 3.1.2 실습 코드: 장기적인 대화와 복잡한 맥락을 효과적으로 요약하고
압축하는 방법을 학습합니다.
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
CONVERSATION_SUMMARY_TOPICS = {
    "1": {"name": "요약 전략", "topic": "효과적인 대화 요약을 위한 전략적 접근법", "output_format": "전략 가이드"},
    "2": {"name": "대화 유형별 요약", "topic": "다양한 대화 유형과 목적별 최적화된 요약 방법", "output_format": "요약 프레임워크"},
    "3": {"name": "압축 기법", "topic": "정보 손실 최소화를 위한 대화 압축 기법", "output_format": "압축 가이드"},
    "4": {"name": "자동화 방법", "topic": "AI를 활용한 대화 자동 요약 최적화 방법", "output_format": "자동화 가이드"},
    "5": {"name": "점진적 요약", "topic": "장기 대화를 위한 점진적 요약 접근법", "output_format": "요약 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 대화 요약과 압축의 목표와 활용 상황 설정",
        "구체적 요청: 체계적인 요약 방법과 실용적 기법 요청",
        "실용적 형식: 즉시 적용 가능한 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 대화 요약은 토큰 효율성과 맥락 보존 사이의 균형에 있습니다",
    "대화의 목적과 유형에 따라 최적화된 요약 접근법을 선택하는 것이 중요합니다",
    "정보 압축 기법은 핵심 내용을 유지하면서 토큰 사용을 최소화합니다",
    "AI를 활용한 자동 요약은 시간을 절약하고 일관된 요약을 생성할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "대화 요약 전문가", 
        "복잡하고 장기적인 대화의 핵심을 효과적으로 포착하고 압축하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 장기적인 대화에서 중요한 맥락과 정보를 효과적으로 요약하고 압축하는 방법을 배우고 싶습니다. "
        f"특히 학업과 연구 프로젝트에서 대화 내용을 효율적으로 관리하고 재사용하는 실용적인 기법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "요약 전략" in topic:
        builder.add_instructions([
            "효과적인 대화 요약을 위한 체계적인 접근법과 전략을 설명해주세요",
            "토큰 효율성과 맥락 보존 사이의 균형을 맞추는 방법을 제시해주세요",
            "대화 요약의 핵심 원칙과 단계별 프로세스를 자세히 설명해주세요",
            "다양한 요약 기법(추출적, 추상적, 혼합적 등)의 장단점을 비교해주세요",
            "효과적인 요약을 위한 실용적인 팁과 일반적인 함정을 피하는 방법도 포함해주세요"
        ])
    elif "대화 유형별 요약" in topic:
        builder.add_instructions([
            "다양한 대화 유형과 목적에 최적화된 요약 방법을 설명해주세요",
            "정보 탐색, 문제 해결, 창작 과정, 학습 세션 등 대화 유형별 최적의 요약 접근법을 비교해주세요",
            "각 대화 유형에서 중요하게 포착해야 할 핵심 요소와 구조를 제시해주세요",
            "대화 유형별 요약 시 특별히 주의해야 할 점과 사용할 수 있는 템플릿을 제공해주세요",
            "다양한 대화 목적에 적용 가능한 범용적인 요약 프레임워크도 제안해주세요"
        ])
    elif "압축 기법" in topic:
        builder.add_instructions([
            "정보 손실을 최소화하면서 대화를 효과적으로 압축하는 기법을 설명해주세요",
            "다양한 압축 기법(정보 밀도 최적화, 중복 제거, 핵심어 중심 등)의 원리와 적용 방법을 제시해주세요",
            "다양한 정보 유형(사실, 개념, 결정사항, 질문 등)에 따른 최적의 압축 전략을 비교해주세요",
            "압축률과 정보 보존 사이의 균형을 맞추는 원칙과 지침을 제공해주세요",
            "압축 과정에서 중요 정보 손실을 방지하는 안전장치와 검증 방법도 포함해주세요"
        ])
    elif "자동화 방법" in topic:
        builder.add_instructions([
            "AI를 활용해 대화를 자동으로 요약하고 압축하는 최적화된 방법을 설명해주세요",
            "효과적인 자동 요약을 위한 프롬프트 디자인 원칙과 템플릿을 제공해주세요",
            "자동 요약의 품질을 평가하고 개선하는 방법을 설명해주세요",
            "자동화된 요약 시스템을 구축하고 워크플로우에 통합하는 방법을 제안해주세요",
            "자동 요약의 한계와 이를 보완하는 전략도 포함해주세요"
        ])
    elif "점진적 요약" in topic:
        builder.add_instructions([
            "장기 대화를 위한 점진적 요약 접근법과 시스템을 설명해주세요",
            "대화가 진행됨에 따라 요약을 어떻게 업데이트하고 관리하는지 단계별로 설명해주세요",
            "다양한 수준(1차, 2차, 3차 등)의 요약과 그 용도를 설명해주세요",
            "장기 프로젝트에서 지속적인 요약 관리를 위한 효과적인 시스템을 제안해주세요",
            "점진적 요약 과정에서 중요한 정보의 손실을 방지하는 전략도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "대화 요약과 압축의 기본 원칙과 중요성을 먼저 설명해주세요",
            "다양한 상황과 요구에 맞는 구체적인 요약 기법과 템플릿을 제시해주세요",
            "실제 적용 사례와 예시를 통해 효과적인 사용 방법을 보여주세요",
            "실무에 바로 적용할 수 있는 체크리스트와 가이드라인을 제공해주세요"
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
        title="대화 요약 및 압축 기법",
        topic_options=CONVERSATION_SUMMARY_TOPICS,
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
