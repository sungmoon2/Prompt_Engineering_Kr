"""
프로그래밍 언어별 특징 비교 및 학습

여러 프로그래밍 언어의 특징과 차이점을 효과적으로 비교하고 학습하는 프롬프트 기법
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
    print("===== 프로그래밍 언어별 특징 비교 및 학습 =====")
    
    # 사용자 입력 받기
    languages = input("비교하고 싶은 프로그래밍 언어들을 입력하세요 (쉼표로 구분): ")
    concept = input("특정 개념이나 기능을 비교하고 싶다면 입력하세요 (예: 배열 처리, 객체지향 기능): ")
    background = input("본인의 프로그래밍 배경을 입력하세요 (예: Python 2년 경험, Java 초보): ")
    learning_goal = input("학습 목표를 입력하세요 (예: 웹 개발을 위한 언어 선택, 데이터 과학 전환): ")
    
    # 언어 목록 정리
    language_list = [lang.strip() for lang in languages.split(',')]
    languages_formatted = ', '.join(language_list)
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{languages_formatted} 언어들의 차이점을 비교해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 언어 비교 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("프로그래밍 다국어 전문가 및 교육 컨설턴트", 
                           f"다양한 프로그래밍 언어에 정통하며, 언어 간 전환 및 비교 학습에 특화된 전문가로서 {languages_formatted} 언어에 대한 심층적인 경험을 보유하고 있습니다.")
    
    # 맥락 제공
    context = f"비교 대상 언어: {languages_formatted}\n" \
             f"학습자 배경: {background}\n" \
             f"학습 목표: {learning_goal}"
    
    if concept:
        context += f"\n비교 초점 개념: {concept}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {languages_formatted} 언어들의 핵심 철학과 설계 원칙을 비교해주세요.",
        "2. 각 언어의 주요 특징, 강점 및 약점을 분석해주세요.",
        "3. 각 언어가 가장 적합한 사용 사례와 도메인을 설명해주세요.",
        f"4. {background}를 고려하여, 언어 간 전환 시 알아야 할 핵심 차이점을 설명해주세요.",
        "5. 동일한 문제를 각 언어로 해결하는 코드 예시를 비교해주세요.",
        "6. 각 언어의 생태계, 라이브러리, 커뮤니티 지원을 비교해주세요.",
        f"7. {learning_goal}을 위해 가장 적합한 언어(들)과 그 이유를 제안해주세요.",
        "8. 각 언어의 학습 곡선과 습득에 필요한 시간을 비교해주세요."
    ]
    
    if concept:
        instructions.append(f"9. {concept}를 각 언어에서 어떻게 구현하고 접근하는지 구체적으로 비교해주세요.")
        instructions.append(f"10. {concept}와 관련된 각 언어의 특별한 기능이나 제한사항을 분석해주세요.")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    sections = [
        "1. 언어별 핵심 철학 및 설계 원칙 비교",
        "2. 주요 특징 및 구문 비교",
        "3. 실용적 코드 예시 비교",
        "4. 성능 및 효율성 비교",
        "5. 생태계 및 커뮤니티 비교"
    ]
    
    if concept:
        sections.append(f"6. {concept} 구현 방식 비교")
    
    sections.extend([
        f"7. {learning_goal}을 위한 최적 언어 분석",
        "8. 언어 전환 및 학습 로드맵",
        "9. 요약 및 추천"
    ])
    
    output_format = "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n" + "\n".join(sections) + "\n\n"
    output_format += "가능한 경우 표, 목록, 코드 블록 등을 활용하여 정보를 명확하게 구조화해주세요. 특히 중요한 차이점은 비교 테이블 형태로 제시해주세요."
    
    prompt_builder.add_format_instructions(output_format)
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 언어 비교 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n언어 비교 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: language_comparison.md): ") or "language_comparison.md"
        save_markdown(enhanced_result, file_path, title=f"{languages_formatted} 프로그래밍 언어 비교")
        print(f"언어 비교 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()