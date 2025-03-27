"""
다양한 관점 통합하기 실습 모듈

Part 2 - 섹션 2.3.1 실습 코드: 서로 다른 이론, 학문 분야, 관점을 효과적으로 통합하는 기법을 학습합니다.
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
PERSPECTIVE_TOPICS = {
    "1": {"name": "학제간 통합", "topic": "다양한 학문 분야의 관점 통합을 위한 학제간 접근법", "output_format": "통합 가이드"},
    "2": {"name": "다이론 통합", "topic": "상충되는 이론과 모델의 효과적인 통합 방법", "output_format": "통합 프레임워크"},
    "3": {"name": "다중방법론", "topic": "양적/질적 방법론을 결합한 혼합 연구 접근법", "output_format": "방법론 가이드"},
    "4": {"name": "대립 관점 조정", "topic": "대립하는 관점과 주장의 조화로운 통합 전략", "output_format": "조정 프레임워크"},
    "5": {"name": "맥락적 통합", "topic": "다양한 맥락과 문화적 관점의 통합적 이해 방법", "output_format": "맥락 분석 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 관점 통합의 필요성과 어려움 설명",
        "구체적 요청: 체계적 통합 프레임워크와 단계 요청",
        "실용적 구성: 실제 적용 가능한 예시와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "다양한 관점의 통합은 복잡한 문제의 심층적 이해와 혁신적 해결책 개발에 핵심입니다",
    "효과적인 관점 통합은 각 관점의 강점과 한계를 균형 있게 고려해야 합니다",
    "상충되는 관점을 통합할 때는 모순을 인정하고 이를 새로운 통찰의 기회로 활용할 수 있습니다",
    "통합 과정에서 개방적 사고와 학제간 소통 능력이 중요한 역할을 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학제간 연구 전문가", 
        "다양한 학문 분야와 관점을 효과적으로 통합하여 복잡한 문제를 해결하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"연구나 과제에서 서로 다른 관점과 접근법을 어떻게 효과적으로 통합해야 할지 어려움을 겪고 있습니다. "
        f"서로 다른 이론, 학문 분야, 방법론, 관점 등을 조화롭게 통합하여 더 포괄적인 이해를 구축하는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "학제간 접근법" in topic:
        builder.add_instructions([
            "학제간 연구(interdisciplinary research)의 개념과 중요성을 설명해주세요",
            "다양한 학문 분야(자연과학, 사회과학, 인문학 등)의 관점을 통합하는 주요 접근법과 프레임워크를 소개해주세요",
            "학제간 통합의 단계별 프로세스와 각 단계에서의 주요 활동을 구체적으로 설명해주세요",
            "학제간 통합 과정에서 발생하는 인식론적, 방법론적, 소통적 장벽과 이를 극복하는 전략을 제시해주세요",
            "학제간 접근법을 활용한 실제 연구 사례와 성공적인 통합을 위한 핵심 원칙도 포함해주세요"
        ])
    elif "이론과 모델" in topic:
        builder.add_instructions([
            "상충되는 이론과 모델을 통합하는 다양한 접근법과 그 개념적 기반을 설명해주세요",
            "이론 통합의 주요 유형(종합, 병합, 변형 등)과 각각의 적용 조건을 소개해주세요",
            "상충되는 이론을 효과적으로 통합하기 위한 단계별 프로세스와 기법을 제시해주세요",
            "이론 통합 과정에서 발생하는 개념적, 논리적 도전과 이를 해결하는 전략을 알려주세요",
            "다양한 학문 분야에서의 이론 통합 사례와 통합 프레임워크 개발을 위한 템플릿도 포함해주세요"
        ])
    elif "혼합 연구" in topic:
        builder.add_instructions([
            "양적/질적 연구 방법론의 특성과 이를 결합한 혼합 연구 방법(mixed methods)의 개념을 설명해주세요",
            "혼합 연구의 주요 설계 유형(수렴적, 설명적, 탐색적 등)과 각각의 특징 및 적용 상황을 소개해주세요",
            "양적/질적 데이터 수집 및 분석을 통합하는 구체적인 전략과 단계를 제시해주세요",
            "혼합 연구 과정에서 발생하는 방법론적 도전과 이를 극복하는 방안을 알려주세요",
            "다양한 연구 주제에 적용할 수 있는 혼합 연구 설계 템플릿과 실제 적용 사례도 포함해주세요"
        ])
    elif "대립 관점" in topic:
        builder.add_instructions([
            "대립하는 관점과 주장을 통합하는 것의 가치와 다양한 접근법을 설명해주세요",
            "대립 관점의 유형(이념적, 방법론적, 해석적 등)과 각 유형에 적합한 통합 전략을 소개해주세요",
            "대립 관점을 조화롭게 통합하기 위한 단계별 프로세스와 중재 기법을 제시해주세요",
            "관점 통합에서 발생하는 인지적, 정서적, 사회적 장벽과 이를 극복하는 방법을 알려주세요",
            "학술적 논쟁, 정책 논의, 팀 의사결정 등 다양한 맥락에서의 대립 관점 통합 사례와 템플릿도 포함해주세요"
        ])
    elif "맥락적 통합" in topic:
        builder.add_instructions([
            "다양한 맥락과 문화적 관점을 통합하는 것의 중요성과 접근법을 설명해주세요",
            "맥락적, 문화적 차이의 유형과 이러한 차이가 이해와 해석에 미치는 영향을 소개해주세요",
            "다양한 맥락적 관점을 통합적으로 이해하기 위한 프레임워크와 단계를 제시해주세요",
            "맥락적 통합에서 발생하는 편향, 오해, 권력 불균형 문제와 이를 해결하는 전략을 알려주세요",
            "글로벌 연구, 다문화 팀, 비교 연구 등에서의 맥락적 통합 사례와 분석 도구도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 개념과 중요성에 대해 설명해주세요",
            "다양한 관점을 효과적으로 통합하기 위한 주요 접근법과 프레임워크를 소개해주세요",
            "관점 통합을 위한 단계별 프로세스와 각 단계에서의 핵심 활동을 설명해주세요",
            "통합 과정에서 발생할 수 있는 주요 도전과 이를 극복하는 전략을 알려주세요",
            "다양한 학문 분야와 상황에 적용할 수 있는 구체적인 통합 기법과 사례를 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"이론적 배경과 함께 실용적이고 단계별로 적용할 수 있는 통합 방법과 프레임워크를 제공해주세요. "
        f"가능한 경우 다이어그램, 표, 프로세스 맵 등을 활용하여 통합 과정을 시각화해주세요. "
        f"대학생이 실제 연구나 과제에 즉시 적용할 수 있는 구체적인 예시, 템플릿, 체크리스트 등을 포함해주세요. "
        f"다양한 학문 분야와 상황에 적용할 수 있도록 범용적이면서도 구체적인 내용으로 구성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="다양한 관점 통합하기",
        topic_options=PERSPECTIVE_TOPICS,
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
