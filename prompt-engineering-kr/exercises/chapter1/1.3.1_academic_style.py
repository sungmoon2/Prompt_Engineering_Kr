"""
학술적 어투와 표현 최적화 프롬프트

학술 논문과 리포트에 적합한 어투와 표현을 최적화하는 프롬프트 기법
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
    print("===== 학술적 어투와 표현 최적화 프롬프트 =====")
    
    # 사용자 입력 받기
    field = input("학문 분야를 입력하세요: ")
    level = input("학술 수준을 입력하세요 (예: 학부, 대학원, 학술지): ")
    text_sample = input("변환하거나 개선할 텍스트 샘플을 입력하세요 (없으면 Enter): ")
    
    if not text_sample:
        text_sample = "AI는 요즘 정말 대세예요. 많은 사람들이 AI를 쓰고 있고, 이로 인해 생산성이 올라갔어요. 하지만 일부 문제점도 있죠. 앞으로 AI가 어떻게 발전할지 궁금해요."
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 텍스트를 학술적인 문체로 바꿔줘:

{text_sample}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 학술적 어투 변환 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 출판 편집자", 
                           f"저명한 {field} 학술지의 수석 편집자로서 수많은 논문을 검토하고 학술적 표현을 최적화해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"학문 분야: {field}\n"
        f"학술 수준: {level}\n"
        f"원문 텍스트 샘플:\n\n{text_sample}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 제공된 텍스트를 학술적 어투와 표현으로 최적화해주세요.",
        f"2. {field} 분야에 적합한 전문적 어휘와 표현을 사용해주세요.",
        f"3. {level} 수준에 맞는 복잡성과 정교함을 유지해주세요.",
        "4. 주관적 표현을 객관적 표현으로 바꿔주세요.",
        "5. 구어체와 비격식 표현을 학술적 문어체로 변환해주세요.",
        "6. 모호한 표현을 명확하고 정밀한 표현으로 개선해주세요.",
        "7. 적절한 헤지 표현(hedging)과 학술적 정확성을 위한 한정어를 추가해주세요.",
        "8. 변환된 문장의 논리적 흐름과 결속성을 강화해주세요.",
        "9. 변환 전후 텍스트를 비교하며 변경된 주요 요소와 이유를 설명해주세요.",
        "10. 학술적 글쓰기에서 일반적으로 피해야 할 표현과 지켜야 할 원칙을 정리해주세요."
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 변환된 학술적 텍스트\n"
        "2. 변환 전후 비교 분석\n"
        "3. 주요 변경 사항 및 이유\n"
        "4. 학술적 글쓰기 원칙과 지침\n"
        "5. 추가 개선을 위한 제안"
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 학술적 어투 변환 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n학술적 어투 변환 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: academic_style_guide.md): ") or "academic_style_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 분야 학술적 표현 최적화 가이드")
        print(f"학술적 어투 변환 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()