"""
프롬프트 개선 사이클 실습 모듈

Part 8 - 섹션 8.2 실습 코드: 반복 개선 사이클을 적용하여 프롬프트 최적화 방법을 학습합니다.
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
from utils.ai_client import get_completion

# 프롬프트 개선 주제 옵션 정의
PROMPT_IMPROVEMENT_TOPICS = {
    "1": {
        "name": "역할 설정 개선", 
        "topic": "AI의 역할 설정이 응답의 전문성에 미치는 영향 분석", 
        "output_format": "A/B 테스트 보고서"
    },
    "2": {
        "name": "맥락 제공 전략", 
        "topic": "프롬프트의 맥락 제공 방식 최적화", 
        "output_format": "개선 프레임워크"
    },
    "3": {
        "name": "지시문 구조화", 
        "topic": "효과적인 지시문 작성을 위한 구조화 전략", 
        "output_format": "지시문 템플릿"
    },
    "4": {
        "name": "예시 활용 전략", 
        "topic": "프롬프트의 예시 포함 방식과 그 영향", 
        "output_format": "예시 활용 가이드라인"
    },
    "5": {
        "name": "출력 형식 최적화", 
        "topic": "원하는 출력 형식을 얻기 위한 프롬프트 최적화", 
        "output_format": "형식 지정 전략"
    }
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["기본 프롬프트로 초기 결과 확인"],
    "enhanced": [
        "체계적인 A/B 테스트 설계",
        "한 가지 변수에 집중한 개선 전략",
        "명확한 평가 기준 설정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트 개선은 체계적이고 반복적인 실험 과정입니다",
    "한 번에 하나의 변수만 변경하여 명확한 개선 효과 식별",
    "객관적인 평가 기준을 통해 프롬프트 성능 비교",
    "실험 결과를 문서화하고 인사이트 축적"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성 - A/B 테스트를 위한 구조"""
    builder = PromptBuilder()
    
    # 주제별 맞춤 프롬프트 설계
    if "역할 설정" in topic:
        builder.add_role(
            "프롬프트 엔지니어링 전문가", 
            "AI 응답의 전문성과 정확성을 높이기 위한 역할 설정 최적화 전략을 제시하는 전문가"
        )
        
        builder.add_context(
            f"AI의 역할 설정이 응답의 전문성에 미치는 영향을 분석하고자 합니다. "
            f"같은 주제에 대해 다양한 역할 설정을 적용했을 때 나타나는 차이점을 체계적으로 비교하고 싶습니다."
        )
        
        builder.add_instructions([
            "다양한 역할 설정이 응답의 깊이, 전문성, 관점에 어떤 영향을 미치는지 분석해주세요",
            "최소 3개의 서로 다른 역할 설정을 비교하여 각각의 장단점을 설명해주세요",
            "역할 설정의 세부 요소(전문성 수준, 관점, 배경 등)가 응답에 미치는 영향을 상세히 설명해주세요",
            "각 역할 설정에 따른 응답 예시를 포함하여 차이점을 명확히 보여주세요"
        ])
        
    elif "맥락 제공" in topic:
        builder.add_role(
            "커뮤니케이션 전략 전문가", 
            "효과적인 맥락 제공을 통해 AI 응답의 정확성과 관련성을 높이는 전문가"
        )
        
        builder.add_context(
            f"프롬프트에서 맥락 제공의 중요성을 탐구하고자 합니다. "
            f"같은 주제에 대해 다양한 수준과 방식으로 맥락을 제공했을 때 응답의 변화를 분석하고 싶습니다."
        )
        
        builder.add_instructions([
            "맥락 제공의 다양한 방식(배경 정보, 목적, 사용 상황 등)을 비교 분석해주세요",
            "최소 3가지 서로 다른 맥락 제공 전략을 비교하여 각각의 효과를 평가해주세요",
            "맥락의 구체성, 깊이, 관련성이 AI 응답에 미치는 영향을 상세히 설명해주세요",
            "각 맥락 제공 방식에 따른 응답 예시를 포함하여 차이점을 명확히 보여주세요"
        ])
        
    # 다른 주제들에 대해서도 유사한 패턴으로 구현 가능
    else:
        builder.add_role(
            "프롬프트 최적화 전문가", 
            "AI 프롬프트의 효과성을 체계적으로 분석하고 개선하는 전문가"
        )
        
        builder.add_context(
            f"{topic}에 대한 프롬프트 개선 전략을 탐구하고자 합니다. "
            f"다양한 접근 방식을 비교하여 최적의 프롬프트 구성 방법을 찾고자 합니다."
        )
        
        builder.add_instructions([
            f"{topic}과 관련된 다양한 프롬프트 구성 방식을 비교 분석해주세요",
            "최소 3가지 서로 다른 접근 방식을 비교하여 각각의 장단점을 평가해주세요",
            "각 접근 방식이 AI 응답에 미치는 영향을 상세히 설명해주세요",
            "명확한 비교를 위한 응답 예시를 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 명확하게 구조화하고, "
        f"각 접근 방식의 차이점을 표, 비교 분석, 구체적 예시를 통해 보여주세요. "
        f"객관적이고 체계적인 분석 결과를 제공해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 개선 사이클과 A/B 테스트",
        topic_options=PROMPT_IMPROVEMENT_TOPICS,
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