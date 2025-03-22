"""
코딩 과제 해결 전략

요구사항 분석, 알고리즘 설계, 단계별 구현, 수준 맞춤 코드 요청을 통합한 접근법
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
    print("===== 코딩 과제 해결 전략 =====")
    
    # 사용자 입력 받기
    assignment = input("과제 설명을 입력하세요: ")
    language = input("사용할 프로그래밍 언어를 입력하세요: ")
    course_context = input("과목/강의 맥락을 입력하세요: ")
    level = input("과목/강의 수준을 입력하세요: ")
    learning_goals = input("학습 목표를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{assignment} 과제를 어떻게 해결하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 과제 해결 전략 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{course_context} 교수 및 소프트웨어 개발 멘토", 
                           f"{course_context} 분야를 가르치고 학생들의 과제 개발을 지도하는 전문가로, {language} 개발에 대한 실무 경험과 교육적 통찰을 갖추고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"과제 설명: {assignment}\n"
        f"프로그래밍 언어: {language}\n"
        f"과목/강의 맥락: {course_context}\n"
        f"수준: {level}\n"
        f"학습 목표: {learning_goals}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 과제 요구사항 분석",
        "   - 과제의 핵심 목표 및 기대 산출물 파악",
        "   - 명시적/암묵적 요구사항 구분 및 우선순위 설정",
        "   - 평가 기준 예측 및 품질 목표 설정",
        
        "2. 알고리즘 설계 및 접근법",
        "   - 문제 해결을 위한 적절한 알고리즘 및 자료구조 선택",
        "   - 단계별 알고리즘 로직 개발 및 의사코드 제안",
        "   - 복잡도 분석 및 최적화 전략",
        
        "3. 단계별 구현 가이드",
        "   - 전체 구현 과정을 관리 가능한 단계로 분해",
        f"   - {language}의 특성을 활용한 효과적인 구현 전략",
        "   - 핵심 로직 구현을 위한 상세 가이드 및 예시",
        
        "4. 학습 수준에 맞는 접근법",
        f"   - {level} 수준에 맞는 코드 복잡성 및 스타일 조정",
        f"   - {learning_goals}에 부합하는 구현 방식 강조",
        "   - 학습자가 직접 해결해야 할 부분과 참고용 부분 구분"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 과제 분석 및 목표 정의\n"
        "2. 접근 전략 및 알고리즘 설계\n"
        "3. 구현 로드맵 (단계별 계획)\n"
        "4. 핵심 구현 가이드\n"
        "5. 테스트 및 검증 전략\n"
        "6. 학습 최적화 및 확장 제안\n\n"
        "코드 예시는 주요 개념을 설명하는 수준으로 제공하되, 과제의 핵심 부분은 학습자가 직접 개발할 수 있도록 가이드라인과 힌트 형태로 제시해주세요. 각 단계에서는 교육적 가치와, 과제 요구사항 충족 사이의 균형을 유지해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 과제 해결 전략 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n과제 해결 전략을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: assignment_strategy.md): ") or "assignment_strategy.md"
        save_markdown(enhanced_result, file_path, title=f"{assignment} 과제 해결 전략")
        print(f"과제 해결 전략이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()