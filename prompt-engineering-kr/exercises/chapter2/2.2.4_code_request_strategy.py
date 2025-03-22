"""
실제 과제 수준에 맞는 코드 요청 전략

학습 목표와 과제 요구 수준에 적합한 코드를 요청하는 프롬프트 기법
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
    print("===== 실제 과제 수준에 맞는 코드 요청 전략 =====")
    
    # 사용자 입력 받기
    assignment = input("과제 설명을 입력하세요: ")
    course_level = input("과목/강의 수준을 입력하세요 (예: 1학년 입문, 3학년 전공): ")
    language = input("사용할 프로그래밍 언어를 입력하세요: ")
    learning_goals = input("과제의 학습 목표를 입력하세요 (예: 정렬 알고리즘 이해, 객체지향 설계): ")
    current_knowledge = input("현재 학습한 개념/기술을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{assignment} 과제를 해결하는 {language} 코드를 작성해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 요청 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("프로그래밍 교육 전문가", 
                           f"{course_level} 수준의 학생들을 위한 교육 자료와 과제를 개발하고, 학습 목표에 맞는 적절한 난이도의 코드를 제공하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"과제 설명: {assignment}\n"
        f"과목/강의 수준: {course_level}\n"
        f"프로그래밍 언어: {language}\n"
        f"학습 목표: {learning_goals}\n"
        f"현재 학습 상태: {current_knowledge}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 과제 수준 분석",
        f"   - {course_level} 수준에 적합한 코드 복잡성 설정",
        f"   - {learning_goals}에 집중된 코드 제공",
        f"   - {current_knowledge}를 활용하되, 아직 배우지 않은 고급 개념 회피",
        
        "2. 교육적 코드 작성",
        "   - 과제 요구사항을 정확히 충족하는 코드 제공",
        "   - 명확한 변수명과 일관된 코딩 스타일 사용",
        "   - 학습 목적에 맞는 주석 및 설명 포함",
        
        "3. 학습 기회 최적화",
        "   - 핵심 학습 개념을 명확히 보여주는 구현 방식 선택",
        "   - 코드의 일부는 직접 작성할 수 있도록 가이드라인만 제공",
        "   - 추가 학습과 탐색을 위한 도전 과제 제안",
        
        "4. 학술적 진실성 고려",
        "   - 과제 제출용 코드는 아닌, 학습 참고용 코드임을 명시",
        "   - 필요한 경우 학생이 직접 완성해야 할 부분 표시",
        "   - 독창적 사고와 문제 해결 능력을 촉진하는 코드 구조"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 과제 목표 및 학습 의도 분석\n"
        "2. 수준별 접근 방법 (기본/도전 구분)\n"
        "3. 핵심 개념 및 구현 전략\n"
        "4. 단계별 코드 구현 (주석 포함)\n"
        "5. 학습자가 직접 시도할 부분 표시\n"
        "6. 학습 심화 및 응용 방향\n\n"
        f"{language} 코드는 마크다운 코드 블록으로 제공하고, {course_level} 수준의 학생이 이해할 수 있도록 충분한 설명을 포함해주세요.\n"
        "코드는 학습 목적에 맞게 최적화되어야 하며, 단순히 문제 해결만이 아닌 교육적 가치를 최대화해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 요청 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 요청 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_request_guide.md): ") or "code_request_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{course_level} {assignment} 코드 가이드")
        print(f"코드 요청 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()