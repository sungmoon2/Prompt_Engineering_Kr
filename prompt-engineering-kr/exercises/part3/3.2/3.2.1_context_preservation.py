"""
효과적인 대화 재설정 기법 실습 모듈

Part 3 - 섹션 3.2.1 실습 코드: 새로운 대화 세션에서 이전 맥락을
효과적으로 유지하기 위한 재설정 기법을 학습합니다.
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
CONVERSATION_RESET_TECHNIQUES = {
    "1": {"name": "기본 재설정 구조", "topic": "효과적인 대화 재설정 프롬프트의 기본 구조와 요소", "output_format": "구조 가이드"},
    "2": {"name": "목적별 재설정", "topic": "다양한 대화 목적에 맞춘 맞춤형 재설정 기법", "output_format": "템플릿 모음"},
    "3": {"name": "토큰 최적화", "topic": "토큰을 효율적으로 사용하는 간결한 재설정 전략", "output_format": "최적화 가이드"},
    "4": {"name": "맥락 선별 기준", "topic": "재설정 시 포함할 핵심 맥락을 선별하는 기준", "output_format": "결정 프레임워크"},
    "5": {"name": "검증 및 개선", "topic": "재설정 효과를 검증하고 지속적으로 개선하는 방법", "output_format": "평가 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 효과적인 대화 재설정의 목표와 필요성 설정",
        "구체적 요청: 체계적인 구조와 맞춤형 접근법 요청",
        "실용적 형식: 즉시 적용 가능한 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 대화 재설정은 프로젝트의 연속성과 일관성을 유지하는 데 필수적입니다",
    "목적과 상황에 맞는 맞춤형 재설정 구조가 더 나은 결과를 제공합니다",
    "토큰 효율성과 맥락 보존 사이의 균형이 성공적인 재설정의 핵심입니다",
    "지속적인 검증과 개선을 통해 재설정 전략을 발전시킬 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "대화 재설정 전략가", 
        "AI와의 대화에서 이전 맥락의 연속성을 유지하기 위한 효과적인 재설정 기법을 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 장기적인 대화와 복잡한 프로젝트에서 새로운 세션을 시작할 때 "
        f"이전 맥락을 효과적으로 재설정하는 방법을 배우고 싶습니다. "
        f"특히 학업과 연구 활동에서 AI와의 대화 연속성을 유지하기 위한 실용적인 기법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "기본 재설정 구조" in topic:
        builder.add_instructions([
            "효과적인 대화 재설정 프롬프트의 기본 구조와 필수 요소를 설명해주세요",
            "재설정 프롬프트의 이상적인 구성 요소와 순서를 체계적으로 설명해주세요",
            "각 구성 요소의 목적과 중요성, 그리고 효과적인 작성법을 설명해주세요",
            "다양한 상황에 적용할 수 있는 범용적인 재설정 프롬프트 템플릿을 제공해주세요",
            "실제 예시를 통해 기본 구조가 어떻게 적용되는지 보여주세요"
        ])
    elif "목적별 재설정" in topic:
        builder.add_instructions([
            "다양한 대화 목적(학술 연구, 창작 활동, 프로그래밍, 문제 해결 등)에 맞춘 재설정 기법을 설명해주세요",
            "각 목적별로 중점을 두어야 할 맥락 요소와 특별히 고려해야 할 사항을 설명해주세요",
            "다양한 목적에 맞는 맞춤형 재설정 템플릿과 예시를 제공해주세요",
            "상황에 따른 템플릿 선택 및 조정 방법을 안내해주세요",
            "각 목적별 재설정 기법의 효과를 극대화하는 팁과 주의사항도 포함해주세요"
        ])
    elif "토큰 최적화" in topic:
        builder.add_instructions([
            "제한된 토큰 내에서 최대한의 맥락을 전달하는 효율적인 재설정 전략을 설명해주세요",
            "토큰 사용을 최적화하는 다양한 기법(압축, 요약, 구조화 등)을 제시해주세요",
            "토큰 절약과 맥락 보존 사이의 균형을 맞추는 원칙과 가이드라인을 설명해주세요",
            "다양한 토큰 제한 상황(매우 제한적, 중간, 여유 있음)에 맞는 전략을 제안해주세요",
            "토큰 효율성을 측정하고 개선하는 방법도 포함해주세요"
        ])
    elif "맥락 선별 기준" in topic:
        builder.add_instructions([
            "재설정 시 포함할 핵심 맥락을 선별하는 체계적인 기준과 프레임워크를 설명해주세요",
            "다양한 유형의 맥락 정보(사실, 결정, 과정, 목표 등)의 중요도를 평가하는 방법을 제시해주세요",
            "상황과 목적에 따라 맥락 선별 기준을 조정하는 방법을 설명해주세요",
            "맥락 정보의 관련성, 최신성, 영향력 등을 평가하는 구체적인 기준을 제공해주세요",
            "맥락 선별 결정을 위한 구체적인 의사결정 트리나 체크리스트를 포함해주세요"
        ])
    elif "검증 및 개선" in topic:
        builder.add_instructions([
            "재설정 효과를 체계적으로 검증하고 지속적으로 개선하는 방법을 설명해주세요",
            "재설정 성공 여부를 평가하는 구체적인 지표와 측정 방법을 제시해주세요",
            "AI의 응답을 통해 재설정의 효과를 분석하는 방법을 설명해주세요",
            "식별된 문제점을 바탕으로 재설정 전략을 개선하는 체계적인 접근법을 제공해주세요",
            "재설정 기법의 지속적 개선을 위한 실험 및 학습 사이클을 설계하는 방법도 포함해주세요"
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
        title="효과적인 대화 재설정 기법",
        topic_options=CONVERSATION_RESET_TECHNIQUES,
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
