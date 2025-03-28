"""
체계적 분해를 위한 5W1H 프레임워크 실습 모듈

Part 2 - 섹션 2.1.2 실습 코드: 5W1H(누가, 무엇을, 언제, 어디서, 왜, 어떻게) 프레임워크를 활용한 과제 분석 방법을 학습합니다.
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
FRAMEWORK_TOPICS = {
    "1": {"name": "학술 연구", "topic": "5W1H 프레임워크를 활용한 학술 연구 분석", "output_format": "분석 가이드"},
    "2": {"name": "에세이 작성", "topic": "5W1H를 활용한 학술 에세이 구조화 방법", "output_format": "작성 가이드"},
    "3": {"name": "프로젝트 기획", "topic": "5W1H 프레임워크를 활용한 프로젝트 기획 및 분석", "output_format": "기획 템플릿"},
    "4": {"name": "문제 해결", "topic": "5W1H를 활용한 체계적인 문제 해결 접근법", "output_format": "문제 해결 가이드"},
    "5": {"name": "발표 준비", "topic": "5W1H 프레임워크를 활용한 효과적인 발표 구성", "output_format": "발표 계획 템플릿"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 5W1H 프레임워크 활용의 필요성과 목적 설명",
        "구체적 요청: 각 요소별 세부 질문과 분석 방법 요청",
        "실용적 형식: 실제 적용 가능한 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "5W1H 프레임워크는 복잡한 과제나 문제를 포괄적으로 분석하는 강력한 도구입니다",
    "각 요소(Who, What, When, Where, Why, How)는 과제의 다른 측면을 탐색하게 해줍니다",
    "체계적인 질문 접근법은 중요한 측면을 놓치지 않도록 도와줍니다",
    "5W1H는 다양한 학술, 전문적, 개인적 과제에 유연하게 적용할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "분석 방법론 전문가", 
        "다양한 과제와 문제를 체계적으로 분석하는 프레임워크와 방법론을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"과제나 프로젝트를 분석할 때 중요한 측면을 놓치거나 체계적이지 못한 접근으로 어려움을 겪곤 합니다. "
        f"5W1H 프레임워크를 활용하여 과제를 포괄적이고 체계적으로 분석하는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "학술 연구" in topic:
        builder.add_instructions([
            "5W1H 프레임워크가 학술 연구 분석에 어떻게 적용되는지 개념적으로 설명해주세요",
            "학술 연구의 각 단계(주제 선정, 문헌 검토, 방법론 설계, 데이터 수집/분석, 결과 해석 등)에 5W1H 요소를 어떻게 적용할 수 있는지 설명해주세요",
            "연구 질문 형성과 연구 설계에 5W1H를 활용하는 구체적인 방법과 예시를 제공해주세요",
            "학술 연구에서 흔히 간과되는 중요한 5W1H 질문들과 이를 다루는 방법을 설명해주세요",
            "5W1H 기반의 연구 계획 템플릿과 체크리스트를 제공해주세요"
        ])
    elif "에세이 작성" in topic:
        builder.add_instructions([
            "학술 에세이 작성에 5W1H 프레임워크를 적용하는 방법을 개념적으로 설명해주세요",
            "에세이 주제 분석과 논증 구조화에 각 5W1H 요소를 어떻게 활용할 수 있는지 설명해주세요",
            "에세이의 서론, 본론, 결론에 맞춘 5W1H 질문 세트와 그 활용법을 제시해주세요",
            "5W1H를 활용한 에세이 개요 작성 방법과 구체적인 예시를 제공해주세요",
            "에세이 작성 전, 중, 후 단계에서 활용할 수 있는 5W1H 기반 체크리스트를 포함해주세요"
        ])
    elif "프로젝트 기획" in topic:
        builder.add_instructions([
            "프로젝트 기획 및 분석에 5W1H 프레임워크를 적용하는 방법을 개념적으로 설명해주세요",
            "프로젝트의 범위, 목표, 이해관계자, 일정, 자원 등을 정의하는 데 각 5W1H 요소를 어떻게 활용할 수 있는지 설명해주세요",
            "5W1H 기반의 프로젝트 제안서 작성 방법과 템플릿을 제공해주세요",
            "프로젝트 기획 과정에서 발생하는 일반적인 문제와 이를 5W1H로 해결하는 방법을 설명해주세요",
            "팀 프로젝트에서 5W1H를 활용한 역할 분담과 협업 방법도 포함해주세요"
        ])
    elif "문제 해결" in topic:
        builder.add_instructions([
            "문제 해결 과정에 5W1H 프레임워크를 적용하는 방법을 개념적으로 설명해주세요",
            "문제 정의, 원인 분석, 해결책 개발, 평가 등 각 단계에서 5W1H 요소를 어떻게 활용할 수 있는지 설명해주세요",
            "5W1H를 활용한 체계적인 문제 분석 워크시트와 템플릿을 제공해주세요",
            "다양한 유형의 문제(기술적, 학술적, 사회적 문제 등)에 5W1H를 적용한 구체적인 예시를 보여주세요",
            "문제 해결 과정에서 흔히 간과되는 중요한 5W1H 질문들과 이를 다루는 방법을 포함해주세요"
        ])
    elif "발표 준비" in topic:
        builder.add_instructions([
            "효과적인 발표 구성에 5W1H 프레임워크를 적용하는 방법을 개념적으로 설명해주세요",
            "발표의 주제, 대상, 목적, 구성, 전달 방식 등을 결정하는 데 각 5W1H 요소를 어떻게 활용할 수 있는지 설명해주세요",
            "5W1H 기반의 발표 계획 템플릿과 체크리스트를 제공해주세요",
            "다양한 유형의 발표(정보 전달, 설득, 교육 등)에 5W1H를 적용하는 방법을 구체적인 예시와 함께 제시해주세요",
            "발표 준비, 실행, 평가 단계에서 5W1H를 활용한 자가 점검 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 5W1H 프레임워크를 적용하는 방법을 개념적으로 설명해주세요",
            "이 맥락에서 각 5W1H 요소(Who, What, When, Where, Why, How)가 어떤 의미를 갖는지, 그리고 어떤 질문들을 다루는지 설명해주세요",
            "5W1H를 활용한 구체적인 분석 방법과 단계를 제시해주세요",
            "실제 적용 사례와 예시를 통해 5W1H 프레임워크의 효과적인 활용법을 보여주세요",
            "이 맥락에 특화된 5W1H 기반 템플릿이나 워크시트를 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"5W1H의 각 요소별로 섹션을 구분하고, 각 요소에 대한 핵심 질문 세트와 그 목적을 포함해주세요. "
        f"실제 사례나 예시를 통해 각 요소의 적용 방법을 구체적으로 보여주시고, 가능한 경우 표나 다이어그램으로 정보를 시각화해주세요. "
        f"대학생이 실제 과제나 프로젝트에 바로 적용할 수 있는 5W1H 기반 템플릿이나 워크시트를 제공해주세요. "
        f"마지막에는 5W1H 접근법을 활용할 때의 주의사항과 팁도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="체계적 분해를 위한 5W1H 프레임워크",
        topic_options=FRAMEWORK_TOPICS,
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