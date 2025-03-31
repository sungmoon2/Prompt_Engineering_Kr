"""
프롬프트 문서화 템플릿 작성 실습 모듈

Part 3 - 섹션 3.4.3 실습 코드: 장기 프로젝트를 위한 체계적인 프롬프트 문서화 
템플릿을 개발하고 적용하는 방법을 학습합니다.
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

# 템플릿 유형 옵션 정의
TEMPLATE_TYPES = {
    "1": {"name": "AI 세션 문서화", "topic": "개별 AI 작업 세션을 체계적으로 문서화하는 템플릿 개발", "output_format": "세션 문서 템플릿"},
    "2": {"name": "의사결정 추적", "topic": "프로젝트 과정의 주요 의사결정을 기록하고 추적하는 시스템", "output_format": "의사결정 기록 템플릿"},
    "3": {"name": "지식 관리 시스템", "topic": "프로젝트 통찰과 지식을 체계적으로 축적하는 지식 베이스", "output_format": "지식 관리 템플릿"},
    "4": {"name": "최종 보고서 계획", "topic": "프로젝트 보고서 작성을 위한 문서화 계획 및 증거 추적", "output_format": "보고서 계획 템플릿"},
    "5": {"name": "종합 문서화 시스템", "topic": "프로젝트 전체를 아우르는 통합 문서화 시스템 설계", "output_format": "통합 문서화 가이드"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["템플릿에 대한 일반적인 질문"],
    "enhanced": [
        "역할 설정: 프로젝트 문서화 전문가",
        "맥락 제공: 학생의 구체적인 프로젝트 상황 설명",
        "구체적 요청: 목적별 상세 기능 요구",
        "형식 지정: 즉시 사용 가능한 템플릿 형식 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "체계적인 문서화는 장기 프로젝트의 일관성과 진행 상황 추적에 필수적입니다",
    "목적에 맞는 템플릿은 효율적인 정보 관리와 검색을 가능하게 합니다",
    "맥락 정보를 포함한 문서화는 미래의 작업과 의사결정에 중요한 자원이 됩니다",
    "효과적인 프롬프트 문서화는 AI 활용의 학습 곡선을 가속화합니다",
    "프로젝트 종료 후에도 활용할 수 있는 지식 자산을 구축하는 것이 중요합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "프로젝트 문서화 전문가", 
        "학술 및 전문 프로젝트의 체계적인 문서화와 지식 관리 시스템 구축에 전문성을 갖춘 컨설턴트입니다."
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 대학생으로 {topic}에 관심이 있습니다. "
        f"한 학기 동안 진행되는 학술 프로젝트를 체계적으로 문서화하고 관리하며, "
        f"AI와의 협업 과정과 그 결과를 효과적으로 기록하고 활용하고자 합니다. "
        f"생성형 AI를 활용하여 다양한 작업을 수행하면서, 이 과정에서 생성된 "
        f"프롬프트, 결과물, 통찰, 의사결정 등을 체계적으로 관리할 수 있는 "
        f"템플릿과 시스템이 필요합니다."
    )
    
    # 구체적인 지시사항 추가
    if "AI 세션 문서화" in topic:
        builder.add_instructions([
            "개별 AI 작업 세션을 체계적으로 문서화하는 포괄적인 템플릿의 구조와 요소를 설명해주세요",
            "세션 목표, 사용한 프롬프트, 결과, 통찰, 의사결정 등을 효과적으로 기록하는 방법을 제안해주세요",
            "세션 간의 연결성과 맥락을 유지하는 참조 시스템도 포함해주세요",
            "프롬프트 반복 사용과 개선 과정을 추적하는 방법도 제시해주세요",
            "템플릿을 마크다운 형식으로 제공하고, 사용 방법에 대한 구체적인 지침도 함께 제공해주세요"
        ])
    elif "의사결정 추적" in topic:
        builder.add_instructions([
            "프로젝트 과정에서 내리는 주요 의사결정을 체계적으로 기록하고 추적하는 시스템의 구조와 요소를 설명해주세요",
            "결정의 배경, 고려한 대안, 선택 근거, 예상 영향 등을 포괄적으로 문서화하는 템플릿을 제안해주세요",
            "의사결정 간의 관계와 의존성을 추적하고 시각화하는 방법도 포함해주세요",
            "시간이 지남에 따라 결정의 효과를 평가하고 학습하는 프로세스를 제안해주세요",
            "템플릿을 마크다운 형식으로 제공하고, 구체적인 작성 예시와 함께 사용 지침을 제공해주세요"
        ])
    elif "지식 관리 시스템" in topic:
        builder.add_instructions([
            "프로젝트 과정에서 얻은 다양한 형태의 지식과 통찰을 체계적으로 축적하고 관리하는 시스템의 구조를 설명해주세요",
            "개념, 사실, 방법론, 패턴 등 다양한 유형의 지식을 분류하고 조직하는 프레임워크를 제안해주세요",
            "지식 간의 연결과 관계를 관리하여 통합된 지식 네트워크를 구축하는 방법을 제시해주세요",
            "프로젝트 완료 후에도 지속적으로 활용할 수 있는 지식 베이스 유지 관리 전략을 포함해주세요",
            "템플릿을 마크다운 형식으로 제공하고, 다양한 지식 유형에 대한 구체적인 기록 예시를 함께 제공해주세요"
        ])
    elif "최종 보고서 계획" in topic:
        builder.add_instructions([
            "장기 프로젝트의 최종 보고서 작성을 위한 체계적인 문서화 계획과 증거 추적 시스템의 구조를 설명해주세요",
            "프로젝트 과정에서 수집해야 할 정보와 증거를 구조화하고 관리하는 방법을 제안해주세요",
            "보고서의 주요 주장과 결론을 뒷받침하는 증거를 체계적으로 연결하고 추적하는 매트릭스를 설계해주세요",
            "AI 활용 과정과 그 가치를 보고서에 효과적으로 통합하는 방법을 포함해주세요",
            "템플릿을 마크다운 형식으로 제공하고, 보고서 작성을 위한 단계별 계획과 체크리스트를 함께 제시해주세요"
        ])
    elif "종합 문서화 시스템" in topic:
        builder.add_instructions([
            "프로젝트 전체를 아우르는 통합 문서화 시스템의 구조와 핵심 구성 요소를 설명해주세요",
            "세션 문서, 의사결정 추적, 지식 관리, 보고서 계획 등 다양한 문서화 요소를 통합하는 시스템을 설계해주세요",
            "효율적인 정보 접근과 검색을 위한 메타데이터 관리 및 문서화 규칙을 제안해주세요",
            "디지털 도구(노션, GitHub, 트렐로 등)를 활용한 실용적인 구현 방법도 포함해주세요",
            "템플릿과 시스템 설계를 마크다운 형식으로 제공하고, 실제 구현을 위한 단계별 가이드를 함께 제시해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 체계적이고 실용적인 템플릿과 접근법을 설명해주세요",
            "프로젝트 문서화의 핵심 원칙과 모범 사례를 포함해주세요",
            "학생이 직접 적용할 수 있는 구체적인 템플릿과 예시를 제공해주세요",
            "문서화 시스템의 효과적인 구현과 유지 관리 방법을 제안해주세요",
            "학업 및 연구 맥락에서의 적용 사례와 팁도 함께 제시해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 즉시 활용 가능한 템플릿을 제공해주시고, "
        f"이 템플릿의 각 요소와 목적을 명확히 설명해주세요. "
        f"가능한 경우 실제 작성 예시를 포함하여 템플릿 사용법을 보여주세요. "
        f"학생들이 노션, 옵시디언, 깃허브 등 일반적인 도구에서 바로 사용할 수 있는 "
        f"실용적인 형식으로 제공해주세요."
    )
    
    return builder.build()

def save_template_to_file(template_type: str, template_content: str, ai_response: str):
    """
    템플릿을 파일로 저장하는 함수
    
    Args:
        template_type: 템플릿 유형 이름
        template_content: 저장할 템플릿 내용
        ai_response: AI의 전체 응답 내용
    """
    # 현재 날짜로 고유 파일명 생성
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"template_{template_type.replace(' ', '_').lower()}_{date_str}.md"
    
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
        # 일반적으로 "템플릿", "양식", "폼" 등의 단어 이후 내용을 찾음
        template_sections = [ai_response]
    
    # 템플릿 파일 저장
    templates_dir = os.path.join(current_dir, "templates")
    os.makedirs(templates_dir, exist_ok=True)
    
    with open(os.path.join(templates_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"# {template_type} 템플릿\n\n")
        f.write(f"생성일: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## 템플릿 내용\n\n")
        
        for section in template_sections:
            f.write(f"{section}\n\n")
    
    print(f"\n템플릿이 저장되었습니다: {os.path.join(templates_dir, filename)}")
    
    return os.path.join(templates_dir, filename)

def apply_template_example():
    """
    템플릿 적용 예시를 생성하는 함수
    """
    # 현재 날짜로 예시 세션 ID 생성
    session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # AI 세션 문서화 예시
    example = {
        "session_id": session_id,
        "date_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "project_stage": "연구 단계",
        "milestone": "문헌 검토 완료",
        "goals": [
            "연구 질문 구체화하기",
            "기존 연구와의 차별점 파악하기"
        ],
        "context": {
            "previous_session": "20231010_152233",
            "related_materials": ["literature_review.md", "research_questions_draft.md"],
            "current_status": "문헌 검토를 완료하고 연구 질문 정교화 필요"
        },
        "prompts": [
            {
                "title": "연구 질문 구체화",
                "text": "제가 진행하는 연구 주제는 '대학생의 온라인 학습 참여 패턴과 학업 성취도의 관계'입니다. 문헌 검토 결과, 다음과 같은 초기 연구 질문을 도출했습니다: '온라인 학습 환경에서 대학생의 참여 패턴은 학업 성취도에 어떤 영향을 미치는가?' 이 연구 질문을 더 구체적이고 연구 가능한 형태로 정교화해주세요."
            }
        ],
        "results": [
            {
                "title": "구체화된 연구 질문 제안",
                "content": "문헌 검토와 현재 연구 방향을 고려할 때, 다음과 같이 연구 질문을 구체화할 수 있습니다:\n\n주요 연구 질문: '비동기식 온라인 학습 환경에서 대학생의 참여 유형(행동적, 인지적, 정서적)과 참여 시점(주중/주말, 아침/저녁)이 학업 성취도와 학습 만족도에 미치는 영향은 어떠한가?'\n\n하위 연구 질문:\n1. 참여 유형별(행동적, 인지적, 정서적) 참여도와 학업 성취도 간의 상관관계는 어떠한가?\n2. 참여 시점 패턴과 학업 성취도 간의 관계는 어떠한가?\n3. 학습자의 자기조절 능력이 참여 패턴과 학업 성취도 간의 관계를 어떻게 매개하는가?"
            }
        ],
        "insights": [
            "행동적, 인지적, 정서적 참여를 구분하여 측정할 필요가 있음",
            "참여 시점 패턴이 중요한 변수가 될 수 있음",
            "자기조절 능력을 매개 변수로 고려해볼 가치가 있음"
        ],
        "decisions": [
            {"decision": "참여 유형을 세 가지 차원으로 구분하여 측정", "rationale": "문헌 검토 결과 다차원적 접근이 더 포괄적인 이해 가능"},
            {"decision": "학습 분석 데이터와 설문 데이터 병행 수집", "rationale": "객관적 행동 데이터와 주관적 인식을 모두 포착하기 위함"}
        ],
        "next_steps": [
            "참여 유형별 측정 도구 개발",
            "데이터 수집 계획 수립",
            "IRB 신청 준비"
        ],
        "notes": "연구 질문이 충분히 구체적이면서도 연구 가능한 범위로 좁혀졌음. 측정 도구 개발이 다음 중요 단계."
    }
    
    # 예시 데이터를 JSON 파일로 저장
    examples_dir = os.path.join(current_dir, "examples")
    os.makedirs(examples_dir, exist_ok=True)
    
    filename = f"example_session_{session_id}.json"
    with open(os.path.join(examples_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(example, f, ensure_ascii=False, indent=2)
    
    # 예시 데이터를 마크다운 형식으로 변환하여 저장
    md_filename = f"example_session_{session_id}.md"
    with open(os.path.join(examples_dir, md_filename), 'w', encoding='utf-8') as f:
        f.write(f"# AI 세션 문서\n\n")
        f.write(f"## 기본 정보\n")
        f.write(f"- **세션 ID**: {example['session_id']}\n")
        f.write(f"- **날짜 및 시간**: {example['date_time']}\n")
        f.write(f"- **프로젝트 단계**: {example['project_stage']}\n")
        f.write(f"- **관련 마일스톤**: {example['milestone']}\n\n")
        
        f.write(f"## 세션 목표\n")
        for goal in example['goals']:
            f.write(f"- {goal}\n")
        f.write("\n")
        
        f.write(f"## 맥락 정보\n")
        f.write(f"- **이전 세션 참조**: {example['context']['previous_session']}\n")
        f.write(f"- **관련 자료**: {', '.join(example['context']['related_materials'])}\n")
        f.write(f"- **현재 상황**: {example['context']['current_status']}\n\n")
        
        f.write(f"## 사용한 프롬프트\n")
        for i, prompt in enumerate(example['prompts'], 1):
            f.write(f"### 프롬프트 {i}: {prompt['title']}\n\n")
            f.write(f"```\n{prompt['text']}\n```\n\n")
        
        f.write(f"## 주요 결과\n")
        for i, result in enumerate(example['results'], 1):
            f.write(f"### 결과 {i}: {result['title']}\n\n")
            f.write(f"```\n{result['content']}\n```\n\n")
        
        f.write(f"## 핵심 통찰 및 발견\n")
        for insight in example['insights']:
            f.write(f"- {insight}\n")
        f.write("\n")
        
        f.write(f"## 의사결정\n")
        for decision in example['decisions']:
            f.write(f"- **{decision['decision']}**: {decision['rationale']}\n")
        f.write("\n")
        
        f.write(f"## 다음 단계\n")
        for step in example['next_steps']:
            f.write(f"- {step}\n")
        f.write("\n")
        
        f.write(f"## 노트 및 관찰\n")
        f.write(f"{example['notes']}\n")
    
    print(f"\n예시 템플릿 적용이 생성되었습니다: {os.path.join(examples_dir, md_filename)}")
    
    return os.path.join(examples_dir, md_filename)

def custom_run_exercise():
    """
    템플릿 개발 실습 실행 함수 (run_exercise 대신 사용자 정의 함수 사용)
    """
    print("\n===== 3.4.3 프롬프트 문서화 템플릿 작성 =====\n")
    print("프로젝트를 체계적으로 관리하기 위한 다양한 문서화 템플릿을 개발하고 적용하는 실습입니다.")
    
    # 템플릿 유형 선택
    print("\n개발할 문서화 템플릿 유형을 선택하세요:")
    for key, value in TEMPLATE_TYPES.items():
        print(f"{key}. {value['name']}: {value['topic']}")
    
    choice = input("\n선택 (1-5): ").strip()
    if choice not in TEMPLATE_TYPES:
        print("유효하지 않은 선택입니다. 1번 템플릿으로 진행합니다.")
        choice = "1"
    
    selected_template = TEMPLATE_TYPES[choice]
    topic = selected_template["topic"]
    output_format = selected_template["output_format"]
    
    print(f"\n선택한 템플릿: {selected_template['name']}")
    print(f"주제: {topic}")
    
    # 기본 프롬프트와 향상된 프롬프트 비교 옵션
    print("\n1. 기본 프롬프트 사용")
    print("2. 향상된 프롬프트 사용")
    print("3. 두 프롬프트 비교")
    
    prompt_choice = input("\n선택 (1-3): ").strip()
    
    # 프롬프트 생성
    basic_prompt = get_basic_prompt(topic)
    enhanced_prompt = get_enhanced_prompt(topic, "학술 프로젝트 관리", output_format)
    
    if prompt_choice == "1":
        print("\n===== 기본 프롬프트 =====")
        print(basic_prompt)
        
        print("\n이 프롬프트로 AI에게 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
        
    elif prompt_choice == "2":
        print("\n===== 향상된 프롬프트 =====")
        print(enhanced_prompt)
        
        print("\n이 프롬프트로 AI에게 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
        
    else:  # 두 프롬프트 비교
        print("\n===== 기본 프롬프트 =====")
        print(basic_prompt)
        
        print("\n이 프롬프트로 AI에게 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
        
        print("\n===== 향상된 프롬프트 =====")
        print(enhanced_prompt)
        
        print("\n이 프롬프트로 AI에게 템플릿 요청하기")
        print("[프롬프트를 복사하여 AI에게 전송하고, 응답을 받은 후 계속하세요]")
        input("\n응답을 받은 후 Enter를 눌러 계속하세요... ")
    
    # 응답 분석 및 템플릿 저장
    print("\n===== 템플릿 저장 및 적용 =====")
    print("AI의 응답에서 템플릿을 저장하고 실제로 적용해보겠습니다.")
    
    # 사용자에게 AI 응답 입력 요청
    print("\nAI의 응답에서 템플릿 부분을 복사하여 붙여넣으세요 (여러 줄 입력 가능, 입력 완료 후 빈 줄에서 Enter 두 번):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    ai_response = "\n".join(lines)
    
    # 응답이 비어있을 경우
    if not ai_response.strip():
        print("응답이 비어있습니다. 예시 템플릿을 생성합니다.")
        template_file = apply_template_example()
    else:
        # 템플릿 파일로 저장
        template_file = save_template_to_file(selected_template["name"], ai_response, ai_response)
    
    # 프롬프트 비교 및 학습 포인트
    print("\n===== 프롬프트 비교 및 학습 =====")
    print("\n기본 프롬프트와 향상된 프롬프트의 주요 차이점:")
    for i, point in enumerate(PROMPT_SUMMARY["enhanced"], 1):
        print(f"{i}. {point}")
    
    print("\n핵심 학습 포인트:")
    for i, point in enumerate(LEARNING_POINTS, 1):
        print(f"{i}. {point}")
    
    # 템플릿 적용 실습
    print("\n===== 템플릿 적용 실습 =====")
    print("생성된 템플릿을 실제 프로젝트에 적용해보겠습니다.")
    
    apply_option = input("\n1. 예시 적용 생성\n2. 직접 템플릿 적용하기\n선택 (1-2): ").strip()
    
    if apply_option == "2":
        print("\n템플릿을 직접 적용하여 문서를 작성합니다.")
        print(f"템플릿 파일을 열어 내용을 확인하세요: {template_file}")
        print("템플릿의 각 섹션을 채우면서 프로젝트 문서화를 진행합니다.")
        
        # 기본 정보 입력 안내
        print("\n==== 기본 정보 입력 ====")
        session_id = input("세션 ID (또는 Enter로 자동 생성): ").strip() or datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        project_stage = input("프로젝트 단계: ").strip() or "연구 단계"
        session_goal = input("세션 주요 목표: ").strip() or "연구 질문 구체화하기"
        
        # 입력된 정보로 템플릿 시작 부분 작성
        print("\n기본 정보가 입력되었습니다. 이제 나머지 섹션을 작성하세요.")
        print("템플릿에 따라 프롬프트, 결과, 통찰, 의사결정 등을 기록합니다.")
        
        # 작성 완료 안내
        print("\n문서화가 완료되면 적절한 형식으로 저장하세요.")
        print("정기적인 문서화를 통해 프로젝트의 진행 상황과 통찰을 체계적으로 관리할 수 있습니다.")
    else:
        # 예시 적용 생성
        example_file = apply_template_example()
        print(f"\n예시 적용이 생성되었습니다: {example_file}")
        print("이 예시를 참고하여 실제 프로젝트에 템플릿을 적용해보세요.")
    
    # 마무리 및 다음 단계
    print("\n===== 실습 마무리 =====")
    print("이 실습을 통해 장기 프로젝트 관리를 위한 문서화 템플릿을 개발하고 적용하는 방법을 학습했습니다.")
    print("\n다음 단계 제안:")
    print("1. 다양한 유형의 템플릿을 개발하여 프로젝트 문서화 시스템을 구축하세요.")
    print("2. 정기적인 문서화 루틴을 수립하여 프로젝트 과정을 체계적으로 기록하세요.")
    print("3. 축적된 문서를 활용하여 프로젝트 진행 상황을 분석하고 개선점을 찾으세요.")
    print("4. 최종 보고서 작성 시 문서화된 내용을 체계적으로 활용하세요.")
    
    print("\n프롬프트 문서화 템플릿 작성 실습을 마칩니다.")

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
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")
