"""
단계별 정보 수집 전략 실습 모듈

Part 2 - 섹션 2.2.1 실습 코드: 정보 요구 파악부터 효율적인 정보 수집까지의 과정을 학습합니다.
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
INFO_COLLECTION_TOPICS = {
    "1": {"name": "정보 요구 정의", "topic": "효과적인 정보 요구 정의 및 범위 설정 방법", "output_format": "가이드"},
    "2": {"name": "정보원 식별", "topic": "연구 목적에 맞는 적절한 정보원 식별 및 선택 전략", "output_format": "리소스 가이드"},
    "3": {"name": "검색 전략", "topic": "효과적인 검색 전략 및 키워드 개발 방법", "output_format": "검색 매뉴얼"},
    "4": {"name": "데이터 추출", "topic": "정보 추출 및 기록을 위한 체계적 접근법", "output_format": "추출 프레임워크"},
    "5": {"name": "정보 관리", "topic": "수집된 정보의 효과적인 조직화 및 관리 방법", "output_format": "정보 관리 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 정보 수집의 필요성과 어려움 설명",
        "구체적 요청: 단계별 접근법과 실용적 전략 요청",
        "구조화된 출력: 실제 적용 가능한 도구와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "명확한 정보 요구 정의는 효율적인 정보 수집의 기반입니다",
    "연구 목적과 맥락에 적합한 정보원 선택이 품질 높은 정보 수집의 핵심입니다",
    "체계적인 검색 전략 개발은 관련성 높은 정보를 효율적으로 찾는 데 도움이 됩니다",
    "일관된 정보 추출과 관리 방법은 수집된 정보의 활용 가치를 높여줍니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "정보 수집 전문가", 
        "학술 및 연구 목적의 체계적인 정보 수집 방법론을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"학술 과제와 연구 프로젝트를 위해 필요한 정보를 효과적으로 수집하는 데 어려움을 겪고 있습니다. "
        f"체계적이고 효율적인 정보 수집 접근법과 실용적인 전략을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "정보 요구 정의" in topic:
        builder.add_instructions([
            "정보 요구 정의의 개념과 중요성을 설명해주세요",
            "연구 질문 또는 과제로부터 명확한 정보 요구를 도출하는 단계별 접근법을 제시해주세요",
            "정보 요구를 명확히 하기 위한 질문 기법, 프레임워크, 도구 등을 소개해주세요",
            "정보 범위 설정, 포함/제외 기준 개발, 우선순위 결정 방법을 설명해주세요",
            "정보 요구 정의 시 흔히 발생하는 오류나 함정과 이를 피하는 방법도 포함해주세요"
        ])
    elif "정보원 식별" in topic:
        builder.add_instructions([
            "다양한 정보원 유형과 각각의 특성, 강점, 한계를 설명해주세요",
            "연구 목적과 정보 요구에 맞는 적절한 정보원을 선택하는 기준과 전략을 제시해주세요",
            "학술 정보원(저널, 데이터베이스, 학술서적 등)의 특징과 활용법을 자세히 설명해주세요",
            "주요 온라인 정보원, 정부/공공 정보원, 일차 자료 정보원 등에 대한 안내와 접근 방법을 알려주세요",
            "정보원 품질 평가, 다양성 확보, 상호보완적 정보원 활용 전략도 포함해주세요"
        ])
    elif "검색 전략" in topic:
        builder.add_instructions([
            "효과적인 검색 전략 개발의 기본 원칙과 단계를 설명해주세요",
            "주제 분석, 키워드 도출, 동의어/관련어 확장, 검색식 구성 등의 방법을 자세히 알려주세요",
            "학술 데이터베이스에서 사용하는 검색 연산자(AND, OR, NOT 등), 고급 필터링, 필드 검색 등의 활용법을 설명해주세요",
            "검색 결과의 관련성과 품질을 높이기 위한 전략과 검색 과정의 문서화 방법을 제시해주세요",
            "다양한 검색 플랫폼(Google Scholar, PubMed, Web of Science 등)별 특화 검색 기법도 소개해주세요"
        ])
    elif "데이터 추출" in topic:
        builder.add_instructions([
            "정보 추출의 기본 원칙과 체계적 접근법을 설명해주세요",
            "다양한 자료 유형(논문, 보고서, 웹페이지 등)별 효과적인 정보 추출 방법을 제시해주세요",
            "표준화된 데이터 추출 양식, 코딩 체계, 주석 방법 등을 소개하고 예시를 보여주세요",
            "핵심 정보 식별, 맥락 유지, 출처 추적 등 정보 추출 시 주의할 점을 설명해주세요",
            "디지털 도구와 소프트웨어를 활용한 효율적인 정보 추출 방법도 포함해주세요"
        ])
    elif "정보 관리" in topic:
        builder.add_instructions([
            "수집된 정보의 효과적인 조직화와 관리의 중요성과 기본 원칙을 설명해주세요",
            "정보 분류 체계, 태그 시스템, 메타데이터 활용 등 정보 구조화 방법을 소개해주세요",
            "참고문헌 관리 도구(Zotero, Mendeley, EndNote 등)의 기능과 효과적인 활용법을 설명해주세요",
            "디지털 노트 시스템, 정보 시각화 도구 등을 활용한 정보 통합 및 연결 방법을 제시해주세요",
            "대규모 정보 세트의 효율적 관리, 백업 전략, 정보 업데이트 관리 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 개념과 중요성을 설명해주세요",
            "이것을 실행하기 위한 단계별 접근법과 주요 고려사항을 제시해주세요",
            "효과적인 실행을 위한 구체적인 도구, 기법, 프레임워크를 소개해주세요",
            "학생들이 흔히 겪는 어려움과 이를 극복하기 위한 실용적인 조언을 제공해주세요",
            "실제 학술 환경에서의 적용 사례와 예시도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"개념 설명과 함께 단계별 프로세스, 실용적인 팁, 구체적인 예시를 포함해주세요. "
        f"가능한 경우 표나 다이어그램을 활용하여 정보를 시각화해주시고, 체크리스트나 템플릿 등 실제 활용할 수 있는 자료도 제공해주세요. "
        f"주요 도구나 리소스에 대한 추천과 간략한 활용법도 포함하면 좋겠습니다. "
        f"학생들이 정보 수집 과정에서 참고할 수 있는 실용적인 자료가 되도록 구성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="단계별 정보 수집 전략",
        topic_options=INFO_COLLECTION_TOPICS,
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
