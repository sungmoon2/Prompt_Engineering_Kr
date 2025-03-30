"""
연구 주제 발굴 및 평가 기법 실습 모듈

Part 4 - 섹션 4.1.1 실습 코드: 광범위한 관심 영역에서 연구 가능한 주제를
체계적으로 발굴하고 평가하는 방법을 학습합니다.
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
TOPIC_DISCOVERY_TOPICS = {
    "1": {"name": "브레인스토밍 기법", "topic": "효과적인 연구 주제 브레인스토밍 기법과 전략", "output_format": "창의적 기법 가이드"},
    "2": {"name": "주제 범위 좁히기", "topic": "광범위한 관심 영역을 연구 가능한 주제로 좁히는 방법", "output_format": "단계별 접근법"},
    "3": {"name": "주제 평가 매트릭스", "topic": "연구 주제 후보를 체계적으로 평가하는 프레임워크", "output_format": "평가 도구 세트"},
    "4": {"name": "다학제적 접근", "topic": "학제간 교차점에서 혁신적 연구 주제 발굴하기", "output_format": "발굴 프레임워크"},
    "5": {"name": "주제 정제 전략", "topic": "선택한 연구 주제를 강화하고 개선하는 효과적인 방법", "output_format": "정제 전략 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "역할 설정: 연구 방법론 전문가",
        "맥락 제공: 학생의 학술적 배경과 필요성 명시",
        "구체적 요청: 체계적인 접근법과 실용적 전략 요청",
        "형식 지정: 단계별 가이드와 평가 도구 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "창의적 사고 기법(브레인스토밍, SCAMPER, 마인드 맵핑 등)은 혁신적인 연구 주제 발굴에 효과적입니다",
    "주제 범위 조정은 너무 넓지도 좁지도 않은 적절한 연구 범위를 찾는 과정입니다",
    "체계적인 평가 프레임워크는 연구 주제의 가치와 실행 가능성을 객관적으로 평가하는 데 중요합니다",
    "학제간 교차점은 독창적이고 가치 있는 연구 주제를 발견할 수 있는 풍부한 영역입니다",
    "효과적인 연구 주제는 학문적 가치, 실행 가능성, 개인적 관심의 균형을 이루어야 합니다"
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
        "학술 연구 주제를 체계적으로 발굴하고 평가하는 방법을 지도하는 전문가로, 다양한 학문 분야의 학생들이 효과적인 연구 주제를 개발할 수 있도록 돕습니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"학술 에세이나 연구 프로젝트를 위한 연구 주제를 개발하는 과정에서 "
        f"체계적이고 효과적인 접근법이 필요합니다. "
        f"저의 학술적 배경은 [관련 학문 분야]이며, 약 [페이지 수/단어 수] 분량의 "
        f"과제를 준비하고 있습니다."
    )
    
    # 구체적인 지시사항 추가
    if "브레인스토밍 기법" in topic:
        builder.add_instructions([
            "효과적인 연구 주제 브레인스토밍을 위한 다양한 창의적 사고 기법을 설명해주세요",
            "각 기법(브레인스토밍, SCAMPER, 마인드 맵핑 등)의 단계별 적용 방법을 구체적으로 안내해주세요",
            "다양한 학문 분야(인문학, 사회과학, 과학기술 등)에 맞는 브레인스토밍 전략의 차이점을 설명해주세요",
            "창의적 사고의 장벽을 극복하는 방법과 효과적인 아이디어 생성 팁을 제공해주세요",
            "생성된 아이디어를 구조화하고 정리하는 효과적인 방법도 포함해주세요"
        ])
    elif "주제 범위 좁히기" in topic:
        builder.add_instructions([
            "광범위한 관심 영역에서 연구 가능한 구체적 주제로 범위를 좁히는 체계적인 방법을 설명해주세요",
            "깔때기 접근법, 차원 추가법 등 주요 범위 좁히기 기법의 단계별 적용 방법을 안내해주세요",
            "적절한 주제 범위를 판단하는 기준과 너무 넓거나 좁은 주제의 징후를 설명해주세요",
            "다양한 학문 분야에 따른 주제 범위 좁히기의 특수성과 차이점을 설명해주세요",
            "범위 좁히기 과정에서 주제의 가치와 중요성을 유지하는 전략도 포함해주세요"
        ])
    elif "주제 평가 매트릭스" in topic:
        builder.add_instructions([
            "연구 주제 후보를 체계적으로 평가하기 위한 프레임워크와 도구를 제공해주세요",
            "CARS(기여도, 접근성, 연구 가능성, 범위) 등 주요 평가 기준과 적용 방법을 설명해주세요",
            "비교 평가 매트릭스의 설계 및 활용 방법을 단계별로 안내해주세요",
            "다양한 유형의 연구 프로젝트(소논문, 학기 과제, 졸업 논문 등)에 맞는 평가 기준 조정 방법을 제안해주세요",
            "평가 과정에서 주관적 편향을 줄이고 객관성을 높이는 전략도 포함해주세요"
        ])
    elif "다학제적 접근" in topic:
        builder.add_instructions([
            "학제간 교차점에서 혁신적인 연구 주제를 발굴하는 체계적인 방법을 설명해주세요",
            "서로 다른 학문 분야를 연결하고 통합하는 효과적인 전략과 프레임워크를 제시해주세요",
            "다학제적 연구의 장점과 잠재적 어려움, 그리고 이를 극복하는 방법을 설명해주세요",
            "다양한 학문 분야 조합(예: 인문학+기술, 사회과학+자연과학 등)에서 유망한 연구 영역을 제안해주세요",
            "성공적인 다학제적 연구 주제의 사례와 성공 요인도 포함해주세요"
        ])
    elif "주제 정제 전략" in topic:
        builder.add_instructions([
            "선택한 연구 주제를 강화하고 개선하는 효과적인 방법을 설명해주세요",
            "SWOT 분석 등 주제 정제를 위한 체계적인 도구와 그 적용 방법을 안내해주세요",
            "연구 주제의 독창성, 중요성, 실행 가능성을 높이는 구체적인 전략을 제시해주세요",
            "주제 정제 과정에서 피드백을 수집하고 통합하는 효과적인 방법을 설명해주세요",
            "최종 주제 선언문 작성과 연구 계획으로의 연결 방법도 포함해주세요"
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
        f"실제 사용 가능한 템플릿, 워크시트, 체크리스트 등의 실용적 도구를 포함해주세요. "
        f"필요한 경우 표, 다이어그램 등의 시각적 요소를 활용해주세요. "
        f"각 섹션에서 학문 분야별 특수성과 적용 예시를 포함해주시고, "
        f"모든 내용은 대학생이 직접 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="연구 주제 발굴 및 평가 기법",
        topic_options=TOPIC_DISCOVERY_TOPICS,
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
