"""
과제 요구사항 분석 프롬프트

프로그래밍 과제의 요구사항을 체계적으로 분석하고 이해하는 프롬프트 기법
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
    print("===== 과제 요구사항 분석 프롬프트 =====")
    
    # 사용자 입력 받기
    assignment = input("프로그래밍 과제 설명을 입력하세요: ")
    language = input("사용할 프로그래밍 언어를 입력하세요: ")
    course_context = input("과목/강의 맥락을 입력하세요 (예: 자료구조, 웹개발): ")
    level = input("과제 난이도 또는 학년을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 프로그래밍 과제를 어떻게 해결하면 좋을까?

과제: {assignment}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 과제 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{course_context} 교수 및 과제 설계 전문가", 
                           f"{course_context} 분야에서 수년간 학생들을 지도하고 과제를 평가해온 경험이 풍부한 교육자로, 복잡한 프로그래밍 문제를 분석하고 체계적으로 접근하는 방법을 가르치는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"프로그래밍 과제: {assignment}\n"
        f"프로그래밍 언어: {language}\n"
        f"과목/강의 맥락: {course_context}\n"
        f"난이도/학년: {level}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 과제 요구사항 분석",
        "   - 과제의 주요 목표와 산출물 명확히 정의",
        "   - 명시적 요구사항과 암묵적 요구사항 구분",
        "   - 과제 평가 기준 예측",
        
        "2. 기술적 요소 분석",
        f"   - {language} 언어의 어떤 기능과 라이브러리가 필요한지 식별",
        "   - 필요한 알고리즘과 자료구조 파악",
        "   - 핵심 기술적 도전 요소 식별",
        
        "3. 과제 분해 및 범위 설정",
        "   - 과제를 관리 가능한 하위 작업으로 분해",
        "   - 각 하위 작업의 우선순위와 의존성 파악",
        "   - 명확한 작업 범위와 경계 설정",
        
        "4. 잠재적 도전과 해결 전략",
        "   - 예상되는 어려움과 장애물 식별",
        "   - 각 도전에 대한 접근 전략 제안",
        "   - 필요한 사전 지식이나 자원 파악"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 과제 요약 및 핵심 목표\n"
        "2. 요구사항 분석 (명시적/암묵적 요구사항 구분)\n"
        "3. 기술적 요소 및 필요한 지식\n"
        "4. 작업 분해 및 단계별 계획\n"
        "5. 잠재적 도전 및 해결 전략\n"
        "6. 평가 기준 예측 및 품질 보장 방법\n"
        "7. 질문 목록 (과제 명확화를 위해 교수/조교에게 물어볼 사항)\n\n"
        "각 섹션에서 분석 내용을 체계적으로 정리하고, 필요한 경우 표나 목록을 활용하여 정보를 구조화해주세요. 코드를 제공하지 말고 과제 분석에 집중해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 과제 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n과제 분석 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: task_analysis.md): ") or "task_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{course_context} 과제 요구사항 분석")
        print(f"과제 분석 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()