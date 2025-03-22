"""
결과 분석 프레임워크

연구 결과를 체계적으로 분석하고 해석하기 위한 구조화된 접근법
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
    print("===== 결과 분석 프레임워크 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    field = input("연구 분야를 입력하세요: ")
    data_type = input("데이터 유형을 입력하세요 (예: 양적, 질적, 혼합): ")
    analysis_goal = input("분석 목표를 입력하세요 (예: 가설 검증, 탐색적 분석, 패턴 발견): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_question}의 {data_type} 데이터 분석 결과를 어떻게 해석해야 할까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 결과 분석 프레임워크 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 결과 분석 및 해석 전문가", 
                           f"{field} 분야에서 {data_type} 데이터 분석 결과의 체계적 해석과 통합적 프레임워크 개발에 전문성을 갖춘 연구자로, 복잡한 데이터에서 의미 있는 패턴과 통찰을 도출한 풍부한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 질문: {research_question}\n"
        f"연구 분야: {field}\n"
        f"데이터 유형: {data_type}\n"
        f"분석 목표: {analysis_goal}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {data_type} 데이터 분석 결과 체계화를 위한 프레임워크 제안",
        f"2. {field} 분야에서 결과 해석의 표준적 접근법",
        f"3. {analysis_goal}에 부합하는 결과 분석 및 평가 기준",
        "4. 분석 결과의 다양한 수준의 해석 방법 (기술적, 분석적, 해석적)",
        "5. 결과의 유의성 및 중요성 평가 방법",
        "6. 이론적 맥락과 결과 연결 전략",
        "7. 예상치 못한 결과 처리 및 해석 방법",
        "8. 결과의 비교 및 대조 전략",
        "9. 통합적 분석을 위한 시각화 및 요약 기법",
        "10. 결과 해석의 한계 인식 및 객관성 유지 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 결과 분석 프레임워크 개요\n"
        "2. 결과 조직화 및 체계화 방법\n"
        "3. 결과 해석 수준 및 접근법\n"
        "4. 결과의 의미와 중요성 평가\n"
        "5. 이론 및 기존 연구와의 연결\n"
        "6. 예상치 못한 결과 처리 전략\n"
        "7. 통합적 분석 및 요약 방법\n\n"
        f"{research_question}에 대한 구체적인 결과 분석 프레임워크와 적용 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 결과 분석 프레임워크 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n결과 분석 프레임워크를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: result_analysis_framework.md): ") or "result_analysis_framework.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 결과 분석 프레임워크")
        print(f"결과 분석 프레임워크가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()