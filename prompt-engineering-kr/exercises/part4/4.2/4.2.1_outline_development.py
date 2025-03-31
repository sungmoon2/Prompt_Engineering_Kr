"""
에세이/보고서 개요 작성 전략 실습 모듈

Part 4 - 섹션 4.2.1 실습 코드: 효과적인 학술 에세이와 보고서 개요 작성 전략을 
학습하고 다양한 유형의 개요를 개발하는 방법을 실습합니다.
"""

import os
import sys
import json
import datetime
from typing import Dict, List, Any, Optional
import re

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 개요 유형 옵션 정의
OUTLINE_TYPES = {
    "1": {"name": "에세이 개요", "topic": "학술 에세이를 위한 효과적인 개요 작성 전략", "output_format": "개요 템플릿과 작성 가이드"},
    "2": {"name": "연구 보고서 개요", "topic": "연구 보고서를 위한 체계적인 개요 구조화 방법", "output_format": "보고서 개요 프레임워크"},
    "3": {"name": "비교/대조 에세이 개요", "topic": "비교/대조 에세이를 위한 최적화된 개요 구조", "output_format": "비교 개요 모델"},
    "4": {"name": "논증적 에세이 개요", "topic": "강력한 논증을 위한 에세이 개요 전략", "output_format": "논증 구조 템플릿"},
    "5": {"name": "문헌 검토 개요", "topic": "체계적인 문헌 검토를 위한 개요 작성 방법", "output_format": "문헌 검토 매트릭스"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["개요 작성에 대한 일반적 질문"],
    "enhanced": [
        "역할 설정: 학술 글쓰기 전문가",
        "맥락 제공: 학생의 에세이/보고서 상황 설명",
        "구체적 요청: 개요 유형별 세부 구조 요청",
        "형식 지정: 실용적인 템플릿과 예시 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 개요는 에세이/보고서 작성의 로드맵 역할을 하며 논리적 구조와 일관성을 제공합니다",
    "목적과 독자에 맞는 개요 유형과 구조를 선택하는 것이 중요합니다",
    "하향식(주요 섹션에서 세부사항으로) 또는 상향식(세부사항에서 큰 구조로) 접근법을 상황에 맞게 활용할 수 있습니다",
    "AI는 개요 브레인스토밍, 구조화, 논리 흐름 최적화에 효과적으로 활용할 수 있습니다",
    "개요-초안 간격을 좁히는 단계적 전환 전략은 실제 작성 과정을 수월하게 합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "학술 글쓰기 전문가", 
        "대학 글쓰기 센터에서 다양한 학문 분야의 학생들에게 효과적인 에세이와 보고서 작성 전략을 지도하는 전문가입니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"다양한 학술 과제를 수행하며 효과적인 개요 작성의 중요성을 깨달았지만, "
        f"체계적이고 효율적인 개요 작성 방법에 대한 구체적인 지침이 필요합니다. "
        f"특히 논리적인 구조를 개발하고 일관성 있는 흐름을 유지하는 데 어려움을 겪고 있습니다. "
        f"생성형 AI를 개요 작성 과정에 효과적으로 활용하는 방법도 배우고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "에세이 개요" in topic:
        builder.add_instructions([
            "학술 에세이를 위한 효과적인 개요의 핵심 요소와 구조를 설명해주세요",
            "다양한 유형의 에세이(설명적, 분석적, 논증적 등)에 맞는 개요 구조의 차이점을 설명해주세요",
            "개요 작성의 사전 준비 단계와 체계적인 접근법을 단계별로 안내해주세요",
            "개요에서 논리적 흐름과 일관성을 확보하는 전략을 제안해주세요",
            "AI를 활용하여 효과적인 에세이 개요를 개발하는 구체적인 프롬프트와 전략도 포함해주세요"
        ])
    elif "연구 보고서 개요" in topic:
        builder.add_instructions([
            "연구 보고서를 위한 체계적인 개요의 핵심 구성 요소와 구조를 설명해주세요",
            "각 주요 섹션(서론, 문헌 검토, 방법론, 결과, 논의 등)의 목적과 포함해야 할 요소를 상세히 안내해주세요",
            "연구 질문, 방법론, 결과가 논리적으로 연결되는 개요 구성 방법을 제안해주세요",
            "효과적인 연구 보고서 개요 작성을 위한 단계별 접근법을 제시해주세요",
            "AI를 활용하여 연구 보고서 개요를 개발하고 개선하는 전략과 프롬프트도 포함해주세요"
        ])
    elif "비교/대조 에세이 개요" in topic:
        builder.add_instructions([
            "비교/대조 에세이를 위한 최적화된 개요 구조의 핵심 요소를 설명해주세요",
            "주제별 구조와 관점별 구조 등 비교/대조 개요의 다양한 구성 방식의 장단점을 분석해주세요",
            "효과적인 비교 기준 선정과 개요에 통합하는 방법을 제안해주세요",
            "균형 잡힌 비교와 논리적 일관성을 유지하는 개요 작성 전략을 설명해주세요",
            "AI를 활용하여 비교/대조 에세이 개요를 효과적으로 개발하는 구체적인 프롬프트와 예시도 포함해주세요"
        ])
    elif "논증적 에세이 개요" in topic:
        builder.add_instructions([
            "설득력 있는 논증적 에세이를 위한 개요 구조의 핵심 요소를 설명해주세요",
            "주요 주장, 지원 증거, 반론 고려 등을 효과적으로 구조화하는 방법을 안내해주세요",
            "논리적으로 견고한 논증 구조를 개발하는 단계별 접근법을 제시해주세요",
            "다양한 논증 패턴(연역적, 귀납적, 인과적 등)에 맞는 개요 구조화 전략을 설명해주세요",
            "AI를 활용하여 논증 구조를 강화하고 개요를 개선하는 프롬프트와 기법도 포함해주세요"
        ])
    elif "문헌 검토 개요" in topic:
        builder.add_instructions([
            "체계적인 문헌 검토를 위한 효과적인 개요의 핵심 요소와 구조를 설명해주세요",
            "문헌 통합적 접근법과 주제별 접근법 등 다양한 문헌 검토 구조화 방법의 장단점을 비교해주세요",
            "문헌 간의 관계, 패턴, 주제를 식별하고 개요에 반영하는 방법을 안내해주세요",
            "비판적 분석과 종합을 위한 개요 구성 전략을 제시해주세요",
            "AI를 활용하여 문헌 검토 개요를 개발하고 문헌 간 연결성을 강화하는 프롬프트와 기법도 포함해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 체계적이고 실용적인 개요 작성 전략을 설명해주세요",
            "개요 작성의 핵심 원칙과 모범 사례를 포함해주세요",
            "학생이 직접 적용할 수 있는 구체적인 가이드와 예시를 제공해주세요",
            "효과적인 개요 구성과 논리적 흐름 개발 방법을 안내해주세요",
            "AI 활용 전략과 프롬프트 예시도 함께 제시해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 즉시 활용 가능한 개요 템플릿과 단계별 작성 가이드를 제공해주시고, "
        f"실제 주제에 적용할 수 있는 구체적인 예시도 포함해주세요. "
        f"대학생이 이해하기 쉬운 언어로 설명하되, 학술적 엄밀성을 유지해주세요. "
        f"특히 AI를 활용한 개요 개발 전략은 구체적인 프롬프트 예시와 함께 제공해주세요."
    )
    
    return builder.build()

def save_outline_template(outline_type: str, template_content: str, ai_response: str):
    """
    개요 템플릿을 파일로 저장하는 함수
    
    Args:
        outline_type: 개요 유형 이름
        template_content: 저장할 템플릿 내용
        ai_response: AI의 전체 응답 내용
    """
    # 현재 날짜로 고유 파일명 생성
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outline_{outline_type.replace(' ', '_').lower()}_{date_str}.md"
    
    # 템플릿 추출 (마크다운 코드 블록 내용 찾기)
    template_sections = []
    
    # 마크다운 코드 블록 추출 (```로 시작하고 ```로 끝나는 부분)
    code_blocks = re.findall(r'```(?:markdown)?(.*?)```', ai_response, re.DOTALL)
    
    # 코드 블록이 있으면 그것을 템플릿으로 사용
    if code_blocks:
        for block in code_blocks:
            template_sections.append(block.strip())
    else:
        # 코드 블록이 없으면 전체 응답에서 템플릿 부분을 추출 시도
        template_sections = [ai_response]
    
    # 템플릿 파일 저장
    templates_dir = os.path.join(current_dir, "templates")
    os.makedirs(templates_dir, exist_ok=True)
    
    with open(os.path.join(templates_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"# {outline_type} 템플릿\n\n")
        f.write(f"생성일: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## 템플릿 내용\n\n")
        
        for section in template_sections:
            f.write(f"{section}\n\n")
    
    print(f"\n템플릿이 저장되었습니다: {os.path.join(templates_dir, filename)}")
    
    return os.path.join(templates_dir, filename)

def create_example_outline():
    """
    예시 개요 템플릿 생성 함수
    """
    # 예시 에세이 개요 템플릿
    essay_outline_template = """# 학술 에세이 개요 템플릿

## 기본 정보
- **주제**: [에세이 주제]
- **유형**: [설명적/분석적/논증적/비교대조 등]
- **대상 독자**: [교수/학생/전문가 등]
- **단어 수**: [목표 단어 수]

## I. 서론 (약 10-15%)
A. 주의 환기 (흥미로운 통계, 인용, 사례 등)
B. 주제 소개 및 배경 정보
C. 논문의 목적/논제 진술문
D. 논문의 범위와 한계
E. 논문의 구조 개요 (로드맵)

## II. 본론 1: [첫 번째 주요 논점] (약 20-25%)
A. 주요 논점 1 진술
   1. 지원 증거/사례 1
   2. 지원 증거/사례 2
   3. 분석 및 해석
B. 하위 논점 1
   1. 지원 증거/사례
   2. 분석 및 해석
C. 하위 논점 2
   1. 지원 증거/사례
   2. 분석 및 해석
D. 섹션 요약 및 다음 섹션과의 연결

## III. 본론 2: [두 번째 주요 논점] (약 20-25%)
A. 주요 논점 2 진술
   1. 지원 증거/사례 1
   2. 지원 증거/사례 2
   3. 분석 및 해석
B. 하위 논점 1
   1. 지원 증거/사례
   2. 분석 및 해석
C. 하위 논점 2
   1. 지원 증거/사례
   2. 분석 및 해석
D. 섹션 요약 및 다음 섹션과의 연결

## IV. 본론 3: [세 번째 주요 논점] (약 20-25%)
A. 주요 논점 3 진술
   1. 지원 증거/사례 1
   2. 지원 증거/사례 2
   3. 분석 및 해석
B. 하위 논점 1
   1. 지원 증거/사례
   2. 분석 및 해석
C. 반론 고려 및 대응
   1. 잠재적 반론 식별
   2. 반론에 대한 대응/반박
D. 섹션 요약

## V. 결론 (약 10-15%)
A. 논문의 주요 논점 및 발견 요약
B. 논제에 대한 최종 입장/답변 재확인
C. 더 넓은 맥락에서의 의미와 시사점
D. 향후 연구/고려 방향 제안
E. 인상적인 마무리 (통찰, 인용, 행동 촉구 등)

## VI. 참고문헌
[참고문헌 목록 - 적절한 인용 스타일 사용]
"""

    # 예시 연구 보고서 개요 템플릿
    research_report_outline = """# 연구 보고서 개요 템플릿

## 기본 정보
- **연구 주제**: [연구 주제]
- **연구 질문/목적**: [주요 연구 질문 또는 목적]
- **방법론**: [양적/질적/혼합 연구 방법]
- **단어 수**: [목표 단어 수]

## I. 서론 (약 10%)
A. 연구 배경
   1. 주제의 중요성 및 맥락
   2. 문제 제기
B. 연구 목적 및 연구 질문
   1. 주요 연구 질문
   2. 하위 연구 질문
C. 연구의 중요성 및 기대 기여
D. 연구의 범위와 한계
E. 보고서 구조 개요

## II. 문헌 검토 (약 20-25%)
A. 이론적 프레임워크
   1. 주요 이론 및 개념 설명
   2. 이론적 모델 제시
B. 선행 연구 분석
   1. 주제별/연대순 선행 연구 고찰
   2. 주요 발견 및 방법론 분석
C. 연구 격차 식별
D. 현 연구의 위치 및 기여점

## III. 연구 방법론 (약 15-20%)
A. 연구 설계
   1. 연구 접근법 정당화
   2. 변수 조작적 정의
B. 자료 수집 방법
   1. 표본 선정 및 특성
   2. 도구 및 측정 방법
   3. 자료 수집 절차
C. 자료 분석 방법
   1. 분석 기법 및 도구
   2. 분석 절차
D. 연구 윤리 고려사항
E. 연구 방법의 한계

## IV. 연구 결과 (약 20-25%)
A. 자료 개요 및 기술 통계
B. 연구 질문 1 관련 결과
   1. 주요 발견
   2. 통계적/질적 분석 결과
   3. 표/그래프/인용 등 증거 제시
C. 연구 질문 2 관련 결과
   [동일한 구조 반복]
D. 연구 질문 3 관련 결과
   [동일한 구조 반복]
E. 예상치 못한 발견 또는 추가 분석

## V. 논의 (약 20%)
A. 주요 발견 요약
B. 결과 해석
   1. 연구 질문 1 관련 논의
   2. 연구 질문 2 관련 논의
   3. 연구 질문 3 관련 논의
C. 이론적 및 실용적 시사점
D. 연구의 한계
E. 향후 연구 방향 제안

## VI. 결론 (약 5%)
A. 연구 요약
B. 주요 기여 강조
C. 최종 통찰 및 마무리

## VII. 참고문헌
[참고문헌 목록 - 적절한 인용 스타일 사용]

## VIII. 부록
A. 설문지/인터뷰 질문
B. 추가 통계 자료
C. 기타 관련 자료
"""

    # 예시 템플릿 저장
    templates_dir = os.path.join(current_dir, "examples")
    os.makedirs(templates_dir, exist_ok=True)
    
    # 에세이 개요 템플릿 저장
    essay_filename = "example_essay_outline_template.md"
    with open(os.path.join(templates_dir, essay_filename), 'w', encoding='utf-8') as f:
        f.write(essay_outline_template)
    
    # 연구 보고서 개요 템플릿 저장
    report_filename = "example_research_report_outline_template.md"
    with open(os.path.join(templates_dir, report_filename), 'w', encoding='utf-8') as f:
        f.write(research_report_outline)
    
    print(f"\n예시 개요 템플릿이 생성되었습니다:")
    print(f"1. 에세이 개요: {os.path.join(templates_dir, essay_filename)}")
    print(f"2. 연구 보고서 개요: {os.path.join(templates_dir, report_filename)}")
    
    return os.path.join(templates_dir, essay_filename), os.path.join(templates_dir, report_filename)

def apply_structure_to_topic(outline_template: str, topic: str):
    """
    개요 템플릿을 특정 주제에 적용하는 함수
    
    Args:
        outline_template: 개요 템플릿 파일 경로
        topic: 적용할 주제
    
    Returns:
        적용된 개요 내용
    """
    # 템플릿 내용 읽기
    with open(outline_template, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 적용된 개요 파일명 생성
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    applied_filename = f"applied_outline_{date_str}.md"
    applied_filepath = os.path.join(os.path.dirname(outline_template), applied_filename)
    
    # 기본 정보 부분 갱신
    topic_placeholder = "[에세이 주제]" if "essay" in outline_template else "[연구 주제]"
    applied_content = template_content.replace(topic_placeholder, topic)
    
    # 주제에 맞는 논점 구조 제안 (예시)
    if "essay" in outline_template:
        # 에세이 주요 논점 예시 (실제로는 AI를 통해 구체적인 논점 생성 가능)
        main_points = [
            "주제의 역사적 배경과 발전",
            "주제와 관련된 주요 이론적 관점",
            "현대 사회에서 주제의 중요성과 영향"
        ]
        
        # 주요 논점 적용
        for i, point in enumerate(main_points, 1):
            placeholder = f"[{(i):WORDS} 번째 주요 논점]".replace(":WORDS", "첫" if i==1 else "두" if i==2 else "세")
            applied_content = applied_content.replace(placeholder, point)
    
    # 적용된 개요 저장
    with open(applied_filepath, 'w', encoding='utf-8') as f:
        f.write(applied_content)
    
    print(f"\n주제 '{topic}'에 개요 템플릿이 적용되었습니다: {applied_filepath}")
    
    return applied_content

def custom_run_exercise():
    """
    개요 작성 실습 실행 함수 (run_exercise 대신 사용자 정의 함수 사용)
    """
    print("\n===== 4.2.1 에세이/보고서 개요 작성 전략 =====\n")
    print("효과적인 학술 에세이와 보고서 개요를 작성하는 전략을 학습하고 실습합니다.")
    
    # 개요 유형 선택
    print("\n개발할 개요 유형을 선택하세요:")
    for key, value in OUTLINE_TYPES.items():
        print(f"{key}. {value['name']}: {value['topic']}")
    
    choice = input("\n선택 (1-5): ").strip()
    if choice not in OUTLINE_TYPES:
        print("유효하지 않은 선택입니다. 1번 유형으로 진행합니다.")
        choice = "1"
    
    selected_type = OUTLINE_TYPES[choice]
    topic = selected_type["topic"]
    output_format = selected_type["output_format"]
    
    print(f"\n선택한 개요 유형: {selected_type['name']}")
    print(f"주제: {topic}")
    
    # 프롬프트 옵션
    print("\n1. 기본 프롬프트 사용")
    print("2. 향상된 프롬프트 사용")
    print("3. 두 프롬프트 비교")
    print("4. 예시 템플릿 사용 (AI 요청 없이)")
    
    prompt_choice = input("\n선택 (1-4): ").strip()
    
    # 프롬프트 생성
    basic_prompt = get_basic_prompt(topic)
    enhanced_prompt = get_enhanced_prompt(topic, "학술 글쓰기", output_format)
    
    if prompt_choice == "1":
        print("\n===== 기본 프롬프트 =====")
        print(basic_prompt)
        
        print("\n이 프롬프트로 AI에게 개요 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
        
        # AI 응답 입력 요청
        print("\nAI의 응답을 복사하여 붙여넣으세요 (여러 줄 입력 가능, 입력 완료 후 빈 줄에서 Enter):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        
        ai_response = "\n".join(lines)
        if ai_response.strip():
            template_file = save_outline_template(selected_type["name"], ai_response, ai_response)
        else:
            print("응답이 비어있습니다. 예시 템플릿을 생성합니다.")
            template_files = create_example_outline()
            template_file = template_files[0] if choice == "1" else template_files[1]
        
    elif prompt_choice == "2":
        print("\n===== 향상된 프롬프트 =====")
        print(enhanced_prompt)
        
        print("\n이 프롬프트로 AI에게 개요 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
        
        # AI 응답 입력 요청
        print("\nAI의 응답을 복사하여 붙여넣으세요 (여러 줄 입력 가능, 입력 완료 후 빈 줄에서 Enter):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        
        ai_response = "\n".join(lines)
        if ai_response.strip():
            template_file = save_outline_template(selected_type["name"], ai_response, ai_response)
        else:
            print("응답이 비어있습니다. 예시 템플릿을 생성합니다.")
            template_files = create_example_outline()
            template_file = template_files[0] if choice == "1" else template_files[1]
        
    elif prompt_choice == "3":
        print("\n===== 기본 프롬프트 =====")
        print(basic_prompt)
        
        print("\n이 프롬프트로 AI에게 개요 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n첫 번째 응답을 받은 후 Enter를 눌러 계속하세요... ")
        
        print("\n===== 향상된 프롬프트 =====")
        print(enhanced_prompt)
        
        print("\n이 프롬프트로 AI에게 개요 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n두 번째 응답을 받은 후 Enter를 눌러 계속하세요... ")
        
        # AI 응답 입력 요청 (두 번째 응답만 저장)
        print("\n두 번째(향상된 프롬프트) AI 응답을 복사하여 붙여넣으세요 (입력 완료 후 빈 줄에서 Enter):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        
        ai_response = "\n".join(lines)
        if ai_response.strip():
            template_file = save_outline_template(selected_type["name"], ai_response, ai_response)
        else:
            print("응답이 비어있습니다. 예시 템플릿을 생성합니다.")
            template_files = create_example_outline()
            template_file = template_files[0] if choice == "1" else template_files[1]
        
    else:  # 예시 템플릿 사용
        print("\n예시 템플릿을 생성합니다...")
        template_files = create_example_outline()
        template_file = template_files[0] if choice == "1" else template_files[1]
    
    # 템플릿 적용 실습
    print("\n===== 개요 템플릿 적용 실습 =====")
    print("1. 특정 주제에 템플릿 적용하기")
    print("2. 개요 논리 흐름 최적화하기")
    print("3. 개요에서 초안으로 전환 연습하기")
    
    apply_choice = input("\n선택 (1-3): ").strip()
    
    if apply_choice == "1":
        # 특정 주제에 템플릿 적용
        print("\n템플릿을 적용할 주제를 입력하세요:")
        specific_topic = input().strip() or "소셜 미디어가 청소년의 정신 건강에 미치는 영향"
        
        apply_structure_to_topic(template_file, specific_topic)
        
    elif apply_choice == "2":
        # 개요 논리 흐름 최적화
        print("\n개요의 논리 흐름을 최적화하는 AI 프롬프트 예시:")
        logic_prompt = f"""다음 개요의 논리적 흐름과 구조를 평가하고, 개선된 버전을 제안해주세요:

[개요 내용 - 여기에 개요를 붙여넣으세요]

특히 다음 측면에 초점을 맞춰주세요:
- 논점 간 논리적 연결성
- 주장-증거 관계의 명확성
- 섹션 간 전환의 자연스러움
- 전체적인 일관성과 균형
"""
        print(logic_prompt)
        print("\n이 프롬프트를 사용하여 AI에게 개요의 논리 흐름 최적화를 요청해보세요.")
        
    elif apply_choice == "3":
        # 개요에서 초안으로 전환 연습
        print("\n개요 섹션을 초안으로 확장하는 AI 프롬프트 예시:")
        expansion_prompt = f"""다음 개요 섹션을 완전한 문단으로 확장해주세요. 핵심 아이디어를 유지하면서 필요한 설명, 증거, 분석을 추가해주세요:

섹션 제목: [섹션 제목]
개요 항목: 
[개요 항목들]

원하는 결과물 톤: [학술적/설명적/설득적 등]
원하는 단어 수: [대략적인 단어 수]
"""
        print(expansion_prompt)
        print("\n이 프롬프트를 사용하여 AI에게 개요 섹션의 확장을 요청해보세요.")
    
    # 프롬프트 비교 및 학습 포인트
    print("\n===== 프롬프트 비교 및 학습 =====")
    
    if prompt_choice in ["1", "2", "3"]:
        print("\n기본 프롬프트와 향상된 프롬프트의 주요 차이점:")
        for i, point in enumerate(PROMPT_SUMMARY["enhanced"], 1):
            print(f"{i}. {point}")
    
    print("\n핵심 학습 포인트:")
    for i, point in enumerate(LEARNING_POINTS, 1):
        print(f"{i}. {point}")
    
    # 마무리 및 다음 단계
    print("\n===== 실습 마무리 =====")
    print("이 실습을 통해 효과적인 학술 에세이와 보고서 개요 작성 전략을 학습하고 실습했습니다.")
    print("\n다음 단계 제안:")
    print("1. 다양한 유형의 개요 템플릿을 개발하여 자신의 템플릿 라이브러리를 구축하세요.")
    print("2. 실제 과제에 개요 템플릿을 적용하고 논리적 구조를 최적화하세요.")
    print("3. 개요에서 초안으로의 단계적 전환 과정을 연습하세요.")
    print("4. AI를 활용하여 개요의 논리적 흐름과 완전성을 평가하고 개선하세요.")
    
    print("\n에세이/보고서 개요 작성 전략 실습을 마칩니다.")

def main():
    """메인 함수"""
    try:
        # 사용자 정의 실행 함수 호출
        custom_run_exercise()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        import traceback
        traceback.print_exc()
        print("API 키나 네트워크 연결을 확인하세요.")

if __name__ == "__main__":
    main()
