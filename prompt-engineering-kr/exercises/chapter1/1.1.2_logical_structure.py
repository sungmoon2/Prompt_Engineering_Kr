"""
논리적 구조와 흐름 설계 프롬프트

효과적인 리포트 구조와 논리적 흐름을 설계하는 프롬프트 패턴
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
    print("===== 논리적 구조와 흐름 설계 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("리포트 주제를 입력하세요: ")
    key_points = input("주요 논점을 입력하세요 (쉼표로 구분): ")
    report_type = input("리포트 유형을 입력하세요 (예: 에세이, 연구보고서, 사례연구): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {report_type} 어떻게 쓰면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 구조 설계 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 출판 편집자", 
                          "수천 개의 논문과 리포트 구조를 검토하고 개선한 경력을 가지고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"주요 논점: {key_points}\n"
        f"리포트 유형: {report_type}\n"
        f"목적: 학술적 우수성과 논리적 일관성 확보"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "전체 리포트의 세부 구조 (모든 섹션과 하위 섹션 포함)",
        "각 섹션의 구체적인 목적과 포함되어야 할 내용",
        "논점 간의 연결성과 전체적인 일관성을 강화할 방법",
        "서론에서 독자의 관심을 끌고 주제의 중요성을 효과적으로 전달하는 방법",
        "각 섹션에서 학술적 논증을 강화하기 위한 증거와 인용 활용 방법",
        "결론에서 연구의 함의와 중요성을 강조하는 방법",
        "독자가 주요 내용을 쉽게 파악할 수 있게 하는 시각적/구조적 요소 제안"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions("마크다운 형식으로 구조화된 응답을 제공해주세요.")
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 구조 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n구조 설계 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: report_structure.md): ") or "report_structure.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 리포트 구조")
        print(f"구조 설계 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()