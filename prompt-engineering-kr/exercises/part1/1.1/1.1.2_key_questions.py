"""
핵심 질문 작성하기 실습 모듈

Part 1 - 섹션 1.1.2 실습 코드: 효과적인 프롬프트를 위한 핵심 질문(무엇을, 어떻게, 왜)의 
중요성과 활용 방법을 학습합니다.
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
KEY_QUESTIONS_TOPICS = {
    "1": {"name": "기업 분석", "topic": "기업 분석 보고서 작성", "output_format": "분석 보고서"},
    "2": {"name": "학술 연구", "topic": "연구 주제 탐색과 문헌 검토", "output_format": "연구 계획서"},
    "3": {"name": "제품 설계", "topic": "사용자 중심 제품 설계", "output_format": "설계 명세서"},
    "4": {"name": "마케팅 전략", "topic": "타겟 고객을 위한 마케팅 전략", "output_format": "전략 제안서"},
    "5": {"name": "문제 해결", "topic": "일반적인 문제 해결 접근법", "output_format": "해결책 프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "무엇을(What): 목표와 필요한 요소 명확화",
        "어떻게(How): 방법과 프로세스 구체화",
        "왜(Why): 목적과 의도 설명"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "핵심 질문(무엇을, 어떻게, 왜)을 명확히 하면 AI의 응답 품질이 크게 향상됩니다",
    "무엇을(What) 질문은 원하는 결과물의 특성과 요소를 정의합니다",
    "어떻게(How) 질문은 접근 방식과 프로세스를 구체화합니다",
    "왜(Why) 질문은 목적과 가치를 명확히 하여 더 관련성 높은 결과를 얻게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    if "기업 분석" in topic:
        builder.add_role(
            "비즈니스 분석가", 
            "복잡한 기업 데이터를 분석하고 의미 있는 인사이트를 도출하는 전문가"
        )
    elif "학술 연구" in topic:
        builder.add_role(
            "연구 방법론 전문가", 
            "효과적인 연구 계획 수립과 문헌 검토를 지원하는 학술 조언자"
        )
    elif "제품 설계" in topic:
        builder.add_role(
            "제품 디자이너", 
            "사용자 중심 설계 방법론을 적용한 혁신적인 제품 개발 전문가"
        )
    elif "마케팅 전략" in topic:
        builder.add_role(
            "마케팅 전략가", 
            "데이터 기반 의사결정과 고객 인사이트를 활용한 마케팅 전문가"
        )
    else:
        builder.add_role(
            "문제 해결 전문가", 
            "체계적인 접근법으로 복잡한 문제를 분석하고 해결책을 제시하는 전략가"
        )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}을 진행하는 대학생으로, 체계적인 프레임워크가 필요합니다. "
        f"5W1H 질문법 중에서도 핵심인 무엇을(What), 어떻게(How), 왜(Why) 질문을 중심으로 "
        f"분석적이고 논리적인 접근 방법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가 - What, How, Why 질문을 명시적으로 포함
    if "기업 분석" in topic:
        builder.add_instructions([
            "무엇을(What): 기업 분석에 필수적인 핵심 요소와 데이터는 무엇인지 구체적으로 설명해주세요",
            "어떻게(How): 효과적인 기업 분석을 위한 단계별 프로세스와 방법론을 제시해주세요",
            "왜(Why): 각 분석 요소와 단계가 중요한 이유와 비즈니스 의사결정에 미치는 영향을 설명해주세요",
            "실제 기업 분석 사례나 템플릿 예시를 포함해주세요",
            "초보자가 쉽게 적용할 수 있는 체크리스트나 프레임워크를 제공해주세요"
        ])
    elif "학술 연구" in topic:
        builder.add_instructions([
            "무엇을(What): 효과적인 연구 주제 선정과 문헌 검토에 필요한 핵심 요소는 무엇인지 설명해주세요",
            "어떻게(How): 연구 주제 구체화부터 문헌 검토까지의 단계별 접근 방법을 안내해주세요",
            "왜(Why): 체계적인 연구 계획과 문헌 검토가 연구의 질과 가치에 미치는 영향을 설명해주세요",
            "연구 주제 선정 기준과 좋은 연구 질문의 특성을 포함해주세요",
            "문헌 검토를 효율적으로 진행하기 위한 도구와 방법론도 소개해주세요"
        ])
    elif "제품 설계" in topic:
        builder.add_instructions([
            "무엇을(What): 사용자 중심 제품 설계에 필요한 핵심 요소와 고려사항은 무엇인지 설명해주세요",
            "어떻게(How): 사용자 요구사항 파악부터 최종 설계까지의 단계별 프로세스를 안내해주세요",
            "왜(Why): 사용자 중심 설계가 제품의 성공과 사용자 만족도에 미치는 영향을 설명해주세요",
            "사용자 리서치 방법과 인사이트 도출 기법을 포함해주세요",
            "효과적인 프로토타이핑과 사용자 테스트 방법론도 소개해주세요"
        ])
    elif "마케팅 전략" in topic:
        builder.add_instructions([
            "무엇을(What): 효과적인 마케팅 전략 수립에 필요한 핵심 구성요소와 데이터는 무엇인지 설명해주세요",
            "어떻게(How): 타겟 고객 분석부터 전략 실행까지의 단계별 접근 방법을 안내해주세요",
            "왜(Why): 데이터 기반 마케팅 전략이 비즈니스 성과와 고객 관계에 미치는 영향을 설명해주세요",
            "고객 페르소나 개발과 타겟 시장 세그먼트 정의 방법을 포함해주세요",
            "디지털 마케팅과 전통적 마케팅 채널의 효과적인 통합 방안도 제시해주세요"
        ])
    else:
        builder.add_instructions([
            "무엇을(What): 효과적인 문제 해결에 필요한 핵심 요소와 정보는 무엇인지 설명해주세요",
            "어떻게(How): 문제 정의부터 해결책 실행까지의 단계별 프로세스를 안내해주세요",
            "왜(Why): 체계적인 문제 해결 접근법이 결과의 질과 지속가능성에 미치는 영향을 설명해주세요",
            "문제의 근본 원인 분석 방법과 다양한 관점에서의 접근법을 포함해주세요",
            "복잡한 문제를 다룰 때 흔히 발생하는 실수와 이를 피하는 방법도 제시해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"각 섹션은 무엇을(What), 어떻게(How), 왜(Why) 구조로 명확하게 구분해주세요. "
        f"실제 적용 가능한 템플릿이나 프레임워크를 포함해주세요. "
        f"핵심 개념이나 중요 포인트는 굵은 글씨로 강조해주세요. "
        f"시각적 이해를 돕기 위한 표나 다이어그램 구조를 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="핵심 질문 작성하기",
        topic_options=KEY_QUESTIONS_TOPICS,
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