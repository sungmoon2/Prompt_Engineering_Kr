"""
대화 브리지 설계 실습 모듈

Part 3 - 섹션 3.2.2 실습 코드: 세션 간의 연속성을 위한
효과적인 대화 브리지를 설계하는 방법을 학습합니다.
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
CONVERSATION_BRIDGE_TOPICS = {
    "1": {"name": "브리지 기본 구조", "topic": "효과적인 대화 브리지의 핵심 구성 요소와 구조", "output_format": "설계 가이드"},
    "2": {"name": "프로젝트별 브리지", "topic": "다양한 프로젝트 유형에 최적화된 대화 브리지 템플릿", "output_format": "템플릿 모음"},
    "3": {"name": "시간 간격별 브리지", "topic": "세션 간 시간 간격에 따른 맞춤형 브리지 설계 전략", "output_format": "전략 가이드"},
    "4": {"name": "브리지 연결성", "topic": "세션 간 자연스러운 흐름과 연결성을 강화하는 기법", "output_format": "기법 가이드"},
    "5": {"name": "브리지 진화 관리", "topic": "장기 프로젝트에서 브리지의 진화와 관리 방법", "output_format": "관리 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 대화 브리지의 목표와 필요성 설정",
        "구체적 요청: 체계적인 브리지 설계와 구성 요소 요청",
        "실용적 형식: 즉시 적용 가능한 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "대화 브리지는 세션 간의 연속성을 유지하여 작업 효율성과 일관성을 높이는 핵심 도구입니다",
    "효과적인 브리지는 이전 세션의 핵심 맥락과 다음 세션의 방향성을 명확히 연결합니다",
    "프로젝트 유형과 세션 간 시간 간격에 따라 브리지 구조와 상세도를 조정해야 합니다",
    "브리지는 단순한 맥락 요약이 아닌 세션 간 자연스러운 전환을 위한 연결 장치입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "대화 연속성 설계자", 
        "AI와의 장기적인 대화에서 세션 간 연속성을 효과적으로 유지하기 위한 대화 브리지 설계 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 장기 프로젝트에서 서로 다른 세션 간의 연속성을 유지하는 것이 중요하다는 것을 깨달았습니다. "
        f"효과적인 대화 브리지를 설계하여 이전 세션의 맥락을 다음 세션으로 자연스럽게 전달하고, "
        f"프로젝트의 일관성과 진행 효율성을 높이는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "브리지 기본 구조" in topic:
        builder.add_instructions([
            "효과적인 대화 브리지의 핵심 구성 요소와 기본 구조를 설명해주세요",
            "각 구성 요소의 목적과 기능, 그리고 효과적인 작성법을 설명해주세요",
            "브리지의 시작, 중간, 종료 부분이 각각 어떤 역할을 하는지 설명해주세요",
            "다양한 상황에 적용할 수 있는 범용적인 브리지 템플릿을 제공해주세요",
            "실제 예시를 통해 효과적인 브리지 구조가 어떻게 적용되는지 보여주세요"
        ])
    elif "프로젝트별 브리지" in topic:
        builder.add_instructions([
            "다양한 프로젝트 유형(학술 연구, 창작 활동, 프로그래밍, 학습 등)에 최적화된 브리지 템플릿을 제공해주세요",
            "각 프로젝트 유형에 중요한 맥락 요소와 브리지 설계 시 고려할 특별한 사항을 설명해주세요",
            "다양한 프로젝트 유형별 맞춤형 브리지 템플릿과 구체적인 예시를 제공해주세요",
            "프로젝트 특성에 따른 브리지 선택 및 조정 방법을 안내해주세요",
            "각 프로젝트 유형별 브리지의 효과를 극대화하는 팁과 주의사항도 포함해주세요"
        ])
    elif "시간 간격별 브리지" in topic:
        builder.add_instructions([
            "세션 간 시간 간격(짧은 간격, 중간 간격, 긴 간격)에 따른 맞춤형 브리지 설계 전략을 설명해주세요",
            "다양한 시간 간격에 따라 브리지에 포함해야 할 정보의 유형과 상세도를 조정하는 방법을 제시해주세요",
            "오랜 시간이 지난 후에도 프로젝트 맥락을 효과적으로 복원하는 브리지 설계 전략을 설명해주세요",
            "시간에 따른 기억 감소를 고려한 브리지 설계 원칙을 제안해주세요",
            "다양한 시간 간격별 브리지 템플릿과 실제 적용 예시를 포함해주세요"
        ])
    elif "브리지 연결성" in topic:
        builder.add_instructions([
            "세션 간 자연스러운 흐름과 연결성을 강화하는 다양한 기법을 설명해주세요",
            "이전 세션의 종료와 다음 세션의 시작을 매끄럽게 연결하는 전략을 제시해주세요",
            "감정적, 인지적 연속성을 유지하는 방법과 그 중요성을 설명해주세요",
            "이전 세션의 미해결 문제나 다음 단계를 효과적으로 연결하는 기법을 알려주세요",
            "연결성을 강화하는 언어적, 구조적 장치와 그 활용 예시를 포함해주세요"
        ])
    elif "브리지 진화 관리" in topic:
        builder.add_instructions([
            "장기 프로젝트에서 브리지의 진화와 체계적 관리 방법을 설명해주세요",
            "프로젝트 진행에 따라 브리지 내용과 구조를 어떻게 발전시켜 나가야 하는지 제시해주세요",
            "여러 세션에 걸친 브리지의 일관성과 연속성을 유지하는 방법을 설명해주세요",
            "브리지 버전 관리 및 중요 변경사항 추적 시스템을 제안해주세요",
            "장기 프로젝트의 다양한 단계에 맞춘 브리지 관리 전략과 실제 적용 사례를 포함해주세요"
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
        title="대화 브리지 설계",
        topic_options=CONVERSATION_BRIDGE_TOPICS,
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
