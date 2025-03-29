"""
대화 히스토리 한계 극복하기 실습 모듈

Part 3 - 섹션 3.1 실습 코드: AI와의 장기적 대화에서 맥락을 유지하고 토큰 제한을 극복하는 방법을 실습합니다.
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
CONVERSATION_TOPICS = {
    "1": {"name": "대화 요약", "topic": "장기 대화 효과적 요약 기법", "output_format": "요약 가이드"},
    "2": {"name": "맥락 압축", "topic": "대화 맥락 압축 및 정제 방법", "output_format": "압축 프레임워크"},
    "3": {"name": "핵심 추출", "topic": "대화에서 핵심 정보 추출 기법", "output_format": "정보 추출 가이드"},
    "4": {"name": "토큰 최적화", "topic": "AI 대화에서 토큰 사용 최적화 전략", "output_format": "최적화 전략"},
    "5": {"name": "맥락 관리", "topic": "장기 프로젝트를 위한 대화 맥락 관리", "output_format": "관리 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["단순한 방법 요청"],
    "enhanced": [
        "체계적 접근: 구체적인 기법과 프레임워크 요청",
        "실용적 예시: 실제 적용 사례와 템플릿 포함",
        "상황별 전략: 다양한 대화 상황에 맞는 맞춤형 접근법"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "AI 대화에는 토큰 제한이라는 기술적 한계가 존재하며, 이를 극복하기 위한 전략이 필요합니다",
    "효과적인 대화 요약과 맥락 압축은 장기적 대화에서 연속성을 유지하는 핵심 기술입니다",
    "대화의 목적과 성격에 따라 다양한 맥락 관리 전략을 적용할 수 있습니다",
    "핵심 정보 추출과 문서화는 AI와의 장기 프로젝트에서 지식 관리의 중요한 요소입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "AI 대화 전략 전문가", 
        "AI와의 장기적 대화에서 맥락을 효과적으로 유지하고 토큰 제한을 극복하는 전략을 개발하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관심 있는 대학생입니다. "
        f"AI와 복잡한 프로젝트나 장기적인 학습을 진행할 때 대화 히스토리의 제한으로 맥락이 유실되는 문제에 자주 직면합니다. "
        f"특히 토큰 제한으로 인해 이전 대화 내용이 모두 유지되지 않아 연속성이 깨지는 경우가 많습니다. "
        f"이런 한계를 극복하고 효과적으로 맥락을 유지하는 실용적인 전략과 기법을 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "대화 요약" in topic:
        builder.add_instructions([
            "장기 대화의 내용을 효과적으로 요약하는 체계적인 방법과 원칙을 설명해주세요",
            "다양한 대화 유형(정보 수집, 브레인스토밍, 문제 해결, 학습 등)에 따른 맞춤형 요약 전략을 제시해주세요",
            "요약의 적절한 상세 수준과 핵심 요소를 결정하는 기준을 설명해주세요",
            "AI에게 이전 대화 요약을 효과적으로 제시하는 방법과 프롬프트 템플릿을 제공해주세요",
            "대화를 진행하면서 요약을 점진적으로 업데이트하는 효율적인 방법도 포함해주세요"
        ])
    elif "맥락 압축" in topic:
        builder.add_instructions([
            "복잡한 대화 맥락을 효율적으로 압축하고 정제하는 체계적인 방법과 원칙을 설명해주세요",
            "토큰 사용을 최소화하면서도 중요한 맥락 정보를 보존하는 압축 기법을 제시해주세요",
            "다양한 주제와 목적에 따른 맞춤형 맥락 압축 전략을 제안해주세요",
            "압축된 맥락을 AI에게 효과적으로 전달하는 프롬프트 구조와 템플릿을 제공해주세요",
            "장기 프로젝트에서 맥락 압축을 체계적으로 관리하는 워크플로우도 설명해주세요"
        ])
    elif "핵심 정보 추출" in topic:
        builder.add_instructions([
            "대화에서 핵심 정보를 식별하고 추출하는 체계적인 방법과 원칙을 설명해주세요",
            "다양한 유형의 핵심 정보(사실, 통찰, 결정사항, 행동 항목 등)를 분류하고 추출하는 방법을 제시해주세요",
            "추출한 핵심 정보를 효과적으로 구조화하고 조직화하는 프레임워크를 제안해주세요",
            "핵심 정보 추출 결과를 AI에게 효율적으로 전달하는 프롬프트 템플릿을 제공해주세요",
            "장기 대화에서 핵심 정보의 업데이트와 버전 관리 방법도 포함해주세요"
        ])
    elif "토큰 최적화" in topic:
        builder.add_instructions([
            "AI 대화에서 토큰 사용을 최적화하는 체계적인 전략과 기법을 설명해주세요",
            "토큰 소비를 최소화하면서도 효과적인 프롬프트를 작성하는 원칙과 방법을 제시해주세요",
            "다양한 AI 모델과 대화 상황에 맞는 토큰 최적화 접근법을 제안해주세요",
            "장기 대화에서 토큰 한계를 관리하기 위한 실용적인 전략과 도구를 제공해주세요",
            "토큰 사용을 모니터링하고 최적화하는 체계적인 프로세스도 포함해주세요"
        ])
    elif "맥락 관리" in topic:
        builder.add_instructions([
            "장기 프로젝트를 위한 대화 맥락 관리 시스템과 방법론을 설명해주세요",
            "프로젝트 유형과 목적에 따른 맞춤형 맥락 관리 전략을 제시해주세요",
            "맥락 정보의 우선순위 설정, 구조화, 업데이트를 위한 체계적인 프레임워크를 제안해주세요",
            "대화 세션 간 맥락의 연속성을 유지하기 위한 실용적인 도구와 템플릿을 제공해주세요",
            "복잡한's 프로젝트에서 맥락 정보를 효과적으로 문서화하고 참조하는 시스템도 설명해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 체계적인 접근법과 실용적인 전략을 설명해주세요",
            "다양한 상황과 목적에 맞는 맞춤형 기법과 도구를 제시해주세요",
            "실제 적용 사례와 구체적인 예시를 통해 개념을 명확히 해주세요",
            "단계별 적용 가이드와 템플릿을 제공해주세요",
            "흔한 문제점과 해결 방법도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"다음 섹션들을 포함해주세요: "
        f"1) 개념 및 원칙: 기본 개념과 핵심 원칙 설명 "
        f"2) 체계적 접근법: 단계별 방법론과 프로세스 "
        f"3) 실용적 전략: 다양한 상황별 구체적 전략과 기법 "
        f"4) 템플릿 및 도구: 바로 적용할 수 있는 템플릿과 프롬프트 예시 "
        f"5) 사례 연구: 실제 적용 예시와 성공 사례 "
        f"6) 문제 해결: 흔한 문제점과 해결 방법 "
        f"실용적이고 적용하기 쉬운 내용을 중심으로, 이론보다는 구체적인 방법과 예시를 강조해주세요. "
        f"표, 다이어그램, 체크리스트 등의 시각적 요소를 적절히 활용하여 이해를 돕고 참조하기 쉽게 만들어주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="대화 히스토리 한계 극복하기",
        topic_options=CONVERSATION_TOPICS,
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
