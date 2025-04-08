"""
프롬프트 개선 워크숍 실습 모듈

Part 8 - 섹션 8.4 실습 코드: 비효과적인 프롬프트를 분석하고, 단계적으로 개선하며, 
체계적인 디버깅 체크리스트를 개발하는 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
PROMPT_IMPROVEMENT_TOPICS = {
    "1": {"name": "학술 연구 프롬프트", "topic": "학술 연구 관련 프롬프트 개선 워크숍", "output_format": "개선 가이드"},
    "2": {"name": "비즈니스 문서", "topic": "비즈니스 문서 작성 프롬프트 개선 워크숍", "output_format": "단계별 분석"},
    "3": {"name": "창의적 콘텐츠", "topic": "창의적 콘텐츠 생성 프롬프트 개선 워크숍", "output_format": "사례 연구"},
    "4": {"name": "코드 및 기술", "topic": "코드 및 기술 관련 프롬프트 개선 워크숍", "output_format": "분석 매트릭스"},
    "5": {"name": "교육 콘텐츠", "topic": "교육 콘텐츠 개발 프롬프트 개선 워크숍", "output_format": "종합 워크북"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["프롬프트 개선 방법에 대한 일반적인 설명 요청"],
    "enhanced": [
        "역할 설정: 프롬프트 엔지니어링 전문가 역할 부여",
        "체계적 접근: 분석-개선-검증의 전체 워크숍 과정 요청",
        "실제 사례: 구체적인 비효과적 프롬프트 사례와 개선 과정 요청",
        "도구 제공: 디버깅 체크리스트와 재사용 가능한 템플릿 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 프롬프트 개선은 체계적인 문제 진단에서 시작됩니다",
    "단계적 개선 접근법은 각 변경의 효과를 명확히 평가할 수 있게 합니다",
    "다양한 프롬프트 디버깅 프레임워크를 상황에 맞게 적용하면 더 효과적인 진단이 가능합니다",
    "개선 과정의 체계적인 기록은 프롬프트 엔지니어링 지식을 축적하는 데 중요합니다",
    "재사용 가능한 디버깅 체크리스트는 프롬프트 품질 관리 프로세스를 효율화합니다"
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
        "비효과적인 프롬프트를 체계적으로 분석하고 개선하는 전문가로, 다양한 분야의 프롬프트 최적화 경험이 풍부합니다"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심이 있는 프롬프트 엔지니어링 학습자입니다. "
        f"비효과적인 프롬프트를 체계적으로 분석하고, 단계적으로 개선하며, "
        f"이 과정에서 얻은 인사이트를 바탕으로 재사용 가능한 디버깅 체크리스트를 개발하는 방법을 배우고 싶습니다. "
        f"실제 사례를 바탕으로 한 완전한 워크숍 형태의 안내가 필요합니다."
    )
    
    # 주제별 비효과적 프롬프트 예시 정의
    ineffective_prompts = {
        "학술 연구": "이 주제에 대한 논문 쓰는 법 알려줘.",
        "비즈니스 문서": "회사 보고서 작성해줘.",
        "창의적 콘텐츠": "재미있는 이야기 써줘.",
        "코드 및 기술": "이 코드 에러 고쳐줘.",
        "교육 콘텐츠": "수업 자료 만들어줘."
    }
    
    # 주제 키워드 추출 (대략적인 매칭)
    topic_key = next((k for k in ineffective_prompts.keys() if k.lower() in topic.lower()), "학술 연구")
    
    # 선택된 비효과적 프롬프트
    selected_prompt = ineffective_prompts[topic_key]
    
    # 공통 지시사항
    common_instructions = [
        f"다음과 같은 비효과적 프롬프트를 예시로 사용해주세요: '{selected_prompt}'",
        "비효과적 프롬프트 분석: GAP 분석, ABCD 프레임워크, 5W1H 접근법 등 다양한 진단 프레임워크를 적용해 문제점을 체계적으로 분석해주세요",
        "단계별 개선 과정: RADIO 프레임워크(인식-분석-설계-실행-최적화)를 적용한 3-4단계의 개선 과정을 보여주세요. 각 단계별 변경 사항, 변경 이유, 예상 효과, 실제 결과를 명확히 기록해주세요",
        "프롬프트 디버깅 체크리스트: 이 분야의 프롬프트를 위한 재사용 가능한 진단 체크리스트를 개발하고, 체크리스트 항목의 중요도와 적용 방법을 설명해주세요",
        "워크플로우 통합: 개발된 체크리스트를 프롬프트 작성 및 개선 워크플로우에 통합하는 방법을 제안해주세요"
    ]
    
    # 주제별 특화 지시사항 추가
    if "학술 연구" in topic:
        specific_instructions = [
            "학술 연구 프롬프트에서 특히 중요한 요소(연구 질문, 방법론, 학술적 맥락, 문헌 검토 등)에 중점을 두고 분석해주세요",
            "학술 연구 프롬프트의 명확성, 구체성, 학문적 엄격성을 향상시키는 구체적인 전략을 제시해주세요",
            "다양한 학문 분야(인문학, 사회과학, 자연과학 등)에 적용할 수 있는 범용 원칙과 분야별 특화 전략을 구분해주세요"
        ]
    elif "비즈니스 문서" in topic:
        specific_instructions = [
            "비즈니스 문서 프롬프트에서 특히 중요한 요소(대상 독자, 목적, 핵심 메시지, 데이터 통합 등)에 중점을 두고 분석해주세요",
            "비즈니스 맥락에 맞는 명확성, 간결성, 설득력을 향상시키는 구체적인 전략을 제시해주세요",
            "다양한 비즈니스 문서 유형(보고서, 제안서, 이메일, 프레젠테이션 등)에 맞는 프롬프트 개선 전략을 구분해주세요"
        ]
    elif "창의적 콘텐츠" in topic:
        specific_instructions = [
            "창의적 콘텐츠 프롬프트에서 특히 중요한 요소(장르, 캐릭터, 설정, 플롯, 톤, 스타일 등)에 중점을 두고 분석해주세요",
            "창의성을 자극하면서도 명확한 방향성을 제시하는 균형 잡힌 프롬프트 개발 전략을 제시해주세요",
            "다양한 창작 장르(소설, 시, 스크립트, 마케팅 카피 등)에 맞는 프롬프트 개선 전략을 구분해주세요"
        ]
    elif "코드 및 기술" in topic:
        specific_instructions = [
            "코드 및 기술 관련 프롬프트에서 특히 중요한 요소(문제 정의, 환경 설정, 제약조건, 예상 결과 등)에 중점을 두고 분석해주세요",
            "기술적 명확성, 정확성, 맥락 제공을 향상시키는 구체적인 전략을 제시해주세요",
            "다양한 기술 영역(웹 개발, 데이터 분석, 알고리즘 등)에 맞는 프롬프트 개선 전략을 구분해주세요"
        ]
    else:  # 교육 콘텐츠
        specific_instructions = [
            "교육 콘텐츠 개발 프롬프트에서 특히 중요한 요소(학습 목표, 대상 학습자, 교육 수준, 평가 방법 등)에 중점을 두고 분석해주세요",
            "교육적 명확성, 구조화, 참여 유도를 향상시키는 구체적인 전략을 제시해주세요",
            "다양한 교육 환경(K-12, 대학, 성인 교육, 온라인 학습 등)과 과목에 맞는 프롬프트 개선 전략을 구분해주세요"
        ]
    
    # 모든 지시사항 추가
    for instruction in common_instructions + specific_instructions:
        builder.add_instructions([instruction])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요: "
        f"1) 워크숍 개요: 목적과 접근법 "
        f"2) 비효과적 프롬프트 분석: 체계적 진단 "
        f"3) 단계별 개선 과정: 각 단계별 변경과 효과 "
        f"4) 프롬프트 디버깅 체크리스트: 재사용 가능한 진단 도구 "
        f"5) 워크플로우 통합: 실무 적용 방법 "
        f"표, 예시, 비교 분석 등을 활용하여 내용을 시각적으로 명확하게 전달해주세요. "
        f"실제 워크숍에서 사용할 수 있는 실용적인 형태로 구성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="여덟 번째 실습: 프롬프트 개선 워크숍",
        topic_options=PROMPT_IMPROVEMENT_TOPICS,
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