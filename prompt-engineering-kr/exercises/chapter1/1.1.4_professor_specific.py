"""
교수 유형별 맞춤형 과제 작성 가이드

다양한 교수 유형과 평가 스타일에 맞춘 과제 작성 전략
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
    print("===== 교수 유형별 맞춤형 과제 작성 가이드 =====")
    
    # 사용자 입력 받기
    professor_type = input("교수 유형을 입력하세요 (예: 이론 중심형, 실용 중심형, 연구 중심형, 비판적 사고 강조형): ")
    assignment_type = input("과제 유형을 입력하세요 (예: 에세이, 연구보고서, 사례분석, 프레젠테이션): ")
    field = input("학문 분야를 입력하세요: ")
    topic = input("과제 주제를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{professor_type} 교수님의 {assignment_type} 과제를 잘 작성하려면 어떻게 해야 할까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 맞춤형 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 컨설턴트", 
                         "다양한 교수 유형과 평가 스타일을 분석하고 학생들에게 맞춤형 전략을 제공하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"교수 유형: {professor_type}\n"
        f"과제 유형: {assignment_type}\n"
        f"학문 분야: {field}\n"
        f"과제 주제: {topic}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"{professor_type} 교수의 특성과 선호하는 학술적 접근 방식 분석",
        f"이 유형의 교수가 과제 평가 시 중요시하는 핵심 요소 설명",
        f"{assignment_type} 작성 시 강조해야 할 요소와 피해야 할 일반적인 실수",
        f"{field} 분야에서 {professor_type} 교수를 위한 효과적인 논증 및 근거 제시 방법",
        "높은 평가를 받기 위한 구체적인 구조 및 내용 구성 전략",
        "교수의 기대를 충족시키는 적절한 어조, 스타일, 형식 가이드",
        "참고문헌 활용 및 인용 전략",
        "제출 전 자가 점검 체크리스트"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 구조화된 응답을 제공해주세요. "
        "실제 적용 가능한 구체적인 팁과 예시를 포함해주세요. "
        "필요한 경우 단계별 접근 방법을 제시해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 맞춤형 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n맞춤형 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: professor_guide.md): ") or "professor_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{professor_type} 교수를 위한 {assignment_type} 작성 가이드")
        print(f"맞춤형 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()