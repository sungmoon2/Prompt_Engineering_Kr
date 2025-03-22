"""
논증 구조 강화 및 근거 제시 기법

학술적 글쓰기에서 논증 구조를 강화하고 효과적인 근거를 제시하는 방법
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
    print("===== 논증 구조 강화 및 근거 제시 기법 =====")
    
    # 사용자 입력 받기
    topic = input("논증할 주제나 주장을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    argument_type = input("논증 유형을 입력하세요 (예: 인과적, 비교 대조, 평가적, 반론, 제안): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 주장을 어떻게 잘 논증할 수 있을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 논증 구조 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("논증 전문가 및 학술 담론 분석가", 
                           f"{field} 분야의 저명한 학자로서 효과적인 논증 구조와 설득력 있는 근거 제시 방법에 관한 저서와 강의로 유명합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"논증 주제: {topic}\n"
        f"학문 분야: {field}\n"
        f"논증 유형: {argument_type}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {topic}에 대한 {argument_type} 논증을 구성하는 효과적인 구조 설계",
        "2. 강력한 주장(thesis)을 구성하는 방법과 명확한 표현 기법",
        "3. 논증을 뒷받침하는 근거 유형과 특성 (실증적, 이론적, 권위적, 논리적 근거 등)",
        f"4. {field} 분야에서 신뢰할 수 있는 근거 선택 기준과 출처",
        "5. 주장-근거-보장(warrant) 간의 논리적 연결 강화 방법",
        "6. 예상 반론을 효과적으로 다루고 논증에 통합하는 전략",
        "7. 논증의 한계를 인정하면서도 설득력을 유지하는 방법",
        "8. 효과적인 논증 표현 및 연결 문구(transitions) 활용법",
        f"9. {argument_type} 논증에 특화된 구조적 요소와 표현 방식",
        "10. 논증 강화를 위한 자가 점검 체크리스트"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        f"1. {topic}에 대한 {argument_type} 논증 구조 설계\n"
        "2. 효과적인 근거 유형 및 선택 기준\n"
        "3. 논증 구성 요소별 작성 가이드\n"
        "4. 설득력 있는 논증 표현 전략\n"
        "5. 논증 구조 자가 점검 체크리스트\n\n"
        f"{topic}에 대한 구체적인 논증 예시와 근거 활용 사례를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 논증 구조 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n논증 구조 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: argumentation_guide.md): ") or "argumentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic}에 대한 {argument_type} 논증 구조 가이드")
        print(f"논증 구조 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()