"""
객체지향 설계 최적화 프롬프트

객체지향 프로그래밍(OOP) 원칙에 따른 설계를 최적화하기 위한 프롬프트 패턴 활용
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import write_file, save_markdown

def main():
    """
    실습 코드 메인 함수
    """
    print("===== 객체지향 설계 최적화 프롬프트 =====")
    
    # 사용자 입력 받기
    project_name = input("프로젝트 이름을 입력하세요: ")
    description = input("프로젝트 설명을 간략히 입력하세요: ")
    programming_language = input("사용할 프로그래밍 언어를 입력하세요 (예: Python, Java, C# 등): ")
    
    # 추가 정보 입력 (선택사항)
    print("\n추가 정보 (선택사항)")
    entities = input("주요 엔티티/모델을 쉼표로 구분하여 입력하세요: ")
    requirements = input("주요 기능 요구사항을 쉼표로 구분하여 입력하세요: ")
    constraints = input("고려해야 할 제약사항이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{project_name}이라는 프로젝트를 객체지향 방식으로 설계해주세요. 
{description}

{programming_language} 언어를 사용할 예정입니다.
주요 클래스와 메소드를 알려주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 OOP 설계 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "객체지향 설계 전문가", 
        "당신은 SOLID 원칙, 디자인 패턴, 클린 코드, 도메인 주도 설계(DDD)에 정통한 소프트웨어 설계 아키텍트입니다."
    )
    
    # 컨텍스트 추가
    context = f"""
프로젝트 정보:
- 이름: {project_name}
- 설명: {description}
- 프로그래밍 언어: {programming_language}
"""
    
    if entities:
        context += f"- 주요 엔티티/모델: {entities}\n"
    if requirements:
        context += f"- 주요 기능 요구사항: {requirements}\n"
    if constraints:
        context += f"- 제약사항: {constraints}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "SOLID 원칙을 적용한 객체지향 설계를 제공해주세요",
        "주요 클래스와 그 책임, 주요 메소드를 정의해주세요",
        "클래스 간의 관계(상속, 컴포지션, 의존성 등)를 설명해주세요",
        "적절한 디자인 패턴을 적용하고 그 이유를 설명해주세요",
        "코드 구현 없이 UML과 유사한 클래스 다이어그램 형태로 표현해주세요",
        f"{programming_language} 언어의 특성과 관용적 표현을 고려해주세요"
    ]
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = """
다음 형식으로 설계를 제공해주세요:

1. **설계 요약**: 전체적인 아키텍처와 주요 설계 결정사항
2. **클래스 다이어그램**: ASCII/마크다운 형식의 클래스 다이어그램
3. **주요 클래스 설명**:
   - 클래스 이름과 책임
   - 주요 속성
   - 주요 메소드
   - 적용된 객체지향 원칙
4. **클래스 간 관계**: 의존성, 상속, 컴포지션 등
5. **디자인 패턴 적용**: 사용된 디자인 패턴과 적용 이유
6. **확장성 및 유지보수성**: 설계의 확장 방법
7. **예상 질문 및 고려사항**: 추가 논의가 필요한 부분
"""
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 OOP 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\nOOP 설계 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: oop_design.md): ") or "oop_design.md"
        save_markdown(enhanced_result, file_path, title=f"{project_name} OOP 설계")
        print(f"OOP 설계 결과가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()