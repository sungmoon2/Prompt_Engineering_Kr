"""
코딩 개념 이해 및 학습

프로그래밍 개념 설명, 코드 동작 원리, 알고리즘 학습, 언어 비교를 통합한 학습 방법
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
    print("===== 코딩 개념 이해 및 학습 =====")
    
    # 사용자 입력 받기
    topic = input("학습하고 싶은 프로그래밍 주제를 입력하세요: ")
    languages = input("관련 프로그래밍 언어들을 입력하세요 (쉼표로 구분): ")
    level = input("자신의 프로그래밍 수준을 입력하세요 (초급/중급/고급): ")
    code_example = input("관련 코드 예시가 있다면 입력하세요 (없으면 Enter): ")
    goal = input("학습 목표를 입력하세요 (예: 개념 이해, 실제 구현, 성능 최적화): ")
    
    # 언어 목록 정리
    language_list = [lang.strip() for lang in languages.split(',')]
    primary_language = language_list[0] if language_list else "Python"
    languages_formatted = ', '.join(language_list)
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대해 설명해줘. {languages_formatted} 언어로 어떻게 구현하는지도 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코딩 개념 학습 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("프로그래밍 교육 및 기술 통합 전문가", 
                           f"다양한 프로그래밍 개념, 알고리즘, 언어의 깊은 이해를 바탕으로 {level} 수준의 학습자를 위한 맞춤형 학습 경험을 제공하는 전문가입니다.")
    
    # 맥락 제공
    context = f"학습 주제: {topic}\n" \
             f"관련 언어: {languages_formatted}\n" \
             f"학습자 수준: {level}\n" \
             f"학습 목표: {goal}"
    
    if code_example:
        context += f"\n\n코드 예시:\n```{primary_language}\n{code_example}\n```"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 개념 설명 및 이해",
        f"   - {topic}의 핵심 개념과 원리를 {level} 수준에 맞게 설명",
        "   - 실생활 비유와 예시를 통한 직관적 이해 지원",
        "   - 관련 개념들과의 관계 및 맥락 제공",
        
        "2. 코드 동작 원리 분석",
        "   - 해당 개념이 실제 코드에서 어떻게 구현되고 작동하는지 설명",
        "   - 코드 실행 과정 및 내부 동작 메커니즘 분석",
        "   - 주요 구성 요소와 그 역할에 대한 소크라테스식 질문-답변",
        
        "3. 알고리즘 및 구현 방법",
        f"   - {topic}와 관련된 주요 알고리즘 또는 패턴 설명",
        "   - 단계별 구현 접근법 및 의사코드 제공",
        "   - 시간 및 공간 복잡도 분석 (해당되는 경우)",
        
        "4. 언어별 구현 비교",
        f"   - {languages_formatted} 언어에서의 구현 방식 비교",
        "   - 각 언어의 특징적 접근법과 장단점 분석",
        "   - 언어별 코드 예시 및 차이점 설명"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 개념 개요 및 중요성\n"
        "2. 핵심 원리 및 동작 방식\n"
        "3. 코드 단계별 분석\n"
        "4. 언어별 구현 비교\n"
        "5. 실제 응용 사례\n"
        "6. 학습 로드맵 및 연습 과제\n"
        "7. 심화 학습 자료\n\n"
        "코드 예시, 다이어그램, 표, 목록 등을 적절히 활용하여 내용을 구조화해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코딩 개념 학습 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코딩 개념 학습 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: coding_concept_guide.md): ") or "coding_concept_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 코딩 개념 통합 학습 가이드")
        print(f"코딩 개념 학습 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()