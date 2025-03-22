"""
논문 구조 설계 가이드

효과적인 학술 논문의 구조 설계와 각 섹션별 작성 전략
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
    print("===== 논문 구조 설계 가이드 =====")
    
    # 사용자 입력 받기
    paper_topic = input("논문 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    paper_type = input("논문 유형을 입력하세요 (예: 실증 연구, 문헌 검토, 이론 개발, 사례 연구): ")
    target_journal = input("목표 학술지 또는 컨퍼런스를 입력하세요 (없으면 Enter): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{paper_topic}에 대한 {paper_type} 논문의 구조를 어떻게 설계하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 논문 구조 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    role_description = f"{field} 분야의 저명한 학술지 편집자이자 교수로서, 수백 편의 논문을 검토하고 출판 과정을 안내한 경험이 있습니다."
    if target_journal:
        role_description += f" {target_journal}와 같은 우수 저널의 출판 기준에 정통합니다."
    
    prompt_builder.add_role("학술 출판 및 논문 구조화 전문가", role_description)
    
    # 맥락 제공
    context = f"논문 주제: {paper_topic}\n" \
             f"학문 분야: {field}\n" \
             f"논문 유형: {paper_type}"
    
    if target_journal:
        context += f"\n목표 학술지/컨퍼런스: {target_journal}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {paper_type} 유형의 논문에 적합한 전체 구조 설계",
        f"2. {field} 분야에서 효과적인 논문 구성 요소 및 순서",
        "3. 강력한 제목과 초록 작성 전략",
        "4. 효과적인 서론 구성 및 연구 동기 제시 방법",
        "5. 문헌 검토 섹션 구조화 및 비판적 통합 접근법",
        "6. 연구 방법론 섹션 작성 가이드",
        "7. 결과 제시의 명확성과 체계성 확보 전략",
        "8. 논의 섹션에서 결과 해석 및 의의 강조 방법",
        "9. 효과적인 결론 구성 요소",
        "10. 각 섹션의 적절한 길이 및 비율 가이드"
    ]
    
    if target_journal:
        instructions.append(f"11. {target_journal}의 특별 요구사항 및 선호 형식")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 논문 전체 구조 개요 및 흐름\n"
        "2. 섹션별 상세 구성 가이드\n"
        "3. 각 섹션 작성 전략 및 핵심 요소\n"
        "4. 논리적 연결 및 일관성 유지 방법\n"
        "5. 논문 구조 평가 체크리스트\n\n"
        f"{paper_topic}에 대한 {paper_type} 논문의 구체적인 개요 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 논문 구조 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n논문 구조 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: paper_structure_guide.md): ") or "paper_structure_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{paper_topic} {paper_type} 논문 구조 가이드")
        print(f"논문 구조 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()