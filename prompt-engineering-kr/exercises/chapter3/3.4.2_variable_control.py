"""
변수 통제 전략 가이드

효과적인 실험 설계를 위한 변수 식별, 조작, 통제 방법
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
    print("===== 변수 통제 전략 가이드 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    field = input("연구 분야를 입력하세요: ")
    iv_dv = input("주요 독립변수와 종속변수를 입력하세요: ")
    potential_confounds = input("잠재적 교란변수를 입력하세요 (쉼표로 구분): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_question} 연구에서 변수를 어떻게 통제해야 할까?
주요 변수: {iv_dv}
교란변수: {potential_confounds}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 변수 통제 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("실험 설계 및 변수 통제 전문가", 
                           f"{field} 분야에서 엄격한 실험 설계와 변수 통제 방법론에 특화된 연구자로, 다양한 실험 환경에서의 변수 관리와 교란요인 최소화에 대한 전문성을 갖추고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 질문: {research_question}\n"
        f"연구 분야: {field}\n"
        f"주요 변수: {iv_dv}\n"
        f"잠재적 교란변수: {potential_confounds}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 변수 유형 분류 및 명확한 조작적 정의 방법",
        "2. 독립변수 조작 및 측정 전략",
        "3. 종속변수 정확한 측정 방법",
        "4. 교란변수 통제를 위한 연구 설계 전략",
        "5. 통제 변수 선정 및 관리 방법",
        "6. 랜덤화 및 무작위 배정 전략",
        "7. 짝짓기 및 블록킹 기법",
        "8. 통계적 통제 방법",
        "9. 변수 통제의 한계 및 대응 방안",
        "10. 변수 통제의 윤리적 고려사항"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 변수 분석 및 조작적 정의\n"
        "2. 실험 설계 내 변수 통제 전략\n"
        "3. 교란변수별 통제 방법\n"
        "4. 랜덤화 및 배정 전략\n"
        "5. 측정 및 도구 최적화\n"
        "6. 통계적 통제 기법\n"
        "7. 잠재적 문제점 및 대응 방안\n\n"
        f"{research_question}에 대한 구체적인 변수 통제 계획과 실행 가이드라인을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 변수 통제 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n변수 통제 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: variable_control_guide.md): ") or "variable_control_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 변수 통제 전략")
        print(f"변수 통제 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()