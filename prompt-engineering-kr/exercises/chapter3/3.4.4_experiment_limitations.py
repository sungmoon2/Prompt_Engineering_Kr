"""
실험 한계점 분석 가이드

연구의 한계점을 건설적으로 인식하고 제시하는 방법
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
    print("===== 실험 한계점 분석 가이드 =====")
    
    # 사용자 입력 받기
    research_design = input("연구/실험 설계 유형을 입력하세요: ")
    field = input("연구 분야를 입력하세요: ")
    known_limitations = input("인식된 한계점이 있다면 입력하세요 (쉼표로 구분): ")
    audience = input("논문/보고서의 대상 독자를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_design} 실험의 한계점을 어떻게 분석하고 기술하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 한계점 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 방법론 및 실험 평가 전문가", 
                           f"{field} 분야의 연구 설계 평가와 한계점 분석에 특화된 학자로, 학술 출판물의 방법론적 엄격성 평가와 건설적인 한계점 제시 방법에 대한 전문성을 갖추고 있습니다.")
    
    # 맥락 제공
    context = f"연구/실험 설계: {research_design}\n" \
             f"연구 분야: {field}\n" \
             f"대상 독자: {audience}"
    
    if known_limitations:
        context += f"\n인식된 한계점: {known_limitations}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {research_design}의 일반적인 방법론적 한계 식별",
        f"2. {field} 분야에서 연구 한계점 분석의 표준적 접근법",
        "3. 내적 타당성 관련 한계점 분석 방법",
        "4. 외적 타당성 및 일반화 가능성 관련 한계점",
        "5. 표본 및 참가자 관련 한계점 고려사항",
        "6. 측정 및 도구 관련 한계점",
        "7. 통계적 및 분석적 한계점",
        "8. 한계점을 건설적이고 균형 있게 제시하는 방법",
        "9. 한계점에서 미래 연구 방향으로 전환하는 전략",
        "10. 한계점 논의의 과도함과 부족함 사이의 균형 유지 방법"
    ]
    
    if known_limitations:
        instructions.append(f"11. 다음 한계점에 대한 구체적 분석: {known_limitations}")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 한계점 식별 및 분석 프레임워크\n"
        "2. 연구 설계별 잠재적 한계점\n"
        "3. 방법론적 한계점 분석\n"
        "4. 표본 및 측정 관련 한계점\n"
        "5. 한계점의 건설적 제시 전략\n"
        "6. 미래 연구 방향 도출 방법\n"
        "7. 한계점 논의 체크리스트\n\n"
        f"{research_design} 설계의 한계점 분석 예시와 효과적인 작성 방법을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 한계점 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n한계점 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: limitations_analysis_guide.md): ") or "limitations_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_design} 연구 한계점 분석 가이드")
        print(f"한계점 분석 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()