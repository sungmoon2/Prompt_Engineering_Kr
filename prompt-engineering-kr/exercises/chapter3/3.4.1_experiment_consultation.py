"""
실험 컨설팅 가이드

효과적인 실험 설계 및 연구 방법론 선택을 위한 전략적 접근법
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
    print("===== 실험 컨설팅 가이드 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    field = input("연구 분야를 입력하세요: ")
    available_resources = input("가용 자원 및 제약사항을 입력하세요 (예: 시간, 예산, 장비, 접근성): ")
    target_validity = input("중점을 두는 타당성 유형을 입력하세요 (예: 내적 타당성, 외적 타당성, 구성 타당성): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_question}을 조사하기 위한 실험 설계 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 실험 컨설팅 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 방법론 및 실험 설계 전문가", 
                           f"{field} 분야에서 엄격한 실험 설계와 연구 방법론 개발에 전문성을 갖춘 연구자로, 다양한 연구 프로젝트의 설계와 실행을 지원한 풍부한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 질문: {research_question}\n"
        f"연구 분야: {field}\n"
        f"가용 자원 및 제약사항: {available_resources}\n"
        f"중점 타당성 유형: {target_validity}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {research_question}에 적합한 실험 설계 유형 제안 및 근거",
        "2. 제안된 설계의 강점과 약점 분석",
        f"3. {field} 분야의 연구 전통과 방법론적 표준 고려",
        "4. 변수 식별 및 조작적 정의 가이드",
        f"5. {available_resources}를 고려한 실용적 실험 실행 전략",
        "6. 표본 선정 및 크기 결정 전략",
        f"7. {target_validity}를 강화하기 위한 설계 요소",
        "8. 데이터 수집 방법 및 도구 추천",
        "9. 예상 가능한 방법론적 문제점 및 대응 전략",
        "10. 윤리적 고려사항 및 연구 승인 절차 안내"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 연구 질문 분석 및 실험 설계 방향\n"
        "2. 추천 실험 설계 및 근거\n"
        "3. 변수 정의 및 측정 전략\n"
        "4. 표본 설계 및 참가자 선정\n"
        "5. 데이터 수집 및 분석 계획\n"
        "6. 타당성 및 신뢰성 강화 전략\n"
        "7. 실험 프로토콜 및 실행 가이드\n"
        "8. 윤리적 고려사항 및 승인 절차\n\n"
        f"{research_question}에 대한 구체적인 실험 설계 계획과 실행 가이드라인을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 실험 컨설팅 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n실험 컨설팅 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: experiment_consultation_guide.md): ") or "experiment_consultation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 실험 설계 컨설팅")
        print(f"실험 컨설팅 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()