"""
논리적 흐름과 일관성 실습 모듈

Part 4 - 섹션 4.2.2 실습 코드: 학술 글쓰기에서 논리적 흐름과 일관성을 강화하는 방법을 학습합니다.
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
LOGICAL_FLOW_TOPICS = {
    "1": {"name": "거시적 흐름 구축", "topic": "학술 글의 거시적 논리 구조와 흐름 설계", "output_format": "구조 가이드"},
    "2": {"name": "단락 구성 최적화", "topic": "효과적인 단락 구성과 일관성 확보 전략", "output_format": "작성 가이드"},
    "3": {"name": "전환구 활용", "topic": "단락 및 섹션 간 효과적인 전환 전략", "output_format": "전략 가이드"},
    "4": {"name": "AI 활용 흐름 강화", "topic": "AI를 활용한 논리적 흐름과 일관성 개선", "output_format": "프롬프트 전략"},
    "5": {"name": "흐름 문제 해결", "topic": "논리적 흐름과 일관성 문제 진단 및 해결", "output_format": "문제해결 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "전문가 역할 설정: 학술 글쓰기 및 논리 구조 전문가 역할 부여",
        "맥락 설정: 논리적 흐름 개선이 필요한 학술 글쓰기 상황 제시",
        "구체적 요청: 논리 구조, 단락 구성, 전환 전략 등에 대한 세부 지침 요청",
        "사례 기반 접근: Before/After 예시와 구체적 적용 사례 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "학술적 글쓰기에서 논리적 흐름과 일관성의 중요성을 이해할 수 있습니다",
    "다양한 논리적 구조 패턴과 적합한 상황을 구분하고 적용할 수 있습니다",
    "MEAL/PEEL 구조를 활용하여 효과적인 단락을 구성하고 일관성을 확보할 수 있습니다",
    "다양한 전환 기법을 활용하여 단락 및 섹션 간 자연스러운 흐름을 만들 수 있습니다",
    "AI를 활용하여 글의 논리적 흐름과 일관성을 분석하고 개선할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 역할 및 맥락 설정
    if "거시적 흐름" in topic:
        builder.add_role(
            "학술 논리 구조 전문가", 
            "저명한 대학의 학술 글쓰기 센터 디렉터로, 수많은 연구자들의 논문과 학술 글의 논리적 구조를 개선한 전문가입니다. 다양한 학문 분야에서 효과적인 논리 구조와 흐름을 설계하는 방법을 가르치고 있습니다."
        )
        
        builder.add_context(
            f"저는 학위 논문을 준비 중인 대학원생으로, {topic}에 어려움을 겪고 있습니다. "
            f"제 논문의 전체적인 논리적 흐름이 약하다는 피드백을 받았고, "
            f"효과적인 거시적 논리 구조를 설계하고 일관된 흐름을 유지하는 방법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "다양한 논리적 구조 패턴(선형적, 비교/대조, 문제/해결, 인과 등)과 각각의 적합한 상황을 설명해주세요",
            "학문 분야별(인문학, 사회과학, 자연과학 등)로 선호되는 논리적 진행 방식의 차이점을 비교해주세요",
            "효과적인 전체 구조 설계를 위한 구체적인 전략과 단계를 제시해주세요",
            "논리적 흐름을 평가하고 개선하기 위한 체크리스트나 진단 도구를 제공해주세요",
            "실제 Before/After 예시를 통해 거시적 논리 구조의 개선 효과를 보여주세요"
        ])
        
    elif "단락 구성" in topic:
        builder.add_role(
            "학술 단락 구성 전문가", 
            "학술 출판 편집자이자 글쓰기 코치로, 효과적인 단락 구성과 논리적 일관성 구축에 전문성을 가진 전문가입니다. 학술 저널에서 수천 편의 논문을 편집하며 단락 수준의 논리와 일관성을 향상시켜 왔습니다."
        )
        
        builder.add_context(
            f"저는 학술 논문 작성에 어려움을 겪는 연구자로, {topic}에 관한 구체적인 지침이 필요합니다. "
            f"제 글에서 단락 내부의 논리와 일관성이 부족하고, 주장-증거-분석의 연결이 약하다는 "
            f"피드백을 받았습니다. 효과적인 단락 구성 방법과 일관성 확보 전략을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "MEAL(Main idea, Evidence, Analysis, Link)과 PEEL(Point, Evidence, Explanation, Link) 구조를 상세히 설명하고 비교해주세요",
            "효과적인 주제문 작성법과 다양한 주제문 유형 및 배치 전략을 예시와 함께 안내해주세요",
            "증거와 분석을 효과적으로 연결하는 구체적인 방법과 예시를 제공해주세요",
            "단락 길이와 구조의 균형을 유지하는 원칙과 전략을 설명해주세요",
            "실제 Before/After 예시를 통해 단락 구성 개선의 효과를 보여주세요"
        ])
        
    elif "전환구 활용" in topic:
        builder.add_role(
            "학술 전환 전략 전문가", 
            "학술 글쓰기 교수이자 저자로, 다양한 전환 기법과 연결 장치를 통해 논리적 흐름을 강화하는 전략에 전문성을 가진 전문가입니다. 여러 학술서와 논문에서 전환 전략의 중요성을 강조해 왔습니다."
        )
        
        builder.add_context(
            f"저는 학위 논문을 작성 중인 학생으로, {topic}에 관심이 있습니다. "
            f"제 글에서 단락과 섹션 간 전환이 갑작스럽고 부자연스럽다는 피드백을 받았습니다. "
            f"자연스러운 논리적 흐름을 위한 다양한 전환 전략과 연결 장치 활용법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "다양한 전환 유형(추가, 대조, 예시, 인과, 시간, 강조, 결론 등)과 각 유형별 적절한 전환어를 체계적으로 정리해주세요",
            "단락 내, 단락 간, 섹션 간 전환을 위한 다양한 전략과 기법을 구체적인 예시와 함께 설명해주세요",
            "효과적인 전환을 위한 키워드 반복, 개념 연결, 질문 활용 등 다양한 기법을 적용한 예시를 제공해주세요",
            "전환 배치 전략(단락 끝, 단락 시작, 전환 단락 등)의 장단점과 적합한 상황을 비교해주세요",
            "실제 Before/After 예시를 통해 전환구 개선의 효과를 보여주세요"
        ])
        
    elif "AI 활용" in topic:
        builder.add_role(
            "AI 활용 학술 글쓰기 전문가", 
            "AI와 학술 글쓰기의 통합에 전문성을 가진 연구자이자 컨설턴트로, AI를 활용하여 논리적 흐름과 일관성을 분석하고 개선하는 혁신적인 방법론을 개발해 왔습니다."
        )
        
        builder.add_context(
            f"저는 AI를 학술 글쓰기 과정에 통합하고자 하는 연구자로, {topic}에 관심이 있습니다. "
            f"특히 AI를 활용하여 글의 논리적 구조를 분석하고, 단락 간 연결성을 개선하며, "
            f"일관성을 강화하는 효과적인 프롬프트 전략과 워크플로우를 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "AI를 활용하여 학술 글의 구조를 분석하고 개선하기 위한 효과적인 프롬프트 전략과 예시를 제공해주세요",
            "단락 수준의 일관성을 평가하고 개선하기 위한 AI 활용 방법과 구체적인 프롬프트를 설명해주세요",
            "전환구 강화와 연결성 향상을 위한 AI 활용 전략과 실용적인 프롬프트 예시를 제공해주세요",
            "AI 생성 콘텐츠를 자신의 학술적 목소리와 효과적으로 통합하는 방법을 안내해주세요",
            "AI 피드백을 바탕으로 논리적 흐름을 개선한 실제 Before/After 사례를 보여주세요"
        ])
        
    else:  # 흐름 문제 해결
        builder.add_role(
            "학술 흐름 문제해결 전문가", 
            "학술 글쓰기 컨설턴트이자 편집자로, 논리적 흐름과 일관성 문제를 진단하고 해결하는 체계적인 접근법에 전문성을 가진 전문가입니다. 수백 명의 학생과 연구자들이 논리적 흐름 문제를 극복하도록 도왔습니다."
        )
        
        builder.add_context(
            f"저는 논문 심사에서 '논리적 흐름이 부족하다'는 피드백을 받은 연구자로, {topic}에 대한 도움이 필요합니다. "
            f"논리적 비약, 주제 이탈, 모순적 주장, 구조적 불균형 등 다양한 흐름 문제를 "
            f"효과적으로 진단하고 해결하는 체계적인 접근법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "논리적 흐름과 일관성의 일반적인 문제 유형(논리적 비약, 주제 이탈, 모순적 주장, 구조적 불균형 등)을 구체적인 예시와 함께 설명해주세요",
            "각 문제 유형을 진단하기 위한 체계적인 방법과 체크리스트를 제공해주세요",
            "문제 유형별 구체적인 해결 전략과 단계별 접근법을 설명해주세요",
            "역구조화(reverse outlining), 단락 수준 검토, 목소리 내어 읽기 등 실용적인 수정 및 개선 전략을 안내해주세요",
            "실제 Before/After 사례를 통해 논리적 흐름 문제 해결의 효과를 보여주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"이론적 설명과 실용적인 적용 전략을 균형 있게 포함해주세요. "
        f"학문 분야별 특성과 다양한 상황에 맞는 맞춤형 접근법을 제시해주세요. "
        f"표, 예시, 체크리스트 등 실용적인 도구를 포함하여 즉시 활용 가능한 자료를 제공해주세요. "
        f"Before/After 예시를 통해 개선 효과를 구체적으로 보여주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="논리적 흐름과 일관성",
        topic_options=LOGICAL_FLOW_TOPICS,
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