"""
문제 진단 프레임워크 실습 모듈

Part 8 - 섹션 8.1 실습 코드: 프롬프트 문제를 체계적으로 진단하고 분석하는 프레임워크를 학습합니다.
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
DIAGNOSTIC_FRAMEWORK_TOPICS = {
    "1": {"name": "프롬프트 진단 기초", "topic": "프롬프트 문제 진단 프레임워크 기초", "output_format": "진단 가이드"},
    "2": {"name": "오류 식별 방법", "topic": "일반적인 프롬프트 오류 식별 방법론", "output_format": "오류 분류 체계"},
    "3": {"name": "체계적 수정 접근법", "topic": "프롬프트 오류 체계적 수정 프로세스", "output_format": "단계별 가이드"},
    "4": {"name": "종합 진단 템플릿", "topic": "프롬프트 종합 진단 및 개선 템플릿", "output_format": "진단 워크시트"},
    "5": {"name": "사례 기반 분석", "topic": "실제 사례를 통한 프롬프트 진단 분석", "output_format": "사례 분석 보고서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["프롬프트 문제 진단에 대한 일반적 질문"],
    "enhanced": [
        "체계적 분석: 구조화된 진단 프레임워크 요청",
        "구체적 사례: 실제 프롬프트 예시를 통한 문제 분석",
        "실용적 도구: 즉시 활용 가능한 진단 템플릿과 체크리스트 제공"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "프롬프트 문제 진단은 기대와 결과 사이의 차이를 체계적으로 분석하는 것에서 시작합니다",
    "일반적인 프롬프트 오류 패턴을 인식하면 문제를 더 빠르고 정확하게 식별할 수 있습니다",
    "체계적인 오류 수정 접근법은 프롬프트 개선 과정을 효율적이고 효과적으로 만듭니다",
    "프롬프트 디버깅과 최적화는 반복적인 실험과 학습을 통해 지속적으로 향상됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요. 어떻게 프롬프트 문제를 진단하고 해결할 수 있을까요?"

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프롬프트 엔지니어링 디버깅 전문가", 
        "프롬프트 문제를 체계적으로 진단하고 효과적으로 개선하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 프롬프트 엔지니어링을 배우는 학생으로, {topic}에 관심이 있습니다. "
        f"프롬프트가 원하는 결과를 생성하지 않을 때 체계적으로 문제를 진단하고 해결하는 접근법을 배우고 싶습니다. "
        f"특히 문제 유형을 정확히 식별하고 체계적으로 수정하는 구조화된 방법론이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "진단 프레임워크 기초" in topic:
        # 기본적인 진단 프레임워크에 대한 지시사항
        builder.add_instructions([
            "프롬프트 문제를 진단하기 위한 체계적인 프레임워크의 기본 구성 요소를 설명해주세요",
            "기대 결과와 실제 결과 사이의 차이를 분석하는 방법을 단계별로 설명해주세요",
            "내용, 형식, 맥락 차원에서 프롬프트 결과를 평가하는 방법을 구체적인 평가 기준과 함께 설명해주세요",
            "프롬프트 진단 과정을 효과적으로 문서화하는 템플릿이나 프레임워크를 제공해주세요",
            "초보자가 쉽게 적용할 수 있는 진단 프로세스와 실용적인 팁을 포함해주세요"
        ])
        
    elif "오류 식별" in topic:
        # 프롬프트 오류 식별 방법에 대한 지시사항
        
        # 예시 오류 프롬프트
        error_prompt = """
파이썬 코드를 작성해줘. 데이터를 분석하고 시각화해야 함. 가능한 빨리 부탁해.
"""
        
        builder.add_instructions([
            "프롬프트에서 발생하는 일반적인 오류 유형을 체계적으로 분류하고 설명해주세요",
            f"다음과 같은 예시 오류 프롬프트를 분석하고 문제점을 식별해주세요: \"{error_prompt}\"",
            "명확성, 맥락, 구조, 전문성 관련 오류의 특징과 식별 방법을 구체적으로 설명해주세요",
            "일반적인 프롬프트 오류를 신속하게 식별할 수 있는 체크리스트나 진단 도구를 제공해주세요",
            "오류 유형별 예시와 대조적인 개선 예시를 함께 제시해주세요"
        ])
        
    elif "체계적 수정" in topic:
        # 오류 수정 접근법에 대한 지시사항
        
        # 예시 문제 프롬프트
        problem_prompt = """
창의적인 마케팅 아이디어가 필요해. 우리 제품은 좋아. 참신한 것으로 부탁해.
"""
        
        builder.add_instructions([
            "프롬프트 오류를 체계적으로 수정하는 단계별 프로세스를 설명해주세요",
            f"다음 예시 프롬프트의 문제점을 진단하고 개선하는 과정을 단계별로 보여주세요: \"{problem_prompt}\"",
            "오류 우선순위 설정, 분리 테스트, 점진적 개선 등 효과적인 오류 수정 전략을 설명해주세요",
            "문제 유형별(명확성, 맥락, 구조, 전문성) 수정 전략과 구체적인 적용 방법을 제시해주세요",
            "프롬프트 오류 수정 과정을 기록하고 추적하기 위한 워크시트나 템플릿을 제공해주세요"
        ])
        
    elif "종합 진단 템플릿" in topic:
        # 종합 진단 템플릿에 대한 지시사항
        builder.add_instructions([
            "프롬프트 문제를 종합적으로 진단하고 개선하기 위한 완전한 템플릿을 개발해주세요",
            "템플릿의 각 섹션(기본 정보, 기대-결과 분석, 오류 식별, 수정 계획 등)을 상세히 설명해주세요",
            "템플릿 작성 시 고려해야 할 핵심 질문과 체크포인트를 포함해주세요",
            "템플릿을 효과적으로 활용하는 방법과 각 단계별 작성 가이드를 제공해주세요",
            "다양한 프롬프트 상황에 템플릿을 적용할 수 있도록 유연한 구조와 변형 방법을 제안해주세요"
        ])
        
    else:  # 사례 기반 분석
        # 실제 사례 분석에 대한 지시사항
        
        # 첫 번째 사례 - 모호한 요청
        case1_prompt = """
에세이 작성 팁을 알려줘.
"""
        
        # 두 번째 사례 - 구조 부족
        case2_prompt = """
인공지능 윤리에 대한 분석을 해줘. 최근 발전과 주요 쟁점, 그리고 미래 전망도 포함해줘. 
철학적, 사회적, 기술적 관점에서 다양하게 다루면 좋겠어. 가능한 자세히 부탁해.
"""
        
        builder.add_instructions([
            "다음 두 가지 실제 사례를 통해 프롬프트 문제 진단 및 개선 과정을 보여주세요:",
            f"사례 1 (모호한 요청): \"{case1_prompt}\"",
            f"사례 2 (구조 부족): \"{case2_prompt}\"",
            "각 사례의 문제점을 체계적으로 진단하고, 명확한 개선 과정과 결과를 보여주세요",
            "사례 분석을 통해 배울 수 있는 주요 교훈과 일반화할 수 있는 원칙을 도출해주세요",
            "독자가 자신의 프롬프트 문제 진단에 적용할 수 있는 실용적인 팁과 가이드라인을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 표, 목록 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요: "
        f"1) 개요: 주요 개념과 원칙 요약 "
        f"2) 체계적 프레임워크: 단계별 진단 및 분석 방법 "
        f"3) 실용적 도구: 진단 템플릿, 체크리스트, 워크시트 등 "
        f"4) 적용 가이드: 실제 상황에서의 활용 방법 "
        f"5) 사례 분석: 구체적인 예시를 통한 적용 "
        f"각 개념은 실제 예시를 통해 설명하고, 즉시 활용 가능한 실용적인 도구와 팁을 제공해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="문제 진단 프레임워크",
        topic_options=DIAGNOSTIC_FRAMEWORK_TOPICS,
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