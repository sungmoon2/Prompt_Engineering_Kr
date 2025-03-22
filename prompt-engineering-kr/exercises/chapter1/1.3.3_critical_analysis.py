"""
비판적 분석과 평가 유도 방법

학술적 글쓰기에서 비판적 사고를 적용하고 깊이 있는 평가를 유도하는 프롬프트 기법
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
    print("===== 비판적 분석과 평가 유도 방법 =====")
    
    # 사용자 입력 받기
    analysis_subject = input("분석 대상(이론, 주장, 연구, 작품 등)을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    analysis_goal = input("분석 목적을 입력하세요 (예: 타당성 검증, 한계점 도출, 대안 제시): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{analysis_subject}에 대해 비판적으로 분석해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 비판적 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("비판적 사고 전문가 및 학술 평론가", 
                           f"{field} 분야에서 비판적 분석 방법론에 관한 다수의 저서를 집필하고, 학술 출판물의 심사와 평가를 담당해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"분석 대상: {analysis_subject}\n"
        f"학문 분야: {field}\n"
        f"분석 목적: {analysis_goal}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {analysis_subject}에 대한 비판적 분석 프레임워크 제시",
        "2. 체계적인 비판적 분석을 위한 단계별 접근법 설명",
        "3. 객관적이고 공정한 비판적 평가를 위한 기준 설정 방법",
        f"4. {field} 분야에서 {analysis_subject}와 같은 대상을 분석할 때 고려해야 할 핵심 질문들",
        "5. 강점과 약점을 균형 있게, 그러나 명확하게 평가하는 표현 방법",
        "6. 다양한 관점에서 대상을 검토하기 위한 방법론적 접근",
        "7. 논리적 오류나 방법론적 한계를 식별하는 기법",
        "8. 상충되는 증거, 이론, 해석을 다루는 방법",
        f"9. {analysis_goal}를 달성하기 위한 분석 결과의 효과적인 제시 방법",
        "10. 공감적 비판(charitable criticism)과 건설적 비판의 균형 유지법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        f"1. {analysis_subject}에 대한 비판적 분석 프레임워크\n"
        "2. 체계적 비판을 위한 핵심 질문과 접근법\n"
        "3. 분석 기준과 평가 방법\n"
        "4. 효과적인 비판적 표현과 서술 전략\n"
        "5. 비판적 분석 적용 예시\n\n"
        f"{analysis_subject}에 대한 실제 비판적 분석 사례와 구체적인 표현 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 비판적 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n비판적 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: critical_analysis_guide.md): ") or "critical_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{analysis_subject}에 대한 비판적 분석 가이드")
        print(f"비판적 분석 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()