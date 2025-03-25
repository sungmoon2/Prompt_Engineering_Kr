"""
무료 및 유료 모델의 차이점과 선택 가이드 실습 모듈

Part 0 - 섹션 0.3.1 실습 코드: 다양한 AI 모델의 무료 및 유료 버전 차이를 비교하고 목적에 맞는 모델을 선택하는 방법을 학습합니다.
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
MODEL_COMPARISON_TOPICS = {
    "1": {"name": "주요 모델 비교", "topic": "ChatGPT, Claude, Gemini 등 주요 AI 모델의 무료/유료 버전 비교", "output_format": "비교표"},
    "2": {"name": "학생 선택 가이드", "topic": "학생 예산에 맞는 AI 모델 선택 가이드", "output_format": "선택 가이드"},
    "3": {"name": "무료 버전 활용", "topic": "무료 AI 모델의 효과적인 활용 전략", "output_format": "활용 전략"},
    "4": {"name": "유료 버전 가치", "topic": "유료 AI 모델 구독의 가치와 활용 방안", "output_format": "투자 가이드"},
    "5": {"name": "모델 전환 전략", "topic": "상황에 따른 모델 전환 및 병행 사용 전략", "output_format": "전략 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용자 맥락 설정: 학생 관점과 예산 고려 명시",
        "구체적 요청사항: 비교 요소, 사용 사례, 비용 효율성 등 세부 요청",
        "실용적 형식 지정: 의사결정에 도움되는 구조화된 비교 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "AI 모델은 무료와 유료 버전 간 성능, 기능, 사용 한도 등에서 중요한 차이가 있습니다",
    "모델 선택은 사용 목적, 사용 빈도, 요구 사항의 복잡성에 따라 달라질 수 있습니다",
    "학생은 효율적인 전략으로 무료 버전의 한계를 극복하거나 유료 모델의 가치를 최대화할 수 있습니다",
    "여러 모델을 상황에 따라 적절히 병행 사용하는 것이 종종 최적의 접근법입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 모델 컨설턴트", 
        "다양한 AI 모델의 특성, 가격, 성능을 분석하고 사용자 요구에 맞는 최적의 선택을 안내하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우는 대학생으로, 제한된 예산 내에서 {topic}에 대한 정보가 필요합니다. "
        f"학업과 프로젝트에 AI를 효과적으로 활용하면서도 비용을 최적화하는 방법을 알고 싶습니다. "
        f"2024년 3월 기준 최신 정보와 가격을 반영한 실용적인 조언을 제공해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "주요 모델 비교" in topic:
        builder.add_instructions([
            "ChatGPT, Claude, Gemini 등 주요 AI 모델의 무료/유료 버전 특성을 객관적으로 비교해주세요",
            "각 모델별 무료 버전의 제한사항(토큰 제한, 요청 빈도 제한, 기능 제한 등)을 구체적으로 설명해주세요",
            "유료 구독의 비용 대비 이점과 추가 기능을 명확히 설명해주세요",
            "각 모델의 주요 강점과 약점, 특화된 용도를 분석해주세요",
            "학생에게 특히 유용한 기능이나 할인 혜택이 있다면 함께 알려주세요"
        ])
    elif "학생 선택 가이드" in topic:
        builder.add_instructions([
            "학생의 다양한 사용 목적(에세이 작성, 연구, 코딩, 창작 등)에 따른 최적의 모델 추천을 제공해주세요",
            "무료로 시작하여 점진적으로 유료 모델을 고려하는 단계별 접근법을 제안해주세요",
            "학생 예산에 맞는 다양한 옵션(월간 구독, 연간 구독, 사용량 기반 API 등)을 비교해주세요",
            "학생 할인이나 교육용 프로그램이 있는 AI 서비스를 알려주세요",
            "비용 대비 학업 생산성 향상을 극대화하는 모델 선택 기준을 제시해주세요"
        ])
    elif "무료 버전 활용" in topic:
        builder.add_instructions([
            "무료 AI 모델을 최대한 효과적으로 활용하는 전략과 팁을 제공해주세요",
            "무료 버전의 일반적인 한계(토큰 제한, 요청 빈도 제한 등)와 이를 극복하는 방법을 설명해주세요",
            "프롬프트 최적화를 통해 무료 모델에서도 높은 품질의 결과를 얻는 방법을 알려주세요",
            "다양한 무료 모델을 병행 사용하여 각각의 강점을 활용하는 전략을 제안해주세요",
            "무료에서 유료로 전환이 필요한 시점을 판단하는 기준도 제시해주세요"
        ])
    elif "유료 버전 가치" in topic:
        builder.add_instructions([
            "학생에게 유료 AI 모델 구독이 실제로 가치 있는 상황과 이유를 분석해주세요",
            "각 유료 모델의 비용 대비 핵심 이점을 학생 관점에서 평가해주세요",
            "유료 모델 투자 비용을 절약하면서도 최대 가치를 얻는 방법을 제안해주세요",
            "학생들이 유료 모델을 통해 얻을 수 있는 구체적인 학업적 이점과 활용 사례를 제시해주세요",
            "다양한 유료 옵션(월간 구독, 연간 구독, API 사용량 기반 등)의 비용 효율성을 비교해주세요"
        ])
    elif "모델 전환 전략" in topic:
        builder.add_instructions([
            "다양한 AI 모델을 상황과 목적에 따라 전환하며 사용하는 효과적인 전략을 설명해주세요",
            "무료와 유료 모델을 병행 사용하여 비용을 최적화하는 방법을 제안해주세요",
            "복잡한 과제를 여러 모델에 분산하여 처리하는 접근법을 설명해주세요",
            "각 모델 간 전환이 필요한 구체적인 상황과 판단 기준을 제시해주세요",
            "여러 모델의 응답을 비교하고 통합하여 더 나은 결과를 얻는 방법도 알려주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 정보를 체계적이고 명확하게 제공해주세요",
            "실제 사용 사례와 예시를 통해 이해를 돕고 실용적인 정보를 제공해주세요",
            "비용과 가치의 균형을 고려한 객관적인 분석을 제공해주세요",
            "학생의 제한된 예산을 고려한 실용적인 조언과 대안을 제시해주세요",
            "시기적절한 의사결정을 위한 명확한 기준을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"비교 정보는 표 형식으로 제공하여 한눈에 비교할 수 있게 해주세요. "
        f"비용 정보는 정확하게 제시하고, 학생 할인이 있는 경우 별도로 표시해주세요. "
        f"권장사항이나 핵심 포인트는 굵은 글씨나 강조 표시를 사용해주세요. "
        f"내용은 학생이 실제 모델 선택과 활용에 바로 적용할 수 있도록 실용적으로 작성해주세요. "
        f"모든 정보는 2024년 3월 기준 최신 데이터를 반영해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="무료 및 유료 모델의 차이점과 선택 가이드",
        topic_options=MODEL_COMPARISON_TOPICS,
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