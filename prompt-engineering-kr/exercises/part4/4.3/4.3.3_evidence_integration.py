"""
표절 위험 없는 AI 활용법 실습 모듈

Part 4 - 섹션 4.3.3 실습 코드: AI 도구를 활용한 학술 글쓰기에서 표절 위험을 방지하는 방법을 학습합니다.
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
AI_ETHICAL_USAGE_TOPICS = {
    "1": {"name": "AI 윤리적 경계", "topic": "AI 활용의 윤리적 스펙트럼과 경계", "output_format": "윤리 가이드"},
    "2": {"name": "AI 생성물 변형", "topic": "AI 생성 콘텐츠의 효과적인 변형과 개인화", "output_format": "변형 전략"},
    "3": {"name": "AI 기여 인정", "topic": "AI 기여의 적절한 인정과 표기 방법", "output_format": "인용 가이드"},
    "4": {"name": "AI 협업 전략", "topic": "AI와의 효과적인 협업 및 워크플로우", "output_format": "협업 프레임워크"},
    "5": {"name": "AI 생성물 검증", "topic": "AI 생성 콘텐츠의 비판적 검토와 검증", "output_format": "검증 체크리스트"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "윤리 전문가 역할 설정: 연구 윤리와 AI 활용 전문가 역할 부여",
        "구체적 상황 설정: 학술 글쓰기에서 AI 활용 상황 구체화",
        "실용적 지침 요청: 표절 방지와 학문적 진정성 유지를 위한 구체적 전략 요청",
        "사례 기반 접근: 다양한 시나리오와 예시를 통한 윤리적 판단 연습 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "AI 도구를 활용한 학술 글쓰기의 윤리적 스펙트럼과 경계선을 이해할 수 있습니다",
    "AI 생성 콘텐츠를 효과적으로 변형하고 자신의 사고와 통합하는 방법을 습득할 수 있습니다",
    "AI의 기여를 적절히 인정하고 표기하는 다양한 방법과 형식을 익힐 수 있습니다",
    "학문적 진정성을 유지하면서 AI와 효과적으로 협업하는 워크플로우를 개발할 수 있습니다",
    "AI 생성 콘텐츠를 비판적으로 검토하고 검증하는 체계적인 접근법을 배울 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 설정
    builder.add_role(
        "연구 윤리 전문가", 
        "AI와 학술 글쓰기의 윤리적 측면을 연구하는 전문가로, 대학의 연구 윤리 위원회에서 활동하며 표절 예방과 학문적 진정성 유지에 관한 지침을 개발하는 윤리학자"
    )
    
    # 주제별 맥락 및 지시사항 설정
    if "AI 윤리적 경계" in topic:
        builder.add_context(
            f"저는 학술 연구에 AI 도구를 활용하고자 하는 대학원생으로, {topic}에 대한 명확한 이해가 필요합니다. "
            f"AI 활용의 허용 가능한 범위와 넘지 말아야 할 경계, 다양한 학문 분야와 상황에 따른 "
            f"윤리적 고려사항에 대한 체계적인 가이드가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 AI 활용의 윤리적 스펙트럼(도구적 활용부터 대체적 활용까지)을 단계별로 설명해주세요",
            "AI 활용이 윤리적으로 허용 가능한 경우와 표절/학문적 부정행위로 간주될 수 있는 경계선을 명확히 구분해주세요",
            "다양한 학문 분야(인문학, 사회과학, 자연과학, 공학 등)에 따른 AI 활용의 윤리적 차이를 비교해주세요",
            "다양한 학술 맥락(학위 논문, 학술지 논문, 과제물, 연구 제안서 등)별 AI 활용의 윤리적 고려사항을 안내해주세요",
            "AI 활용 관련 최신 학술지 정책과 대학 지침의 동향을 요약하고, 실제 사례를 통한 윤리적 판단 연습을 포함해주세요"
        ])
        
    elif "AI 생성물 변형" in topic:
        builder.add_context(
            f"저는 연구 과정에서 AI를 보조 도구로 활용하는 연구자로, {topic}에 대한 구체적인 전략이 필요합니다. "
            f"AI가 생성한 콘텐츠를 단순히 복사하는 것이 아니라, 효과적으로 변형하고 개인화하여 "
            f"학문적 진정성을 유지하면서 연구 생산성을 높이는 방법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "AI 생성 콘텐츠의 '실질적 변형'(substantial transformation)의 의미와 중요성을 설명해주세요",
            "AI 생성 텍스트를 효과적으로 재구성하고 개인화하는 단계별 접근법을 구체적으로 안내해주세요",
            "자신의 관점, 비판적 분석, 독창적 기여를 AI 생성 콘텐츠에 통합하는 구체적인 방법을 예시와 함께 제시해주세요",
            "학문 분야별로 효과적인 변형 전략의 차이(예: 인문학적 텍스트 vs. 과학적 설명)를 비교해주세요",
            "AI 생성 콘텐츠의 변형 전과 후를 보여주는 최소 3개의 구체적인 예시와 변형 과정 설명을 포함해주세요"
        ])
        
    elif "AI 기여 인정" in topic:
        builder.add_context(
            f"저는 AI 도구를 활용한 연구 논문을 준비 중인 대학원생으로, {topic}에 대한 지침이 필요합니다. "
            f"AI의 기여를 투명하고 정확하게 인정하고 표기하는 방법, 다양한 인용 스타일과 학술지 요구사항에 "
            f"맞는 AI 활용 공개 방식에 대한 구체적인 가이드가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 글쓰기에서 AI 기여 인정의 필요성과 기본 원칙(투명성, 정확성, 비례성 등)을 설명해주세요",
            "주요 인용 스타일(APA, MLA, Chicago 등)에 따른 AI 도구 인용 및 표기 형식을 구체적인 예시와 함께 제공해주세요",
            "논문의 다양한 섹션(방법론, 감사의 글, 각주 등)에 AI 기여를 표기하는 적절한 방법과 예시 문구를 제안해주세요",
            "AI 기여 정도에 따른 차별화된 인정 방식(단순 도구적 활용 vs. 내용 생성 기여)을 설명해주세요",
            "주요 학술지와 기관의 AI 활용 공개 정책 동향을 요약하고, 현재 논쟁 중인 쟁점(예: AI를 공동 저자로 표시할 수 있는가?)도 다뤄주세요"
        ])
        
    elif "AI 협업 전략" in topic:
        builder.add_context(
            f"저는 복잡한 연구 프로젝트를 진행 중인 학자로, {topic}에 관심이 있습니다. "
            f"학문적 진정성을 유지하면서 AI와 효과적으로 협업하는 단계별 프로세스, "
            f"연구 및 글쓰기 워크플로우에 AI를 윤리적으로 통합하는 구체적인 전략이 필요합니다."
        )
        
        builder.add_instructions([
            "연구 및 학술 글쓰기의 각 단계(아이디어 생성, 자료 수집, 구조화, 초안 작성, 수정)별 AI 활용 전략을 설명해주세요",
            "학문적 진정성을 유지하면서 AI와 효과적으로 협업하기 위한 단계별 워크플로우를 구체적으로 제안해주세요",
            "AI에 효과적인 프롬프트를 작성하는 전략(학습 촉진, 비판적 사고 강화, 개인화 등)을 예시와 함께 제공해주세요",
            "AI 협업 과정을 기록하고 투명성을 유지하는 시스템 구축 방법을 안내해주세요",
            "AI 협업 시 흔히 발생하는 윤리적 함정과 이를 피하기 위한 구체적인 전략도 포함해주세요"
        ])
        
    else:  # AI 생성물 검증
        builder.add_context(
            f"저는 AI를 연구 보조 도구로 활용하는 연구자로, {topic}에 관한 체계적인 접근법이 필요합니다. "
            f"AI가 생성한 내용의 사실적 정확성, 논리적 일관성, 학술적 적절성을 체계적으로 검증하고, "
            f"AI가 제공한, 존재하지 않는 '가상의' 참고문헌이나 데이터를 식별하는 방법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
    "AI 생성 콘텐츠의 주요 검증 영역(사실 정확성, 논리적 일관성, 학술적 적절성, 출처 검증 등)을 설명해주세요",
    "AI의 '환각'(hallucination) 현상을 이해하고 허위 정보, 가상의 참고문헌, 잘못된 인용을 식별하는 방법을 제시해주세요",
    "AI 생성 콘텐츠를 검증하기 위한 체계적인 단계별 프로세스와 체크리스트를 개발해주세요",
    "다양한 학문 분야별로 AI 생성 콘텐츠를 검증하는 특화된 접근법과 고려사항을 설명해주세요",
    "AI 생성 콘텐츠의 검증을 위한 유용한 도구와 리소스(학술 데이터베이스, 표절 검사 도구 등)를 소개해주세요"
])
    
# 출력 형식 지정
builder.add_format_instructions(
    f"응답은 {output_format} 형식으로 구성해주세요. "
    f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
    f"윤리적 고려사항과 원칙은 명확하게 설명하고, 구체적인 예시와 사례를 통해 이해를 돕습니다. "
    f"체크리스트, 표, 플로우차트 등 시각적 요소를 활용하여 복잡한 윤리적 판단을 돕는 도구를 제공해주세요. "
    f"학술적 정확성을 유지하면서도 실용적이고 적용 가능한 전략과 지침을 강조해주세요. "
    f"다양한 학문 분야와 상황에 맞게 조정할 수 있는 유연한 프레임워크를 제시해주세요."
)
    
return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="표절 위험 없는 AI 활용법",
        topic_options=AI_ETHICAL_USAGE_TOPICS,
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
