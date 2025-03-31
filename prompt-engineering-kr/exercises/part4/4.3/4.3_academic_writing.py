"""
학술적 표현과 인용 실습 모듈

Part 4 - 섹션 4.3 실습 코드: 학술적 표현과 인용 방법, 표절 위험 없는 AI 활용법을 학습합니다.
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
ACADEMIC_WRITING_TOPICS = {
    "1": {"name": "일상 언어를 학술 언어로", "topic": "일상 언어에서 학술 언어로 전환하기", "output_format": "가이드"},
    "2": {"name": "인용 스타일 적용", "topic": "적절한 인용과 참고문헌 관리", "output_format": "가이드"},
    "3": {"name": "AI 활용 학술 글쓰기", "topic": "표절 위험 없는 AI 활용법", "output_format": "윤리적 가이드"},
    "4": {"name": "학술 논문 작성", "topic": "학술 논문의 구조와 표현", "output_format": "템플릿"},
    "5": {"name": "연구 윤리", "topic": "연구 윤리와 학문적 진정성", "output_format": "체크리스트"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "학술적 역할 설정: 해당 분야 전문가 역할 부여",
        "세부 요청: 학술적 용어, 인용 방법, 표절 방지 전략 등 구체적 요청",
        "형식 지정: 학술적 문서 형식과 구조 명시",
        "윤리적 고려: AI 활용의 윤리적 측면 고려 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "일상 언어와 학술 언어의 차이점을 이해하고 적절히 전환할 수 있습니다",
    "다양한 인용 스타일과 참고문헌 관리 방법을 익히고 적용할 수 있습니다",
    "AI 도구를 활용한 학술 글쓰기에서 표절 위험을 방지하는 전략을 개발할 수 있습니다",
    "학술적 표현과 인용을 통해 글의 전문성과 신뢰성을 향상시킬 수 있습니다",
    "학술 글쓰기에서 윤리적 고려사항과 학문적 진정성의 중요성을 인식할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 역할 및 맥락 설정
    if "일상 언어" in topic:
        builder.add_role(
            "학술 글쓰기 전문가", 
            "다양한 학문 분야의 학술적 표현과 문체를 가르치는 글쓰기 교수로, 일상 언어를 학술적 표현으로 전환하는 방법론에 정통한 전문가"
        )
        
        builder.add_context(
            f"저는 대학원생으로 {topic}에 어려움을 겪고 있습니다. "
            f"논문 작성 시 일상적인 표현이 자주 사용되어 학술적 품격이 떨어진다는 지적을 받았습니다. "
            f"일상 언어를 학술 언어로 효과적으로 전환하는 구체적인 방법과 예시가 필요합니다."
        )
        
        builder.add_instructions([
            "일상 언어와 학술 언어의 주요 차이점을 분야별 예시와 함께 설명해주세요",
            "일상적 표현을 학술적 표현으로 전환하는 구체적인 전략과 단계별 접근법을 제시해주세요",
            "학술 언어의 특성(객관성, 정밀성, 형식성 등)을 구체적인 예시와 함께 설명해주세요",
            "분야별(인문학, 사회과학, 자연과학 등) 학술적 문체의 특징과 차이점을 비교해주세요",
            "일상 표현→학술 표현 전환 예시 표를 최소 10개 제공해주세요"
        ])
        
    elif "인용" in topic:
        builder.add_role(
            "학술 인용 전문가", 
            "연구 방법론과 학술 출판 분야의 전문가로, 다양한 인용 스타일과 참고문헌 관리 시스템에 정통한 학술 사서"
        )
        
        builder.add_context(
            f"저는 학부생으로 {topic}에 대해 체계적으로 배우고 싶습니다. "
            f"다양한 인용 스타일(APA, MLA, Chicago 등)의 차이점과 적절한 사용법, "
            f"효율적인 참고문헌 관리 방법에 대한 실용적인 가이드가 필요합니다."
        )
        
        builder.add_instructions([
            "주요 인용 스타일(APA, MLA, Chicago, Vancouver, IEEE)의 기본 규칙과 형식을 비교해주세요",
            "다양한 출처 유형(저널 논문, 책, 웹사이트, 학위논문 등)의 인용 방법을 예시와 함께 제시해주세요",
            "직접 인용, 간접 인용, 요약 인용 등 다양한 인용 유형의 적절한 사용법을 설명해주세요",
            "참고문헌 관리 도구(Zotero, Mendeley, EndNote 등)의 특징과 효과적인 활용법을 안내해주세요",
            "학술 글쓰기에서 인용의 전략적 배치와 효과적인 통합 방법을 구체적으로 설명해주세요"
        ])
        
    elif "AI 활용" in topic:
        builder.add_role(
            "연구 윤리 전문가", 
            "AI와 학술 글쓰기의 윤리적 측면을 연구하는 전문가로, 표절 예방과 학문적 진정성 유지에 관한 지침을 개발하는 윤리 위원회 자문위원"
        )
        
        builder.add_context(
            f"저는 연구자로서 {topic}에 관심이 있습니다. "
            f"AI 도구(예: 대규모 언어 모델)를 학술 글쓰기에 활용하면서 "
            f"표절 위험을 방지하고 학문적 진정성을 유지하는 방법에 대한 실질적인 지침이 필요합니다."
        )
        
        builder.add_instructions([
            "AI를 활용한 학술 글쓰기의 윤리적 스펙트럼과 경계선을 명확히 설명해주세요",
            "AI 생성 콘텐츠와 관련된 다양한 유형의 표절 위험과 해결 전략을 제시해주세요",
            "AI 기여를 적절히 인정하고 표기하는 방법(인용 형식, 감사의 글 등)을 구체적으로 안내해주세요",
            "AI와 효과적으로 협업하면서 학문적 진정성을 유지하는 단계별 프로세스를 설명해주세요",
            "AI 활용의 투명성을 높이고 비판적 검토를 강화하는 구체적인 프롬프팅 전략을 제안해주세요"
        ])
        
    elif "학술 논문" in topic:
        builder.add_role(
            "학술 논문 전문가", 
            "다양한 학술지의 편집위원으로 활동하는 연구 방법론 교수로, 효과적인 학술 논문 작성법과 출판 전략에 정통한 전문가"
        )
        
        builder.add_context(
            f"저는 대학원생으로 첫 학술 논문을 준비 중입니다. {topic}에 대한 체계적인 이해가 필요합니다. "
            f"논문의 각 섹션별 학술적 표현과 구조, 효과적인 논증 전개 방법, "
            f"투고 준비를 위한 실질적인 조언이 담긴 가이드가 필요합니다."
        )
        
        builder.add_instructions([
            "학술 논문의 표준 구조(서론, 방법론, 결과, 논의 등)와 각 섹션별 핵심 요소를 설명해주세요",
            "각 섹션에 적합한 학술적 표현과 문체, 시제 사용에 관한 구체적인 지침을 제공해주세요",
            "효과적인 논증 구성과 비판적 분석을 위한 학술적 표현과 전략을 제시해주세요",
            "논문 초록, 키워드, 제목 작성을 위한 최적의 접근법과 예시를 포함해주세요",
            "학술지 투고 준비와 심사 과정에서의 학술적 커뮤니케이션 방법을 안내해주세요"
        ])
        
    else:  # 연구 윤리
        builder.add_role(
            "연구 윤리 전문가", 
            "학술 기관의 연구 윤리 위원회 책임자로, 학문적 진정성과 연구 윤리 교육을 담당하는 전문가"
        )
        
        builder.add_context(
            f"저는 연구자로서 {topic}에 대한 이해를 높이고 싶습니다. "
            f"학술 연구와 글쓰기에서 지켜야 할 윤리적 원칙과 가이드라인, "
            f"흔히 발생하는 윤리적 문제와 예방 전략에 관한 체계적인 체크리스트가 필요합니다."
        )
        
        builder.add_instructions([
            "학문적 진정성의 핵심 원칙과 연구 윤리의 중요성을 구체적인 사례와 함께 설명해주세요",
            "표절, 데이터 조작, 부적절한 인용 등 주요 연구 윤리 위반 유형과 예방 전략을 제시해주세요",
            "공동 연구와 저자 표시에 관련된 윤리적 고려사항과 모범 사례를 안내해주세요",
            "디지털 시대의 새로운 윤리적 도전(AI 활용, 온라인 자료 인용 등)과 대응 방안을 설명해주세요",
            "연구 계획부터 출판까지 각 단계별 윤리적 고려사항을 포함한 체크리스트를 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"학술적 표현과 용어를 적절히 사용하여 내용의 전문성을 보여주세요. "
        f"구체적인 예시와 비교 표, 체크리스트 등 실용적인 요소를 포함해주세요. "
        f"본문 내 인용이 필요한 경우 일관된 인용 스타일을 사용하고, 참고문헌 목록을 포함해주세요. "
        f"내용은 학문적 정확성과 실용성의 균형을 유지하며, 초보자도 이해할 수 있도록 명확하게 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="학술적 표현과 인용",
        topic_options=ACADEMIC_WRITING_TOPICS,
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
