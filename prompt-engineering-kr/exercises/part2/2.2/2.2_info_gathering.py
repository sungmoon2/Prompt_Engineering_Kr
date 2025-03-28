"""
정보 수집과 검증의 순환 실습 모듈

Part 2 - 섹션 2.2 실습 코드: 단계별 정보 수집 전략과 수집된 정보의 정확성 검증 방법을 학습합니다.
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
INFO_GATHERING_TOPICS = {
    "1": {"name": "문헌 조사", "topic": "체계적인 문헌 조사 및 검증 방법", "output_format": "연구 가이드"},
    "2": {"name": "데이터 수집", "topic": "신뢰할 수 있는 데이터 수집 및 검증 전략", "output_format": "데이터 수집 프레임워크"},
    "3": {"name": "인터뷰/설문", "topic": "효과적인 인터뷰 및 설문 설계와 결과 검증", "output_format": "조사 방법론 가이드"},
    "4": {"name": "웹 리서치", "topic": "온라인 정보 수집 및 신뢰성 평가 방법", "output_format": "리서치 가이드"},
    "5": {"name": "다양한 정보원", "topic": "다양한 정보원을 활용한 종합적 정보 수집 및 검증", "output_format": "정보 수집 매뉴얼"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 정보 수집과 검증의 필요성과 과제 설명",
        "구체적 요청: 단계별 전략과 검증 방법 요청",
        "실용적 구성: 실제 적용 가능한 프로세스와 도구 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 정보 수집은 올바른 방향성과 전략적 접근법이 중요합니다",
    "수집된 정보의 신뢰성과 타당성 검증은 고품질 결과물의 핵심입니다",
    "다양한 정보원과 방법을 활용한 교차 검증은 정보의 객관성을 높여줍니다",
    "정보 수집과 검증은 반복적인 순환 과정으로 지속적인 개선이 필요합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "리서치 방법론 전문가", 
        "체계적인 정보 수집과 검증을 위한 전략과 방법론을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"종종 수집한 정보의 신뢰성이나 완전성에 의문이 들어 어려움을 겪습니다. "
        f"체계적으로 정보를 수집하고, 그 정보의 정확성과 신뢰성을 효과적으로 검증하는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "문헌 조사" in topic:
        builder.add_instructions([
            "체계적인 문헌 조사의 기본 원칙과 단계별 접근법을 설명해주세요",
            "학술 데이터베이스 활용 방법, 키워드 선택 전략, 검색 연산자 활용법 등 효과적인 문헌 검색 방법을 알려주세요",
            "일차 자료와 이차 자료의 구분, 학술적 신뢰성 평가, 인용 지수 활용 등 문헌의 품질과 신뢰성을 평가하는 방법을 설명해주세요",
            "체계적 문헌 검토(Systematic Review) 방법론과 PRISMA 체크리스트 같은 검증된 프레임워크 활용법을 소개해주세요",
            "수집한 문헌 관리, 정리, 종합하는 효과적인 방법과 도구도 추천해주세요"
        ])
    elif "데이터 수집" in topic:
        builder.add_instructions([
            "다양한 데이터 유형(양적/질적, 일차/이차 등)과 각 유형별 수집 전략의 기본 원칙을 설명해주세요",
            "데이터 수집 계획 수립, 샘플링 방법, 도구 선택 등 체계적인 데이터 수집 프로세스를 단계별로 설명해주세요",
            "데이터의 신뢰성, 타당성, 정확성을 평가하는 방법과 일반적인 데이터 오류나 편향을 식별하는 방법을 알려주세요",
            "데이터 품질 관리, 이상치 처리, 결측값 관리 등 데이터 정제 및 검증 과정을 설명해주세요",
            "연구 윤리, 개인정보 보호, 데이터 관리 모범 사례 등 데이터 수집 및 활용 시 고려해야 할 윤리적 측면도 포함해주세요"
        ])
    elif "인터뷰/설문" in topic:
        builder.add_instructions([
            "효과적인 인터뷰와 설문조사 설계의 기본 원칙과 주요 고려사항을 설명해주세요",
            "연구 목적에 맞는 질문 유형, 질문 순서, 척도 선택 등 설문지/인터뷰 가이드 개발 방법을 알려주세요",
            "표본 선정, 응답 편향 최소화, 질문 명확성 확보 등 신뢰할 수 있는 데이터 수집을 위한 전략을 제시해주세요",
            "응답의 일관성, 내적 타당도, 신뢰도 등을 검증하는 방법과 도구를 설명해주세요",
            "인터뷰/설문 결과 분석, 해석, 보고 시 주의해야 할 사항과 모범 사례도 포함해주세요"
        ])
    elif "웹 리서치" in topic:
        builder.add_instructions([
            "효과적인 온라인 정보 검색과 수집을 위한 기본 원칙과 전략을 설명해주세요",
            "검색엔진 고급 활용법, 학술 데이터베이스, 디지털 아카이브 등 다양한 온라인 정보원의 특징과 활용법을 알려주세요",
            "온라인 정보의 신뢰성, 정확성, 최신성, 객관성 등을 평가하는 구체적인 기준과 방법을 제시해주세요",
            "디지털 미디어 리터러시, 정보 편향 인식, 가짜 뉴스 식별 등 온라인 정보의 비판적 평가 방법을 설명해주세요",
            "데이터 스크래핑, 소셜 미디어 분석 등 고급 웹 리서치 기법과 그 윤리적 고려사항도 포함해주세요"
        ])
    elif "다양한 정보원" in topic:
        builder.add_instructions([
            "학술 문헌, 정부 보고서, 미디어 자료, 전문가 인터뷰 등 다양한 정보원의 특징과 활용 가치를 설명해주세요",
            "연구 목적과 맥락에 맞는 정보원 선택 및 우선순위 설정 전략을 제시해주세요",
            "다양한 정보원에서 수집한 정보를 교차 검증하고 통합하는 방법을 알려주세요",
            "정보원별 신뢰성 평가 기준과 잠재적 편향 식별 방법을 설명해주세요",
            "다양한 유형의 정보를 체계적으로 정리, 분류, 종합하는 효과적인 방법과 도구도 추천해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적인 접근법과 기본 원칙을 설명해주세요",
            "정보 수집을 위한 단계별 프로세스와 전략을 알려주세요",
            "수집된 정보의 신뢰성, 정확성, 관련성을 평가하고 검증하는 방법을 설명해주세요",
            "정보 수집 및 검증 과정에서 흔히 발생하는 문제점과 그 해결책을 제시해주세요",
            "정보를 효과적으로 정리, 분석, 종합하는 방법과 도구도 추천해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"정보 수집 및 검증의 주요 단계별로 섹션을 나누고, 각 단계에서의 구체적인 방법과 도구를 설명해주세요. "
        f"실제 사례나 예시를 통해 설명하고, 가능한 경우 표나 다이어그램으로 정보를 시각화해주세요. "
        f"학생들이 바로 활용할 수 있는 체크리스트, 템플릿, 평가 도구 등의 실용적인 자료도 포함해주세요. "
        f"마지막에는 주요 정보원 목록, 추천 도구, 참고할 만한 추가 자료도 제안해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="정보 수집과 검증의 순환",
        topic_options=INFO_GATHERING_TOPICS,
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
