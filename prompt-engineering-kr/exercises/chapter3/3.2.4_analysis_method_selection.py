"""
분석 방법 선택 가이드

연구 질문과 데이터 유형에 따른 최적의 통계 및 분석 방법 선택 전략
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
    print("===== 분석 방법 선택 가이드 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    data_description = input("데이터 특성을 입력하세요 (예: 표본 크기, 분포 특성, 변수 유형): ")
    research_field = input("연구 분야를 입력하세요: ")
    analysis_goal = input("분석 목표를 입력하세요 (예: 차이 검증, 관계 파악, 예측, 분류): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_question}을 조사하기 위해 어떤 통계 분석 방법을 사용해야 할까?
데이터 특성: {data_description}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 분석 방법 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 방법론 및 통계 분석 전문가", 
                           f"{research_field} 분야의 연구 설계와 분석 방법론에 정통한 전문가로, 다양한 연구 질문과 데이터 유형에 적합한 분석 전략 수립에 풍부한 경험을 가지고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 질문: {research_question}\n"
        f"데이터 특성: {data_description}\n"
        f"연구 분야: {research_field}\n"
        f"분석 목표: {analysis_goal}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {research_question}에 답하기 위한 적절한 분석 방법 후보군 제시",
        f"2. {data_description}을 고려한 각 분석 방법의 적합성 평가",
        f"3. {research_field} 분야에서 일반적으로 사용되는 표준 분석 접근법",
        f"4. {analysis_goal}을 달성하기 위한 최적의 분석 전략 추천",
        "5. 추천 분석 방법의 강점, 약점, 가정 및 제한사항",
        "6. 분석 전 데이터 전처리 및 준비 단계 가이드",
        "7. 대안적 분석 방법과 그 장단점 비교",
        "8. 결과 해석 및 보고 방법 가이드",
        "9. 분석 오류를 방지하기 위한 체크리스트",
        "10. 고급 분석 기법 및 새로운 연구 동향 (해당되는 경우)"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 연구 질문 및 데이터 분석\n"
        "2. 추천 분석 방법 및 근거\n"
        "3. 분석 가정 및 전제조건\n"
        "4. 분석 구현 단계\n"
        "5. 결과 해석 가이드\n"
        "6. 대안적 접근법 및 고려사항\n"
        "7. 분석 품질 보장 체크리스트\n\n"
        f"{research_field} 분야의 구체적인 분석 예시와 코드(R, Python 등) 스니펫을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 분석 방법 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n분석 방법 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: analysis_method_guide.md): ") or "analysis_method_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{analysis_goal}을 위한 분석 방법 선택 가이드")
        print(f"분석 방법 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()