"""
문제 해결 과정 시각화 요청 방법 실습 모듈

Part 7 - 섹션 7.2.3 실습 코드: 복잡한 문제 해결 과정을 다양한 형태로 시각화하는 효과적인 
프롬프트 작성 방법을 학습합니다.
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
VISUALIZATION_TOPICS = {
    "1": {"name": "알고리즘 시각화", "topic": "이진 탐색 알고리즘의 단계별 시각화", "output_format": "플로우차트"},
    "2": {"name": "프로젝트 계획", "topic": "웹 개발 프로젝트 일정 및 의존성 시각화", "output_format": "간트 차트"},
    "3": {"name": "개념 관계도", "topic": "프롬프트 엔지니어링 핵심 개념 관계 시각화", "output_format": "개념도"},
    "4": {"name": "의사결정 과정", "topic": "복잡한 연구 주제 선정 과정 시각화", "output_format": "의사결정 트리"},
    "5": {"name": "문제 분해", "topic": "학술 논문 작성 과정의 체계적 분해 시각화", "output_format": "계층적 분해 다이어그램"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["시각화에 대한 일반적인 요청"],
    "enhanced": [
        "시각화 목적 명시: 시각화를 통해 달성하려는 구체적 목표 설정",
        "형식 및 요소 세부 지정: 원하는 시각화 유형과 포함될 핵심 요소 명시",
        "기술적 형식 지정: Mermaid, 마크다운 표 등 구체적인 출력 형식 요청",
        "시각적 속성 요청: 강조, 그룹화, 관계 표현 방식 등 세부 속성 지정"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "복잡한 문제 해결 과정은 시각화를 통해 더 명확하게 이해할 수 있습니다",
    "목적에 맞는 적절한 시각화 유형을 선택하는 것이 중요합니다",
    "구체적인 시각화 요소를 프롬프트에 명시하면 더 유용한 결과를 얻을 수 있습니다",
    "시각화 결과는 반복적인 피드백을 통해 지속적으로 개선할 수 있습니다",
    "효과적인 시각화는 복잡한 문제의 패턴과 구조를 발견하는 데 도움이 됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대한 시각화를 만들어주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "시각화 전문가", 
        "복잡한 개념, 프로세스, 데이터를 명확하고 효과적으로 시각화하는 전문가로, 다양한 시각화 기법을 통해 이해하기 어려운 문제를 직관적으로 표현하는 능력을 갖추고 있습니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 대한 시각화를 만들고자 합니다. "
        f"이 시각화는 {purpose}의 일부로 사용될 예정이며, {output_format} 형태로 표현하고 싶습니다. "
        f"복잡한 과정이나 관계를 명확하게 이해하고 다른 사람들과 효과적으로 공유할 수 있는 "
        f"시각적 표현이 필요합니다."
    )
    
    # 주제별 맞춤 지시사항 추가
    if "이진 탐색" in topic:
        builder.add_instructions([
            "이진 탐색 알고리즘의 단계별 실행 과정을 플로우차트로 시각화해주세요",
            "입력 배열, 중간값 선택, 비교 연산, 탐색 범위 조정 등의 핵심 단계를 포함해주세요",
            "각 단계에서의 배열 상태와 탐색 범위 변화를 명확히 표시해주세요",
            "성공 및 실패 종료 조건을 포함한 전체 프로세스를 보여주세요",
            "알고리즘의 시간 복잡도가 어떻게 O(log n)이 되는지 시각적으로 표현해주세요"
        ])
        
        builder.add_format_instructions(
            "Mermaid 문법을 사용하여 플로우차트를 작성해주세요. "
            "flowchart TD 형식을 사용하고, 다음 요소를 포함해주세요:\n"
            "1. 각 노드는 의미 있는 ID와 설명 텍스트 포함\n"
            "2. 의사결정 노드는 다이아몬드 형태로 표현\n"
            "3. 프로세스 노드는 직사각형으로 표현\n"
            "4. 시작과 종료는 원형이나 둥근 직사각형으로 표현\n"
            "5. 화살표에는 조건이나 설명 추가\n"
            "6. 가능하면 단계별로 색상 구분하거나 스타일 적용\n\n"
            "예시 배열 [1, 3, 5, 7, 9, 11, 13, 15]에서 값 7을 찾는 과정을 구체적인 예시로 포함해주세요."
        )
        
    elif "웹 개발 프로젝트" in topic:
        builder.add_instructions([
            "웹 개발 프로젝트의 주요 단계와 일정을 간트 차트로 시각화해주세요",
            "기획, 디자인, 프론트엔드 개발, 백엔드 개발, 테스트, 배포 등 핵심 단계를 포함해주세요",
            "각 작업의 예상 기간과 시작/종료 날짜를 명확히 표시해주세요",
            "작업 간 의존성과 병렬 진행 가능한 작업을 시각적으로 표현해주세요",
            "중요 마일스톤과 납기일을 강조해주세요"
        ])
        
        builder.add_format_instructions(
            "Mermaid 문법을 사용하여 간트 차트를 작성해주세요. "
            "gantt 형식을 사용하고, 다음 요소를 포함해주세요:\n"
            "1. 프로젝트 제목과 날짜 형식 지정\n"
            "2. 섹션별로 관련 작업 그룹화\n"
            "3. 각 작업의 ID, 설명, 기간 명시\n"
            "4. 작업 간 의존성 표시 (after 키워드 사용)\n"
            "5. 중요 마일스톤 표시\n"
            "6. 가능한 경우 색상 코드 활용\n\n"
            "3개월(12주) 기간의 웹 개발 프로젝트를 가정하고, 주 단위로 일정을 계획해주세요."
        )
        
    elif "프롬프트 엔지니어링" in topic:
        builder.add_instructions([
            "프롬프트 엔지니어링의 핵심 개념과 그 관계를 개념도로 시각화해주세요",
            "주요 기법(역할 기반, 단계적 사고, 형식 지정 등)과 그 목적을 표현해주세요",
            "각 개념 간의 관계와 상호작용을 명확하게 표시해주세요",
            "초보자부터 전문가까지의 발전 경로를 보여주는 구조로 구성해주세요",
            "프롬프트 엔지니어링의 응용 영역과 효과도 포함해주세요"
        ])
        
        builder.add_format_instructions(
            "Mermaid 문법을 사용하여 개념도를 작성해주세요. "
            "flowchart LR 또는 mindmap 형식을 사용하고, 다음 요소를 포함해주세요:\n"
            "1. 핵심 개념은 명확한 노드로 표현\n"
            "2. 개념 간 관계는 연결선과 설명 라벨로 표시\n"
            "3. 관련 개념은 시각적으로 그룹화\n"
            "4. 계층 구조나 중요도를 크기나 색상으로 구분\n"
            "5. 주요 카테고리별 구분\n\n"
            "프롬프트 엔지니어링을 처음 접하는 사람도 전체 구조를 이해할 수 있도록 명확하게 표현해주세요."
        )
        
    elif "연구 주제 선정" in topic:
        builder.add_instructions([
            "복잡한 연구 주제 선정 과정을 의사결정 트리로 시각화해주세요",
            "연구 관심사 정의, 문헌 검토, 연구 질문 형성, 방법론 선택 등의 주요 결정 지점을 포함해주세요",
            "각 의사결정 지점에서의 선택지와 그에 따른 경로를 명확히 표시해주세요",
            "결정에 영향을 미치는 주요 요인과 고려사항을 포함해주세요",
            "가능한 연구 주제의 최종 결과와 그 특성을 시각화해주세요"
        ])
        
        builder.add_format_instructions(
            "Mermaid 문법을 사용하여 의사결정 트리를 작성해주세요. "
            "flowchart TD 형식을 사용하고, 다음 요소를 포함해주세요:\n"
            "1. 의사결정 지점은 다이아몬드 형태로 표현\n"
            "2. 각 선택지는 명확한 라벨이 있는 화살표로 표시\n"
            "3. 결정 경로에 따른 후속 단계나 결과를 노드로 표현\n"
            "4. 주요 결정 기준이나 고려사항을 노트로 추가\n"
            "5. 최종 연구 주제 유형이나 결과를 말단 노드로 표시\n\n"
            "사회과학 분야의 연구 주제 선정 과정을 예시로 사용하여 시각화해주세요."
        )
        
    elif "학술 논문 작성" in topic:
        builder.add_instructions([
            "학술 논문 작성 과정을 체계적으로 분해한 계층적 다이어그램을 만들어주세요",
            "연구 계획, 문헌 검토, 방법론 설계, 데이터 수집/분석, 논문 작성, 검토/수정 등 주요 단계를 포함해주세요",
            "각 주요 단계를 더 작은 작업으로 분해하고 계층적으로 구성해주세요",
            "작업 간 의존성이나 선후 관계를 명확하게 표시해주세요",
            "각 단계나 작업의 예상 소요 시간이나 난이도도 표시해주세요"
        ])
        
        builder.add_format_instructions(
            "Mermaid 문법을 사용하여 계층적 분해 다이어그램을 작성해주세요. "
            "flowchart TD 또는 classDiagram 형식을 사용하고, 다음 요소를 포함해주세요:\n"
            "1. 최상위 목표(학술 논문 작성)를 루트 노드로 표현\n"
            "2. 주요 단계를 2단계 노드로 구성\n"
            "3. 각 주요 단계 아래 세부 작업을 하위 노드로 확장\n"
            "4. 단계별로 색상이나 스타일을 구분하여 가시성 높이기\n"
            "5. 작업 간 의존성이나 관계를 화살표로 표시\n\n"
            "인문학 분야의 학술 논문 작성을 예시로 사용하여 시각화해주세요."
        )
    else:
        builder.add_instructions([
            f"{topic}의 과정이나 구조를 {output_format} 형태로 시각화해주세요",
            "주요 구성 요소와 그들 사이의 관계를 명확하게 표현해주세요",
            "프로세스의 흐름이나 단계를 논리적 순서로 구성해주세요",
            "중요한 결정 지점이나 분기점을 강조해주세요",
            "복잡한 관계나 구조를 직관적으로 이해할 수 있게 표현해주세요"
        ])
        
        builder.add_format_instructions(
            f"Mermaid 문법을 사용하여 {output_format}을 작성해주세요. "
            "시각화에 적합한 형식(flowchart, mindmap, gantt, classDiagram 등)을 선택하고, "
            "다음 요소를 포함해주세요:\n"
            "1. 명확한 노드와 연결 구조\n"
            "2. 논리적 흐름이나 관계 표현\n"
            "3. 중요 요소 강조 및 구분\n"
            "4. 적절한 라벨과 설명\n"
            "5. 가능한 경우 색상 코드나 스타일 차별화\n\n"
            "시각화의 목적과 주제에 맞는 적절한 상세도와 구조로 표현해주세요."
        )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="문제 해결 과정 시각화 요청 방법",
        topic_options=VISUALIZATION_TOPICS,
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