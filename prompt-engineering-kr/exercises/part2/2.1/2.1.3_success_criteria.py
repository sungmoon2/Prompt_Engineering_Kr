"""
단계적 질문 체인 구성하기 실습 모듈

Part 2 - 섹션 2.1.3 실습 코드: 복잡한 과제를 해결하기 위한 단계적 질문 체인 구성 방법을 학습합니다.
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
QUESTION_CHAIN_TOPICS = {
    "1": {"name": "연구 설계", "topic": "연구 프로젝트를 위한 단계적 질문 체인 구성", "output_format": "질문 로드맵"},
    "2": {"name": "논증 구축", "topic": "논리적 논증을 위한 질문 체인 개발", "output_format": "논증 프레임워크"},
    "3": {"name": "복잡한 문제 해결", "topic": "복잡한 문제 해결을 위한 순차적 질문 접근법", "output_format": "문제 해결 가이드"},
    "4": {"name": "창의적 프로젝트", "topic": "창의적 프로젝트 개발을 위한 질문 체인", "output_format": "아이디어 개발 체계"},
    "5": {"name": "비판적 분석", "topic": "비판적 분석을 위한 체계적 질문 프레임워크", "output_format": "분석 템플릿"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "맥락 제공: 질문 체인의 필요성과 목적 설명",
        "구체적 요청: 단계별 질문 구성 및 연결 방법 요청",
        "실용적 구성: 실제 적용 가능한 예시와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "단계적 질문 체인은 복잡한 과제를 체계적으로 해결하는 강력한 도구입니다",
    "좋은 질문 체인은 기초적인 질문에서 점차 심화된 질문으로 발전합니다",
    "질문 간의 논리적 연결은 체계적인 사고와 분석을 촉진합니다",
    "맥락과 목적에 맞는 질문 체인 구성은 효율적인 과제 해결의 핵심입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "질문 설계 전문가", 
        "복잡한 과제를 해결하기 위한 효과적인 질문 체계와 프레임워크를 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"복잡한 과제나 문제를 다룰 때 체계적인 접근법이 부족하여 어려움을 겪곤 합니다. "
        f"순차적이고 논리적인 질문 체인을 구성하여 복잡한 과제를 단계별로 해결하는 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "연구 설계" in topic:
        builder.add_instructions([
            "연구 프로젝트를 위한 단계적 질문 체인의 개념과 중요성을 설명해주세요",
            "연구 주제 선정, 문헌 검토, 방법론 설계, 데이터 수집/분석 등 주요 연구 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 다음 질문으로 연결되고 발전하는지, 그 논리적 흐름을 설명해주세요",
            "연구 유형(양적/질적, 실험/조사 등)에 따른 질문 체인의 차이점과 조정 방법을 포함해주세요",
            "실제 연구 프로젝트에 적용할 수 있는 구체적인 질문 체인 템플릿과 워크시트를 제공해주세요"
        ])
    elif "논증 구축" in topic:
        builder.add_instructions([
            "논리적 논증 구축을 위한 질문 체인의 개념과 중요성을 설명해주세요",
            "주장 설정, 근거 개발, 반론 예상 및 대응 등 논증 구축의 주요 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 논증의 강화와 발전으로 이어지는지 그 논리적 흐름을 설명해주세요",
            "다양한 논증 유형(인과, 유추, 귀납, 연역 등)에 맞춘 질문 체인의 조정 방법을 포함해주세요",
            "에세이, 논문, 토론 등 다양한 맥락에 적용할 수 있는 논증 구축 질문 체인 템플릿을 제공해주세요"
        ])
    elif "복잡한 문제 해결" in topic:
        builder.add_instructions([
            "복잡한 문제 해결을 위한 순차적 질문 접근법의 개념과 중요성을 설명해주세요",
            "문제 정의, 원인 분석, 해결책 개발, 실행 계획, 평가 등 문제 해결의 주요 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 다음 단계로의 진전을 이끌어내는지 그 연결성을 설명해주세요",
            "다양한 유형의 문제(구조화된/비구조화된, 기술적/인적 등)에 맞춘 질문 체인의 조정 방법을 포함해주세요",
            "실제 문제 상황에 적용할 수 있는 단계별 질문 프레임워크와 워크시트를 제공해주세요"
        ])
    elif "창의적 프로젝트" in topic:
        builder.add_instructions([
            "창의적 프로젝트 개발을 위한 질문 체인의 개념과 중요성을 설명해주세요",
            "아이디어 발상, 개념 개발, 구체화, 실현 계획 등 창의적 프로세스의 주요 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 창의적 사고를 자극하고 프로젝트 발전으로 이어지는지 설명해주세요",
            "다양한 창의적 분야(디자인, 예술, 혁신 제품 등)에 맞춘 질문 체인의 조정 방법을 포함해주세요",
            "실제 창의적 프로젝트에 적용할 수 있는 단계별 질문 템플릿과 예시를 제공해주세요"
        ])
    elif "비판적 분석" in topic:
        builder.add_instructions([
            "비판적 분석을 위한 체계적 질문 프레임워크의 개념과 중요성을 설명해주세요",
            "정보 평가, 가정 검토, 논리 분석, 대안적 관점 탐색 등 비판적 사고의 주요 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 더 깊은 분석과 이해로 이어지는지 그 진행 과정을 설명해주세요",
            "다양한 분석 대상(텍스트, 주장, 정책, 이론 등)에 맞춘 질문 체인의 조정 방법을 포함해주세요",
            "학술 논문 비평, 미디어 분석, 아이디어 평가 등에 활용할 수 있는 비판적 분석 질문 템플릿을 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}을 위한 단계적 질문 체인의 개념과 중요성을 설명해주세요",
            "이 맥락에서 필요한 주요 단계들과 각 단계별 핵심 질문들을 제시해주세요",
            "각 질문이 어떻게 다음 질문으로 연결되고 발전하는지 그 논리적 흐름을 설명해주세요",
            "다양한 상황과 맥락에 맞춘 질문 체인의 조정 방법을 포함해주세요",
            "실제 적용할 수 있는 구체적인 질문 체인 템플릿과 예시를 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"주요 단계별로 섹션을 구분하고, 각 단계에서의 핵심 질문 세트와 그 목적을 명확히 설명해주세요. "
        f"질문 간의 연결성과 흐름을 시각적으로 표현한 다이어그램이나 표를 포함해주면 더욱 좋습니다. "
        f"실제 사례나 예시를 통해 질문 체인의 적용 방법을 구체적으로 보여주세요. "
        f"대학생이 즉시 활용할 수 있는 템플릿과 워크시트를 제공해주시고, 마지막에는 효과적인 질문 체인 개발과 활용을 위한 팁도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="단계적 질문 체인 구성하기",
        topic_options=QUESTION_CHAIN_TOPICS,
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