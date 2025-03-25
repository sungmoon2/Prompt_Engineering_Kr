"""
실습 환경 준비 및 기본 팁 실습 모듈

Part 0 - 섹션 0.3 실습 코드: 프롬프트 엔지니어링 실습을 위한 환경 준비와 기본 팁을 학습합니다.
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
ENVIRONMENT_SETUP_TOPICS = {
    "1": {"name": "모델 선택", "topic": "무료 및 유료 AI 모델의 차이점과 선택 가이드", "output_format": "비교 가이드"},
    "2": {"name": "프롬프트 관리", "topic": "프롬프트 저장 및 관리 방법", "output_format": "관리 시스템 가이드"},
    "3": {"name": "대화 관리", "topic": "채팅 히스토리의 중요성과 관리 전략", "output_format": "실천 가이드"},
    "4": {"name": "API 활용", "topic": "API를 통한 AI 모델 활용 기초", "output_format": "시작 가이드"},
    "5": {"name": "작업 환경", "topic": "효율적인 프롬프트 엔지니어링 작업 환경 구성", "output_format": "환경 설정 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 맥락 설정: 초보자 관점과 실용적 목적 명시",
        "세부 요청사항: 비교 정보, 단계별 가이드, 구체적 예시 등 요청",
        "구조화된 형식 요청: 참조하기 쉬운 가이드 형식 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "적절한 AI 모델 선택은 비용, 기능, 목적에 따라 달라질 수 있습니다",
    "프롬프트와 대화 히스토리를 체계적으로 관리하면 학습과 재사용이 용이해집니다",
    "효율적인 작업 환경 구성은 프롬프트 엔지니어링 생산성을 크게 높입니다",
    "API 활용은 자동화와 맞춤형 응용 프로그램 개발에 중요한 기술입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 엔지니어링 환경 전문가", 
        "AI와 효과적으로 작업하기 위한 실용적인 환경 설정과 도구 활용법에 정통한 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 시작하는 대학생으로 {topic}에 대해 배우고 있습니다. "
        f"효율적인 학습과 실습을 위한 실용적인 정보와 구체적인 방법이 필요합니다. "
        f"2024년 최신 정보와 도구를 기준으로 초보자도 쉽게 따라할 수 있는 가이드를 제공해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "모델 선택" in topic:
        builder.add_instructions([
            "ChatGPT, Claude, Gemini 등 주요 AI 모델의 무료/유료 버전 차이를 명확히 비교해주세요",
            "각 모델의 장단점, 특징, 사용 제한 등을 객관적으로 분석해주세요",
            "학생 예산에 맞는 최적의 모델 선택 기준과 추천을 제공해주세요",
            "무료 버전으로 최대한의 효과를 얻는 전략과 팁을 알려주세요",
            "유료 모델이 특히 유용한 상황과 투자 가치가 있는 경우를 설명해주세요"
        ])
    elif "프롬프트 관리" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 저장 및 관리 시스템 구축 방법을 단계별로 설명해주세요",
            "다양한 프롬프트 관리 도구와 방법(노트앱, 전용 도구, 분류 시스템 등)을 비교해주세요",
            "재사용 가능한 프롬프트 템플릿 작성 및 관리 전략을 제안해주세요",
            "프롬프트 버전 관리와 개선 기록 방법을 설명해주세요",
            "프롬프트 정리를 위한 효과적인 태깅 및 분류 시스템을 제안해주세요"
        ])
    elif "대화 관리" in topic:
        builder.add_instructions([
            "채팅 히스토리가 프롬프트 효과성에 미치는 영향을 설명해주세요",
            "효과적인 대화 히스토리 관리 전략과 방법을 단계별로 제시해주세요",
            "대화 맥락 유지를 위한 기술과 주의사항을 설명해주세요",
            "대화 히스토리의 한계(토큰 제한 등)와 이를 극복하는 방법을 알려주세요",
            "학습과 참조를 위한 대화 내용 저장 및 정리 방법을 제안해주세요"
        ])
    elif "API 활용" in topic:
        builder.add_instructions([
            "AI 모델 API 활용의 기본 개념과 이점을 초보자도 이해할 수 있게 설명해주세요",
            "API 키 설정, 기본 요청 구조, 응답 처리 등 시작 단계를 명확히 안내해주세요",
            "주요 AI 모델(OpenAI, Anthropic, Google 등)의 API 특징과 차이점을 비교해주세요",
            "간단한 API 사용 예시와 코드 템플릿을 제공해주세요",
            "API 사용 시 비용 관리와 토큰 최적화 방법도 포함해주세요"
        ])
    elif "작업 환경" in topic:
        builder.add_instructions([
            "효율적인 프롬프트 엔지니어링을 위한 이상적인 작업 환경 구성 요소를 설명해주세요",
            "유용한 도구, 앱, 브라우저 확장 프로그램 등을 카테고리별로 추천해주세요",
            "작업 흐름 최적화를 위한 환경 설정 팁과 단축키 활용법을 알려주세요",
            "다양한 기기(데스크톱, 모바일)에서의 효과적인 AI 활용 환경 설정 방법을 설명해주세요",
            "무료로 시작할 수 있는 기본 설정과 점진적으로 개선할 수 있는 방법을 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 정보를 초보자도 이해하기 쉽게 설명해주세요",
            "실용적인 적용 방법과 단계별 가이드를 제공해주세요",
            "다양한 옵션이나 도구를 객관적으로 비교하여 선택에 도움을 주세요",
            "비용 효율적인 접근법과 무료 대안에 대한 정보도 포함해주세요",
            "실제 적용 시 주의사항과 팁도 함께 알려주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"비교 정보는 표 형식으로 제공하여 한눈에 파악할 수 있게 해주세요. "
        f"단계별 설명은 번호를 매겨 순서대로 안내해주세요. "
        f"중요한 정보나 주의사항은 강조 표시를 사용하여 눈에 띄게 해주세요. "
        f"복잡한 개념은 예시나 비유를 통해 이해하기 쉽게 설명해주세요. "
        f"실용적이고 즉시 적용 가능한 정보에 중점을 두어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="실습 환경 준비 및 기본 팁",
        topic_options=ENVIRONMENT_SETUP_TOPICS,
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