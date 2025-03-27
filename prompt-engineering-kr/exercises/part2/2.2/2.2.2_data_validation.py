"""
정보의 신뢰성과 타당성 평가 실습 모듈

Part 2 - 섹션 2.2.2 실습 코드: 수집된 정보의 품질과 신뢰성을 체계적으로 평가하는 방법을 학습합니다.
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
INFO_EVALUATION_TOPICS = {
    "1": {"name": "학술 자료", "topic": "학술 논문 및 연구의 신뢰성 평가 방법", "output_format": "평가 가이드"},
    "2": {"name": "온라인 정보", "topic": "웹 정보 및 디지털 콘텐츠의 신뢰성 평가 기준", "output_format": "평가 체크리스트"},
    "3": {"name": "데이터셋", "topic": "데이터셋의 품질 및 타당성 평가 프레임워크", "output_format": "평가 프레임워크"},
    "4": {"name": "미디어 보도", "topic": "뉴스 및 미디어 보도의 비판적 평가 방법", "output_format": "미디어 리터러시 가이드"},
    "5": {"name": "전문가 의견", "topic": "전문가 의견 및 증언의 신뢰성 평가 접근법", "output_format": "평가 매트릭스"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 정보 평가의 필요성과 어려움 설명",
        "구체적 요청: 체계적 평가 방법과 기준 요청",
        "실용적 형식: 즉시 활용 가능한 도구와 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "모든 정보에는 편향, 오류, 한계가 있을 수 있으므로 체계적인 평가가 필수적입니다",
    "정보 유형에 따라 다른 평가 기준과 방법이 필요합니다",
    "신뢰성과 타당성 평가는 비판적 사고 능력과 도메인 지식을 결합해야 합니다",
    "체계적인 평가 프레임워크와 도구는 일관된 정보 평가를 가능하게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "정보 평가 전문가", 
        "정보의 신뢰성, 타당성, 품질을 체계적으로 평가하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"정보와 자료가 넘쳐나는 현대 사회에서 수집한 정보의 품질과 신뢰성을 평가하는 데 어려움을 겪고 있습니다. "
        f"체계적이고 객관적으로 정보를 평가할 수 있는 방법과 기준을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "학술 논문" in topic:
        builder.add_instructions([
            "학술 논문 및 연구의 신뢰성과 타당성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "연구 설계, 방법론, 샘플링, 데이터 분석 등 학술 연구의 주요 구성 요소를 평가하는 방법을 자세히 알려주세요",
            "동료 심사, 학술지 품질, 인용 지수, 연구자 신뢰도 등 외부 품질 지표를 활용하는 방법을 설명해주세요",
            "선택 편향, 출판 편향, 이해 충돌 등 학술 연구에서 흔히 발생하는 문제점을 식별하는 방법을 알려주세요",
            "학술 논문 평가를 위한 체계적인 체크리스트나 프레임워크를 예시와 함께 제공해주세요"
        ])
    elif "웹 정보" in topic:
        builder.add_instructions([
            "웹사이트, 블로그, 소셜 미디어 등 온라인 정보의 신뢰성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "웹 정보의 저자/출처, 목적, 최신성, 정확성, 객관성 등을 평가하는 구체적인 방법을 알려주세요",
            "CRAAP 테스트, 웹사이트 평가 루브릭 등 디지털 정보 평가를 위한 검증된 프레임워크를 소개해주세요",
            "가짜 뉴스, 잘못된 정보, 허위 정보 등을 식별하는 방법과 팩트 체킹 기술을 설명해주세요",
            "디지털 정보 평가를 위한 유용한 도구, 플러그인, 웹사이트 등도 추천해주세요"
        ])
    elif "데이터셋" in topic:
        builder.add_instructions([
            "데이터셋의 품질, 신뢰성, 타당성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "데이터 출처, 수집 방법, 대표성, 완전성, 정확성, 일관성 등 데이터셋의 주요 품질 차원을 평가하는 방법을 알려주세요",
            "데이터 편향, 이상치, 결측값, 중복 등 데이터셋의 일반적인 문제점을 식별하고 처리하는 방법을 설명해주세요",
            "탐색적 데이터 분석(EDA), 데이터 프로파일링, 데이터 시각화 등을 통한 데이터 품질 평가 방법을 소개해주세요",
            "데이터셋 평가를 위한 체계적인 프레임워크와 도구도 예시와 함께 제공해주세요"
        ])
    elif "뉴스" in topic or "미디어 보도" in topic:
        builder.add_instructions([
            "뉴스 및 미디어 보도의 신뢰성과 정확성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "미디어 출처, 저자/기자, 목적, 관점, 증거 사용 등을 평가하는 구체적인 방법을 알려주세요",
            "미디어 편향, 선정주의, 프레이밍 효과, 오정보/허위정보 등을 식별하는 방법을 설명해주세요",
            "다양한 관점에서 뉴스를 비교하고, 사실과 의견을 구분하며, 증거의 품질을 평가하는 기법을 소개해주세요",
            "미디어 리터러시 향상을 위한 실용적인 체크리스트와 평가 도구도 제공해주세요"
        ])
    elif "전문가 의견" in topic:
        builder.add_instructions([
            "전문가 의견, 증언, 주장 등의 신뢰성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "전문가의 자격, 전문성, 경험, 평판, 잠재적 이해충돌 등을 평가하는 방법을 알려주세요",
            "주장의 증거 기반, 논리적 일관성, 합리성 등을 평가하는 구체적인 접근법을 제시해주세요",
            "전문가 집단 내 합의 수준, 소수 의견, 다양한 관점 등을 고려하는 방법을 설명해주세요",
            "전문가 의견 평가를 위한 체계적인 프레임워크와 매트릭스를 예시와 함께 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 신뢰성과 타당성을 평가하는 핵심 원칙과 기준을 설명해주세요",
            "구체적인 평가 방법, 기준, 지표 등을 단계별로 설명해주세요",
            "이 유형의 정보에서 흔히 발생하는 문제점, 편향, 오류 등을 식별하는 방법을 알려주세요",
            "실제 사례와 예시를 통해 평가 방법의 적용을 보여주세요",
            "체계적인 평가를 위한 프레임워크, 체크리스트, 도구 등도 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"정보 평가의 이론적 배경과 함께 실용적이고 구체적인 평가 방법, 기준, 체크리스트 등을 제공해주세요. "
        f"가능한 경우 표, 다이어그램, 평가 루브릭 등을 활용하여 정보를 시각화해주세요. "
        f"실제 평가 사례나 예시를 포함하여 이해를 돕고, 대학생이 즉시 활용할 수 있는 실용적인 평가 도구를 제공해주세요. "
        f"정보 평가 시 주의해야 할 점과 흔한 실수에 대한 조언도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="정보의 신뢰성과 타당성 평가",
        topic_options=INFO_EVALUATION_TOPICS,
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
