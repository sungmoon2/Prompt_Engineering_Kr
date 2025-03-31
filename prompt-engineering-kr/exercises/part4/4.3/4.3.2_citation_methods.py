"""
적절한 인용과 참고문헌 관리 실습 모듈

Part 4 - 섹션 4.3.2 실습 코드: 다양한 인용 스타일과 참고문헌 관리 방법을 학습합니다.
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
CITATION_TOPICS = {
    "1": {"name": "인용 스타일 비교", "topic": "주요 인용 스타일(APA, MLA, Chicago) 비교", "output_format": "스타일 가이드"},
    "2": {"name": "인용 유형 활용", "topic": "다양한 인용 유형과 적절한 사용법", "output_format": "실습 가이드"},
    "3": {"name": "참고문헌 관리", "topic": "효과적인 참고문헌 관리 도구와 방법", "output_format": "도구 가이드"},
    "4": {"name": "인용 통합 전략", "topic": "인용을 학술 글에 효과적으로 통합하는 방법", "output_format": "전략 가이드"},
    "5": {"name": "온라인 자료 인용", "topic": "디지털 자료와 온라인 출처의 인용법", "output_format": "인용 매뉴얼"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "전문가 역할 설정: 인용과 참고문헌 관리 전문가 역할 부여",
        "구체적 요청: 인용 스타일, 유형, 관리 도구에 대한 상세 정보 요청",
        "예시 요청: 다양한 출처 유형별 실제 인용 예시 요청",
        "실용적 지침: 실제 적용 가능한 단계별 가이드 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "다양한 인용 스타일(APA, MLA, Chicago 등)의 특징과 적절한 사용 맥락을 이해할 수 있습니다",
    "직접 인용, 간접 인용, 블록 인용 등 다양한 인용 유형을 적절히 활용할 수 있습니다",
    "참고문헌 관리 도구(Zotero, Mendeley, EndNote 등)의 장단점과 효과적인 활용법을 습득할 수 있습니다",
    "인용을 학술 글에 자연스럽고 효과적으로 통합하는 전략을 개발할 수 있습니다",
    "디지털 시대의 다양한 온라인 자료와 새로운 미디어 형식을 정확히 인용하는 방법을 익힐 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "학술 인용 전문가", 
        "다양한 인용 스타일과 참고문헌 관리 시스템에 정통한 대학 학술 사서로, 여러 학문 분야의 연구자들에게 인용 관련 지도를 제공하는 전문가"
    )
    
    # 주제별 맥락 및 지시사항 설정
    if "인용 스타일 비교" in topic:
        builder.add_context(
            f"저는 여러 학문 분야에 걸친 연구를 수행하는 대학원생으로, {topic}에 대해 배우고 싶습니다. "
            f"주요 인용 스타일(APA, MLA, Chicago 등)의 차이점과 각 스타일이 적합한 학문 분야, "
            f"그리고 동일한 출처를 다양한 스타일로 인용하는 구체적인 예시가 필요합니다."
        )
        
        builder.add_instructions([
            "주요 인용 스타일(APA, MLA, Chicago, Vancouver, IEEE)의 특징과 주로 사용되는 학문 분야를 비교해주세요",
            "각 스타일의 본문 내 인용 방식과 참고문헌 목록 형식의 핵심 차이점을 표로 정리해주세요",
            "다양한 출처 유형(저널 논문, 책, 웹사이트, 학위논문, 회의 자료 등)을 각 스타일로 인용하는 예시를 제공해주세요",
            "하나의 동일한 출처를 모든 주요 스타일로 인용하는 비교 예시를 최소 3개 이상 보여주세요",
            "스타일 선택 기준과 특정 학술지나 학문 분야의 인용 요구사항을 확인하는 방법도 안내해주세요"
        ])
        
    elif "인용 유형 활용" in topic:
        builder.add_context(
            f"저는 학부 논문을 작성 중인 학생으로, {topic}에 대해 더 자세히 배우고 싶습니다. "
            f"직접 인용, 간접 인용(패러프레이징), 요약 인용, 블록 인용 등 다양한 인용 유형의 "
            f"적절한 사용 시점과 방법, 그리고 각 유형별 구체적인 예시가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 사용되는 주요 인용 유형(직접 인용, 간접 인용, 요약 인용, 블록 인용 등)의 정의와 특징을 설명해주세요",
            "각 인용 유형의 적절한 사용 시점과 학술적 맥락을 구체적으로 안내해주세요",
            "모든 인용 유형의 구체적인 예시와 형식을 주요 인용 스타일(APA, MLA)별로 보여주세요",
            "효과적인 패러프레이징(간접 인용) 기법과 표절을 피하는 방법을 단계별로 설명해주세요",
            "인용 유형의 균형 있는 활용 전략과 글의 흐름을 유지하면서 다양한 인용을 통합하는 방법을 제안해주세요"
        ])
        
    elif "참고문헌 관리" in topic:
        builder.add_context(
            f"저는 장기적인 연구 프로젝트를 시작하는 연구자로, {topic}에 대한 실용적인 가이드가 필요합니다. "
            f"다양한 참고문헌 관리 도구(Zotero, Mendeley, EndNote 등)의 비교와 효과적인 활용법, "
            f"그리고 대규모 문헌을 체계적으로 관리하는 전략에 대해 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "주요 참고문헌 관리 도구(Zotero, Mendeley, EndNote, RefWorks, Citavi 등)의 특징, 장단점을 비교해주세요",
            "선택한 도구의 설치부터 기본 사용법까지 단계별 실용 가이드를 제공해주세요",
            "참고문헌 관리 도구와 워드 프로세서의 연동 방법 및 인용 삽입, 참고문헌 목록 자동 생성 방법을 설명해주세요",
            "대규모 문헌을 효과적으로 구성하고 태그, 폴더, 키워드 등으로 관리하는 전략을 제안해주세요",
            "연구 협업 상황에서 참고문헌을 공유하고 관리하는 방법과 데이터베이스 동기화/백업 전략도 포함해주세요"
        ])
        
    elif "인용 통합 전략" in topic:
        builder.add_context(
            f"저는 학술 논문 작성에 어려움을 겪고 있는 대학원생으로, {topic}에 대한 도움이 필요합니다. "
            f"인용을 학술 글에 자연스럽게 통합하는 방법, 다양한 인용 동사의 활용, "
            f"여러 출처를 효과적으로 종합하는 전략 등에 대한 구체적인 지침이 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 인용을 효과적으로 통합하는 주요 원칙과 전략을 설명해주세요",
            "다양한 인용 동사(주장하다, 분석하다, 강조하다 등)와 그 뉘앙스 차이, 적절한 사용 맥락을 설명하고 예시를 제공해주세요",
            "저자 중심 vs. 정보 중심 인용 방식의 차이와 각각의 효과적인 활용 상황을 설명해주세요",
            "여러 출처를 종합하고 대조되는 관점을 효과적으로 제시하는 구체적인 방법과 예시를 제공해주세요",
            "논문의 각 섹션(서론, 문헌 검토, 방법론, 결과, 논의 등)에 적합한 인용 통합 전략을 섹션별로 안내해주세요"
        ])
        
    else:  # 온라인 자료 인용
        builder.add_context(
            f"저는 디지털 미디어를 연구하는 학생으로, {topic}에 대한 최신 지침이 필요합니다. "
            f"웹사이트, 소셜 미디어 포스트, 온라인 비디오, 데이터셋, 소프트웨어 등 "
            f"다양한 디지털 자료의 정확한 인용 방법과 최신 인용 스타일 가이드의 관련 규정을 알고 싶습니다."
        )
        
        builder.add_instructions([
            "다양한 디지털/온라인 자료 유형(웹사이트, 블로그, 소셜 미디어, 온라인 비디오, 팟캐스트, 앱, 데이터셋 등)의 인용 원칙을 설명해주세요",
            "주요 인용 스타일(APA, MLA, Chicago)에 따른 다양한 온라인 자료 인용 형식을 구체적인 예시와 함께 제공해주세요",
            "URL, DOI, 접속일자 등 온라인 자료 인용 시 포함해야 할 필수 요소와 형식을 설명해주세요",
            "온라인 자료의 영구성 문제와 웹 아카이브(예: Internet Archive)를 활용한 인용 방법을 안내해주세요",
            "불안정하거나 자주 변경되는 온라인 출처를 인용할 때의 모범 사례와 주의사항도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"인용 예시와 스타일 비교는 표 형식으로 정리하여 시각적으로 명확하게 보여주세요. "
        f"이론적 설명과 함께 실제 적용 가능한 단계별 지침이나 체크리스트를 포함해주세요. "
        f"학술적 정확성을 유지하면서도 초보자가 이해하기 쉬운 명확한 언어로 작성해주세요. "
        f"실제 예시는 가능한 다양한 학문 분야(인문학, 사회과학, 자연과학 등)를 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="적절한 인용과 참고문헌 관리",
        topic_options=CITATION_TOPICS,
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
