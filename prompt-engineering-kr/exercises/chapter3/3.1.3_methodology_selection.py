"""
연구 방법론 선택 및 설계 프롬프트

연구 질문에 적합한 방법론을 선택하고 설계하는 프롬프트 기법
"""

import os
import sys
import random

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.example_provider import get_random_research_method

def main():
    """
    실습 코드 메인 함수
    """
    print("===== 연구 방법론 선택 및 설계 프롬프트 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    preferred_approach = input("선호하는 접근법이 있다면 입력하세요 (정량적/정성적/혼합): ")
    constraints = input("연구 제약 조건이 있다면 입력하세요 (예: 시간, 예산, 접근성): ")
    
    # 방법론 예시 제공
    print("\n참고할 수 있는 연구 방법론 예시:")
    methods = []
    for _ in range(5):
        method = get_random_research_method()
        if method not in methods:
            methods.append(method)
    
    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
"{research_question}" 연구 질문에 적합한 연구 방법론을 추천해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 방법론 선택 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 연구 방법론 전문가", 
        f"{field} 분야에서 다양한 연구 방법론을 활용한 풍부한 경험을 가진 학자로, 연구 설계 컨설팅과 방법론 워크숍을 통해 연구자들을 지도하고 있습니다. 특히 {preferred_approach if preferred_approach else '다양한'} 접근법에 정통합니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 정보:
- 연구 질문: {research_question}
- 학문 분야: {field}
"""
    
    if preferred_approach:
        context += f"- 선호하는 접근법: {preferred_approach}\n"
    if constraints:
        context += f"- 제약 조건: {constraints}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 연구 질문 분석 및 방법론적 요구사항 파악",
        f"   - '{research_question}'의 본질과 목적 분석",
        "   - 핵심 변수, 관계, 맥락 식별",
        "   - 잠재적 데이터 유형 및 수집 요구사항 파악",
        
        "2. 적합한 연구 방법론 대안 제시",
        f"   - {field} 분야에 적합한 3-5개의 방법론 대안 제안",
        "   - 각 방법론의 장단점 및 적합성 평가",
        "   - 방법론 선택 기준 및 의사결정 프레임워크",
        
        "3. 최적 방법론 설계 및 구체화",
        "   - 권장되는 최적 방법론의 상세 설계",
        "   - 참여자/샘플링 전략, 데이터 수집 방법, 분석 기법",
        "   - 타당성과 신뢰성 확보 전략",
        
        "4. 실행 계획 및 잠재적 문제 해결책",
        "   - 단계별 연구 수행 계획",
        "   - 잠재적 방법론적 문제와 해결 전략",
        "   - 연구 윤리 고려사항 및 대응 방안"
    ]
    
    if constraints:
        instructions.append(
            "5. 제약 조건 내에서의 최적화 전략",
            f"   - {constraints} 제약 하에서의 연구 설계 조정 방안",
            "   - 제약 조건을 고려한 대안적 접근법",
            "   - 제한된 자원의 효율적 활용 전략"
        )
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **연구 질문 분석**: '{research_question}'의 방법론적 요구 분석

2. **방법론 대안 분석**:
   - 방법론 1: [이름]
     - 설명 및 적합성
     - 장단점
     - 적용 시 고려사항
   - 방법론 2: [이름]
     ...
   (3-5개 방법론)

3. **최적 연구 설계 제안**:
   - 권장 방법론 및 이유
   - 연구 설계 상세 내용
     - 참여자/샘플링
     - 데이터 수집 방법
     - 분석 기법
   - 타당성/신뢰성 전략

4. **실행 계획**:
   - 단계별 연구 수행 계획
   - 잠재적 문제 및 해결책
   - 윤리적 고려사항
"""
    
    if constraints:
        output_format += """
5. **제약 조건 대응 전략**:
   - 제약 내 최적화 방안
   - 대안적 접근법
   - 자원 활용 전략
"""
    
    output_format += """
마크다운 형식으로 체계적인 연구 방법론 선택 및 설계 가이드를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 방법론 선택 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n방법론 선택 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: methodology_guide.md): ") or "methodology_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 연구 방법론 선택 가이드")
        print(f"방법론 선택 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()