"""
참고문헌 및 인용 최적화 전략

학술적 인용과 참고문헌 관리를 최적화하는 프롬프트 기법
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
    print("===== 참고문헌 및 인용 최적화 전략 =====")
    
    # 사용자 입력 받기
    citation_style = input("사용할 인용 스타일을 입력하세요 (예: APA, MLA, Chicago, Harvard): ")
    field = input("학문 분야를 입력하세요: ")
    reference_info = input("참고문헌 정보를 입력하세요 (저자, 제목, 출판정보 등): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{reference_info}를 {citation_style} 스타일로 인용하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 인용 최적화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 출판 및 인용 전문가", 
                         "주요 학술지의 편집위원으로 활동하며 다양한 인용 스타일에 대한 심층적인 이해를 갖고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"인용 스타일: {citation_style}\n"
        f"학문 분야: {field}\n"
        f"참고문헌 정보:\n{reference_info}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"{citation_style} 스타일의 정확한 인용 형식 제공 (본문 내 인용 및 참고문헌 목록용)",
        f"{field} 분야에서 효과적인 인용 전략 제안",
        "인용 시 흔히 발생하는 실수와 방지 방법",
        "적절한 인용 빈도와 배치에 대한 가이드라인",
        "2차 인용 및 간접 인용의 올바른 처리 방법",
        "다양한 출처 유형(저널, 웹사이트, 책, 학위논문 등)의 인용 형식",
        "참고문헌 목록 관리 및 정리 도구 추천",
        "표절을 방지하면서 효과적으로 인용하는 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 응답을 구조화하고, 예시와 함께 명확하게 설명해주세요. "
        "각 섹션을 명확히 구분하고, 필요시 표나 목록을 활용해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 인용 최적화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n인용 최적화 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: citation_guide.md): ") or "citation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{citation_style} 인용 가이드: {field} 분야")
        print(f"인용 최적화 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()