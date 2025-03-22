"""
코드 동작 원리 이해를 위한 질문 방법

코드의 실행 과정과 작동 원리를 깊이 이해하기 위한 효과적인 질문 기법
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
    print("===== 코드 동작 원리 이해를 위한 질문 방법 =====")
    
    # 사용자 입력 받기
    code_snippet = input("분석할 코드 스니펫을 입력하세요: ")
    language = input("코드 언어를 입력하세요: ")
    focus = input("특별히 이해하고 싶은 측면을 입력하세요 (예: 메모리 사용, 성능, 알고리즘 로직): ")
    level = input("자신의 프로그래밍 수준을 입력하세요 (초급/중급/고급): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드가 어떻게 동작하는지 설명해줘:

```{language}
{code_snippet}
```
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{language} 전문 개발자 및 코드 분석가", 
                           f"{language} 언어의 내부 작동 방식에 대한 깊은 이해를 가지고 있으며, 코드 분석 및 최적화에 특화된 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"분석할 코드:\n```{language}\n{code_snippet}\n```\n\n"
        f"코드 언어: {language}\n"
        f"관심 영역: {focus}\n"
        f"학습자 수준: {level}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 아래 소크라테스식 질문 방법을 활용하여 코드 분석을 진행해주세요:",
        "   a. 코드의 기본 목적과 기능에 대한 질문",
        "   b. 각 구성 요소(변수, 함수, 클래스 등)의 역할에 대한 질문",
        "   c. 코드 실행 과정을 단계별로 추적하는 질문",
        "   d. 특정 라인이나 블록의 존재 이유를 묻는 질문",
        f"   e. {focus}와 관련된 심층적 질문",
        "   f. 코드의 효율성과 최적화에 관한 질문",
        "   g. 대안적 구현 방법을 탐색하는 질문",
        "   h. 잠재적 오류나 예외 상황을 고려하는 질문",
        
        "2. 각 질문에 대한 명확하고 교육적인 답변을 제공해주세요.",
        
        f"3. {level} 수준의 학습자가 이해할 수 있는 설명을 제공하되, 점진적으로 깊이 있는 개념으로 안내해주세요.",
        
        "4. 질문과 답변을 통해 코드의 실행 흐름을 시각화할 수 있도록 도와주세요.",
        
        "5. 필요한 경우 코드의 실행 결과나 중간 상태를 예시로 보여주세요.",
        
        "6. 비유와 은유를 활용하여 복잡한 개념을 이해하기 쉽게 설명해주세요.",
        
        "7. 학습자가 스스로 더 탐구해볼 수 있는 후속 질문이나 실험을 제안해주세요."
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 코드 개요 및 목적\n"
        "2. 코드 구성 요소 분석 (소크라테스식 질문-답변 형식)\n"
        "3. 실행 흐름 추적 (소크라테스식 질문-답변 형식)\n"
        "4. 심층 분석: " + focus + " (소크라테스식 질문-답변 형식)\n"
        "5. 대안적 접근법 탐색 (소크라테스식 질문-답변 형식)\n"
        "6. 핵심 통찰 및 학습 포인트\n"
        "7. 추가 탐구를 위한 질문\n\n"
        "소크라테스식 질문-답변 형식으로 독자가 코드의 동작 원리를 단계적으로 이해할 수 있도록 안내해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 분석을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_analysis.md): ") or "code_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 동작 원리 분석")
        print(f"코드 분석이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()