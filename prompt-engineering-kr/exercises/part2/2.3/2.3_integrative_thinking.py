"""
통합적 관점 구축하기 실습 모듈

Part 2 - 섹션 2.3 실습 코드: 다양한 정보와 관점을 종합하여 포괄적인 이해를 형성하는 방법을 학습합니다.
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
INTEGRATION_TOPICS = {
    "1": {"name": "다관점 접근", "topic": "다양한 학문적 관점 통합을 위한 방법론", "output_format": "통합 프레임워크"},
    "2": {"name": "데이터 통합", "topic": "다양한 유형과 출처의 데이터 통합 기법", "output_format": "통합 가이드"},
    "3": {"name": "이론 통합", "topic": "서로 다른 이론과 개념적 프레임워크의 통합 방법", "output_format": "이론 통합 모델"},
    "4": {"name": "결과 종합", "topic": "다양한 연구 결과와 발견의 체계적 종합 방법", "output_format": "종합 방법론"},
    "5": {"name": "통합적 결론", "topic": "다양한 증거와 관점에 기반한 통합적 결론 도출 방법", "output_format": "의사결정 프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 정보 통합의 필요성과 복잡성 설명",
        "구체적 요청: 체계적 통합 방법과 접근법 요청",
        "실용적 형식: 적용 가능한 프레임워크와 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "다양한 관점과 정보의 통합은 복잡한 문제에 대한 보다 완전한 이해를 가능하게 합니다",
    "효과적인 통합은 단순한 정보 수집 이상의 체계적인 분석과 종합을 필요로 합니다",
    "통합 과정에서 대립되는 관점이나 모순되는 정보를 균형 있게 다루는 것이 중요합니다",
    "통합적 관점은 더 강력한 결론과 보다 신뢰할 수 있는 의사결정의 기반이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "연구 통합 전문가", 
        "다양한 정보, 관점, 방법론, 결과를 효과적으로 통합하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"연구나 과제를 진행하면서 다양한 출처와 관점에서 수집한 정보를 효과적으로 통합하는 데 어려움을 겪고 있습니다. "
        f"단순히 정보를 나열하는 것이 아니라, 의미 있는 통합적 관점을 구축하는 체계적인 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "다양한 학문적 관점" in topic:
        builder.add_instructions([
            "다양한 학문적 관점을 통합하는 것의 중요성과 이점을 설명해주세요",
            "학제간 연구(interdisciplinary research)의 주요 접근법과 방법론을 소개해주세요",
            "서로 다른 학문 분야(예: 자연과학, 사회과학, 인문학)의 관점을 통합하는 구체적인 프레임워크와 단계를 제시해주세요",
            "다학문적 관점 통합 시 발생할 수 있는 어려움과 이를 극복하는 전략을 알려주세요",
            "학문적 관점 통합을 효과적으로 수행한 실제 사례와 적용 예시도 포함해주세요"
        ])
    elif "데이터 통합" in topic:
        builder.add_instructions([
            "다양한 유형(양적/질적)과 출처의 데이터를 통합하는 방법론적 접근법을 설명해주세요",
            "혼합 연구 방법(mixed methods)의 주요 설계와 통합 지점을 소개해주세요",
            "데이터 통합의 주요 단계와 각 단계에서 고려해야 할 사항을 체계적으로 설명해주세요",
            "데이터 통합 시 발생할 수 있는 호환성, 품질, 편향 등의 문제와 해결 방안을 제시해주세요",
            "다양한 학문 분야와 연구 상황에 적용할 수 있는 데이터 통합 기법과 도구도 추천해주세요"
        ])
    elif "이론 통합" in topic:
        builder.add_instructions([
            "서로 다른 이론과 개념적 프레임워크를 통합하는 접근법과 방법론을 설명해주세요",
            "이론 통합의 다양한 유형(종합, 병합, 변환 등)과 각각의 적용 상황을 소개해주세요",
            "상충되거나 경쟁하는 이론을 조화롭게 통합하는 구체적인 전략과 단계를 제시해주세요",
            "이론 통합 과정에서 발생하는 철학적, 방법론적 도전과 이를 해결하는 방안을 알려주세요",
            "효과적인 이론 통합의 사례와 통합 모델 개발을 위한 템플릿도 포함해주세요"
        ])
    elif "결과 종합" in topic:
        builder.add_instructions([
            "다양한 연구 결과와 발견을 체계적으로 종합하는 방법론과 접근법을 설명해주세요",
            "메타 분석, 체계적 문헌 고찰, 내러티브 종합 등 주요 종합 방법론의 특징과 적용 조건을 소개해주세요",
            "일관된 결과와 상충되는 결과를 모두 고려한 균형 있는 종합 방법을 제시해주세요",
            "연구 결과 종합 시 주의해야 할 편향과 오류, 그리고 이를 최소화하는 전략을 알려주세요",
            "다양한 학문 분야에 적용할 수 있는 결과 종합 프로세스와 보고 템플릿도 제공해주세요"
        ])
    elif "통합적 결론" in topic:
        builder.add_instructions([
            "다양한 증거와 관점에 기반한 통합적 결론을 도출하는 방법론과 원칙을 설명해주세요",
            "증거의 강도, 일관성, 적용 가능성 등을 평가하여 결론에 반영하는 방법을 소개해주세요",
            "불확실성과 제한점을 인정하면서도 강력한 통합적 결론을 개발하는 구체적인 단계를 제시해주세요",
            "통합적 결론 도출 시 발생할 수 있는 인지적 편향과 이를 극복하는 전략을 알려주세요",
            "학술 연구, 정책 개발, 실무 적용 등 다양한 맥락에서의 통합적 결론 도출 사례와 템플릿도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 개념과 중요성에 대해 설명해주세요",
            "이 영역에서 통합적 접근의 주요 방법론과 프레임워크를 소개해주세요",
            "효과적인 통합을 위한 단계별 프로세스와 각 단계에서의 핵심 고려사항을 설명해주세요",
            "통합 과정에서 발생할 수 있는 주요 도전과 한계, 그리고 이를 극복하는 전략을 알려주세요",
            "다양한 학문 분야와 상황에 적용할 수 있는 구체적인 통합 기법과 도구를 추천해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"이론적 배경과 함께 실용적이고 단계별로 적용할 수 있는 통합 방법과 프레임워크를 제공해주세요. "
        f"가능한 경우 다이어그램, 표, 프로세스 맵 등을 활용하여 통합 과정을 시각화해주세요. "
        f"다양한 학문 분야와 상황에 적용할 수 있는 예시와 템플릿을 포함하고, 대학생이 실제 과제와 연구에 즉시 활용할 수 있는 실용적인 가이드가 되도록 구성해주세요. "
        f"통합 과정에서 주의해야 할 사항과 성공적인 통합을 위한 팁도 함께 제공해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="통합적 관점 구축하기",
        topic_options=INTEGRATION_TOPICS,
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
