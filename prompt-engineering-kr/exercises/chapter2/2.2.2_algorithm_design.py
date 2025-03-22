"""
알고리즘 설계 및 의사코드 생성

문제 해결을 위한 알고리즘을 설계하고 의사코드로 표현하는 프롬프트 기법
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
    print("===== 알고리즘 설계 및 의사코드 생성 =====")
    
    # 사용자 입력 받기
    problem = input("해결할 문제를 입력하세요: ")
    constraints = input("제약 조건이 있다면 입력하세요 (예: 시간/공간 복잡도, 메모리 제한): ")
    target_language = input("최종 구현 언어를 입력하세요: ")
    level = input("알고리즘 복잡성 수준을 입력하세요 (초급/중급/고급): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{problem} 문제를 해결하는 알고리즘을 설계하고 의사코드를 작성해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 알고리즘 설계 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("알고리즘 설계 및 문제 해결 전문가", 
                           "다양한 복잡도의 알고리즘 문제를 체계적으로 접근하고 해결하는 방법론에 정통한 전문가로, 효율적인 알고리즘 설계와 명확한 의사코드 작성에 특화되어 있습니다.")
    
    # 맥락 제공
    context = f"문제 설명: {problem}\n" \
             f"목표 구현 언어: {target_language}\n" \
             f"복잡성 수준: {level}"
    
    if constraints:
        context += f"\n제약 조건: {constraints}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 문제 분석 및 이해",
        "   - 문제의 핵심 요구사항 명확화",
        "   - 입력과 출력 형식 정의",
        "   - 문제 해결에 필요한 개념적 도구 식별",
        
        "2. 해결 접근법 탐색",
        "   - 다양한 접근 방법 검토 (분할 정복, 그리디, 동적 계획법 등)",
        "   - 각 접근법의 장단점 분석",
        "   - 가장 적합한 접근법 선택 및 정당화",
        
        "3. 알고리즘 설계",
        "   - 단계별 알고리즘 로직 개발",
        "   - 핵심 자료구조 선택 및 활용 방법",
        "   - 주요 함수 및 루틴의 역할 정의",
        
        "4. 의사코드 작성",
        "   - 명확하고 읽기 쉬운 의사코드로 알고리즘 표현",
        "   - 주요 단계와 로직에 주석 추가",
        f"   - {target_language} 구현을 염두에 둔 의사코드 구조화",
        
        "5. 알고리즘 분석",
        "   - 시간 및 공간 복잡도 계산",
        f"   - {constraints}와 같은 제약 조건 충족 여부 검토",
        "   - 최적화 가능성 및 방향 탐색"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 문제 이해 및 분석\n"
        "2. 접근법 탐색 및 선택\n"
        "3. 알고리즘 설계 (핵심 아이디어 및 자료구조)\n"
        "4. 의사코드 (주석 포함)\n"
        "5. 복잡도 분석 및 정당성\n"
        "6. 최적화 및 대안 고려사항\n"
        "7. 구현 시 주의점\n\n"
        f"의사코드는 {target_language} 구현으로 쉽게 변환할 수 있도록 작성하되, 실제 코드보다는 알고리즘의 로직에 초점을 맞춰주세요. 필요한 경우 다이어그램이나 표를 활용하여 알고리즘을 시각화해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 알고리즘 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n알고리즘 설계 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: algorithm_design.md): ") or "algorithm_design.md"
        save_markdown(enhanced_result, file_path, title=f"{problem} 알고리즘 설계 및 의사코드")
        print(f"알고리즘 설계 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()