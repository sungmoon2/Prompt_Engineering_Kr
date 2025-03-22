"""
복잡한 문제 분해 프롬프트

복잡한 문제를 체계적으로 분해하여 해결 가능한 하위 문제로 만드는 기법
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
    print("===== 복잡한 문제 분해 프롬프트 =====")
    
    # 사용자 입력 받기
    complex_problem = input("분해할 복잡한 문제나 과제를 입력하세요: ")
    field = input("관련 분야를 입력하세요: ")
    constraints = input("시간, 자원, 범위 등의 제약 조건이 있다면 입력하세요: ")
    goal = input("최종 목표나 기대 결과를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{complex_problem} 문제를 어떻게 해결할 수 있을까요?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 문제 해결 접근법 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("복잡한 문제 분해 전문가", 
                           f"{field} 분야의 복잡한 문제를 체계적으로 분석하고 관리 가능한 하위 문제로 분해하는 전문가입니다. 문제 구조를 명확히 파악하고 효율적인 해결 전략을 설계하는 데 특화되어 있습니다.")
    
    # 맥락 제공
    context = f"복잡한 문제: {complex_problem}\n" \
             f"관련 분야: {field}\n" \
             f"최종 목표: {goal}"
    
    if constraints:
        context += f"\n제약 조건: {constraints}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {complex_problem}의 본질과 핵심 구성 요소를 파악해주세요.",
        "2. 이 복잡한 문제를 체계적으로 분해하여 명확하게 정의된 하위 문제들로 나눠주세요.",
        "3. 각 하위 문제의 성격, 범위, 핵심 도전 요소를 설명해주세요.",
        "4. 하위 문제들 간의 의존성과 상호 관계를 분석해주세요.",
        "5. 해결 순서와 우선순위를 논리적으로 제안해주세요.",
        "6. 각 하위 문제에 적합한 접근 방법과 도구를 제안해주세요.",
        f"7. 제시된 목표({goal})를 달성하기 위한 전체적인 해결 전략을 설계해주세요."
    ]
    
    if constraints:
        instructions.append(f"8. 제약 조건({constraints})을 고려한 현실적인 해결 방안을 제시해주세요.")
        instructions.append("9. 제약 내에서 가능한 대안과 절충안을 탐색해주세요.")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 문제의 본질 및 전체 구조 분석\n"
        "2. 하위 문제 목록 및 상세 설명\n"
        "3. 하위 문제 간 관계 및 의존성 맵\n"
        "4. 해결 전략 및 접근 방법\n"
        "5. 실행 계획 및 우선순위\n"
        "6. 잠재적 장애물 및 대응 전략\n\n"
        "각 하위 문제를 명확하게 정의하고, 왜 이러한 분해가 효과적인지 설명해주세요. 가능한 경우 다이어그램이나 구조화된 표현을 활용해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 문제 분해 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n문제 분해 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: problem_decomposition.md): ") or "problem_decomposition.md"
        save_markdown(enhanced_result, file_path, title=f"{complex_problem} 문제 분해 분석")
        print(f"문제 분해 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()