"""
프로젝트 진행 추적 및 관리 실습 모듈

Part 3 - 섹션 3.4.2 실습 코드: 장기 프로젝트의 진행 상황을 효과적으로
추적하고 관리하는 방법을 학습합니다.
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
PROGRESS_TRACKING_TOPICS = {
    "1": {"name": "추적 프레임워크", "topic": "장기 프로젝트 진행을 체계적으로 추적하는 TRACKS 프레임워크", "output_format": "프레임워크 가이드"},
    "2": {"name": "추적 도구", "topic": "다양한 프로젝트 추적 도구와 템플릿 및 그 활용법", "output_format": "도구 가이드"},
    "3": {"name": "결정 관리", "topic": "프로젝트 결정사항 기록 및 추적 시스템", "output_format": "결정 관리 시스템"},
    "4": {"name": "변화 관리", "topic": "프로젝트 변경사항 식별 및 관리 전략", "output_format": "변화 관리 가이드"},
    "5": {"name": "일상적 추적", "topic": "일상 워크플로우에 통합된 프로젝트 진행 추적 습관", "output_format": "습관 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프로젝트 진행 추적의 필요성과 목표 설정",
        "구체적 요청: 체계적인 추적 방법론과 실용적인 도구 요청",
        "맞춤화 요소: 개인 환경에 적합한 추적 시스템과 관행 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 진행 추적은 장기 프로젝트의 방향성과 진행 상황 파악에 필수적입니다",
    "다양한 추적 도구와 템플릿은 프로젝트 유형과 복잡성에 맞게 선택해야 합니다",
    "결정사항과 변화를 효과적으로 문서화하는 것은 프로젝트 일관성 유지에 중요합니다",
    "일상 워크플로우에 통합된 간결한 추적 습관이 지속 가능한 관리를 가능하게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프로젝트 추적 전문가", 
        "복잡한 장기 프로젝트의 진행 상황을 효과적으로 추적하고 관리하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI를 활용한 장기 프로젝트를 진행하면서 효과적으로 진행 상황을 추적하고, "
        f"중요한 결정사항과 변화를 관리하고, 일관성을 유지하는 방법을 배우고 싶습니다. "
        f"특히 개인 프로젝트 환경에서 관리 오버헤드를 최소화하면서도 "
        f"프로젝트를 효과적으로 관리할 수 있는 실용적인 접근법이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "추적 프레임워크" in topic:
        builder.add_instructions([
            "장기 프로젝트 진행을 체계적으로 추적하는 TRACKS 프레임워크를 상세히 설명해주세요",
            "프레임워크의 각 구성 요소(Track progress, Record decisions, Adapt to changes, Capture insights, Keep focus, Synchronize components)를 구체적으로 설명해주세요",
            "TRACKS 프레임워크를 개인 프로젝트에 적용하는 방법과 단계별 구현 전략을 제안해주세요",
            "복잡성과 목적에 따라 프레임워크를 조정하는 방법을 설명해주세요",
            "프레임워크 적용의 실제 예시와 사례 연구도 포함해주세요"
        ])
    elif "추적 도구" in topic:
        builder.add_instructions([
            "다양한 프로젝트 추적 도구와 템플릿 및 그 효과적인 활용법을 설명해주세요",
            "칸반 보드, 진행 로그, 마일스톤 차트 등 다양한 추적 도구의 장단점과 적합한 사용 상황을 비교해주세요",
            "각 도구의 구체적인 템플릿과 설정 방법을 상세히 안내해주세요",
            "디지털 도구와 아날로그 방식의 장단점을 비교하고 개인 프로젝트에 적합한 접근법을 제안해주세요",
            "최소한의 설정으로 최대 효과를 낼 수 있는 효율적인 도구 활용 전략도 포함해주세요"
        ])
    elif "결정 관리" in topic:
        builder.add_instructions([
            "프로젝트 진행 중 내리는 중요 결정사항을 효과적으로 기록하고 추적하는 시스템을 설명해주세요",
            "결정 로그의 구조와 핵심 구성 요소(결정 내용, 근거, 시점, 영향, 대안 등)를 상세히 설명해주세요",
            "결정 기록을 위한 효과적인 템플릿과 포맷을 제안해주세요",
            "결정사항을 검색하고 참조하기 쉽게 조직화하는 방법을 설명해주세요",
            "과거 결정을 검토하고 필요시 재평가하는 프로세스도 포함해주세요"
        ])
    elif "변화 관리" in topic:
        builder.add_instructions([
            "프로젝트 진행 중 발생하는 변경사항을 식별하고 효과적으로 관리하는 전략을 설명해주세요",
            "다양한 유형의 변화(범위, 일정, 접근법, 요구사항 등)와 그 영향을 분석하는 방법을 설명해주세요",
            "변화 요청과 결정을 평가하고 처리하는 구조화된 프로세스를 제안해주세요",
            "변화가 프로젝트의 다른 측면에 미치는 영향을 추적하고 관리하는 방법을 설명해주세요",
            "변화 관리를 위한 실용적인 템플릿과 체크리스트도 포함해주세요"
        ])
    elif "일상적 추적" in topic:
        builder.add_instructions([
            "일상 워크플로우에 자연스럽게 통합할 수 있는 프로젝트 진행 추적 습관을 설명해주세요",
            "프로젝트 작업 세션 전, 중, 후에 적용할 수 있는 간결하고 효과적인 추적 루틴을 제안해주세요",
            "최소한의 시간과 노력으로 일관된 추적을 유지하는 전략과 팁을 제공해주세요",
            "추적 습관을 장기적으로 유지하기 위한 동기부여 전략과 기법을 설명해주세요",
            "다양한 학습/작업 환경에 맞춰 조정할 수 있는 유연한 추적 관행도 포함해주세요"
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
        f"모든 내용은 대학생이 개인 프로젝트의 진행 상황을 추적하는 데 바로 적용할 수 있도록 "
        f"실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프로젝트 진행 추적 및 관리",
        topic_options=PROGRESS_TRACKING_TOPICS,
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
