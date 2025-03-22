"""
코드 설명 및 주석 생성 전략

코드의 목적, 작동 방식, 로직을 명확하게 설명하는 문서와 주석 생성 기법
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """
    실습 코드 메인 함수
    """
    print("===== 코드 설명 및 주석 생성 전략 =====")
    
    # 사용자 입력 받기
    code = input("설명이 필요한 코드를 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    audience = input("설명 대상을 입력하세요 (예: 동료 개발자, 초보 프로그래머, 비개발자): ")
    documentation_type = input("원하는 문서화 형태를 입력하세요 (예: 인라인 주석, 함수 docstring, 기술문서): ")
    code_context = input("코드의 맥락이나 프로젝트 정보가 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드가 어떻게 동작하는지 설명해줘:

```{language}
{code}
```
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 설명 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("기술 문서화 및 코드 커뮤니케이션 전문가", 
                           f"복잡한 코드와 기술적 개념을 {audience} 수준에 맞게 명확하게 설명하고 문서화하는 데 특화된 전문가로, 효과적인 코드 주석과 기술 문서 작성에 풍부한 경험을 보유하고 있습니다.")
    
    # 맥락 제공
    context = f"대상 코드:\n```{language}\n{code}\n```\n\n" \
             f"프로그래밍 언어: {language}\n" \
             f"설명 대상: {audience}\n" \
             f"문서화 형태: {documentation_type}"
    
    if code_context:
        context += f"\n코드 맥락: {code_context}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 코드 분석 및 이해",
        "   - 코드의 목적과 전체적인 기능 파악",
        "   - 주요 알고리즘 및 로직 흐름 분석",
        "   - 핵심 함수 및 변수의 역할 식별",
        
        "2. 대상 맞춤 설명 생성",
        f"   - {audience}의 이해 수준과 배경 고려",
        "   - 적절한 상세도와 기술적 깊이 조절",
        "   - 필요시 비유나 시각적 설명 활용",
        
        "3. 구조화된 문서화 제공",
        f"   - {documentation_type} 형식에 맞는 문서화",
        f"   - {language} 문서화 관행 및 모범 사례 준수",
        "   - 명확하고 간결한 설명 작성",
        
        "4. 코드 주석 생성",
        "   - 코드 블록, 함수, 클래스 수준의 주석",
        "   - 복잡한 로직이나 비자명한 부분에 대한 인라인 주석",
        "   - 주석과 원본 코드의 통합 예시"
    ])
    
    # 출력 형식 지정
    sections = [
        "1. 코드 개요 및 목적",
        "2. 주요 구성 요소 설명",
        "3. 동작 흐름 및 로직 분석"
    ]
    
    if documentation_type.lower() in ["인라인 주석", "주석", "comments"]:
        sections.append("4. 주석이 포함된 코드")
    elif documentation_type.lower() in ["docstring", "함수 docstring"]:
        sections.append("4. 함수/클래스 Docstring 예시")
    elif documentation_type.lower() in ["기술문서", "문서", "documentation"]:
        sections.append("4. 기술 문서 형식의 상세 설명")
    else:
        sections.append("4. 문서화 및 주석 예시")
    
    sections.append("5. 활용 및 확장 가이드")
    
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n" + 
        "\n".join(sections) + 
        f"\n\n코드 블록은 {language} 문법 하이라이팅을 사용하고, {audience}가 이해하기 쉽도록 적절한 수준의 설명과 예시를 제공해주세요. {documentation_type} 형식에 맞게 내용을 구성하고, 필요한 경우 다이어그램이나 표를 활용하여 이해를 돕습니다."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 설명 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 설명 및 문서화 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_explanation.md): ") or "code_explanation.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 설명 및 문서화")
        print(f"코드 설명 및 문서화 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()