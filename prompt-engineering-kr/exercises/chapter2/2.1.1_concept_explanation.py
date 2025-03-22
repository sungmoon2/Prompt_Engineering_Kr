"""
프로그래밍 개념 설명 프롬프트

복잡한 프로그래밍 개념을 이해하기 쉽게 설명받는 프롬프트 기법
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
    print("===== 프로그래밍 개념 설명 프롬프트 =====")
    
    # 사용자 입력 받기
    concept = input("이해하고 싶은 프로그래밍 개념을 입력하세요: ")
    language = input("관련 프로그래밍 언어를 입력하세요: ")
    level = input("자신의 프로그래밍 수준을 입력하세요 (초급/중급/고급): ")
    application = input("이 개념을 적용하고 싶은 분야나 프로젝트가 있다면 입력하세요 (선택사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{concept} 개념을 설명해줘. {language} 언어로 예시도 보여줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 개념 설명 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("프로그래밍 교육 전문가", 
                           f"10년 이상 {language} 언어를 가르치고 복잡한 개념을 이해하기 쉽게 설명하는 데 특화된 교수법 전문가입니다.")
    
    # 맥락 제공
    context = f"학습 개념: {concept}\n" \
             f"프로그래밍 언어: {language}\n" \
             f"학습자 수준: {level}"
    
    if application:
        context += f"\n적용 분야/프로젝트: {application}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {concept}의 핵심 개념을 {level} 수준에 맞게 명확하고 간결하게 설명해주세요.",
        "2. 일상적인 비유나 실생활 예시를 통해 개념을 이해하기 쉽게 설명해주세요.",
        f"3. {language} 언어로 실제 코드 예시를 제공해주세요. 코드는 간결하되 이해를 돕기 위한 주석을 포함해주세요.",
        "4. 이 개념이 왜 중요한지, 어떤 문제를 해결하는지 설명해주세요.",
        "5. 이 개념과 관련된 다른 개념들과의 관계를 설명해주세요.",
        "6. 흔히 발생하는 오해나 실수에 대해 알려주세요.",
        f"7. {level} 수준의 학습자가 이 개념을 마스터하기 위한 단계별 접근법을 제안해주세요.",
        "8. 이 개념을 확장하거나 더 깊이 탐구할 수 있는 고급 주제나 리소스를 추천해주세요."
    ])
    
    if application:
        prompt_builder.add_instructions([
            f"9. {application}에 이 개념을 적용하는 구체적인 방법과 예시를 제공해주세요.",
            f"10. {application} 맥락에서 이 개념의 가치와 한계점을 설명해주세요."
        ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 개념 소개 및 정의\n"
        "2. 쉬운 비유와 예시\n"
        "3. 코드 예시 (주석 포함)\n"
        "4. 개념의 중요성 및 활용 사례\n"
        "5. 관련 개념과의 관계\n"
        "6. 흔한 오해와 주의점\n"
        "7. 학습 단계 제안\n"
        "8. 추가 학습 자료\n\n"
        "코드 예시는 마크다운 코드 블록으로 제공해주세요. 필요한 경우 다이어그램이나 표를 활용하여 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 개념 설명 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n개념 설명을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: concept_explanation.md): ") or "concept_explanation.md"
        save_markdown(enhanced_result, file_path, title=f"{language} {concept} 개념 설명")
        print(f"개념 설명이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()