"""
다양한 AI 도구 비교와 특징 실습 모듈

Part 0 - 섹션 0.1.3 실습 코드: ChatGPT, Claude, Gemini 등 주요 AI 도구의 특징, 장단점 및 활용 방법을 비교합니다.
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
AI_TOOLS_TOPICS = {
    "1": {"name": "주요 모델 비교", "topic": "ChatGPT, Claude, Gemini 등 주요 생성형 AI 모델 비교", "output_format": "비교표"},
    "2": {"name": "ChatGPT 특징", "topic": "ChatGPT의 주요 특징, 장단점 및 활용 사례", "output_format": "안내서"},
    "3": {"name": "Claude 특징", "topic": "Claude의 주요 특징, 장단점 및 활용 사례", "output_format": "안내서"},
    "4": {"name": "Gemini 특징", "topic": "Gemini의 주요 특징, 장단점 및 활용 사례", "output_format": "안내서"},
    "5": {"name": "목적별 모델 선택", "topic": "사용 목적에 따른 적합한 AI 모델 선택 가이드", "output_format": "의사결정 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "사용 목적 제시: 모델 비교와 선택을 위한 정보 요청",
        "구체적 분석 요청: 기능, 장단점, 비용, 최적 사용 사례 등 상세 정보 요청",
        "실용적 출력 형식: 의사결정이나 참조에 적합한 구조화된 형식 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "다양한 생성형 AI 모델은 각각 고유한 특성, 강점, 약점을 가지고 있습니다",
    "모델 선택은 사용 목적, 필요한 기능, 비용, 접근성 등 여러 요소를 고려해야 합니다",
    "각 모델에 최적화된 프롬프트 전략은 다를 수 있으며, 이를 이해하는 것이 중요합니다",
    "모델 간 비교 정보를 구체적으로 요청하면 더 유용한 의사결정 자료를 얻을 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 도구 분석 전문가", 
        "다양한 생성형 AI 모델의 특성과 활용 방법에 정통한 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 학업과 프로젝트에 가장 적합한 AI 도구를 선택하기 위해 {topic}에 대한 정보가 필요합니다. "
        f"다양한 옵션 중에서 상황에 맞는 최적의 도구를 선택하고 활용하기 위한 안내가 필요합니다. "
        f"2024년 최신 정보를 기준으로 실용적인 가이드를 제공해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "비교" in topic:
        builder.add_instructions([
            "ChatGPT, Claude, Gemini 등 주요 생성형 AI 모델의 핵심 특징을 비교해주세요",
            "각 모델의 강점과 약점을 객관적으로 분석해주세요",
            "모델별 비용 구조, 무료/유료 버전의 차이점을 설명해주세요",
            "접근성(API 지원, 지역 제한 등)과 사용자 인터페이스 특징도 비교해주세요",
            "각 모델이 특히 뛰어난 작업이나 사용 사례를 구체적으로 제시해주세요"
        ])
    elif "ChatGPT" in topic:
        builder.add_instructions([
            "ChatGPT의 다양한 버전과 각 버전의 주요 특징을 설명해주세요",
            "ChatGPT의 강점과 약점을 구체적인 예시와 함께 분석해주세요",
            "무료 버전과 유료 버전(ChatGPT Plus)의 차이점을 명확히 설명해주세요",
            "ChatGPT가 특히 효과적인 학업/프로젝트 활용 사례를 최소 5가지 제시해주세요",
            "ChatGPT 사용 시 알아두면 좋을 팁과 주의사항을 공유해주세요"
        ])
    elif "Claude" in topic:
        builder.add_instructions([
            "Claude의 다양한 버전과 각 버전의 주요 특징을 설명해주세요",
            "Claude의 강점과 약점을 구체적인 예시와 함께 분석해주세요",
            "무료 버전과 유료 버전의 차이점을 명확히 설명해주세요",
            "Claude가 특히 효과적인 학업/프로젝트 활용 사례를 최소 5가지 제시해주세요",
            "Claude 사용 시 알아두면 좋을 팁과 주의사항을 공유해주세요"
        ])
    elif "Gemini" in topic:
        builder.add_instructions([
            "Gemini의 다양한 버전과 각 버전의 주요 특징을 설명해주세요",
            "Gemini의 강점과 약점을 구체적인 예시와 함께 분석해주세요",
            "무료 버전과 유료 버전의 차이점을 명확히 설명해주세요",
            "Gemini가 특히 효과적인 학업/프로젝트 활용 사례를 최소 5가지 제시해주세요",
            "Gemini 사용 시 알아두면 좋을 팁과 주의사항을 공유해주세요"
        ])
    elif "선택" in topic:
        builder.add_instructions([
            "다양한 학업/프로젝트 상황별로 최적의 AI 모델 추천과 그 이유를 설명해주세요",
            "에세이 작성, 코딩 도움, 연구 분석, 창작 활동 등 구체적인 사용 목적별 비교를 제공해주세요",
            "예산 제약이 있는 학생을 위한 무료/저비용 옵션과, 성능 중심 유료 옵션을 구분해서 설명해주세요",
            "특정 모델 선택 시 고려해야 할 프롬프트 엔지니어링 전략의 차이점도 설명해주세요",
            "AI 도구 활용 시 일반적인 윤리적 고려사항과 학문적 진실성 유지 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 핵심 정보를 명확하고 객관적으로 제공해주세요",
            "장점과 단점을 균형 있게 분석해주세요",
            "실제 사용 사례와 예시를 통해 이해를 돕고 실용적인 정보를 제공해주세요",
            "비용, 접근성, 사용자 경험 등 실질적인 고려 사항을 포함해주세요",
            "추가 학습이나 참고할 수 있는 자료도 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"비교 정보는 가능한 표 형식으로 제공하여 한눈에 파악할 수 있게 해주세요. "
        f"핵심 정보와 중요한 차이점은 굵은 글씨나 강조 표시를 사용해주세요. "
        f"실용적인 팁이나 주의사항은 별도 섹션으로 구분하여 제공해주세요. "
        f"모든 정보는 2024년 3월 기준으로 최신 정보를 반영해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="다양한 AI 도구 비교와 특징",
        topic_options=AI_TOOLS_TOPICS,
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