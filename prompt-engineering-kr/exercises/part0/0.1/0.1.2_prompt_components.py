"""
프롬프트 엔지니어링의 핵심 개념과 중요성 실습 모듈

Part 0 - 섹션 0.1.2 실습 코드: 프롬프트 엔지니어링의 정의, 기술, 중요성과 실제 적용 방법을 학습합니다.
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
PROMPT_ENGINEERING_TOPICS = {
    "1": {"name": "기본 개념", "topic": "프롬프트 엔지니어링의 정의와 기본 개념", "output_format": "개념 가이드"},
    "2": {"name": "핵심 기술", "topic": "효과적인 프롬프트 작성을 위한 핵심 기술", "output_format": "단계별 가이드"},
    "3": {"name": "중요성", "topic": "AI 활용에서 프롬프트 엔지니어링의 중요성", "output_format": "주요 포인트"},
    "4": {"name": "실제 적용", "topic": "학업과 프로젝트에서 프롬프트 엔지니어링 적용 방법", "output_format": "실전 가이드"},
    "5": {"name": "주요 사례", "topic": "효과적인 프롬프트 엔지니어링의 성공 사례", "output_format": "사례 연구"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학습 목표 제시: 프롬프트 엔지니어링 기술 습득 목적 명시",
        "구체적 요청사항: 개념, 기술, 예시, 단계별 가이드 등 요청",
        "구조화된 출력 형식: 학습과 참조가 용이한 형식 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트 엔지니어링은 AI에게 효과적으로 지시하여 원하는 결과를 얻는 기술입니다",
    "명확한 지시, 맥락 제공, 구체적 요청이 프롬프트 품질을 결정하는 핵심 요소입니다",
    "효과적인 프롬프트는 AI 응답의 정확성, 관련성, 유용성을 크게 향상시킵니다",
    "프롬프트 엔지니어링은 실험과 반복을 통해 지속적으로 개선할 수 있는 기술입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 엔지니어링 전문가", 
        "AI와의 효과적인 커뮤니케이션 기술을 가르치는 교육자"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 대해 배우고 있습니다. "
        f"AI를 활용한 학업과 프로젝트에서 더 효과적으로 결과를 얻기 위해 {purpose}을 이해하고 싶습니다. "
        f"이론적 개념뿐만 아니라 실제 적용 방법과 구체적인 예시를 포함해 설명해주세요."
    )
    
    # 구체적인 지시사항 추가
    if "기본 개념" in topic:
        builder.add_instructions([
            "프롬프트 엔지니어링의 정의와 기본 개념을 명확히 설명해주세요",
            "프롬프트 엔지니어링이 왜 필요한지 구체적인 이유를 설명해주세요",
            "프롬프트 엔지니어링의 핵심 원칙 5가지를 알려주세요",
            "좋은 프롬프트와 나쁜 프롬프트의 차이점을 예시와 함께 설명해주세요",
            "초보자가 프롬프트 엔지니어링을 시작할 때 흔히 범하는 실수 3가지를 알려주세요"
        ])
    elif "핵심 기술" in topic:
        builder.add_instructions([
            "효과적인 프롬프트 작성을 위한 핵심 기술을 체계적으로 설명해주세요",
            "각 기술의 목적과 적용 방법을 구체적인 예시와 함께 설명해주세요",
            "다양한 AI 과제(정보 검색, 창작, 분석 등)에 따른 프롬프트 최적화 방법을 알려주세요",
            "프롬프트 개선을 위한 반복 과정과 피드백 활용법을 설명해주세요",
            "학생들이 학업에 바로 적용할 수 있는 프롬프트 템플릿 3가지를 제공해주세요"
        ])
    elif "중요성" in topic:
        builder.add_instructions([
            "프롬프트 엔지니어링이 AI 활용 결과에 미치는 영향을 구체적으로 설명해주세요",
            "동일한 AI 모델에서 프롬프트에 따라 결과가 어떻게 달라지는지 예시를 들어 설명해주세요",
            "프롬프트 엔지니어링 기술이 학업, 연구, 직무에서 어떤 이점을 제공하는지 설명해주세요",
            "프롬프트 엔지니어링 없이 AI를 사용할 때의 한계와 문제점을 분석해주세요",
            "프롬프트 엔지니어링의 중요성이 앞으로 어떻게 변화할지 전망해주세요"
        ])
    elif "실제 적용" in topic:
        builder.add_instructions([
            "학업과 프로젝트에서 프롬프트 엔지니어링을 적용하는 구체적인 방법을 단계별로 설명해주세요",
            "에세이 작성, 연구 계획, 코딩 과제 등 다양한 학업 상황에 맞는 프롬프트 예시를 제공해주세요",
            "복잡한 과제를 해결하기 위한 프롬프트 체인(여러 단계의 프롬프트) 구성 방법을 설명해주세요",
            "프롬프트 결과를 평가하고 개선하는 실용적인 방법을 알려주세요",
            "윤리적 측면을 고려한 프롬프트 엔지니어링 실천 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}의 핵심 내용을 체계적으로 설명해주세요",
            "이론적 개념과 함께 실제 적용 방법을 구체적인 예시와 함께 제시해주세요",
            "초보자가 쉽게 이해하고 적용할 수 있는 단계별 접근법을 제공해주세요",
            "흔히 발생하는 문제나 오해와 그 해결책을 포함해주세요",
            "더 심화 학습을 위한 추천 자료나 연습 방법도 제안해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"핵심 개념은 굵은 글씨로 강조하고, 중요한 팁이나 주의사항은 따로 박스 형태로 표시해주세요. "
        f"실제 프롬프트 예시는 코드 블록으로 구분하여 제시해주세요. "
        f"내용은 대학생이 이해하기 쉽게 작성하되, 실용적인 적용을 위한 충분한 깊이를 유지해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 엔지니어링의 핵심 개념과 중요성",
        topic_options=PROMPT_ENGINEERING_TOPICS,
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