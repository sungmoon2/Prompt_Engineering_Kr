"""
학기 프로젝트 관리 실습 모듈

Part 3 - 섹션 3.4.1 실습 코드: 장기 학기 프로젝트에서 대화 맥락을 효과적으로 
관리하고 유지하는 방법을 학습합니다.
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
SEMESTER_PROJECT_TOPICS = {
    "1": {"name": "프로젝트 계획", "topic": "학기 프로젝트를 위한 AI 지원 계획 및 초기 설정", "output_format": "프로젝트 계획서"},
    "2": {"name": "맥락 관리", "topic": "학기 프로젝트의 장기적 대화 맥락 유지 전략", "output_format": "맥락 관리 가이드"},
    "3": {"name": "진행 추적", "topic": "학기 프로젝트 진행 상황을 효과적으로 추적하는 방법", "output_format": "진행 추적 시스템"},
    "4": {"name": "지식 통합", "topic": "학기 프로젝트에서 수집한 정보와 통찰을 통합하는 방법", "output_format": "지식 통합 프레임워크"},
    "5": {"name": "피드백 관리", "topic": "학기 프로젝트에서 받은 피드백을 효과적으로 관리하고 반영하는 전략", "output_format": "피드백 관리 시스템"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "목적 명시: 학기 프로젝트 관리 목표와 활용 상황 설정",
        "구체적 요청: 체계적인 관리 방법과 실용적 전략 요청",
        "맞춤화 요소: 대학생 상황과 학업 환경에 맞는 접근법 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "장기 학기 프로젝트는 AI와의 대화 맥락 관리를 위한 체계적인 접근이 필요합니다",
    "효과적인 초기 설정과 프로젝트 계획은 장기적인 맥락 유지의 기반을 마련합니다",
    "정기적인 요약과 진행 상황 추적이 장기 프로젝트의 일관성을 유지하는 핵심입니다",
    "학기 프로젝트 관리를 위한 템플릿과 구조화된 접근법은 시간과 노력을 절약합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학업 프로젝트 관리 전문가", 
        "복잡하고 장기적인 학업 프로젝트를 체계적으로 관리하고 AI를 효과적으로 활용하여 성공적으로 완수하는 방법을 가르치는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"이번 학기에 중요한 연구 프로젝트를 진행 중이며, AI를 활용하여 정보 수집, 분석, 아이디어 발전 등을 효과적으로 "
        f"지원받고 싶습니다. 특히 프로젝트가 몇 개월에 걸쳐 진행되기 때문에 AI와의 대화 맥락을 효과적으로 유지하고 "
        f"관리하는 방법이 필요합니다. 시간이 지나도 일관된 방향성을 유지하고 이전 작업과 연결성을 확보하고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "프로젝트 계획" in topic:
        builder.add_instructions([
            "학기 프로젝트를 위한 AI 지원 계획의 핵심 구성 요소와 초기 설정 방법을 설명해주세요",
            "프로젝트의 목표, 범위, 주요 단계를 AI와 함께 정의하는 효과적인 방법을 제안해주세요",
            "장기 대화 맥락 관리를 위한 초기 구조와 템플릿을 설계하는 방법을 설명해주세요",
            "프로젝트 전반에 걸쳐 AI를 효과적으로 활용할 수 있는 영역과 전략을 제시해주세요",
            "학기 초에 수립해야 할 프로젝트 관리 습관과 루틴을 제안해주세요"
        ])
    elif "맥락 관리" in topic:
        builder.add_instructions([
            "학기 프로젝트를 위한 장기적 대화 맥락을 효과적으로 유지하는 방법을 설명해주세요",
            "세션 간 연속성을 보장하는 효과적인 요약과 참조 전략을 제안해주세요",
            "시간이 지남에 따라 맥락이 손실되는 것을 방지하는 구조적 접근법을 설명해주세요",
            "중요한 결정, 통찰, 진행 방향을 효과적으로 기록하고 추적하는 방법을 제시해주세요",
            "학기 중간에 방향이 변경되거나 새로운 정보가 추가될 때 맥락을 조정하는 전략도 포함해주세요"
        ])
    elif "진행 추적" in topic:
        builder.add_instructions([
            "학기 프로젝트의 진행 상황을 효과적으로 추적하는 체계적인 방법을 설명해주세요",
            "목표 대비 진행 상황을 시각화하고 모니터링하는 도구와 전략을 제안해주세요",
            "주간/월간 진행 상황 검토 및 업데이트 프로세스를 설계하는 방법을 설명해주세요",
            "진행 상황 정보를 AI와의 대화에 효과적으로 통합하는 전략을 제시해주세요",
            "병목 현상이나 지연 발생 시 적시에 파악하고 대응하는 방법도 포함해주세요"
        ])
    elif "지식 통합" in topic:
        builder.add_instructions([
            "학기 프로젝트에서 수집한 다양한 정보와 통찰을 효과적으로 통합하는 방법을 설명해주세요",
            "AI와의 여러 대화에서 얻은 정보를 구조화하고 연결하는 전략을 제안해주세요",
            "다양한 소스의 정보를 일관된 지식 베이스로 구축하는 단계별 접근법을 설명해주세요",
            "지식 간의 관계와 패턴을 발견하고 시각화하는 방법을 제시해주세요",
            "프로젝트 종료 시 완성된 지식 베이스를 최종 결과물에 효과적으로 활용하는 방법도 포함해주세요"
        ])
    elif "피드백 관리" in topic:
        builder.add_instructions([
            "학기 프로젝트에서 교수, 동료, AI 등 다양한 소스에서 받은 피드백을 효과적으로 관리하는 방법을 설명해주세요",
            "피드백 수집, 기록, 우선순위 지정을 위한 체계적인 접근법을 제안해주세요",
            "상충되는 피드백을 조정하고 관리하는 전략을 설명해주세요",
            "피드백을 AI와의 대화에 효과적으로 통합하여 개선된 결과를 얻는 방법을 제시해주세요",
            "피드백 기반 개선 사항을 추적하고 그 효과를 평가하는 방법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 대한 체계적이고 실용적인 접근법을 설명해주세요",
            "학기 프로젝트의 특성과 도전 과제를 고려한 맞춤형 전략을 제안해주세요",
            "대학생의 실제 상황과 제약 조건에 맞는 실용적인 방법을 제시해주세요",
            "시간이 제한된 학생도 효과적으로 적용할 수 있는 효율적 접근법을 포함해주세요",
            "구체적인 예시와 템플릿으로 실용적인 적용을 지원해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 사용 가능한 템플릿과 예시는 코드 블록으로 제시해주세요. "
        f"프로세스와 워크플로우는 단계별 목록이나 다이어그램으로 설명해주세요. "
        f"학생이 바로 적용할 수 있는 구체적인 전략과 실용적인 팁을 강조해주세요. "
        f"모든 내용은 대학생이 학기 프로젝트에 바로 적용할 수 있도록 실용적이고 구체적으로 작성해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="학기 프로젝트 관리",
        topic_options=SEMESTER_PROJECT_TOPICS,
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
