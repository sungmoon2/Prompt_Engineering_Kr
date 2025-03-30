"""
토큰 제한의 이해와 대응 전략 실습 모듈

Part 3 - 섹션 3.1.1 실습 코드: AI 모델과의 대화에서 토큰 제한을 이해하고
효과적인 대응 전략을 학습합니다.
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
TOKEN_LIMITATION_TOPICS = {
    "1": {"name": "토큰 이해", "topic": "AI 대화에서 토큰의 개념과 제한 이해하기", "output_format": "개념 가이드"},
    "2": {"name": "모델별 특성", "topic": "다양한 AI 모델의 토큰 특성과 제한 비교", "output_format": "비교 분석"},
    "3": {"name": "토큰 최적화", "topic": "토큰 사용을 최적화하는 프롬프트 작성 전략", "output_format": "전략 가이드"},
    "4": {"name": "길이 관리", "topic": "긴 대화와 복잡한 맥락의 토큰 관리 방법", "output_format": "실용 가이드"},
    "5": {"name": "세션 분할", "topic": "복잡한 작업의 효과적인 세션 분할 전략", "output_format": "분할 프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 토큰 제한 이해와 대응 목표 설정",
        "구체적 요청: 다양한 모델과 상황에 맞는 전략 요청",
        "실용적 형식: 즉시 적용 가능한 예시와 기법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "토큰은 AI 모델이 텍스트를 처리하는 기본 단위로, 각 모델마다 처리할 수 있는 토큰 수에 제한이 있습니다",
    "모델별 토큰 제한과 특성을 이해하면 각 상황에 맞게 대화를 최적화할 수 있습니다",
    "효율적인 프롬프트 작성과 구조화는 토큰 사용을 최소화하면서 원하는 결과를 얻는 데 핵심입니다",
    "복잡한 작업은 논리적 세션으로 분할하여 토큰 제한 내에서 효과적으로 처리할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 토큰 전문가", 
        "AI 대화 모델의 토큰 처리 방식과 제한을 깊이 이해하고 효과적인 대응 전략을 제시하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와의 대화에서 토큰 제한으로 인한 문제를 자주 경험하고 있으며, 이를 효과적으로 이해하고 대응하는 방법을 배우고 싶습니다. "
        f"특히 학업과 연구 프로젝트에서 복잡한 주제와 긴 대화를 관리하는 실용적인 전략이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "토큰 이해" in topic:
        builder.add_instructions([
            "AI 대화에서 토큰의 기본 개념과 작동 원리를 명확히 설명해주세요",
            "토큰이 어떻게 계산되고 다양한 언어 요소(단어, 구두점, 공백 등)가 토큰으로 어떻게 변환되는지 설명해주세요",
            "토큰 제한이 대화에 미치는 영향과 주요 도전 과제를 분석해주세요",
            "토큰 수를 대략적으로 추정하는 실용적인 방법을 제시해주세요",
            "토큰의 개념을 이해하는 데 도움이 되는 시각적 비유나 예시를 포함해주세요"
        ])
    elif "모델별 특성" in topic:
        builder.add_instructions([
            "주요 AI 모델(GPT-3.5, GPT-4, Claude 등)의 토큰 제한과 특성을 비교 분석해주세요",
            "각 모델의 토큰 처리 방식과 고유한 강점/약점을 설명해주세요",
            "모델별 맥락 창(context window) 크기와 이것이 대화에 미치는 영향을 설명해주세요",
            "다양한 모델에 대해 비용 효율적인 토큰 사용 방법을 제안해주세요",
            "특정 작업이나 목적에 가장 적합한 모델을 선택하는 기준도 포함해주세요"
        ])
    elif "토큰 최적화" in topic:
        builder.add_instructions([
            "토큰 사용을 최적화하면서도 효과적인 프롬프트를 작성하는 전략을 설명해주세요",
            "불필요한 토큰을 줄이는 구체적인 기법과 작성 패턴을 제시해주세요",
            "정보 밀도를 높이는 효율적인 구조화 방법을 안내해주세요",
            "다양한 목적(정보 요청, 창작, 코딩 등)에 따른 최적화된 프롬프트 예시를 제공해주세요",
            "토큰 최적화와 명확한 의사소통 사이의 균형을 맞추는 방법도 설명해주세요"
        ])
    elif "길이 관리" in topic:
        builder.add_instructions([
            "긴 대화와 복잡한 맥락에서 토큰을 효과적으로 관리하는 방법을 설명해주세요",
            "장기적인 대화에서 맥락 연속성을 유지하면서 토큰을 절약하는 전략을 제시해주세요",
            "대화 요약, 압축, 참조 기법 등 맥락 보존 전략을 자세히 설명해주세요",
            "토큰 제한에 접근했을 때의 경고 신호와 대응 방법을 안내해주세요",
            "학술 연구나 복잡한 프로젝트에 특화된 토큰 관리 전략도 포함해주세요"
        ])
    elif "세션 분할" in topic:
        builder.add_instructions([
            "복잡한 작업을 토큰 제한에 맞게 효과적으로 분할하는 전략을 설명해주세요",
            "논리적이고 효율적인 세션 분할 지점을 식별하는 방법을 제시해주세요",
            "세션 간 연속성과 맥락을 유지하기 위한 기법을 자세히 설명해주세요",
            "다양한 작업 유형(연구, 창작, 프로그래밍 등)에 최적화된 분할 접근법을 비교해주세요",
            "분할된 세션을 관리하고 통합하는 체계적인 워크플로우도 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "기본 개념과 원칙을 명확히 설명해주세요",
            "다양한 상황과 목적에 맞는 구체적인 전략과 기법을 제시해주세요",
            "실제 사례와 예시를 통해 적용 방법을 보여주세요",
            "실무에 바로 적용할 수 있는 팁과 가이드라인을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 예시와 비교는 표 형식으로 제시하면 이해하기 쉽습니다. "
        f"코드 블록을 사용하여 템플릿이나 예시 프롬프트를 구분해주세요. "
        f"핵심 개념은 굵은 글씨로 강조하고, 중요한 팁은 인용 형식으로 표시해주세요. "
        f"모든 내용은 대학생이 실제 AI 대화에 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="토큰 제한의 이해와 대응 전략",
        topic_options=TOKEN_LIMITATION_TOPICS,
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
