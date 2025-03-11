"""
프롬프트 관리 유틸리티

이 모듈은 프롬프트 템플릿 관리, 포맷팅, 그리고 다양한 프롬프트 패턴 생성을 위한 
함수들을 제공합니다.
"""
import os
import json
import re

# 기본 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "samples", "templates")

# 필요한 디렉토리 생성
os.makedirs(TEMPLATE_DIR, exist_ok=True)

def format_prompt(template_name=None, **kwargs):
    """템플릿을 사용하여 프롬프트 포맷팅

    Args:
        template_name (str, optional): 템플릿 파일명. Defaults to None.
        **kwargs: 템플릿에 적용할 변수들

    Returns:
        str: 포맷팅된 프롬프트
    """
    # 템플릿 이름이 제공되면 파일에서 로드
    if template_name:
        template_path = os.path.join(TEMPLATE_DIR, f"{template_name}.txt")
        try:
            with open(template_path, "r", encoding="utf-8") as f:
                template = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"템플릿 파일을 찾을 수 없습니다: {template_path}")
    # kwargs에 'template' 키가 있으면 직접 사용
    elif 'template' in kwargs:
        template = kwargs.pop('template')
    else:
        raise ValueError("템플릿 이름이나 내용을 제공해야 합니다.")
    
    # 템플릿 변수 포맷팅
    return template.format(**kwargs)

def save_template(template_name, content):
    """템플릿 저장

    Args:
        template_name (str): 템플릿 이름
        content (str): 템플릿 내용

    Returns:
        str: 저장된 파일 경로
    """
    # 확장자가 없으면 .txt 추가
    if not template_name.endswith('.txt'):
        template_name = f"{template_name}.txt"
    
    filepath = os.path.join(TEMPLATE_DIR, template_name)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        raise Exception(f"템플릿 저장 중 오류 발생: {str(e)}")

def create_role_prompt(role, task, context=None, constraints=None):
    """역할 기반 프롬프트 생성

    Args:
        role (str): AI에게 부여할 역할
        task (str): 수행할 작업
        context (str, optional): 작업 컨텍스트. Defaults to None.
        constraints (list, optional): 제약사항 목록. Defaults to None.

    Returns:
        str: 조합된 역할 기반 프롬프트
    """
    prompt = f"당신은 {role}입니다.\n\n"
    
    if context:
        prompt += f"컨텍스트: {context}\n\n"
    
    prompt += f"작업: {task}\n\n"
    
    if constraints:
        prompt += "제약사항:\n"
        for i, constraint in enumerate(constraints, 1):
            prompt += f"{i}. {constraint}\n"
    
    return prompt

def create_academic_prompt(subject, topic, assignment_type, length=None, requirements=None):
    """학술적 프롬프트 생성

    Args:
        subject (str): 학문 분야
        topic (str): 주제
        assignment_type (str): 과제 유형 (에세이, 보고서, 리뷰 등)
        length (str, optional): 길이 요구사항. Defaults to None.
        requirements (list, optional): 추가 요구사항 목록. Defaults to None.

    Returns:
        str: 학술적 프롬프트
    """
    prompt = f"{subject} 분야의 '{topic}'에 관한 {assignment_type}을(를) 작성해주세요.\n\n"
    
    if length:
        prompt += f"길이: {length}\n\n"
    
    if requirements:
        prompt += "다음 요구사항을 충족해야 합니다:\n"
        for i, req in enumerate(requirements, 1):
            prompt += f"{i}. {req}\n"
    
    return prompt

def create_structured_prompt(question, output_format, sections=None, examples=None):
    """구조화된 프롬프트 생성

    Args:
        question (str): 주요 질문 또는 지시
        output_format (str): 원하는 출력 형식 설명
        sections (list, optional): 포함해야 할 섹션 목록. Defaults to None.
        examples (str, optional): 예시. Defaults to None.

    Returns:
        str: 구조화된 프롬프트
    """
    prompt = f"{question}\n\n"
    
    prompt += f"다음 형식으로 답변해주세요: {output_format}\n\n"
    
    if sections:
        prompt += "다음 섹션을 포함해주세요:\n"
        for i, section in enumerate(sections, 1):
            prompt += f"{i}. {section}\n"
        prompt += "\n"
    
    if examples:
        prompt += f"예시:\n{examples}\n"
    
    return prompt

def create_chain_of_thought_prompt(question, steps=True, reasoning=True, verification=False):
    """단계적 사고 유도(Chain-of-Thought) 프롬프트 생성

    Args:
        question (str): 주요 질문 또는 문제
        steps (bool, optional): 단계별 생각 지시 포함 여부. Defaults to True.
        reasoning (bool, optional): 추론 과정 요청 여부. Defaults to True.
        verification (bool, optional): 자가 검증 요청 여부. Defaults to False.

    Returns:
        str: Chain-of-Thought 프롬프트
    """
    prompt = f"{question}\n\n"
    
    if steps:
        prompt += "단계별로 생각해보세요.\n"
    
    if reasoning:
        prompt += "각 단계에서 당신의 추론 과정을 상세히 설명해주세요.\n"
    
    if verification:
        prompt += "최종 답변을 제시하기 전에, 당신의 접근 방식과 결론을 검증해주세요.\n"
    
    return prompt

def create_few_shot_prompt(task, examples, question):
    """Few-shot 학습 프롬프트 생성

    Args:
        task (str): 수행할 작업에 대한 설명
        examples (list): (입력, 출력) 튜플로 구성된 예시 목록
        question (str): 실제 질문 또는 입력

    Returns:
        str: Few-shot 프롬프트
    """
    prompt = f"{task}\n\n"
    
    for i, (input_ex, output_ex) in enumerate(examples, 1):
        prompt += f"예시 {i} 입력:\n{input_ex}\n\n"
        prompt += f"예시 {i} 출력:\n{output_ex}\n\n"
    
    prompt += f"입력:\n{question}\n\n출력:"
    
    return prompt