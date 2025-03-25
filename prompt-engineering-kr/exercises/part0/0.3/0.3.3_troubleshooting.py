"""
채팅 히스토리의 중요성과 관리 전략 실습 모듈

Part 0 - 섹션 0.3.3 실습 코드: 대화 맥락 유지와 효과적인 채팅 히스토리 관리 방법을 학습합니다.
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
CHAT_HISTORY_TOPICS = {
    "1": {"name": "중요성 이해", "topic": "채팅 히스토리가 AI 응답 품질에 미치는 영향", "output_format": "분석 가이드"},
    "2": {"name": "맥락 유지", "topic": "효과적인 대화 맥락 유지 전략", "output_format": "전략 가이드"},
    "3": {"name": "히스토리 관리", "topic": "채팅 히스토리 저장 및 관리 방법", "output_format": "관리 시스템"},
    "4": {"name": "한계 극복", "topic": "토큰 제한 등 채팅 히스토리 한계 극복 방법", "output_format": "해결책 가이드"},
    "5": {"name": "대화 재구성", "topic": "이전 대화 맥락을 효과적으로 요약하고 재구성하는 방법", "output_format": "프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용자 맥락 설정: 학습 목적과 필요성 명시",
        "구체적 요청사항: 중요성, 전략, 한계 극복 방법 등 세부 요청",
        "실용적 형식 지정: 단계별 접근법과 즉시 적용 가능한 전략 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "채팅 히스토리는 AI가 대화 맥락을 이해하고 일관된 응답을 제공하는 데 중요합니다",
    "히스토리 관리의 핵심은 토큰 한계 내에서 관련 맥락을 효과적으로 유지하는 것입니다",
    "대화 요약 및 재구성 기술은 장기 대화나 복잡한 주제를 다룰 때 특히 유용합니다",
    "채팅 히스토리의 효과적인 활용은 반복을 줄이고 AI 응답의 품질을 높여줍니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "대화 관리 전문가", 
        "AI와의 대화 맥락을 효과적으로 유지하고 관리하는 방법에 정통한 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우는 대학생으로, {topic}에 대해 이해하고 싶습니다. "
        f"AI와의 대화에서 맥락 유지의 중요성을 깨닫고 있으며, 효과적인 채팅 히스토리 관리 방법을 배우고 싶습니다. "
        f"실용적이고 즉시 적용 가능한 전략과 팁을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "중요성" in topic:
        builder.add_instructions([
            "채팅 히스토리가 AI의 응답 품질과 정확성에 미치는 영향을 설명해주세요",
            "히스토리 없이 질문할 때와 히스토리가 있을 때의 차이를 구체적인 예시와 함께 보여주세요",
            "어떤 유형의 작업이나 대화에서 채팅 히스토리가 특히 중요한지 분석해주세요",
            "히스토리 관리의 잘못된 접근법과 그 결과에 대해서도 설명해주세요",
            "학습과 프로젝트에서 채팅 히스토리 활용의 장기적 이점을 설명해주세요"
        ])
    elif "맥락 유지" in topic:
        builder.add_instructions([
            "효과적인 대화 맥락 유지를 위한 핵심 전략과 원칙을 설명해주세요",
            "대화 초기에 맥락을 명확히 설정하는 방법과 그 중요성을 설명해주세요",
            "맥락 단절이 발생했을 때 대화를 다시 연결하는 효과적인 방법을 알려주세요",
            "주제 전환 시 맥락을 유지하면서 새로운 정보를 도입하는 방법을 설명해주세요",
            "대화의 목적과 성격에 따른 맥락 유지 전략의 차이점도 분석해주세요"
        ])
    elif "히스토리 관리" in topic:
        builder.add_instructions([
            "다양한 채팅 히스토리 저장 및 관리 방법과 도구를 비교 설명해주세요",
            "효과적인 채팅 세션 구성과 분리 기준을 제안해주세요",
            "중요한 대화를 체계적으로 기록하고 검색할 수 있는 시스템을 설명해주세요",
            "다양한 목적(학습, 프로젝트, 참조 등)에 맞는 히스토리 관리 전략을 제시해주세요",
            "프라이버시와 보안을 고려한 채팅 히스토리 관리 방법도 포함해주세요"
        ])
    elif "한계 극복" in topic:
        builder.add_instructions([
            "AI 모델의 토큰 제한과 그것이 채팅 히스토리에 미치는 영향을 설명해주세요",
            "토큰 제한 내에서 핵심 맥락을 유지하는 효과적인 전략을 제시해주세요",
            "긴 대화나 복잡한 정보를 효율적으로 관리하는 방법을 알려주세요",
            "히스토리가 잘릴 때 중요한 정보를 보존하기 위한 우선순위 설정 방법을 설명해주세요",
            "새 세션에서 이전 대화의 핵심 맥락을 효과적으로 재설정하는 방법을 알려주세요"
        ])
    elif "대화 재구성" in topic:
        builder.add_instructions([
            "이전 대화 내용을 효과적으로 요약하고 재구성하는 방법을 단계별로 설명해주세요",
            "요약 시 포함해야 할 핵심 요소와 생략 가능한 요소를 구분하는 기준을 제시해주세요",
            "AI에게 이전 대화 맥락을 효과적으로 전달하는 방법을 구체적인 예시와 함께 설명해주세요",
            "대화 목적에 따른 다양한 요약 및 재구성 템플릿을 제공해주세요",
            "복잡한 프로젝트나 장기 대화의 맥락을 유지하기 위한 점진적 요약 전략을 설명해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 개념과 원칙을 명확하게 설명해주세요",
            "구체적인 예시와 사례를 통해 이해를 돕고 실제 적용 방법을 보여주세요",
            "초보자가 바로 적용할 수 있는 단계별 접근법을 제시해주세요",
            "흔한 문제점과 해결책, 주의사항을 포함해주세요",
            "더 효과적인 대화 관리를 위한 고급 팁과 전략도 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"핵심 개념이나 중요 포인트는 굵은 글씨로 강조하고, 예시는 인용구로 구분해주세요. "
        f"단계별 전략이나 방법은 번호를 매겨 순서대로 설명해주세요. "
        f"비교 정보는 표 형식으로 제공하여 한눈에 파악할 수 있게 해주세요. "
        f"실제 대화 예시는 사용자와 AI의 대화 형식으로 표현해주세요. "
        f"모든 내용은 초보자도 쉽게 이해하고 바로 적용할 수 있도록 설명해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="채팅 히스토리의 중요성과 관리 전략",
        topic_options=CHAT_HISTORY_TOPICS,
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