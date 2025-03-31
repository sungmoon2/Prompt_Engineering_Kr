"""
논리적 구조 개발 실습 모듈

Part 4 - 섹션 4.2 실습 코드: 논리적 구조를 효과적으로 개발하여 
학술 에세이와 보고서의 설득력을 높이는 방법을 실습합니다.
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
STRUCTURE_TOPICS = {
    "1": {"name": "구조 유형", "topic": "다양한 학술 글쓰기 구조 유형과 적용 방법", "output_format": "비교 가이드"},
    "2": {"name": "개요 작성", "topic": "효과적인 에세이/보고서 개요 작성 전략", "output_format": "단계별 가이드"},
    "3": {"name": "논리적 흐름", "topic": "논리적 흐름과 일관성 확보 방법", "output_format": "체크리스트"},
    "4": {"name": "주장-근거", "topic": "설득력 있는 주장-근거-반론 구조 개발", "output_format": "프레임워크"},
    "5": {"name": "구조 평가", "topic": "글의 논리적 구조 평가 및 개선 방법", "output_format": "평가 도구"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "역할 설정: 학술 글쓰기 전문가",
        "맥락 제공: 학생의 글쓰기 목표와 어려움 명시",
        "구체적 요청: 체계적인 접근법과 실용적 도구 요청",
        "형식 지정: 단계별 가이드와 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 학술 글쓰기는 명확한 논리적 구조를 기반으로 합니다",
    "글의 목적과 주제에 따라 다양한 구조적 접근법(논증 중심, 문제-해결, 비교-대조 등)을 선택할 수 있습니다",
    "체계적인 개요 작성은 글의 방향성을 명확히 하고 논리적 흐름을 설계하는 핵심 단계입니다",
    "단락 내부 구조와 단락 간 전환은 글 전체의 일관성과 응집성을 결정합니다",
    "효과적인 주장-근거-반론 구조는 글의 설득력과 학술적 깊이를 크게 향상시킵니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학술 글쓰기 전문가", 
        "효과적인 학술 에세이와 보고서 작성을 위한 논리적 구조 개발을 지도하는 전문가로, 다양한 학문 분야에서 명확하고 설득력 있는 글쓰기를 지원합니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"현재 중요한 학술 에세이/보고서를 작성 중이며, 논리적 구조를 효과적으로 "
        f"개발하는 데 어려움을 겪고 있습니다. 제 글이 명확하고 설득력 있게 "
        f"구성될 수 있도록 체계적인 방법과 실용적인 도구가 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "구조 유형" in topic:
        builder.add_instructions([
            "학술 글쓰기에 활용할 수 있는 다양한 구조 유형(논증 중심, 문제-해결, 비교-대조 등)을 상세히 설명해주세요",
            "각 구조 유형의 특징, 장단점, 적합한 상황을 비교해주세요",
            "다양한 학문 분야(인문학, 사회과학, 자연과학 등)에 적합한 구조 유형을 제안해주세요",
            "특정 주제나 목적에 가장 적합한 구조를 선택하는 기준을 제시해주세요",
            "각 구조 유형의 실제 적용 예시와 템플릿을 제공해주세요"
        ])
    elif "개요 작성" in topic:
        builder.add_instructions([
            "효과적인 에세이/보고서 개요 작성을 위한 단계별 접근법을 상세히 설명해주세요",
            "다양한 개요 형식(알파벳-숫자 계층형, 십진법 계층형, 마인드맵 등)과 각각의 장단점을 비교해주세요",
            "주요 논점, 하위 논점, 증거, 분석의 계층적 구조화 방법을 안내해주세요",
            "개요에서 중요한 균형과 비중을 결정하는 기준을 제시해주세요",
            "개요를 초안으로 효과적으로 전환하는 전략을 설명해주세요"
        ])
    elif "논리적 흐름" in topic:
        builder.add_instructions([
            "학술 글쓰기에서 논리적 흐름과 일관성의 중요성을 설명해주세요",
            "단락 내부와 단락 간의 논리적 연결을 강화하는 구체적인 전략을 제시해주세요",
            "효과적인 전환구와 연결 장치의 다양한 유형과 활용법을 설명해주세요",
            "일관된 용어, 시제, 관점 유지를 위한 실용적인 팁을 제공해주세요",
            "글 전체의 논리적 흐름을 평가하고 개선하는 체크리스트를 개발해주세요"
        ])
    elif "주장-근거" in topic:
        builder.add_instructions([
            "설득력 있는 주장-근거-반론 구조의 핵심 요소와 기능을 상세히 설명해주세요",
            "명확하고 방어 가능한 주장을 개발하고 정교화하는 방법을, 안내해주세요",
            "다양한 유형의 근거(통계, 연구 결과, 사례 연구 등)를 효과적으로 통합하는 전략을 제시해주세요",
            "잠재적 반론을 예상하고 효과적으로 대응하는 기법을 설명해주세요",
            "균형 잡힌 주장-근거-반론 구조를 평가하고 개선하는 프레임워크를 제공해주세요"
        ])
    elif "구조 평가" in topic:
        builder.add_instructions([
            "학술 글의 논리적 구조를 체계적으로 평가하는 방법을 상세히 설명해주세요",
            "구조적 일관성, 논리적 흐름, 균형성 등을 평가하는 구체적인 기준을 제시해주세요",
            "일반적인 구조적 문제(논리적 비약, 불균형, 중복 등)를 식별하고 해결하는 전략을 안내해주세요",
            "역방향 개요 작성과 같은 구조 분석 기법을 설명해주세요",
            "피드백을 바탕으로 구조를 효과적으로 개선하는 단계별 프로세스를 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "이론적 배경과 주요 개념을 명확히 설명해주세요",
            "단계별 프로세스와 구체적인 적용 방법을 제시해주세요",
            "학생이 직접 적용할 수 있는 실용적인 전략과 도구를 포함해주세요",
            "다양한 학문적 맥락에 맞게 조정할 수 있는 유연한 접근법을 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 체크리스트, 템플릿, 평가 도구 등의 실용적인 자료를 포함해주세요. "
        f"다양한 학문 분야에서의 구체적인 예시와 사례를 포함하여 개념을 명확히 해주세요. "
        f"모든 내용은 대학생이 직접 적용할 수 있도록 실용적이고 단계별로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="논리적 구조 개발",
        topic_options=STRUCTURE_TOPICS,
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
