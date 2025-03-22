"""
실험 설계 통합 가이드

연구 질문부터 결과 분석까지 효과적인 실험 설계의 모든 단계를 포괄하는 접근법
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
    print("===== 실험 설계 통합 가이드 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    field = input("연구 분야를 입력하세요: ")
    design_preference = input("선호하는 실험 설계 유형이 있다면 입력하세요 (예: 무작위 통제 실험, 준실험 설계, 시계열 분석): ")
    constraints = input("연구 제약 사항이 있다면 입력하세요 (예: 시간, 예산, 윤리적 고려사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_question}을 조사하기 위한 실험을 어떻게 설계해야 할까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 실험 설계 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 방법론 및 실험 설계 전문가", 
                           f"{field} 분야에서 다양한 실험 설계 방법론을 개발하고 평가한 경험이 풍부한 연구자로, 복잡한 연구 질문을 엄격하고 적절한 실험 설계로 변환하는 전문성을 갖추고 있습니다.")
    
    # 맥락 제공
    context = f"연구 질문: {research_question}\n" \
             f"연구 분야: {field}"
    
    if design_preference:
        context += f"\n선호하는 설계 유형: {design_preference}"
    
    if constraints:
        context += f"\n연구 제약 사항: {constraints}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        # 통합적 접근법
        "1. 연구 질문 분석 및 실험 가능한 형태로 재구성",
        f"2. {field} 분야에 적합한 실험 설계 유형 및 선정 기준",
        
        # 주요 설계 단계
        "3. 변수 식별, 조작적 정의 및 측정 방법 설계",
        "4. 표본 설계, 크기 결정 및 참가자 선정 전략",
        "5. 무작위화, 통제, 균형화 전략",
        "6. 데이터 수집 도구, 프로토콜 및 절차 설계",
        "7. 잠재적 혼동 변수 통제 방법",
        
        # 분석 및 평가
        "8. 데이터 분석 계획 및 통계적 접근법",
        "9. 결과 해석 프레임워크 및 평가 기준",
        "10. 실험 타당성 및 신뢰성 확보 전략",
        "11. 윤리적 고려사항 및 연구 무결성 유지 방법",
        
        # 실용적 고려사항
        "12. 파일럿 테스트 및 사전 검증 방법"
    ]
    
    if constraints:
        instructions.append(f"13. {constraints} 제약 조건 하에서의 최적화 전략")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 연구 질문 분석 및 실험 설계 방향\n"
        "2. 최적 실험 설계 유형 및 접근법\n"
        "3. 변수 정의 및 측정 전략\n"
        "4. 표본 설계 및 참가자 선정\n"
        "5. 실험 절차 및 프로토콜\n"
        "6. 데이터 수집 및 분석 계획\n"
        "7. 타당성 및 신뢰성 확보 전략\n"
        "8. 잠재적 문제점 및 대응 방안\n"
        "9. 윤리적 고려사항\n"
        "10. 실험 구현 로드맵\n\n"
        f"{research_question}에 대한 구체적인 실험 설계 계획과 단계별 구현 가이드를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 실험 설계 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n실험 설계 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: experiment_design_guide.md): ") or "experiment_design_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 실험 설계 가이드")
        print(f"실험 설계 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()