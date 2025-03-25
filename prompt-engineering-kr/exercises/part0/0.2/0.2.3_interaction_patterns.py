"""
실험 마인드셋: 시도와 오류를 통한 학습 실습 모듈

Part 0 - 섹션 0.2.3 실습 코드: 프롬프트 엔지니어링을 과학적 실험처럼 접근하여 지속적인 개선 방법을 학습합니다.
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
EXPERIMENT_MINDSET_TOPICS = {
    "1": {"name": "실험 접근법", "topic": "프롬프트 엔지니어링에 실험 마인드셋 적용하기", "output_format": "접근법 가이드"},
    "2": {"name": "반복 개선", "topic": "시도와 오류를 통한 프롬프트 반복 개선 방법", "output_format": "개선 과정 안내"},
    "3": {"name": "변형 실험", "topic": "체계적인 프롬프트 변형 실험 설계하기", "output_format": "실험 설계 가이드"},
    "4": {"name": "결과 분석", "topic": "프롬프트 실험 결과 분석 및 학습 방법", "output_format": "분석 프레임워크"},
    "5": {"name": "실패 학습", "topic": "실패한 프롬프트에서 배우는 방법", "output_format": "학습 전략"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "과학적 맥락 설정: 실험 마인드셋과 학습 목적 명시",
        "구체적 요청사항: 실험 설계, 분석 방법, 개선 전략 등 요청",
        "실용적 형식 지정: 단계별 접근법과 실험 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트 엔지니어링은 한 번에 완벽한 결과보다 지속적인 실험과 개선의 과정입니다",
    "체계적인 변수 조정과 결과 분석을 통해 효과적인 패턴을 발견할 수 있습니다",
    "실패한 프롬프트에서도 중요한 교훈을 배울 수 있으며, 이는 학습의 중요한 일부입니다",
    "실험 마인드셋은 새로운 AI 도구나 기능에 적응하는 능력을 키워줍니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "실험적 프롬프트 엔지니어", 
        "과학적 실험 방법론을 프롬프트 엔지니어링에 적용하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우는 대학생으로 {topic}에 관심이 있습니다. "
        f"완벽한 프롬프트를 즉시 만들기보다는 실험적 접근을 통해 점진적으로 개선하는 방법을 배우고 싶습니다. "
        f"과학 실험 방법론(가설, 실험, 관찰, 분석, 개선)을 프롬프트 엔지니어링에 적용하는 방법을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "실험 접근법" in topic:
        builder.add_instructions([
            "프롬프트 엔지니어링에 실험 마인드셋을 적용하는 기본 원칙을 설명해주세요",
            "과학적 실험 방법론의 단계(가설, 실험, 관찰, 분석, 개선)를 프롬프트 개발에 적용하는 방법을 설명해주세요",
            "실험 마인드셋이 프롬프트 개발에 주는 이점과 중요성을 구체적으로 설명해주세요",
            "초보자가 실험 접근법을 시작할 수 있는 간단한 프레임워크와 단계별 가이드를 제공해주세요",
            "실험 접근법을 사용한 프롬프트 개발 사례를 구체적으로 보여주세요"
        ])
    elif "반복 개선" in topic:
        builder.add_instructions([
            "시도와 오류를 통한 프롬프트 반복 개선 과정을 단계별로 설명해주세요",
            "초기 프롬프트에서 시작하여 점진적으로 개선해나가는 실제 사례를 보여주세요",
            "각 반복 단계에서 무엇을 관찰하고 어떤 변경을 결정해야 하는지 설명해주세요",
            "반복 개선 과정에서 흔히 발생하는 함정과 이를 피하는 방법을 알려주세요",
            "반복 개선의 결과를 체계적으로 기록하고 추적하는 방법도 제안해주세요"
        ])
    elif "변형 실험" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 변형 실험을 설계하는 단계별 방법을 설명해주세요",
            "한 번에 하나의 변수만 변경하는 통제된 실험 설계 방법과 그 중요성을 설명해주세요",
            "테스트할 수 있는 다양한 프롬프트 변수(길이, 구조, 지시 방식, 예시 등)를 분석해주세요",
            "A/B 테스트 접근법을 프롬프트 엔지니어링에 적용하는 방법을 설명해주세요",
            "실험 결과를 객관적으로 평가할 수 있는 기준과 방법을 제안해주세요"
        ])
    elif "결과 분석" in topic:
        builder.add_instructions([
            "프롬프트 실험 결과를 체계적으로 분석하는 프레임워크를 제시해주세요",
            "정량적, 정성적 평가 방법을 모두 포함한 종합적 분석 접근법을 설명해주세요",
            "결과 분석에서 주목해야 할 핵심 패턴과 인사이트를 파악하는 방법을 알려주세요",
            "분석 결과를 다음 실험 설계에 반영하는 효과적인 방법을 설명해주세요",
            "실험 결과 분석을 위한 실용적인 템플릿이나 도구를 제안해주세요"
        ])
    elif "실패 학습" in topic:
        builder.add_instructions([
            "실패한 프롬프트에서 배울 수 있는 중요한 교훈과 그 가치를 설명해주세요",
            "실패한 프롬프트를 체계적으로 분석하고 개선점을 찾는 방법을 단계별로 알려주세요",
            "일반적인 프롬프트 실패 유형과 각각의 근본 원인을 분석해주세요",
            "실패를 긍정적인 학습 경험으로 전환하는 마인드셋과 접근법을 설명해주세요",
            "실패로부터 배운 교훈을 기록하고 공유하는 효과적인 방법을 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 핵심 원칙과 접근법을 명확하게 설명해주세요",
            "초보자도 쉽게 따라할 수 있는 단계별 적용 방법을 제시해주세요",
            "실제 사례와 예시를 통해 개념을 구체화해주세요",
            "흔한 문제와 해결 방법을 포함해주세요",
            "지속적인 학습과 개선을 위한 실용적인 팁과 전략을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"과학 실험 보고서처럼 구조화된 형식(목적, 방법, 결과, 분석, 결론)을 활용하면 좋겠습니다. "
        f"체계적인 단계와 프로세스는 번호를 매겨 순서대로 설명해주세요. "
        f"프롬프트 실험 예시와 결과는 표나 비교 형식으로 명확하게 시각화해주세요. "
        f"핵심 개념과 주요 인사이트는 굵은 글씨나 인용구로 강조해주세요. "
        f"실제 실험과 적용을 위한 템플릿이나 워크시트 형식도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="실험 마인드셋: 시도와 오류를 통한 학습",
        topic_options=EXPERIMENT_MINDSET_TOPICS,
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