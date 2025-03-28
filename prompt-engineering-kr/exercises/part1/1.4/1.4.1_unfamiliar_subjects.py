"""
IR 자료 분석 접근법 실습 모듈

Part 1 - 섹션 1.4.1 실습 코드: 투자자 관계(IR) 자료 분석을 위한 효과적인 프롬프트 작성 방법을 학습합니다.
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
IR_ANALYSIS_TOPICS = {
    "1": {"name": "재무제표 분석", "topic": "IR 자료의 재무제표 분석 방법", "output_format": "분석 가이드"},
    "2": {"name": "사업 전략", "topic": "IR 자료를 통한 기업 사업 전략 이해", "output_format": "해석 프레임워크"},
    "3": {"name": "투자 전망", "topic": "IR 자료의 투자 전망 및 위험 요소 분석", "output_format": "평가 체계"},
    "4": {"name": "산업 비교", "topic": "IR 자료를 활용한 동종 산업 기업 비교", "output_format": "비교 매트릭스"},
    "5": {"name": "CEO 메시지", "topic": "IR 자료의 CEO 메시지 및 경영진 발언 분석", "output_format": "분석 템플릿"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "분석 목적 제시: IR 자료 분석을 통해 얻고자 하는 인사이트 명시",
        "구체적 요청: 특정 분석 영역과 접근 방법 요청",
        "구조화된 출력: 체계적 분석을 위한 프레임워크와 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "IR 자료는 기업의 재무 상태, 전략, 비전을 파악할 수 있는 중요한 정보원입니다",
    "체계적인 분석 접근법으로 복잡한 IR 자료에서 핵심 정보를 추출할 수 있습니다",
    "맥락을 제공하고 구체적인 분석 영역을 지정하면 더 유용한 인사이트를 얻을 수 있습니다",
    "비전문가도 적절한 프롬프트를 통해 IR 자료의 핵심을 파악하는 능력을 개발할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "재무 분석 전문가", 
        "투자자 관계(IR) 자료를 분석하고 해석하는 전문 애널리스트"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 경영학과 대학생으로 {topic}에 대해 학습하고 있습니다. "
        f"기업의 IR 자료를 처음 접하는 초보자로서, 복잡한 재무 데이터와 전문 용어가 어렵게 느껴집니다. "
        f"IR 자료를 효과적으로 분석하고 이해하는 방법에 대한 안내가 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "재무제표" in topic:
        builder.add_instructions([
            "IR 자료에서 핵심 재무제표(손익계산서, 재무상태표, 현금흐름표)를 분석하는 방법을 단계별로 설명해주세요",
            "초보자도 이해할 수 있도록 주요 재무 지표와 용어를 쉽게 설명해주세요",
            "재무제표 간의 연결성과 상호 관계를 파악하는 방법을 알려주세요",
            "재무제표 분석을 통해 기업의 건전성과 성장성을 평가하는 방법을 구체적인 예시와 함께 설명해주세요",
            "재무제표 분석 시 주의해야 할 점과 흔히 범하는 실수를 알려주세요"
        ])
    elif "사업 전략" in topic:
        builder.add_instructions([
            "IR 자료에서 기업의 사업 전략과 비전을 파악하는 방법을 설명해주세요",
            "수치 이외의 정성적 정보(경영진 메시지, 사업 계획 등)를 분석하는 접근법을 알려주세요",
            "표면적인 내용 너머의 실질적인 전략 방향과 우선순위를 파악하는 방법을 설명해주세요",
            "과거 IR 자료와 비교하여 전략 변화와 일관성을 평가하는 방법을 알려주세요",
            "기업의 실제 행동과 IR 자료에 명시된 전략 간의 일치도를 판단하는 방법도 포함해주세요"
        ])
    elif "투자 전망" in topic:
        builder.add_instructions([
            "IR 자료에서 기업의 미래 성장 가능성과 투자 매력도를 분석하는 방법을 설명해주세요",
            "IR 자료에 명시적/암묵적으로 포함된 위험 요소와 불확실성을 파악하는 방법을 알려주세요",
            "기업이 제시하는 미래 전망의 신뢰성과 타당성을 평가하는 기준을 제안해주세요",
            "투자 결정에 영향을 미치는 IR 자료의 핵심 요소와 그 중요도를 설명해주세요",
            "IR 자료 분석을 통한 투자 의사결정 프로세스를 단계별로 제시해주세요"
        ])
    elif "산업 비교" in topic:
        builder.add_instructions([
            "여러 기업의 IR 자료를 비교 분석하는 체계적인 방법을 설명해주세요",
            "동종 산업 내 기업들의 성과와 전략을 비교할 수 있는 핵심 지표를 제시해주세요",
            "산업 평균 대비 기업의 강점과 약점을 파악하는 방법을 알려주세요",
            "경쟁사 IR 자료와의 비교를 통해 경쟁 구도와 시장 포지셔닝을 분석하는 프레임워크를 제안해주세요",
            "다양한 기업의 IR 자료를 효율적으로 분석하기 위한 템플릿이나 체크리스트도 포함해주세요"
        ])
    elif "CEO 메시지" in topic:
        builder.add_instructions([
            "IR 자료의 CEO 메시지와 경영진 발언을 분석하는 방법을 설명해주세요",
            "공식적인 메시지 속에 숨겨진 함의와 우선순위를 파악하는 방법을 알려주세요",
            "언어적 표현, 강조점, 생략된 내용 등을 통해 기업의 실제 상황을 유추하는 기법을 제시해주세요",
            "과거 메시지와의 비교를 통해 전략 변화와 일관성을 평가하는 방법을 설명해주세요",
            "CEO 메시지 분석을 통해 기업 문화와 경영 스타일을 파악하는 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적인 분석 방법을 초보자도 이해할 수 있게 설명해주세요",
            "핵심 개념과 용어를 쉽게 설명하고, 실제 IR 자료 예시를 통한 적용 방법을 보여주세요",
            "단계별 접근법을 통해 복잡한 정보를 체계적으로 분석하는 방법을 제시해주세요",
            "분석 과정에서 주의해야 할 점과 흔히 범하는 실수를 알려주세요",
            "초보자가 실제로 활용할 수 있는 분석 템플릿이나 체크리스트를 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"핵심 개념과 용어는 굵은 글씨로 강조하고, 예시나 사례는 인용 형식으로 구분해주세요. "
        f"가능한 경우 분석 단계나 체크포인트를 표 형식으로 정리해주세요. "
        f"복잡한 개념은 비유나 예시를 통해 이해하기 쉽게 설명해주세요. "
        f"모든 내용은 경영학과 대학생이 이해할 수 있는 수준으로, 실무에 바로 적용 가능하도록 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="IR 자료 분석 접근법",
        topic_options=IR_ANALYSIS_TOPICS,
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