"""
프롬프트 버전 관리와 개선 기록 실습 모듈

Part 3 - 섹션 3.3.3 실습 코드: 프롬프트의 반복적 개선을 체계적으로 
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
VERSION_MANAGEMENT_TOPICS = {
    "1": {"name": "버전 관리 방법", "topic": "프롬프트 버전을 효과적으로 관리하는 접근법과 도구", "output_format": "관리 가이드"},
    "2": {"name": "변경 추적", "topic": "프롬프트 변경 사항과 개선 과정을 체계적으로 추적하는 방법", "output_format": "추적 시스템"},
    "3": {"name": "A/B 테스트", "topic": "프롬프트 변형을 설계하고 테스트하는 체계적인 방법", "output_format": "테스트 프레임워크"},
    "4": {"name": "개선 프로세스", "topic": "프롬프트를 단계적으로 개선하는 체계적인 프로세스", "output_format": "개선 가이드"},
    "5": {"name": "협업적 관리", "topic": "팀 환경에서 프롬프트 버전을 협업적으로 관리하는 방법", "output_format": "협업 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 프롬프트 버전 관리와 개선 추적의 필요성과 목표 설정",
        "구체적 요청: 체계적인 버전 관리와 개선 프로세스에 대한 상세 지침 요청",
        "맞춤화 요소: 개인/팀 환경과 프롬프트 복잡성에 맞는 접근법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 버전 관리는 프롬프트의 발전 과정을 추적하고 필요할 때 이전 버전으로 되돌릴 수 있게 합니다",
    "변경 사항과 개선 근거를 명확히 문서화하면 프롬프트 개발의 학습 효과가 극대화됩니다",
    "A/B 테스트를 통한 체계적인 비교는 프롬프트 성능 향상의 핵심 전략입니다",
    "단계적인 개선 프로세스를 따르면 프롬프트의 품질과 효과성을 지속적으로 향상시킬 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "버전 관리 전문가", 
        "복잡한 콘텐츠의 버전을 체계적으로 관리하고 반복적 개선 과정을 효과적으로 추적하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"AI 프롬프트를 개발하고 지속적으로 개선하면서, 이 과정을 체계적으로 "
        f"추적하고 관리하는 효과적인 시스템이 필요합니다. "
        f"프롬프트의 다양한, 버전 변경 사항, 성능 변화 등을 명확히 기록하고, "
        f"개선 과정에서 얻은 통찰을 활용하고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "버전 관리 방법" in topic:
        builder.add_instructions([
            "프롬프트 버전을 효과적으로 관리하는 다양한 접근법과 도구를 비교 분석해주세요",
            "직접 포함형, 파일명 기반, 폴더 구조 기반, 버전 관리 시스템, 데이터베이스 기반 등 다양한 방법의 장단점을 설명해주세요",
            "개인 사용자에게 적합한 간단하면서도 효과적인 버전 관리 시스템을 제안해주세요",
            "프롬프트 버전 관리의 핵심 원칙과 모범 사례를 설명해주세요",
            "다양한 복잡도와 용도의 프롬프트에 맞는 버전 관리 전략도 포함해주세요"
        ])
    elif "변경 추적" in topic:
        builder.add_instructions([
            "프롬프트 변경 사항과 개선 과정을 체계적으로 추적하는 방법을 설명해주세요",
            "효과적인 변경 로그 템플릿과 변경 사항을 기록하는 구조화된 접근법을 제안해주세요",
            "변경의 근거, 영향, 성과를 포괄적으로 문서화하는 방법을 설명해주세요",
            "프롬프트 버전 간의 차이를 명확히 비교하고 시각화하는 기법을 제시해주세요",
            "변경 추적을 일상적인 프롬프트 개발 워크플로우에 통합하는 방법도 포함해주세요"
        ])
    elif "A/B 테스트" in topic:
        builder.add_instructions([
            "프롬프트 변형을 체계적으로 설계하고 테스트하는 A/B 테스트 방법론을 설명해주세요",
            "효과적인 A/B 테스트를 위한 프레임워크와 단계별 프로세스를 제안해주세요",
            "프롬프트 변형을 평가하기 위한 객관적인 기준과 지표를 설명해주세요",
            "테스트 결과를 기록하고 분석하는 구조화된 접근법을 제시해주세요",
            "A/B 테스트에서 얻은 통찰을 프롬프트 개선에 반영하는 방법도 포함해주세요"
        ])
    elif "개선 프로세스" in topic:
        builder.add_instructions([
            "프롬프트를 단계적으로 개선하는 체계적인 IMPROVE 프로세스를 상세히 설명해주세요",
            "기준 설정, 전략적 수정, 변형 생성, 성능 검토, 추가 최적화, 철저한 검증, 새 버전 확립의 각 단계를 구체적으로 안내해주세요",
            "각 개선 단계에서 고려해야 할 핵심 질문과 체크포인트를 제시해주세요",
            "프롬프트 개선 과정에서 흔히 발생하는 함정과 이를 피하는 방법을 설명해주세요",
            "개선 프로세스의 반복 주기와 지속 가능한 개선 시스템 구축 방법도 포함해주세요"
        ])
    elif "협업적 관리" in topic:
        builder.add_instructions([
            "팀 환경에서 프롬프트 버전을 협업적으로 관리하는 방법을 설명해주세요",
            "여러 사람이 함께 프롬프트를 개발하고 개선할 때 효과적인 워크플로우와 역할 분담을 제안해주세요",
            "변경 충돌을 방지하고 일관성을 유지하는 협업 프로토콜을 설명해주세요",
            "팀 프롬프트 라이브러리의 품질과 표준을 관리하는 거버넌스 구조를 제시해주세요",
            "협업 도구와 플랫폼을 활용한 효율적인 관리 시스템도 포함해주세요"
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
        f"실제 사용 가능한 템플릿과 예시를 코드 블록으로 제시해주세요. "
        f"프로세스와 워크플로우는 시각적 다이어그램이나 단계별 목록으로 설명해주세요. "
        f"비교 분석이 필요한 부분은 표 형식으로 명확하게 보여주세요. "
        f"모든 내용은 대학생이 프롬프트 버전 관리와 개선을 시작하는 데 바로 적용할 수 있도록 "
        f"실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="프롬프트 버전 관리와 반복 개선 기록",
        topic_options=VERSION_MANAGEMENT_TOPICS,
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
