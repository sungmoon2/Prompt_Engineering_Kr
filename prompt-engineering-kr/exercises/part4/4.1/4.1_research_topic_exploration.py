"""
연구 주제 탐색 및 구체화 실습 모듈

Part 4 - 섹션 4.1 실습 코드: 광범위한 연구 분야에서 구체적인 연구 주제를 
도출하고 발전시키는 방법을 학습합니다.
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
RESEARCH_TOPICS = {
    "1": {"name": "주제 탐색", "topic": "광범위한 연구 분야에서 잠재적 연구 주제 발굴하기", "output_format": "주제 맵"},
    "2": {"name": "주제 평가", "topic": "연구 주제의 가치와 실행 가능성 평가하기", "output_format": "평가 매트릭스"},
    "3": {"name": "연구 질문", "topic": "명확하고 연구 가능한 연구 질문 개발하기", "output_format": "질문 프레임워크"},
    "4": {"name": "문헌 검토", "topic": "초기 문헌 검토를 통한 연구 격차 식별하기", "output_format": "문헌 검토 요약"},
    "5": {"name": "연구 설계", "topic": "연구 주제에 적합한 연구 방법론 선택하기", "output_format": "연구 계획서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "역할 설정: 연구 방법론 전문가",
        "맥락 제공: 학생의 관심 분야와 목표 명시",
        "구체적 요청: 체계적인 접근법과 구조화된 결과물 요청",
        "형식 지정: 학술적 맥락에 맞는 산출물 형식 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 연구 주제는 구체적이고, 연구 가능하며, 중요성을 가져야 합니다",
    "넓은 관심 영역에서 점진적으로 구체적인 연구 주제로 좁혀가는 접근이 효과적입니다",
    "잠재적 주제의 체계적 평가는 연구의 실행 가능성과 가치를 높입니다",
    "초기 문헌 검토는 연구 격차를 식별하고 독창적인 기여를 가능하게 합니다",
    "연구 질문은 연구의 방향을 결정하는 핵심 요소로, 명확하고 답변 가능해야 합니다"
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
        "다양한 학문 분야에서 효과적인 연구 주제 개발과 발전을 지원하는 전문가로, 학생들이 의미 있고 실행 가능한 연구를 설계하도록 돕는 풍부한 경험을 갖고 있습니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"현재 학술 에세이/보고서를 위한 연구 주제를 개발하고 있으며, 너무 광범위하지도 "
        f"너무 좁지도 않은 적절한 주제를 찾는 과정에서 도움이 필요합니다. "
        f"제 관심 학문 분야는 [학생의 관심 분야]이며, 약 [페이지 수/단어 수] 분량의 "
        f"에세이/보고서를 작성할 계획입니다."
    )
    
    # 구체적인 지시사항 추가
    if "주제 탐색" in topic:
        builder.add_instructions([
            "광범위한 연구 분야에서 잠재적 연구 주제를 체계적으로 발굴하는 방법을 설명해주세요",
            "브레인스토밍, 마인드 맵, 관심 영역 좁히기 등 효과적인 주제 발굴 기법을 제안해주세요",
            "일반적인 관심 영역에서 구체적인 연구 주제로 좁혀가는 단계별 접근법을 제시해주세요",
            "다양한 학문 분야(인문학, 사회과학, 자연과학 등)에 적용할 수 있는 주제 발굴 전략을 포함해주세요",
            "주제 탐색 과정에서 AI를 효과적으로 활용하는 방법도 설명해주세요"
        ])
    elif "주제 평가" in topic:
        builder.add_instructions([
            "잠재적 연구 주제의 가치와 실행 가능성을 평가하는 체계적인 방법을 설명해주세요",
            "연구 주제 평가를 위한 주요 기준(중요성, 독창성, 실행 가능성 등)과 그 의미를 설명해주세요",
            "각 평가 기준을 적용하여 주제를 분석하는 구체적인 방법과 질문을 제안해주세요",
            "여러 주제 후보를 비교 평가할 수 있는 의사결정 매트릭스나 프레임워크를 제공해주세요",
            "주제 평가 후 개선 및 정제하는 과정에 대한 지침도 포함해주세요"
        ])
    elif "연구 질문" in topic:
        builder.add_instructions([
            "연구 주제에서 명확하고 연구 가능한 연구 질문을 개발하는 방법을 설명해주세요",
            "효과적인 연구 질문의 특성과 구성 요소를 상세히 설명해주세요",
            "다양한 유형의 연구 질문(설명적, 탐색적, 인과적 등)과 그 적용 상황을 비교해주세요",
            "연구 질문을 구체화하고 정제하는 단계별 프로세스를 제안해주세요",
            "학문 분야별 효과적인 연구 질문의 예시와 일반적인 실수나 주의사항도 포함해주세요"
        ])
    elif "문헌 검토" in topic:
        builder.add_instructions([
            "초기 문헌 검토를 통해 연구 격차를 식별하는 체계적인 방법을 설명해주세요",
            "효과적인 문헌 검색 전략과 핵심 자료를 식별하는 방법을 제안해주세요",
            "선행 연구를 분석하고 종합하여 연구 격차를 발견하는 프로세스를 설명해주세요",
            "문헌 검토 결과를 구조화하고 시각화하는 효과적인 방법을 제시해주세요",
            "초기 문헌 검토에서 AI를 활용하여 효율성을 높이는 방법도 포함해주세요"
        ])
    elif "연구 설계" in topic:
        builder.add_instructions([
            "연구 주제와 질문에 적합한 연구 방법론을 선택하는 방법을 설명해주세요",
            "주요 연구 방법론(양적, 질적, 혼합 등)의 특성과 적합한 상황을 비교해주세요",
            "연구 질문 유형에 따른 적절한 방법론 선택 기준을 제시해주세요",
            "초기 연구 계획을 구조화하고 개발하는 단계별 프로세스를 설명해주세요",
            "대학생 수준에서 실행 가능한 소규모 연구 설계에 대한 현실적인 조언도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 학술적인 접근법을 설명해주세요",
            "이론적 배경과 주요 개념을 명확히 설명해주세요",
            "단계별 프로세스와 구체적인 방법론을 제시해주세요",
            "학생이 직접 적용할 수 있는 실용적인 전략과 도구를 포함해주세요",
            "일반적인 실수와 그 해결 방법에 대한 조언도 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"학술적이고 체계적인 접근법을 제시하되, 대학생이 실제로 적용할 수 있는 "
        f"실용적인 방법과 구체적인 예시를 포함해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"필요한 경우 표, 플로우차트, 매트릭스 등의 시각적 요소를 활용해주세요. "
        f"언어는 학술적이되 접근하기 쉽게 유지해주시고, 즉시 적용 가능한 템플릿이나 "
        f"체크리스트가 있다면 함께 제공해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="연구 주제 탐색 및 구체화",
        topic_options=RESEARCH_TOPICS,
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
