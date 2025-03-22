"""
단계적 사고 유도 (Chain-of-Thought)

복잡한 문제를 단계별로 사고하는 프롬프트 패턴
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
    print("===== 단계적 사고 유도 (Chain-of-Thought) =====")
    
    # 사용자 입력 받기
    problem = input("해결할 문제나 질문을 입력하세요: ")
    problem_type = input("문제 유형을 선택하세요 (1: 수학/논리, 2: 개념 분석, 3: 의사결정, 4: 프로그래밍): ")
    depth = input("원하는 사고 깊이 수준을 입력하세요 (기본/중간/심층): ")
    
    # 기본 프롬프트 - 단순한 버전
    basic_prompt = f"""
다음 문제를 해결해주세요: {problem}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 문제 해결 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성 - 단계적 사고 유도
    prompt_builder = PromptBuilder()
    
    # 문제 유형에 따른 역할 설정
    if problem_type == "1":  # 수학/논리
        prompt_builder.add_role("논리적 문제 해결 전문가", 
                              "복잡한 수학적, 논리적 문제를 단계적으로 분석하고 명확한 사고 과정을 통해 해결책에 도달하는 전문가입니다.")
    elif problem_type == "2":  # 개념 분석
        prompt_builder.add_role("개념 분석 전문가", 
                              "복잡한 개념과 아이디어를 체계적으로 분해하고 깊이 있게 분석하여 명확한 이해를 도출하는 전문가입니다.")
    elif problem_type == "3":  # 의사결정
        prompt_builder.add_role("의사결정 분석가", 
                              "복잡한 상황에서 다양한 요소를 고려하여 단계적으로 최적의 의사결정에 도달하는 전문가입니다.")
    else:  # 프로그래밍
        prompt_builder.add_role("알고리즘 설계자", 
                              "프로그래밍 문제를 체계적으로 분해하고 효율적인 알고리즘을 단계적으로 설계하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"문제/질문: {problem}\n"
        f"문제 유형: {'수학/논리 문제' if problem_type == '1' else '개념 분석' if problem_type == '2' else '의사결정 문제' if problem_type == '3' else '프로그래밍 문제'}\n"
        f"사고 깊이: {depth}"
    )
    
    # 단계적 사고 유도 지시사항
    instructions = [
        "이 문제를 해결하기 위해 단계적 사고 과정(Chain-of-Thought)을 활용해주세요.",
        "각 사고 단계를 명시적으로 표시하고, 이유와 근거를 포함해주세요.",
        "어떤 가정을 하는지 명확히 설명해주세요.",
        "가능한 경우 다양한 접근법이나 대안을 고려해주세요.",
        "중간 결론을 도출하고 이를 다음 단계에 활용하는 방식으로 진행해주세요."
    ]
    
    # 문제 유형별 추가 지시사항
    if problem_type == "1":  # 수학/논리
        instructions.extend([
            "관련 수학적 개념이나 공식을 명확히 설명해주세요.",
            "계산 과정을 단계별로 상세히 보여주세요.",
            "각 단계가 다음 단계로 어떻게 연결되는지 설명해주세요."
        ])
    elif problem_type == "2":  # 개념 분석
        instructions.extend([
            "주요 개념을 정의하고 구성 요소로 분해해주세요.",
            "개념 간의 관계를 명확히 분석해주세요.",
            "다양한 관점과 맥락에서 개념을 검토해주세요."
        ])
    elif problem_type == "3":  # 의사결정
        instructions.extend([
            "의사결정 기준을 명확히 설정해주세요.",
            "각 선택지의 장단점을 체계적으로 분석해주세요.",
            "가능한 결과와 영향을 평가해주세요."
        ])
    else:  # 프로그래밍
        instructions.extend([
            "문제 요구사항을 명확히 분석해주세요.",
            "알고리즘의 로직을 단계별로 설계해주세요.",
            "시간 및 공간 복잡도를 고려해주세요."
        ])
    
    # 사고 깊이에 따른 추가 지시사항
    if depth.lower() == "중간":
        instructions.append("중간 수준의 복잡성과 깊이로 문제를 분석해주세요.")
    elif depth.lower() == "심층":
        instructions.append("가능한 모든 세부 단계와 고려사항을 포함한 심층적인 분석을 제공해주세요.")
    else:  # 기본
        instructions.append("핵심 단계와 주요 고려사항을 중심으로 명확한 분석을 제공해주세요.")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음과 같은 형식으로 단계적 사고 과정을 마크다운으로 표현해주세요:\n\n"
        "# 문제 분석 및 해결\n\n"
        "## 1단계: 문제 이해\n[이 단계에서의 세부 사고 과정]\n\n"
        "## 2단계: 접근법 선택\n[이 단계에서의 세부 사고 과정]\n\n"
        "## 3단계: [이후 단계]\n[이 단계에서의 세부 사고 과정]\n\n"
        "...\n\n"
        "## 최종 단계: 결론 도출\n[최종 결론 및 해결책]\n\n"
        "# 요약 및 검증\n[전체 사고 과정 요약 및 해결책 검증]"
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 단계적 사고 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 단계적 사고 해결 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n단계적 사고 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: chain_of_thought.md): ") or "chain_of_thought.md"
        save_markdown(enhanced_result, file_path, title=f"{problem}에 대한 단계적 사고 분석")
        print(f"단계적 사고 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()