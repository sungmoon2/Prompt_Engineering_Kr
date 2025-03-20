"""
프롬프트 생성 도구 모듈

효과적인 프롬프트를 구성하는 다양한 패턴과 기법을 제공합니다.
"""

from typing import Dict, List, Any, Optional, Union

class PromptBuilder:
    """프롬프트 구성 클래스"""
    
    def __init__(self, base_prompt: Optional[str] = None):
        """
        프롬프트 빌더 초기화
        
        Args:
            base_prompt: 기본 프롬프트 (없으면 빈 문자열)
        """
        self.sections = []
        if base_prompt:
            self.sections.append(base_prompt)
    
    def add_text(self, text: str) -> 'PromptBuilder':
        """
        프롬프트에 일반 텍스트 추가
        
        Args:
            text: 추가할 텍스트
            
        Returns:
            self (메서드 체이닝용)
        """
        self.sections.append(text)
        return self
    
    def add_section(self, header: str, content: str) -> 'PromptBuilder':
        """
        프롬프트에 제목과 내용으로 구성된 섹션 추가
        
        Args:
            header: 섹션 제목
            content: 섹션 내용
            
        Returns:
            self (메서드 체이닝용)
        """
        self.sections.append(f"## {header}\n{content}")
        return self
    
    def add_role(self, role: str, details: Optional[str] = None) -> 'PromptBuilder':
        """
        프롬프트에 역할 설정 추가
        
        Args:
            role: 역할명
            details: 역할 상세 설명 (선택사항)
            
        Returns:
            self (메서드 체이닝용)
        """
        role_prompt = f"당신은 {role}입니다."
        
        if details:
            role_prompt += f" {details}"
        
        self.sections.append(role_prompt)
        return self
    
    def add_examples(self, examples: List[Dict[str, str]], 
                     input_key: str = "input", 
                     output_key: str = "output") -> 'PromptBuilder':
        """
        프롬프트에 예시 추가 (Few-shot 학습용)
        
        Args:
            examples: 예시 목록 (딕셔너리 형태)
            input_key: 입력값 키
            output_key: 출력값 키
            
        Returns:
            self (메서드 체이닝용)
        """
        examples_text = "# 예시\n\n"
        
        for i, example in enumerate(examples, 1):
            examples_text += f"## 예시 {i}\n"
            examples_text += f"입력: {example.get(input_key, '')}\n"
            examples_text += f"출력: {example.get(output_key, '')}\n\n"
        
        self.sections.append(examples_text)
        return self
    
    def add_instructions(self, instructions: Union[str, List[str]]) -> 'PromptBuilder':
        """
        프롬프트에 지시사항 추가
        
        Args:
            instructions: 지시사항 (문자열 또는 목록)
            
        Returns:
            self (메서드 체이닝용)
        """
        if isinstance(instructions, list):
            instr_text = "# 지시사항\n\n"
            for i, instruction in enumerate(instructions, 1):
                instr_text += f"{i}. {instruction}\n"
            self.sections.append(instr_text)
        else:
            self.sections.append(f"# 지시사항\n\n{instructions}")
        
        return self
    
    def add_format_instructions(self, output_format: str) -> 'PromptBuilder':
        """
        프롬프트에 출력 형식 지시사항 추가
        
        Args:
            output_format: 원하는 출력 형식 설명
            
        Returns:
            self (메서드 체이닝용)
        """
        self.sections.append(f"# 출력 형식\n\n{output_format}")
        return self
    
    def add_context(self, context: str, header: str = "맥락") -> 'PromptBuilder':
        """
        프롬프트에 맥락 정보 추가
        
        Args:
            context: 맥락 정보
            header: 섹션 제목
            
        Returns:
            self (메서드 체이닝용)
        """
        self.sections.append(f"# {header}\n\n{context}")
        return self
    
    def build(self) -> str:
        """
        최종 프롬프트 생성
        
        Returns:
            구성된 최종 프롬프트
        """
        return "\n\n".join(self.sections)
    
    def reset(self) -> 'PromptBuilder':
        """
        프롬프트 초기화
        
        Returns:
            self (메서드 체이닝용)
        """
        self.sections = []
        return self


def add_role(prompt: str, role: str, details: Optional[str] = None) -> str:
    """
    프롬프트에 역할 설정 추가하는 헬퍼 함수
    
    Args:
        prompt: 원본 프롬프트
        role: 역할명
        details: 역할 상세 설명 (선택사항)
        
    Returns:
        역할이 추가된 프롬프트
    """
    role_text = f"당신은 {role}입니다."
    if details:
        role_text += f" {details}"
    
    return f"{role_text}\n\n{prompt}"


def add_examples(prompt: str, examples: List[Dict[str, str]], 
                input_key: str = "input", 
                output_key: str = "output") -> str:
    """
    프롬프트에 예시 추가하는 헬퍼 함수 (Few-shot 학습용)
    
    Args:
        prompt: 원본 프롬프트
        examples: 예시 목록 (딕셔너리 형태)
        input_key: 입력값 키
        output_key: 출력값 키
        
    Returns:
        예시가 추가된 프롬프트
    """
    examples_text = "# 예시\n\n"
    
    for i, example in enumerate(examples, 1):
        examples_text += f"## 예시 {i}\n"
        examples_text += f"입력: {example.get(input_key, '')}\n"
        examples_text += f"출력: {example.get(output_key, '')}\n\n"
    
    return f"{examples_text}\n\n{prompt}"