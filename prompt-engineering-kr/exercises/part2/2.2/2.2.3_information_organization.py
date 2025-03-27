"""
정보 격차 식별 및 보완 실습 모듈

Part 2 - 섹션 2.2.3 실습 코드: 수집한 정보의 부족한 부분을 파악하고 추가 정보를 수집하는 전략을 학습합니다.
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
INFO_GAP_TOPICS = {
    "1": {"name": "격차 분석", "topic": "정보 격차의 체계적 식별 및 분석 방법", "output_format": "분석 가이드"},
    "2": {"name": "추가 정보 수집", "topic": "식별된 격차를 보완하기 위한 추가 정보 수집 전략", "output_format": "전략 매뉴얼"},
    "3": {"name": "정보 보완 기법", "topic": "불완전한 정보를 효과적으로 보완하는 방법", "output_format": "방법론 가이드"},
    "4": {"name": "판단 기준", "topic": "제한된 정보 상황에서의 의사결정 및 판단 기준", "output_format": "의사결정 프레임워크"},
    "5": {"name": "재검토 전략", "topic": "정보 보완 후 종합적 재검토 및 통합 방법", "output_format": "재검토 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 정보 격차와 보완의 필요성 설명",
        "구체적 요청: 체계적 접근법과 실용적 전략 요청",
        "구조화된 출력: 실제 적용 가능한 도구와 프로세스 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "모든 정보 수집 과정에는 불가피한 격차와 한계가 존재합니다",
    "체계적인 격차 분석은 연구와 결론의 완전성과 신뢰성을 높이는 핵심 단계입니다",
    "다양한 보완 전략을 통해 중요한 정보 격차를 효과적으로 해소할 수 있습니다",
    "정보 수집과 격차 보완은 반복적이고 순환적인 과정으로 접근해야 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "연구 방법론 전문가", 
        "체계적인 정보 수집, 분석 및 격차 해소 전략을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"연구나 과제를 위해 정보를 수집할 때, 종종 부족한 정보나 데이터 격차로 인해 어려움을 겪습니다. "
        f"수집한 정보의 한계와 격차를 체계적으로 식별하고 효과적으로 보완하는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "격차 분석" in topic:
        builder.add_instructions([
            "정보 격차와 한계의 유형 및 잠재적 영향에 대해 설명해주세요",
            "수집된 정보에서 격차를 체계적으로 식별하는 방법과 도구를 제시해주세요",
            "정보 맵핑, 갭 분석 매트릭스 등 격차 시각화 및 분석 기법을 소개해주세요",
            "격차의 중요도와 우선순위를 평가하는 방법을 설명해주세요",
            "학술 연구, 프로젝트 계획, 의사결정 등 다양한 상황에서의 격차 분석 적용 예시를 포함해주세요"
        ])
    elif "추가 정보 수집" in topic:
        builder.add_instructions([
            "격차 유형에 따른 최적의 추가 정보 수집 전략을 설명해주세요",
            "효율적인 추가 정보 수집을 위한 단계별 접근법을 제시해주세요",
            "제한된 시간과 자원 상황에서의 정보 수집 우선순위 설정 방법을 알려주세요",
            "추가 정보 수집을 위한 다양한 방법(추가 문헌 검색, 전문가 consulatio, 일차 데이터 수집 등)과 각각의 장단점을 설명해주세요",
            "추가 수집된 정보의 품질과 적합성을 평가하는 방법도 포함해주세요"
        ])
    elif "정보 보완 기법" in topic:
        builder.add_instructions([
            "완전한 정보를 얻기 어려운 상황에서 활용할 수 있는 정보 보완 기법과 원칙을 설명해주세요",
            "삼각 측량법, 교차 검증, 데이터 통합 등 불완전한 정보를 보완하는 방법론을 소개해주세요",
            "정보 추론, 외삽, 모델링 등을 통한 격차 해소 접근법과 주의사항을 설명해주세요",
            "메타 분석, 체계적 문헌 고찰 등을 활용한 기존 정보의 종합 및 재해석 방법을 알려주세요",
            "각 보완 기법의 적용 사례와 한계점도 함께 제시해주세요"
        ])
    elif "판단 기준" in topic:
        builder.add_instructions([
            "불완전한 정보 상황에서 의사결정이나 결론 도출을 위한 기본 원칙과 접근법을 설명해주세요",
            "정보 불확실성과 리스크를 고려한 판단 프레임워크를 제시해주세요",
            "정보 격차의 유형과 중요도에 따른 의사결정 전략의 조정 방법을 알려주세요",
            "결론의 신뢰도 수준을 명시하고 제한 사항을 투명하게 커뮤니케이션하는 방법을 설명해주세요",
            "불완전한 정보에 기반한 의사결정 사례와 교훈도 포함해주세요"
        ])
    elif "재검토 전략" in topic:
        builder.add_instructions([
            "추가 정보 수집 후 전체 정보 세트를 종합적으로 재검토하는 방법과 원칙을 설명해주세요",
            "새로운 정보와 기존 정보의 통합 및 정합성 확인 방법을 제시해주세요",
            "정보 통합 후 남아 있는 격차나 한계를 식별하고 문서화하는 방법을 알려주세요",
            "통합된 정보 세트의 전반적 품질과 신뢰성을 재평가하는 프로세스를 설명해주세요",
            "효과적인, 재검토 세션 운영 방법이나 체크리스트 등의 실용적 도구도 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 개념과 중요성에 대해 설명해주세요",
            "이를 실행하기 위한 체계적인 접근법과 단계를 제시해주세요",
            "다양한 상황에서 활용할 수 있는 구체적인 전략과 방법을 알려주세요",
            "실제 적용 사례와 예시를 통해 효과적인 적용 방법을 보여주세요",
            "주의해야 할 점과 한계, 그리고 이를 극복하는 방법도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"이론적 설명과 함께 실용적이고 단계별로 적용할 수 있는 방법과 도구를 제공해주세요. "
        f"가능한 경우 표, 다이어그램, 분석 템플릿 등을 포함하여 정보를 시각화해주세요. "
        f"다양한 학문 분야와 과제 유형에 적용할 수 있는 예시를 포함하고, 대학생이 즉시 활용할 수 있는 실용적인 자료가 되도록 구성해주세요. "
        f"특히 실제 상황에서 발생할 수 있는 문제와 그 해결책도 논의해주시면 좋겠습니다."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="정보 격차 식별 및 보완",
        topic_options=INFO_GAP_TOPICS,
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
