"""
학술 보고서 향상시키기 실습 모듈

Part 4 - 섹션 4.4 실습 코드: 학술 보고서 향상을 위한 단계별 개선 프로세스와 피드백 활용 전략을 학습합니다.
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
REPORT_IMPROVEMENT_TOPICS = {
    "1": {"name": "보고서 진단", "topic": "학술 보고서 종합적 평가 및 진단", "output_format": "진단 가이드"},
    "2": {"name": "구조적 개선", "topic": "학술 보고서 구조적 요소 향상", "output_format": "개선 전략"},
    "3": {"name": "내용적 개선", "topic": "학술 보고서 내용 품질 향상", "output_format": "개선 프레임워크"},
    "4": {"name": "표현적 개선", "topic": "학술 보고서 표현 및 문체 향상", "output_format": "실용 가이드"},
    "5": {"name": "개선 통합", "topic": "종합적 학술 보고서 개선 프로세스", "output_format": "단계별 워크플로우"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "전문가 역할 설정: 학술 글쓰기 및 편집 전문가 역할 부여",
        "맥락 설정: 실제 학술 보고서 개선 과정의 구체적 상황 제시",
        "구체적 요청: 학술 보고서의 구조, 내용, 표현 측면에서의 개선 전략 요청",
        "사례 기반 접근: Before/After 예시와 실제 적용 가능한 전략 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "학술 보고서의 구조적, 내용적, 표현적 측면에서 체계적인 진단과 평가 방법을 습득할 수 있습니다",
    "학술 보고서의 논리적 흐름과 조직을 개선하기 위한 실용적인 전략을 배울 수 있습니다",
    "학술적 주장, 근거, 분석의 질을 향상시키는 방법을 익힐 수 있습니다",
    "학술적 표현과 문체를 세련되게 다듬는 기법을 습득할 수 있습니다",
    "보고서 개선을 위한 체계적인 워크플로우를 개발하고 적용할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 역할 및 맥락 설정
    if "진단" in topic:
        builder.add_role(
            "학술 보고서 진단 전문가", 
            "저명한 학술지 편집자이자 대학 글쓰기 센터 디렉터로, 수많은 학술 보고서의 강점과 약점을 분석하고 개선 방향을 제시해온 전문가"
        )
        
        builder.add_context(
            f"저는 대학원생으로 학위 논문을 준비 중이며, {topic}에 대한 체계적인 접근법이 필요합니다. "
            f"제 보고서가 학술적 기준을 충족하는지 객관적으로 평가하고, 주요 개선점을 파악하는 "
            f"체계적인 진단 프레임워크와 실용적인 체크리스트가 필요합니다."
        )
        
        builder.add_instructions([
    "학술 보고서의 구조적, 내용적, 표현적 측면에서 종합적인 진단 프레임워크를 제공해주세요",
    "각 영역별 주요 평가 기준과 구체적인 체크포인트를 상세히 설명해주세요",
    "학술 보고서 유형별(연구 논문, 문헌 검토, 사례 연구 등) 특수한 진단 기준도 포함해주세요",
    "자가 진단을 위한 단계별 프로세스와 구체적인 질문 목록을 제안해주세요",
    "진단 결과를 바탕으로 개선 우선순위를 설정하는 방법론도 제시해주세요"
])
        
    elif "구조적 개선" in topic:
        builder.add_role(
            "학술 구조화 전문가", 
            "학술 출판사의 구조 편집자이자 대학 연구 글쓰기 코치로, 복잡한 학술 내용을 명확하고 논리적인 구조로 조직화하는 데 전문성을 가진 전문가"
        )
        
        builder.add_context(
            f"저는 학술 논문을 준비 중인 연구자로, {topic}에 어려움을 겪고 있습니다. "
            f"논문의 전체적인 구조와 논리적 흐름이 명확하지 않다는 피드백을 받았습니다. "
            f"학술 보고서의 구조적 측면(전체 조직, 섹션 간 연결성, 논리적 흐름, 정보의 계층화 등)을 "
            f"효과적으로 개선하기 위한 구체적인 전략과 사례가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 보고서의 효과적인 구조화 원칙과 다양한 구조적 모델을 설명해주세요",
            "구조적 문제를 진단하고 개선하기 위한 구체적인 기법(역구조화, 논증 매핑 등)을 단계별로 안내해주세요",
            "섹션 간 연결성과 논리적 흐름을 강화하는 전략을 구체적인 예시와 함께 제시해주세요",
            "학술 보고서 유형별(실험 연구, 질적 연구, 문헌 검토 등) 최적의 구조적 모델을 비교해주세요",
            "Before/After 예시를 통해 구조적 개선의 실제 효과를 보여주는 사례를 포함해주세요"
        ])
        
    elif "내용적 개선" in topic:
        builder.add_role(
            "학술 내용 개발 전문가", 
            "저명한 학술지의 내용 편집자이자 연구 방법론 교수로, 학술적 주장, 근거, 분석의 질을 향상시키는 전문성을 가진 전문가"
        )
        
        builder.add_context(
            f"저는 박사과정 학생으로 학위 논문의 {topic}에 관심이 있습니다. "
            f"방대한 데이터와 분석 결과를 가지고 있지만, 주장과 근거의 연결, 분석의 깊이, "
            f"학술적 기여도의 명확한 제시 등에서 어려움을 겪고 있습니다. "
            f"학술 보고서의 내용적 측면을 체계적으로 향상시키는 방법론이 필요합니다."
        )
        
        builder.add_instructions([
            "학술 보고서의 내용적 품질을 결정하는 핵심 요소(주장의 명확성, 근거의 질, 분석의 깊이 등)를 설명해주세요",
            "주장-근거 연결을 강화하고 근거의 다양성과 설득력을 높이는 구체적인 전략을 제시해주세요",
            "분석의 깊이와 비판적 사고를 강화하는 체계적인 방법론을 단계별로 안내해주세요",
            "상반된 관점과 반론을 효과적으로 통합하고 대응하는 전략을 예시와 함께 설명해주세요",
            "학문 분야별 내용적 기대와 표준의 차이(예: 자연과학 vs. 인문학)도 고려한 맞춤형 전략을 제안해주세요"
        ])
        
    elif "표현적 개선" in topic:
        builder.add_role(
            "학술 표현 및 문체 전문가", 
            "학술 출판사의 문체 편집자이자 학술 글쓰기 워크숍 진행자로, 명확하고 세련된 학술적 표현과 효과적인 문체 개발에 전문성을 가진 전문가"
        )
        
        builder.add_context(
            f"저는 비영어권 연구자로 영어 학술 논문 작성에 어려움을 겪고 있어 {topic}에 관심이 있습니다. "
            f"내용은 가치 있지만 표현, 문체, 어휘 선택 등이 학술적 기준에 미치지 못한다는 피드백을 받았습니다. "
            f"학술적 명확성을 유지하면서도 세련된 표현과 효과적인 학술 문체를 개발하는 방법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "효과적인 학술 문체의 핵심 특성(명확성, 간결성, 정밀성, 객관성 등)과 일반적인 문체적 문제를 설명해주세요",
            "일상 언어에서 학술적 표현으로 전환하는 구체적인 전략과 다양한 예시를 제공해주세요",
            "문장 구조, 단락 구성, 전환어 활용 등 미시적/거시적 표현 개선 전략을 단계별로 안내해주세요",
            "학술적 헤지 표현(hedging)과 강조 표현(boosting)의 적절한 활용법을 예시와 함께 설명해주세요",
            "비영어권 연구자들이 자주 범하는 표현적 오류와 그 해결책에 특별히 초점을 맞추어 조언해주세요"
        ])
        
    else:  # 개선 통합
        builder.add_role(
            "학술 보고서 개선 전문가", 
            "저명한 대학의 학술 글쓰기 센터 디렉터이자 학술 출판 컨설턴트로, 수많은 학술 보고서의 종합적 개선을 지도해온 전문가"
        )
        
        builder.add_context(
            f"저는 중요한 학술지 투고를 앞둔 연구자로, {topic}에 대한 체계적인 접근법이 필요합니다. "
            f"좋은 연구 결과가 있지만 이를 효과적으로 전달하는 보고서 작성에 어려움을 겪고 있습니다. "
            f"구조적, 내용적, 표현적 측면을 통합적으로 개선하는 체계적인 프로세스와 워크플로우가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 보고서 개선을 위한 종합적인 워크플로우를 단계별로 상세히 설명해주세요",
            "구조, 내용, 표현의 상호 연관성을 고려한 통합적 개선 접근법을 제시해주세요",
            "학술 보고서 개선 과정에서 직면하는 일반적인 도전과 이를 극복하는 전략을 안내해주세요",
            "시간 효율적인 개선을 위한 우선순위 설정 및 자원 할당 방법을 제안해주세요",
            "다양한 유형의 학술 보고서(학위 논문, 학술지 논문, 연구 제안서 등)에 맞춤화할 수 있는 유연한 개선 프레임워크를 개발해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"개념적 설명과 함께 실제 적용 가능한 구체적인 전략과 예시를 균형 있게 포함해주세요. "
        f"가능한 경우 Before/After 예시를 통해 개선 효과를 시각적으로 보여주세요. "
        f"표, 체크리스트, 워크시트 등 실용적인 도구를 포함하여 즉시 활용 가능한 자료를 제공해주세요. "
        f"학문 분야별 특수성을 고려하되, 다양한 분야의 연구자들이 적용할 수 있는 보편적 원칙과 맞춤형 전략을 모두 다루어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="학술 보고서 향상시키기",
        topic_options=REPORT_IMPROVEMENT_TOPICS,
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