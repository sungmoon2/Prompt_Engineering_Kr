"""
일상 언어에서 학술 언어로 전환하기 실습 모듈

Part 4 - 섹션 4.3.1 실습 코드: 일상적인 언어 표현을 학술적 표현으로 전환하는 방법을 학습합니다.
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
ACADEMIC_LANGUAGE_TOPICS = {
    "1": {"name": "어휘 업그레이드", "topic": "일상 어휘에서 학술 어휘로 전환", "output_format": "변환 가이드"},
    "2": {"name": "객관화 전략", "topic": "주관적 표현을 객관적 표현으로 변환", "output_format": "전환 전략"},
    "3": {"name": "복합 문장 구성", "topic": "단순 문장을 학술적 복합 문장으로 변환", "output_format": "문장 구성 가이드"},
    "4": {"name": "분야별 학술 표현", "topic": "학문 분야별 특수 표현과 용어", "output_format": "분야별 가이드"},
    "5": {"name": "헤지 표현 활용", "topic": "학술적 헤지 표현과 부스터 표현", "output_format": "표현 사전"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "전문가 역할 설정: 학술 글쓰기 전문가 역할 부여",
        "변환 대상 명시: 특정 유형의 일상 표현에서 학술 표현으로 변환 요청",
        "예시 요청: 다양한 학문 분야의 구체적인 변환 예시 요청",
        "적용 전략 요청: 단계별 전환 과정과 적용 가능한 전략 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "일상 언어와 학술 언어의 핵심 차이점을 이해하고 구분할 수 있습니다",
    "일상적 어휘를 적절한 학술적 어휘로 전환하는 방법을 습득할 수 있습니다",
    "주관적 표현을 객관적이고 정밀한 학술 표현으로 변환할 수 있습니다",
    "단순한 문장 구조를 논리적이고 복합적인 학술 문장으로 발전시킬 수 있습니다",
    "자신의 학문 분야에 적합한 특수 표현과 용어를 활용할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "학술 글쓰기 전문가", 
        "다양한 학문 분야의 학술 글쓰기를 가르치는 교수로, 일상 언어를 학술적 표현으로 전환하는 방법론에 정통한 전문가"
    )
    
    # 주제별 맥락 및 지시사항 설정
    if "어휘 업그레이드" in topic:
        builder.add_context(
            f"저는 학부생으로 {topic}에 어려움을 겪고 있습니다. "
            f"일상적인 단어와 표현을 학술적으로 더 적합한 어휘로 전환하는 체계적인 방법이 필요합니다. "
            f"특히 동사, 형용사, 부사 등 품사별로 일상 어휘를 학술 어휘로 업그레이드하는 구체적인 가이드가 필요합니다."
        )
        
        builder.add_instructions([
            "일상 어휘와 학술 어휘의 차이점과 특성을 설명해주세요",
            "품사별(동사, 명사, 형용사, 부사)로 일상 어휘→학술 어휘 변환 예시를 최소 10개씩 표로 제공해주세요",
            "학문 분야별(인문학, 사회과학, 자연과학, 공학) 특화된 어휘 전환 예시도 포함해주세요",
            "일상 어휘를 학술 어휘로 업그레이드하는 단계별 접근법과 검증 방법을 설명해주세요",
            "어휘 업그레이드 시 흔히 범하는 실수와 이를 피하는 방법도 제안해주세요"
        ])
        
    elif "객관화 전략" in topic:
        builder.add_context(
            f"저는 대학원생으로 {topic}에 관심이 있습니다. "
            f"글쓰기 시 주관적이고 개인적인 표현이 자주 사용된다는 피드백을 받았습니다. "
            f"1인칭 표현, 감정적 언어, 주관적 판단 등을 객관적이고 학술적인 표현으로 전환하는 구체적인 전략이 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 객관성의 중요성과 특징을 설명해주세요",
            "주관적 표현→객관적 표현 전환의 주요 원칙과 전략을 제시해주세요",
            "1인칭 진술을 3인칭/수동태로 변환하는 구체적인 방법과 예시를 제공해주세요",
            "감정적/가치 판단적 표현을 증거 기반 표현으로 전환하는 방법을 예시와 함께 설명해주세요",
            "분야별로 객관성이 다르게 적용되는 방식(인문학 vs. 자연과학 등)도 비교해주세요"
        ])
        
    elif "복합 문장 구성" in topic:
        builder.add_context(
            f"저는 논문 작성 중인 연구자로 {topic}에 도움이 필요합니다. "
            f"문장이 단순하고 연결성이 부족하다는 피드백을 받았습니다. "
            f"단순한 문장을 논리적 관계가 명확한 복합 문장으로 발전시키는 구체적인 방법과 예시가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 복합 문장의 역할과 중요성을 설명해주세요",
            "단순 문장→복합 문장 전환의 기본 원리와 다양한 접근법을 제시해주세요",
            "인과관계, 양보, 조건, 비교 등 다양한 논리적 관계를 표현하는 연결어와 구문을 제공해주세요",
            "실제 단순 문장 5개 이상을 학술적 복합 문장으로 전환하는 예시를 단계별로 보여주세요",
            "복합 문장 구성 시 명확성을 유지하고 과도한 복잡성을 피하는 전략도 조언해주세요"
        ])
        
    elif "분야별 학술 표현" in topic:
        builder.add_context(
            f"저는 다학제적 연구를 준비 중인 대학원생으로 {topic}에 관심이 있습니다. "
            f"각 학문 분야(인문학, 사회과학, 자연과학, 공학 등)별로 선호되는 "
            f"특수 표현, 용어, 문체의 차이를 이해하고 적절히 활용하는 방법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "주요 학문 분야별(인문학, 사회과학, 자연과학, 공학) 학술적 문체와 표현의 특징을 비교해주세요",
            "각 분야의 대표적인 특수 용어와 표현을 최소 10개씩 예시와 함께 정리해주세요",
            "분야별 선호되는 문장 구조, 시제 사용, 능동태/수동태 선호도의 차이를 설명해주세요",
            "다학제적 연구에서 여러 분야의 문체를 적절히 조화시키는 전략을 제안해주세요",
            "각 분야의 대표적인 학술지 문장을 분석하여 문체적 특성을 보여주는 예시도 포함해주세요"
        ])
        
    else:  # 헤지 표현 활용
        builder.add_context(
            f"저는 영어로 학술 논문을 작성하는 대학원생으로 {topic}에 대해 배우고 싶습니다. "
            f"주장의 강도와 확실성을 적절히 조절하는 헤지 표현(hedging)과 "
            f"부스터 표현(boosting)의 효과적인 활용법과 예시가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 헤지 표현과 부스터 표현의 역할과 중요성을 설명해주세요",
            "다양한 유형의 헤지 표현(가능성 표현, 한정사, 완충어 등)을 범주별로 정리하고 예시를 제공해주세요",
            "효과적인 부스터 표현과 그 적절한 사용 맥락을 예시와 함께 설명해주세요",
            "학문 분야별로 헤지 표현과 부스터 표현의 사용 빈도와 선호도 차이를 비교해주세요",
            "헤지 표현과 부스터 표현의 과다/과소 사용 시 발생하는 문제와 균형 있는 사용 전략을 제안해주세요"
        ])
    
    # 출력 형식 지정
builder.add_format_instructions(
    f"응답은 {output_format} 형식으로 구성해주세요. "
    f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
    f"변환 예시는 표 형태로 '일상 표현' → '학술 표현' 형식으로 정리해주세요. "
    f"학술적 개념은 명확하게 정의하고, 적용 가능한 구체적인 전략을 단계별로 설명해주세요. "
    f"실제 글쓰기에 바로 적용할 수 있는 체크리스트나 가이드라인도 포함해주세요. "
    f"내용은 학부생/대학원생이 쉽게 이해하고 적용할 수 있도록, 전문적이면서도 접근하기 쉽게 작성해주세요."
)
    
return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="일상 언어에서 학술 언어로 전환하기",
        topic_options=ACADEMIC_LANGUAGE_TOPICS,
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
