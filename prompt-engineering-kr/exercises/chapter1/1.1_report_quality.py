"""
리포트 품질 향상 기법

주제 분석, 논리적 구조 설계, 인용 최적화, 맞춤형 과제 작성을 위한 통합 도구
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
    print("===== 리포트 품질 향상 기법 =====")
    
    # 사용자 입력 받기
    topic = input("리포트 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    professor_type = input("교수 유형을 입력하세요 (예: 이론 중심형, 실용 중심형): ")
    assignment_type = input("과제 유형을 입력하세요 (예: 에세이, 연구 보고서): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {assignment_type} 어떻게 쓰면 좋을까?
"""
    
    print("\n===== 기본 통합 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 통합 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - 모든 요소를 통합하되 더 구체적인 지시
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("최고의 학술 컨설턴트", 
                          "학생들이 최상의 학술 리포트를 작성할 수 있도록 지원하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"학문 분야: {field}\n"
        f"교수 유형: {professor_type}\n"
        f"과제 유형: {assignment_type}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 주제 분석 및 논점 도출",
        "   - 주제의 학술적 중요성과 배경",
        "   - 핵심 논점 3-5개와 각각의 학문적 의의",
        "   - 관련된 주요 학술적 개념이나 이론",
        
        "2. 논리적 구조와 흐름 설계",
        "   - 과제 유형에 적합한 전체 구조 설계",
        "   - 각 섹션의 목적과 포함할 내용",
        "   - 논리적 흐름과 일관성 유지 전략",
        
        "3. 참고문헌 및 인용 최적화",
        "   - 해당 분야의 적절한 인용 스타일과 형식",
        "   - 효과적인 인용 배치와 활용 방법",
        "   - 참고문헌 목록 작성 팁",
        
        "4. 교수 유형별 맞춤 전략",
        "   - 해당 교수 유형의 특성과 선호도",
        "   - 교수의 기대를 충족시키는 작성 방법",
        "   - 피해야 할 실수와 강조해야 할 요소"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions("마크다운 형식으로 구조화된 응답을 제공해주세요.")
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 통합 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 통합 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n통합 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: report_guide.md): ") or "report_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 리포트 작성 통합 가이드")
        print(f"통합 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()