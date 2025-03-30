"""
장기 프로젝트 관리 실습 모듈

Part 3 - 섹션 3.4 실습 코드: 장기적인 AI 프로젝트의 일관성을 유지하고
효과적으로 관리하는 방법을 학습합니다.
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
PROJECT_MANAGEMENT_TOPICS = {
    "1": {"name": "프로젝트 계획", "topic": "효과적인 장기 프로젝트 계획 및 구조화 방법", "output_format": "계획 가이드"},
    "2": {"name": "진행 추적", "topic": "장기 프로젝트 진행 상황 추적 및 관리 시스템", "output_format": "추적 시스템"},
    "3": {"name": "맥락 관리", "topic": "여러 대화 세션에 걸친 장기 프로젝트 맥락 관리 전략", "output_format": "맥락 가이드"},
    "4": {"name": "프로젝트 유형별", "topic": "다양한 프로젝트 유형별 맞춤형 관리 전략", "output_format": "전략 가이드"},
    "5": {"name": "통합 접근법", "topic": "장기 프로젝트 성공을 위한 통합적 관리 프레임워크", "output_format": "프레임워크 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 장기 프로젝트 관리의 목표와 필요성 설정",
        "구체적 요청: 체계적인 관리 방법과 실용적인 도구 요청",
        "맞춤화 요소: 프로젝트 유형과 환경에 맞는 접근법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 계획과 구조화는 장기 프로젝트의 일관성과 성공 가능성을 크게 높입니다",
    "진행 상황을 효과적으로 추적하고 문서화하는 것은 복잡한 프로젝트 관리의 핵심입니다",
    "대화 세션 간의 맥락 연속성 유지는 AI를 활용한 장기 프로젝트의 중요 과제입니다",
    "프로젝트 유형과 목적에 맞는 맞춤형 관리 전략이 최적의 결과를 가져옵니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프로젝트 관리 전문가", 
        "복잡하고 장기적인 프로젝트를 체계적으로 계획하고 효과적으로 관리하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI를 활용한 장기 프로젝트(연구, 창작, 개발 등)를 진행하면서 "
        f"일관성을 유지하고 효율적으로 관리하는 방법을 배우고 싶습니다. "
        f"특히 여러 대화 세션에 걸쳐 맥락을 유지하고, 진행 상황을 추적하며, "
        f"프로젝트를 성공적으로 완료하기 위한 체계적인 접근법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "프로젝트 계획" in topic:
        builder.add_instructions([
            "장기 프로젝트를 효과적으로 계획하고 구조화하는 방법을 설명해주세요",
            "명확한 목표 설정, 범위 정의, 모듈화 접근법 등 핵심 계획 원칙을 설명해주세요",
            "장기 프로젝트를 관리 가능한 단계와 구성 요소로 분해하는 전략을 제안해주세요",
            "현실적인 타임라인과 마일스톤을 개발하는 방법을 설명해주세요",
            "프로젝트 청사진 템플릿과 구체적인 예시도 포함해주세요"
        ])
    elif "진행 추적" in topic:
        builder.add_instructions([
            "장기 프로젝트의 진행 상황을 효과적으로 추적하고 관리하는 시스템을 설명해주세요",
            "TRACKS 프레임워크와 같은 체계적인 프로젝트 추적 방법론을 상세히 설명해주세요",
            "진행 상황, 결정사항, 통찰 등을 효과적으로 기록하고 문서화하는 템플릿과 도구를 제안해주세요",
            "칸반 보드, 진행 로그, 마일스톤 차트 등 다양한 추적 도구의 장단점과 활용법을 설명해주세요",
            "관리 오버헤드를 최소화하면서도 효과적인 추적을 가능하게 하는 균형 잡힌 접근법도 포함해주세요"
        ])
    elif "맥락 관리" in topic:
        builder.add_instructions([
            "여러 대화 세션에 걸쳐 프로젝트 맥락의 연속성을 유지하는 효과적인 전략을 설명해주세요",
            "다양한 맥락 브리지 전략과 그 적용 방법을 상세히 설명해주세요",
            "프로젝트 메모리 문서를 설계하고 관리하는 방법을 제안해주세요",
            "ID 기반 참조, 태그 시스템, 앵커 포인트 등 효과적인 참조 시스템을 설명해주세요",
            "세션 시작/종료 루틴 등 일상적인 맥락 관리 관행도 포함해주세요"
        ])
    elif "프로젝트 유형별" in topic:
        builder.add_instructions([
            "다양한 유형의 장기 프로젝트에 최적화된 관리 전략과 접근법을 설명해주세요",
            "연구, 창작, 소프트웨어/기술 개발, 교육/학습 등 다양한 프로젝트 유형별 특성과 관리 요소를 비교해주세요",
            "각 프로젝트 유형에 적합한 구조, 단계, 추적 방법을 제안해주세요",
            "특정 유형의 프로젝트에서 흔히 발생하는 도전 과제와 그 해결 전략을 설명해주세요",
            "다양한 프로젝트 유형별 실제 적용 사례와 템플릿도 포함해주세요"
        ])
    elif "통합 접근법" in topic:
        builder.add_instructions([
            "장기 프로젝트의 효과적인 관리를 위한 종합적인 프레임워크와 통합 접근법을 설명해주세요",
            "PROJECT 프레임워크와 같은 통합 관리 시스템의 각 요소와 적용 방법을 상세히 설명해주세요",
            "일상적인 프로젝트 관리 관행과 효과적인 루틴을 제안해주세요",
            "다양한 디지털 도구와 시스템을 활용하여 통합 관리 접근법을 구현하는 방법을 설명해주세요",
            "장기 프로젝트 관리의 성공 요인과 일반적인 함정 및 그 극복 전략도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "기본 원칙과 모범 사례를 명확하게 설명해주세요",
            "다양한 상황과 요구에 맞게 조정할 수 있는 유연한 프레임워크를 제공해주세요",
            "초보자도 쉽게 시작할 수 있는 단계별 가이드를 포함해주세요",
            "구체적인 예시와 템플릿으로 실용적인 적용을 지원해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 템플릿과 예시는 코드 블록으로 제시해주세요. "
        f"프로세스와 워크플로우는 시각적 다이어그램이나 단계별 목록으로 설명해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"모든 내용은 대학생이 AI를 활용한 장기 프로젝트를 관리하는 데 바로 적용할 수 있도록 "
        f"실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="장기 프로젝트 관리하기",
        topic_options=PROJECT_MANAGEMENT_TOPICS,
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
