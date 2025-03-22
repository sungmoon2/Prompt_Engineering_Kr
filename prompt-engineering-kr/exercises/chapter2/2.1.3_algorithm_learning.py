"""
알고리즘 학습 및 이해 지원 프롬프트

알고리즘의 원리와 작동 방식을 효과적으로 학습하기 위한 프롬프트 기법
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
    print("===== 알고리즘 학습 및 이해 지원 프롬프트 =====")
    
    # 사용자 입력 받기
    algorithm = input("학습하고 싶은 알고리즘을 입력하세요: ")
    level = input("자신의 알고리즘 이해 수준을 입력하세요 (초급/중급/고급): ")
    language = input("선호하는 프로그래밍 언어를 입력하세요: ")
    learning_focus = input("특별히 집중하고 싶은 측면을 입력하세요 (예: 시간 복잡도, 구현 방법, 최적화): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{algorithm} 알고리즘에 대해 설명해줘. {language}로 구현 방법도 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 알고리즘 설명 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("알고리즘 교육 전문가 및 컴퓨터 과학자", 
                           "알고리즘 설계, 분석 및 최적화에 관한 광범위한 지식을 갖추고 있으며, 다양한 난이도 수준의 학습자에게 복잡한 개념을 이해하기 쉽게 설명하는 데 특화된 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"학습 대상 알고리즘: {algorithm}\n"
        f"학습자 수준: {level}\n"
        f"선호 프로그래밍 언어: {language}\n"
        f"학습 초점: {learning_focus}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {algorithm} 알고리즘의 핵심 개념과 기본 원리를 {level} 수준에 맞게 설명해주세요.",
        "2. 이 알고리즘이 해결하는 문제와 실생활 응용 사례를 소개해주세요.",
        "3. 알고리즘의 작동 방식을 단계별로 분해하여 설명해주세요.",
        "4. 알고리즘의 주요 구성 요소와 각 부분의 역할을 설명해주세요.",
        f"5. {language} 언어로 알고리즘의 구현 예시를 제공해주세요 (주석 포함).",
        f"6. {learning_focus}에 초점을 맞춘 심층 분석을 제공해주세요.",
        "7. 알고리즘의 시간 및 공간 복잡도를 분석하고 설명해주세요.",
        "8. 유사하거나 대안이 되는 알고리즘과의 비교 분석을 제공해주세요.",
        "9. 이 알고리즘을 학습할 때 흔히 발생하는 오해나 어려움을 미리 알려주세요.",
        f"10. {level} 수준의 학습자가 이 알고리즘을 단계적으로 마스터하기 위한 학습 경로를 제안해주세요."
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 알고리즘 개요 및 목적\n"
        "2. 핵심 원리 및 작동 방식\n"
        "3. 시각적 설명 (필요한 경우 다이어그램이나 단계별 시각화)\n"
        "4. 구현 예시 (주석이 포함된 코드)\n"
        "5. " + learning_focus + " 심층 분석\n"
        "6. 시간 및 공간 복잡도 분석\n"
        "7. 대안 및 비교 분석\n"
        "8. 단계별 학습 가이드\n"
        "9. 연습 문제 및 응용 과제\n\n"
        "가능한 경우 표, 목록, 다이어그램 등을 활용하여 정보를 명확하게 구조화해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 알고리즘 설명 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n알고리즘 학습 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: algorithm_guide.md): ") or "algorithm_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{algorithm} 알고리즘 학습 가이드")
        print(f"알고리즘 학습 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()