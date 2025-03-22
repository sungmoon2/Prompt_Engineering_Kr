"""
단계별 코드 구현 가이드 요청 방법

알고리즘을 실제 코드로 구현하는 과정을 단계별로 안내받는 프롬프트 기법
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
    print("===== 단계별 코드 구현 가이드 요청 방법 =====")
    
    # 사용자 입력 받기
    algorithm = input("구현할 알고리즘이나 기능을 입력하세요: ")
    language = input("사용할 프로그래밍 언어를 입력하세요: ")
    level = input("본인의 프로그래밍 수준을 입력하세요 (초급/중급/고급): ")
    specific_focus = input("특별히 상세한 설명이 필요한 부분이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{language}로 {algorithm}를 구현하는 코드를 작성해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 구현 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{language} 전문 개발자 및 프로그래밍 교육자", 
                          f"{language}를 사용한 실제 개발 경험이 풍부하고, 다양한 수준의 학습자에게 코드 작성을 가르치는 데 전문성을 가진 교육자입니다.")
    
    # 맥락 제공
    context = f"구현 대상: {algorithm}\n" \
             f"프로그래밍 언어: {language}\n" \
             f"학습자 수준: {level}"
    
    if specific_focus:
        context += f"\n상세 설명 필요 부분: {specific_focus}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 구현 준비",
        "   - 필요한 라이브러리와 의존성 설명",
        "   - 개발 환경 설정 가이드 (필요한 경우)",
        "   - 기본 파일 구조 제안",
        
        "2. 단계별 구현 안내",
        "   - 전체 구현 과정을 논리적 단계로 분해",
        "   - 각 단계의 목적과 역할 명확히 설명",
        "   - 단계별 코드 블록 제공 (상세한 주석 포함)",
        
        "3. 핵심 로직 심층 설명",
        "   - 알고리즘의 중요 부분 상세 해설",
        "   - 왜 특정 접근법을 사용했는지 설명",
        f"   - {level} 수준에 맞는 설명 깊이 조절",
        
        "4. 코드 통합 및 테스트",
        "   - 모든 단계를 통합한 완성 코드 제공",
        "   - 테스트 방법 및 예시 입력/출력 제안",
        "   - 디버깅 및 문제 해결 가이드"
    ]
    
    if specific_focus:
        instructions.append(f"5. {specific_focus}에 대한 특별 심화 설명")
        instructions.append("   - 해당 부분의 작동 원리 상세 분석")
        instructions.append("   - 관련 개념 및 패턴 설명")
        instructions.append("   - 대안적 구현 방법 비교")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 구현 개요 및 준비\n"
        "2. 단계별 구현 가이드\n"
        "   - 각 단계는 명확히 구분하고 번호 매기기\n"
        "   - 코드 블록과 설명 번갈아 제공\n"
        "3. 핵심 로직 심층 분석\n"
        "4. 통합 코드 및 테스트 가이드\n"
        "5. 학습 심화 및 추가 리소스\n\n"
        f"코드 예시는 마크다운 코드 블록으로 제공하고, {language} 언어의 모범 사례와 코딩 스타일을 준수해주세요.\n"
        f"작성하는 모든 코드에 충분한 주석을 달고, {level} 수준의 학습자가 이해할 수 있도록 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 구현 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 구현 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: implementation_guide.md): ") or "implementation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{algorithm} {language} 구현 가이드")
        print(f"코드 구현 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()