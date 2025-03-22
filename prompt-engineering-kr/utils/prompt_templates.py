"""
프롬프트 템플릿 모듈

목차의 각 파트에서 사용되는 기본 및 향상된 프롬프트 템플릿을 제공합니다.
"""

from typing import Dict, List, Any, Optional
from utils.prompt_builder import PromptBuilder

# Part 1: 기초 프롬프트 작성법 템플릿
def get_basic_knowledge_prompt(topic: str) -> str:
    """
    배경 지식 없는 기본 프롬프트 생성
    
    Args:
        topic: 질문할 주제
        
    Returns:
        기본 프롬프트
    """
    return f"{topic}에 대해 알려주세요."

def get_enhanced_knowledge_prompt(topic: str) -> str:
    """
    배경 지식 없는 향상된 프롬프트 생성
    
    Args:
        topic: 질문할 주제
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role("전문 교육자", f"{topic}에 대해 초보자에게 설명해주는 전문가")
    
    builder.add_context(
        f"저는 {topic}에 대해 아무것도 모릅니다. 이 분야의 기본 개념부터 차근차근 이해하고 싶습니다."
    )
    
    builder.add_instructions([
        "가장 기초적인 개념부터 설명해주세요",
        "전문 용어가 나올 경우 바로 풀어서 설명해주세요",
        "실생활에서 볼 수 있는 비유나 예시를 들어주세요",
        "이 주제를 이해하기 위한 사전 지식이 있다면 알려주세요",
        "처음 접하는 초보자도 이해할 수 있는 수준으로 설명해주세요",
        "더 알아보기 위해 물어볼 수 있는 후속 질문 3개를 제안해주세요"
    ])
    
    builder.add_format_instructions(
        "단계별로 명확하게 설명해주세요. 복잡한 개념은 더 작은 부분으로 나누어 설명해주세요."
    )
    
    return builder.build()

def get_basic_clear_instruction_prompt(task: str) -> str:
    """
    명확한 지시문 기본 프롬프트 생성
    
    Args:
        task: 요청할 작업
        
    Returns:
        기본 프롬프트
    """
    return f"{task}에 대해 알려주세요."

def get_enhanced_clear_instruction_prompt(task: str, purpose: str, output_format: str) -> str:
    """
    명확한 지시문 향상된 프롬프트 생성
    
    Args:
        task: 요청할 작업
        purpose: 정보를 사용할 목적
        output_format: 원하는 출력 형식
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    
    builder.add_context(
        f"저는 {purpose}를 위해 {task}에 대한 정보가 필요합니다."
    )
    
    builder.add_instructions([
        f"정확하고 구체적인 {task}에 대한 정보를 제공해주세요",
        "핵심 개념과 중요 포인트를 명확하게 설명해주세요",
        "가능하면 단계별로 구분하여 설명해주세요",
        "실제 예시나 사례를 포함해주세요",
        "전문 용어가 있다면 간략한 설명을 함께 제공해주세요"
    ])
    
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 제공해주세요."
    )
    
    return builder.build()

# Part 2: 복잡한 과제 분해하기 템플릿
def get_basic_task_decomposition_prompt(task: str) -> str:
    """
    과제 분해 기본 프롬프트 생성
    
    Args:
        task: 분해할 과제
        
    Returns:
        기본 프롬프트
    """
    return f"""
다음 과제를 어떻게 진행해야 할지 단계별로 알려주세요:
{task}
"""

def get_enhanced_task_decomposition_prompt(task: str, domain: str) -> str:
    """
    과제 분해 향상된 프롬프트 생성
    
    Args:
        task: 분해할 과제
        domain: 과제 도메인
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        f"{domain} 프로젝트 관리자", 
        f"{domain} 분야에서 복잡한 프로젝트를 체계적으로 분해하고 관리하는 전문가로, 다년간의 경험을 통해 효율적인 과제 분석 및 실행 계획을 수립합니다."
    )
    
    builder.add_context(
        f"분석할 과제: {task}\n"
        f"분야: {domain}\n"
        "목표: 이 복잡한 과제를 관리 가능한 작은 단계로 분해하고 체계적인 접근 방법을 개발하려 합니다. "
        "대학생이 이 과제를 처음부터 끝까지 효과적으로 수행할 수 있도록 구체적인 안내가 필요합니다."
    )
    
    builder.add_instructions([
        "1. 과제의 최종 목표와 핵심 요구사항 분석",
        "2. 5W1H 프레임워크를 사용한 과제 분석 (Who, What, When, Where, Why, How)",
        "3. 과제를 5-8개의 주요 단계로 분해",
        "4. 각 단계별 세부 작업과 필요한 자원 식별",
        "5. 각 단계의 예상 난이도와 소요 시간 평가",
        "6. 단계 간 의존성과 우선순위 파악",
        "7. 각 단계에서 발생할 수 있는 도전과제와 대응 전략 제안",
        "8. 전체 과제 완료를 위한 체계적인 워크플로우 제시"
    ])
    
    builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 과제 개요 및 목표 분석\n"
        "2. 5W1H 분석\n"
        "3. 주요 단계 분해 (5-8단계)\n"
        "4. 단계별 세부 작업 및 자원\n"
        "5. 워크플로우 다이어그램\n"
        "6. 실행 계획 및 일정\n"
        "7. 잠재적 도전과제 및 대응 전략\n\n"
        "가능한 표와 목록을 활용하여 정보를 명확하게 구조화해주세요."
    )
    
    return builder.build()

# Part 3: 맥락 유지와 대화 관리 템플릿
def get_basic_conversation_prompt(previous_context: str, new_question: str) -> str:
    """
    대화 맥락 유지 기본 프롬프트 생성
    
    Args:
        previous_context: 이전 대화 맥락
        new_question: 새로운 질문
        
    Returns:
        기본 프롬프트
    """
    return f"""
이전 대화 내용:
{previous_context}

새로운 질문:
{new_question}
"""

def get_enhanced_conversation_prompt(previous_context: str, key_points: List[str], new_question: str) -> str:
    """
    대화 맥락 유지 향상된 프롬프트 생성
    
    Args:
        previous_context: 이전 대화 맥락 요약
        key_points: 이전 대화의 핵심 포인트 목록
        new_question: 새로운 질문
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    
    # 이전 맥락 요약
    context = f"이전 대화 맥락 요약:\n{previous_context}\n\n"
    
    # 핵심 포인트 추가
    context += "핵심 포인트:\n"
    for i, point in enumerate(key_points, 1):
        context += f"{i}. {point}\n"
    
    builder.add_context(context)
    
    builder.add_instructions([
        "이전 대화 맥락을 고려하여 응답해주세요",
        "이전에 논의된 핵심 포인트를 기억하고 연결성 있게 답변해주세요",
        "맥락상 불분명한 부분이 있다면 명확히 해주세요",
        "새로운 정보와 이전 정보를 일관성 있게 통합해주세요"
    ])
    
    builder.add_text(f"새로운 질문: {new_question}")
    
    return builder.build()

# Part 4: 학술 에세이 및 보고서 작성 템플릿
def get_basic_academic_writing_prompt(topic: str, type: str = "에세이") -> str:
    """
    학술 글쓰기 기본 프롬프트 생성
    
    Args:
        topic: 글쓰기 주제
        type: 글쓰기 유형 (에세이, 보고서 등)
        
    Returns:
        기본 프롬프트
    """
    return f"""
다음 주제에 대한 {type}의 구조와 주요 내용을 개발해주세요:

주제: {topic}
"""

def get_enhanced_academic_writing_prompt(topic: str, field: str, type: str = "에세이") -> str:
    """
    학술 글쓰기 향상된 프롬프트 생성
    
    Args:
        topic: 글쓰기 주제
        field: 학문 분야
        type: 글쓰기 유형 (에세이, 보고서 등)
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        f"{field} 학술 글쓰기 전문가", 
        f"{field} 분야에서 학술 {type}를 지도하는 교수로, 논리적 구조와 학술적 표현에 대한 깊은 이해를 갖고 있습니다."
    )
    
    builder.add_context(
        f"작성할 {type} 주제: {topic}\n"
        f"학문 분야: {field}\n"
        f"목표: 논리적이고 설득력 있는 학술 {type}의 구조와 내용을 개발하고자 합니다. "
        f"대학생의 {type} 작성을 가이드할 수 있는 상세한 안내가 필요합니다."
    )
    
    builder.add_instructions([
        f"1. {topic}에 대한 핵심 논점 및 연구 질문 도출",
        f"2. {type}의 논리적 구조 설계 (서론, 본론, 결론의 세부 구성)",
        "3. 각 섹션에서 다룰 주요 내용과 논증 방식 제안",
        "4. 적절한 학술적 표현과 용어 제시",
        "5. 효과적인 인용 및 참고문헌 활용 방법",
        f"6. {field} 분야에서 중요한 학술적 관점 및 이론 제안",
        f"7. {type} 작성 시 흔히 범하는 실수와 주의점"
    ])
    
    builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        f"1. {topic} 분석 및 접근법\n"
        f"2. {type} 구조 설계\n"
        "3. 주요 논점 및 논증 전략\n"
        "4. 섹션별 상세 내용 가이드\n"
        "5. 학술적 표현 및 용어 제안\n"
        "6. 인용 및 참고문헌 전략\n"
        "7. 작성 팁 및 주의사항\n\n"
        "가능한 글머리 기호와 번호 매기기를 활용하여 명확하게 구조화해주세요."
    )
    
    return builder.build()

# Part 5: 프로그래밍 과제 해결 템플릿
def get_basic_coding_prompt(task: str, language: str) -> str:
    """
    프로그래밍 과제 기본 프롬프트 생성
    
    Args:
        task: 코딩 과제
        language: 프로그래밍 언어
        
    Returns:
        기본 프롬프트
    """
    return f"""
{language}로 다음 프로그램을 작성해주세요:
{task}
"""

def get_enhanced_coding_prompt(task: str, language: str, features: str = "", level: str = "중급") -> str:
    """
    프로그래밍 과제 향상된 프롬프트 생성
    
    Args:
        task: 코딩 과제
        language: 프로그래밍 언어
        features: 특별 요구사항/기능
        level: 난이도 수준
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        f"{language} 개발 전문가", 
        f"{language} 프로그래밍에 깊은 전문성을 가진 시니어 개발자로, 클린 코드, 효율적인 알고리즘, 사용자 친화적 디자인에 중점을 둡니다."
    )
    
    context = f"개발 과제: {task}\n프로그래밍 언어: {language}\n난이도 수준: {level}"
    if features:
        context += f"\n특별 요구사항: {features}"
    
    builder.add_context(context)
    
    builder.add_instructions([
        "1. 코드 설계 및 구조",
        f"   - {language}의 모범 사례에 따른 파일 및 함수 구조 설계",
        "   - 관심사 분리와 모듈화 원칙 적용",
        "   - 확장성과 유지보수성을 고려한 구조",
        
        "2. 코드 구현",
        "   - 명확하고 이해하기 쉬운 코드 작성",
        "   - 각 함수와 클래스의 목적과 책임 명확히 정의",
        "   - 포괄적인 오류 처리 및 예외 관리",
        
        "3. 기능 최적화",
        f"   - {language}에 최적화된 알고리즘 및 데이터 구조 활용",
        "   - 성능과 메모리 사용 고려",
        "   - 병목 현상이 발생할 수 있는 부분 식별 및 최적화",
        
        "4. 사용자 경험",
        "   - 직관적이고 사용하기 쉬운 인터페이스 설계",
        "   - 명확한 사용자 피드백 및 오류 메시지 제공",
        "   - 다양한 사용자 상황 고려"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n\n"
        "1. **설계 개요**: 전체 구조와 주요 컴포넌트 설명\n"
        "2. **구현 코드**: 완전한 소스 코드 (파일별로 구분)\n"
        "3. **주요 함수/클래스 설명**: 각 구성 요소의 목적과 작동 방식\n"
        "4. **사용 방법**: 프로그램 설치 및 실행 방법\n"
        "5. **확장 및 개선 가능성**: 추가할 수 있는 기능 제안\n\n"
        f"코드는 {language} 문법 하이라이팅이 적용된 마크다운 코드 블록으로 제공해주세요."
    )
    
    return builder.build()

# Part 6: 도메인별 프롬프트 최적화 템플릿
def get_basic_domain_prompt(topic: str, field: str) -> str:
    """
    특정 도메인 기본 프롬프트 생성
    
    Args:
        topic: 주제
        field: 학문/도메인 분야
        
    Returns:
        기본 프롬프트
    """
    return f"""
{field} 분야에서 {topic}에 대해 알려주세요.
"""

def get_enhanced_domain_prompt(topic: str, field: str, purpose: str, expertise_level: str = "초보자") -> str:
    """
    특정 도메인 향상된 프롬프트 생성
    
    Args:
        topic: 주제
        field: 학문/도메인 분야
        purpose: 목적
        expertise_level: 전문성 수준
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        f"{field} 전문가", 
        f"{field} 분야에서 {topic}에 대한 깊은 지식과 경험을 갖춘 전문가"
    )
    
    builder.add_context(
        f"주제: {field} 분야의 {topic}\n"
        f"목적: {purpose}\n"
        f"지식 수준: {expertise_level}\n"
        f"저는 {field} 분야에서 {expertise_level} 수준으로, {purpose}를 위해 이 정보가 필요합니다."
    )
    
    # 분야별 맞춤 지시사항
    field_specific_instructions = {
        "경영학": [
            "비즈니스 맥락과 실제 적용 사례 포함",
            "주요 이론과 모델의 실용적 측면 강조",
            "최신 산업 트렌드와 연결"
        ],
        "심리학": [
            "주요 연구 방법론과 발견 설명",
            "이론적 기반과 실제 임상 적용 연결",
            "윤리적 고려사항 설명"
        ],
        "컴퓨터과학": [
            "기술적 개념의 단계별 설명",
            "코드 예시나 알고리즘 설명 포함",
            "실제 구현 사례 및 성능 고려사항"
        ],
        "문학/어학": [
            "주요 텍스트, 작가, 이론적 접근법 설명",
            "사회문화적 맥락 제공",
            "분석 및 해석 방법론 설명"
        ]
    }
    
    # 기본 지시사항 설정
    instructions = [
        f"{field} 분야의 {topic}에 대한 핵심 개념 설명",
        f"{expertise_level} 수준에 맞는 전문 용어 및 개념 설명",
        "주요 연구자, 학파, 이론 소개",
        f"{purpose}에 직접적으로 관련된 정보 강조"
    ]
    
    # 분야별 특화 지시사항 추가
    if field in field_specific_instructions:
        instructions.extend(field_specific_instructions[field])
    
    builder.add_instructions(instructions)
    
    builder.add_format_instructions(
        "다음 구조로 응답해주세요:\n"
        "1. 개요 및 핵심 개념\n"
        "2. 역사적/이론적 배경\n"
        "3. 주요 접근법 및 방법론\n"
        "4. 현대적 적용 및 중요성\n"
        "5. 핵심 참고자료 및 추가 학습 자원\n\n"
        f"{field} 분야의 전문성을 반영하는 용어와 구조를 활용하되, {expertise_level} 수준에서 이해할 수 있도록 설명해주세요."
    )
    
    return builder.build()

# Part 7: 고급 프롬프트 테크닉 템플릿
def get_basic_role_prompt(question: str, field: str) -> str:
    """
    역할 기반 기본 프롬프트 생성
    
    Args:
        question: 질문
        field: 분야
        
    Returns:
        기본 프롬프트
    """
    return f"""
{field} 전문가로서 다음 질문에 답해주세요:
{question}
"""

def get_enhanced_role_prompt(question: str, role: str, role_description: str, perspective: str = "") -> str:
    """
    역할 기반 향상된 프롬프트 생성
    
    Args:
        question: 질문
        role: 역할 (예: 심리학 교수)
        role_description: 역할 상세 설명
        perspective: 특정 관점 (선택사항)
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(role, role_description)
    
    context = f"다음 질문에 {role}의 관점에서 답변해주세요:"
    if perspective:
        context += f"\n특히 {perspective} 관점에서 접근해주세요."
    
    builder.add_context(context)
    builder.add_text(f"질문: {question}")
    
    builder.add_instructions([
        f"{role}의 전문성과 배경지식을 활용하여 답변해주세요",
        "관련 이론, 연구, 방법론을 언급해주세요",
        "실무적 경험이나 사례를 통한 통찰을 제공해주세요",
        "복잡한 개념은 이해하기 쉽게 설명해주세요"
    ])
    
    return builder.build()

def get_basic_cot_prompt(problem: str) -> str:
    """
    단계적 사고 기본 프롬프트 생성
    
    Args:
        problem: 문제
        
    Returns:
        기본 프롬프트
    """
    return f"""
다음 문제를 해결해주세요:
{problem}
"""

def get_enhanced_cot_prompt(problem: str, complexity: str = "중간") -> str:
    """
    단계적 사고 향상된 프롬프트 생성
    
    Args:
        problem: 문제
        complexity: 복잡도
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        "논리적 사고 전문가", 
        "복잡한 문제를 단계별로 분석하고 해결하는 전문가로, 명확한 사고 과정과 논리적 접근법을 중시합니다."
    )
    
    builder.add_context(
        f"다음 {complexity} 난이도의 문제를 단계적 사고 과정을 통해 해결해주세요:"
    )
    
    builder.add_text(f"문제: {problem}")
    
    builder.add_instructions([
        "문제를 이해하고 핵심 요소를 파악하세요",
        "가능한 해결 접근법을 검토하세요",
        "선택한 접근법에 따라 단계별로 문제를 해결하세요",
        "각 단계마다 '단계 X:'라고 명시하고 해당 단계의 사고 과정을 상세히 설명하세요",
        "중간 결과와 계산 과정을 모두 표시하세요",
        "최종 결론을 도출하세요",
        "필요시 해결책의 한계나 대안도 언급하세요"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 답변해주세요:\n\n"
        "**문제 분석:**\n[문제의 핵심 요소 파악]\n\n"
        "**접근법 검토:**\n[가능한 접근법들과 선택 이유]\n\n"
        "**단계별 풀이:**\n"
        "단계 1: [첫 번째 단계 설명]\n"
        "단계 2: [두 번째 단계 설명]\n"
        "...\n"
        "단계 N: [마지막 단계 설명]\n\n"
        "**최종 결론:**\n[최종 답변]\n\n"
        "**추가 고려사항:**\n[한계, 대안 등]"
    )
    
    return builder.build()

# Part 8: 프롬프트 디버깅과 개선 템플릿
def get_prompt_analysis(original_prompt: str) -> str:
    """
    프롬프트 분석 및 개선 프롬프트 생성
    
    Args:
        original_prompt: 분석할 원본 프롬프트
        
    Returns:
        분석 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        "프롬프트 엔지니어링 전문가", 
        "생성형 AI를 위한 효과적인 프롬프트를 설계하고 개선하는 전문가"
    )
    
    builder.add_context(
        "다음 프롬프트를 분석하고 개선점을 제안해주세요:"
    )
    
    builder.add_text(f"원본 프롬프트:\n'''\n{original_prompt}\n'''")
    
    builder.add_instructions([
        "프롬프트의 구성 요소를 분석해주세요 (역할, 맥락, 지시사항 등)",
        "프롬프트의 강점과 약점을 파악해주세요",
        "모호하거나 명확하지 않은 부분이 있는지 확인해주세요",
        "더 구체적이고 효과적인 표현으로 대체할 수 있는 부분을 제안해주세요",
        "프롬프트의 구조와 흐름을 개선할 방법을 제시해주세요",
        "위 분석을 바탕으로 개선된 프롬프트를 작성해주세요"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n\n"
        "**프롬프트 분석:**\n\n"
        "1. 구성 요소: [역할, 맥락, 지시사항 등 식별]\n"
        "2. 강점: [프롬프트의 장점들]\n"
        "3. 약점: [개선이 필요한 부분들]\n\n"
        "**개선 제안:**\n\n"
        "1. 구체성 향상: [더 명확하게 할 수 있는 부분]\n"
        "2. 구조 개선: [구성 변경 제안]\n"
        "3. 표현 개선: [더 효과적인 단어/표현 제안]\n\n"
        "**개선된 프롬프트:**\n\n"
        "[여기에 개선된 프롬프트 작성]"
    )
    
    return builder.build()

def get_enhanced_prompt_debugging(original_prompt: str, desired_output: str, actual_output: str) -> str:
    """
    프롬프트 디버깅 및 개선 향상된 프롬프트 생성
    
    Args:
        original_prompt: 원본 프롬프트
        desired_output: 원하는 출력 샘플
        actual_output: 실제 받은 출력 샘플
        
    Returns:
        향상된 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        "프롬프트 디버깅 전문가", 
        "문제가 있는 프롬프트를 분석하고 구체적인 개선점을 찾아내는 전문가"
    )
    
    builder.add_context(
        "다음 프롬프트와 그 결과를 분석하여 문제점을 찾고 개선해주세요:"
    )
    
    builder.add_text(f"원본 프롬프트:\n'''\n{original_prompt}\n'''")
    builder.add_text(f"\n원하는 출력 예시:\n'''\n{desired_output}\n'''")
    builder.add_text(f"\n실제 받은 출력 예시:\n'''\n{actual_output}\n'''")
    
    builder.add_instructions([
        "프롬프트와 결과 간의 불일치를 분석해주세요",
        "프롬프트에서 모호하거나 오해의 소지가 있는 부분을 식별해주세요",
        "빠졌거나 추가되어야 할 중요한 정보나 지시사항을 파악해주세요",
        "프롬프트의 구조, 명확성, 구체성 측면에서 개선점을 제안해주세요",
        "원하는 출력을 얻기 위한 개선된 프롬프트를 작성해주세요"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n\n"
        "**불일치 분석:**\n[원하는 출력과 실제 출력 간의 차이점 분석]\n\n"
        "**문제점 식별:**\n\n"
        "1. [문제점 1]\n"
        "2. [문제점 2]\n"
        "...\n\n"
        "**개선 전략:**\n\n"
        "1. [전략 1]\n"
        "2. [전략 2]\n"
        "...\n\n"
        "**개선된 프롬프트:**\n\n"
        "[여기에 개선된 프롬프트 작성]"
    )
    
    return builder.build()

# Part 9: 윤리적 활용과 한계 인식 템플릿
def get_ethical_usage_prompt(topic: str, purpose: str) -> str:
    """
    윤리적 AI 활용을 위한 프롬프트 생성
    
    Args:
        topic: 주제
        purpose: 용도
        
    Returns:
        윤리적 활용 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        "학술 윤리 전문가", 
        "AI 활용의 윤리적 측면과 학문적 진실성에 대한 깊은 이해를 갖춘 전문가"
    )
    
    builder.add_context(
        f"주제: {topic}\n"
        f"용도: {purpose}\n\n"
        "AI 활용과 학문적 진실성의 균형에 대해 조언이 필요합니다."
    )
    
    builder.add_instructions([
        f"{topic}에 관한 연구/과제에서 AI를 윤리적으로 활용하는 방법을 제안해주세요",
        "AI 활용이 적절한 영역과 그렇지 않은 영역을 구분해주세요",
        "학문적 진실성을 유지하면서 AI를 보조 도구로 활용하는 구체적인 방법을 제시해주세요",
        "AI 생성 내용을 적절히 인용하고 참조하는 방법을 설명해주세요",
        "AI 활용의 잠재적 함정과 이를 피하는 방법을 설명해주세요"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n\n"
        "**AI 활용의 윤리적 경계:**\n[적절한 활용과 부적절한 활용의 구분]\n\n"
        "**학문적 진실성 유지 방법:**\n[AI를 사용하면서 학문적 진실성을 지키는 구체적 방법]\n\n"
        "**적절한 인용 및 참조 방법:**\n[AI 생성 내용을 인용할 때의 가이드라인]\n\n"
        "**잠재적 함정과 주의사항:**\n[주의해야 할 문제와 이를 피하는 방법]\n\n"
        "**모범 사례:**\n[윤리적 AI 활용의 구체적 예시]"
    )
    
    return builder.build()

def get_ai_critical_evaluation_prompt(ai_response: str, topic: str) -> str:
    """
    AI 응답에 대한 비판적 평가 프롬프트 생성
    
    Args:
        ai_response: AI가 생성한 응답
        topic: 주제
        
    Returns:
        비판적 평가 프롬프트
    """
    builder = PromptBuilder()
    builder.add_role(
        f"{topic} 전문가", 
        f"{topic} 분야의 깊은 지식과 비판적 분석 능력을 갖춘 전문가"
    )
    
    builder.add_context(
        f"다음은 {topic}에 관한 AI 생성 응답입니다. 이 내용을 비판적으로 평가해주세요:"
    )
    
    builder.add_text(f"AI 응답:\n'''\n{ai_response}\n'''")
    
    builder.add_instructions([
        "제공된 정보의 사실적 정확성을 평가해주세요",
        "누락되었거나 불완전한 정보가 있는지 식별해주세요",
        "편향되거나 한쪽으로 치우친 관점이 있는지 확인해주세요",
        "추가적인 맥락이나 중요한 정보를 제공해주세요",
        "정보의 출처나 근거가 필요한 주장이 있는지 지적해주세요",
        "AI 응답의 한계를 넘어서는 추가 고려사항을 제시해주세요"
    ])
    
    builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n\n"
        "**정확성 평가:**\n[사실적 정확성에 대한 평가]\n\n"
        "**불완전/누락된 정보:**\n[추가되어야 할 중요한 정보]\n\n"
        "**편향 및 관점 분석:**\n[편향되거나 한쪽으로 치우친 부분 식별]\n\n"
        "**추가 맥락 및 고려사항:**\n[더 넓은 맥락에서 고려해야 할 사항]\n\n"
        "**결론:**\n[전반적인 평가 및 AI 응답 활용에 대한 조언]"
    )
    
    return builder.build()

# 프롬프트 요약 포인트 (UI 표시용)
PROMPT_SUMMARY = {
    "basic_knowledge": ["주제에 대한 직접적인 질문"],
    "enhanced_knowledge": [
        "역할 지정: 전문 교육자",
        "지식 수준 명시: 아무것도 모르는 상태",
        "구체적 지시사항: 6가지 세부 요청",
        "출력 형식 지정: 단계별 설명 요청"
    ],
    "basic_task": ["과제에 대한 단계별 접근 요청"],
    "enhanced_task": [
        "역할 지정: 프로젝트 관리자",
        "상세 맥락 제공: 과제, 분야, 목표 명시",
        "구체적 지시사항: 8단계 분석 프레임워크",
        "출력 형식 지정: 7개 섹션으로 구조화된 마크다운"
    ],
    "basic_academic": ["주제에 대한 구조와 내용 요청"],
    "enhanced_academic": [
        "역할 지정: 학술 글쓰기 전문가",
        "상세 맥락 제공: 주제, 분야, 목표 명시",
        "구체적 지시사항: 7가지 글쓰기 지침",
        "출력 형식 지정: 구조화된 마크다운 섹션"
    ],
    "basic_coding": ["프로그램 작성 직접 요청"],
    "enhanced_coding": [
        "역할 지정: 개발 전문가",
        "상세 맥락 제공: 과제, 언어, 난이도, 요구사항",
        "구체적 지시사항: 4가지 영역별 개발 지침",
        "출력 형식 지정: 5개 섹션으로 구조화"
    ],
    "basic_domain": ["분야별 주제에 대한 직접 질문"],
    "enhanced_domain": [
        "역할 지정: 분야별 전문가",
        "상세 맥락 제공: 목적, 지식 수준 명시",
        "분야별 맞춤 지시사항",
        "출력 형식 지정: 학문 분야에 맞는 구조화"
    ],
    "basic_cot": ["문제 직접 제시"],
    "enhanced_cot": [
        "역할 지정: 논리적 사고 전문가",
        "단계별 사고 과정 요청",
        "상세한 설명 지시",
        "출력 형식 지정: 체계적 문제 해결 구조"
    ]
}

# 학습 포인트 모음 (UI 표시용)
LEARNING_POINTS = {
    "knowledge": [
        "자신의 지식 수준을 명확히 전달하는 것이 중요합니다",
        "적절한 역할 지정으로 AI의 응답 방식을 유도할 수 있습니다",
        "구체적인 지시사항이 더 체계적인 응답을 이끌어냅니다",
        "낯선 주제를 탐색할 때는 단계적 접근이 효과적입니다"
    ],
    "task": [
        "복잡한 과제는 체계적으로 분해하면 관리하기 쉬워집니다",
        "5W1H 프레임워크는 과제 분석에 효과적입니다",
        "역할 지정은 전문적인 관점을 이끌어냅니다",
        "형식을 지정하면 더 체계적인 분석 결과를 얻을 수 있습니다"
    ],
    "academic": [
        "학술 글쓰기에는 분야별 특화된 접근이 필요합니다",
        "구체적인 구조 요청이 논리적 흐름을 개선합니다",
        "전문가 역할 부여로 학술적 깊이를 더할 수 있습니다",
        "목적과 대상 독자를 명시하면 더 적합한 내용을 얻을 수 있습니다"
    ],
    "coding": [
        "코딩 요청에는 언어와 함께 구체적인 기능 설명이 중요합니다",
        "설계부터 구현까지 단계별 접근이 더 완성도 높은 코드를 만듭니다",
        "성능, 가독성, 확장성 등 다양한 측면을 고려해 요청할 수 있습니다",
        "특정 프로그래밍 모범 사례를 언급하면 더 나은 코드를 얻을 수 있습니다"
    ]
}