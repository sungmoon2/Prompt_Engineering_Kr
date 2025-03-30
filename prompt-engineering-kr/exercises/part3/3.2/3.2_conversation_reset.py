"""
대화 재설정 기술 실습 모듈

Part 3 - 섹션 3.2 실습 코드: 장기적인 대화를 관리하기 위한
효과적인 대화 재설정 기술을 학습합니다.
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
CONVERSATION_RESET_TOPICS = {
    "1": {"name": "대화 재설정 기본", "topic": "효과적인 대화 재설정의 기본 원칙과 방법", "output_format": "가이드"},
    "2": {"name": "맥락 유지 전략", "topic": "새 대화 세션에서 이전 맥락을 효과적으로 유지하는 전략", "output_format": "전략 가이드"},
    "3": {"name": "대화 브리지", "topic": "세션 간의 연속성을 위한 대화 브리지 설계 방법", "output_format": "템플릿 모음"},
    "4": {"name": "프로젝트 맥락", "topic": "장기 프로젝트에서 대화 재설정을 위한 맥락 관리 방법", "output_format": "관리 시스템"},
    "5": {"name": "자동화 방법", "topic": "대화 재설정을 자동화하기 위한 프롬프트 설계 기법", "output_format": "프롬프트 템플릿"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 대화 재설정의 목표와 필요성 설정",
        "구체적 요청: 체계적인 재설정 방법과 맥락 유지 전략 요청",
        "실용적 형식: 즉시 적용 가능한 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "대화 재설정은 AI 토큰 제한의 문제를 극복하고 장기적인 작업 연속성을 유지하는 핵심 기술입니다",
    "효과적인 맥락 요약과 핵심 정보 전달은 새 대화 세션의 품질을 결정합니다",
    "대화 브리지는 세션 간 정보 손실을 최소화하여 작업 효율성을 높입니다",
    "프로젝트 맥락 관리는 복잡한 장기 프로젝트의 일관성 유지에 필수적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "대화 연속성 전문가", 
        "장기적인 AI 대화에서 맥락의 연속성을 유지하고 효과적인 대화 재설정 전략을 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 대화에서 토큰 제한으로 인한 맥락 손실 문제를 해결하고, 여러 세션에 걸친 작업의 연속성을 유지하는 방법을 배우고 싶습니다. "
        f"특히 복잡한 프로젝트와 학습 과정에서 이전 대화의 핵심 맥락을 효과적으로 다음 세션에 전달하는 실용적인 기법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "대화 재설정 기본" in topic:
        builder.add_instructions([
            "효과적인 대화 재설정의 기본 원칙과 중요성을 설명해주세요",
            "대화 재설정이 필요한 상황과 징후를 식별하는 방법을 제시해주세요",
            "재설정 과정에서 반드시 포함해야 할 핵심 요소와 정보 유형을 설명해주세요",
            "재설정 프롬프트의 기본 구조와 효과적인 작성법을 알려주세요",
            "대화 재설정 시 흔히 발생하는 실수와 이를 피하는 방법도 포함해주세요"
        ])
    elif "맥락 유지 전략" in topic:
        builder.add_instructions([
            "새 대화 세션에서 이전 맥락을 효과적으로 유지하기 위한 다양한 전략을 설명해주세요",
            "맥락의 다양한 측면(목적, 진행 상황, 결정사항, 미해결 문제 등)을 전달하는 방법을 제시해주세요",
            "상황에 따라 맥락의 상세 수준을 조절하는 방법을 설명해주세요",
            "맥락 유지와 토큰 효율성 사이의 균형을 맞추는 전략을 제안해주세요",
            "다양한 AI 모델과 토큰 제한에 맞춘 맥락 유지 전략도 포함해주세요"
        ])
    elif "대화 브리지" in topic:
        builder.add_instructions([
            "세션 간의 연속성을 위한 대화 브리지의 개념과 설계 원칙을 설명해주세요",
            "다양한 대화 브리지 템플릿과 각각의 장단점 및 적합한 상황을 제시해주세요",
            "대화의 목적과 유형에 따라 최적화된 브리지 구조를 제안해주세요",
            "브리지에 포함할 핵심 정보를 선별하는 기준과 방법을 설명해주세요",
            "실제 사용 가능한 다양한 대화 브리지 템플릿 예시와 활용 지침을 제공해주세요"
        ])
    elif "프로젝트 맥락" in topic:
        builder.add_instructions([
            "장기 프로젝트에서 일관된 맥락 관리를 위한 체계적인 접근법을 설명해주세요",
            "프로젝트 진행에 따른 맥락 변화를 추적하고 관리하는 방법을 제시해주세요",
            "핵심 프로젝트 정보(목표, 제약조건, 결정사항, 진행 상황 등)를 효과적으로 관리하는 시스템을 설명해주세요",
            "프로젝트 맥락을 시각화하고 구조화하는 다양한 방법과 도구를 제안해주세요",
            "프로젝트 유형별(연구, 창작, 개발 등) 맞춤형 맥락 관리 전략도 포함해주세요"
        ])
    elif "자동화 방법" in topic:
        builder.add_instructions([
            "대화 재설정을 자동화하기 위한 효과적인 프롬프트 설계 기법을 설명해주세요",
            "AI에게 이전 대화 요약 및 맥락 추출을 요청하는 프롬프트 템플릿을 제공해주세요",
            "자동 맥락 전달 시스템 구축을 위한 단계별 접근법을 제시해주세요",
            "자동화된 재설정의 품질을 평가하고 개선하는 방법을 설명해주세요",
            "다양한 상황에 맞는 자동화된 재설정 프롬프트 템플릿 예시를 포함해주세요"
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
        title="대화 재설정 기술",
        topic_options=CONVERSATION_RESET_TOPICS,
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
