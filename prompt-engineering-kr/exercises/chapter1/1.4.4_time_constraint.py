"""
시간 제약 상황에서의 효율적 작성법

제한된 시간 내에 높은 품질의 보고서를 작성하기 위한 전략과 기법
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
    print("===== 시간 제약 상황에서의 효율적 작성법 =====")
    
    # 사용자 입력 받기
    report_type = input("보고서 유형을 입력하세요 (예: 에세이, 실험 보고서, 문헌 연구): ")
    field = input("학문 분야를 입력하세요: ")
    available_time = input("가용 시간을 입력하세요 (예: 2일, 5시간): ")
    report_length = input("요구되는 보고서 길이를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{available_time} 안에 {report_length} 길이의 보고서를 어떻게 효율적으로 작성할 수 있을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 시간 효율화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학습 전략 전문가 및 시간 관리 컨설턴트", 
                           f"학생들이 제한된 시간 내에 {field} 분야의 높은 품질의 학술 보고서를 작성할 수 있도록 지원하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"보고서 유형: {report_type}\n"
        f"학문 분야: {field}\n"
        f"가용 시간: {available_time}\n"
        f"보고서 길이: {report_length}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {available_time} 내에 {report_length} 길이의 {report_type}을 작성하기 위한 시간 분배 계획",
        "2. 품질을 유지하면서 시간을 절약하는 연구 및 자료 수집 전략",
        "3. 신속한 개요 작성과 구조화 방법",
        "4. 효율적인 초안 작성 기법 (완벽주의 극복, 흐름 유지 등)",
        "5. 시간 제약 상황에서의 효과적인 편집 및 교정 접근법",
        f"6. {field} 분야에서 빠르게 학술적 품질을 확보하는 방법",
        "7. 시간 압박 상황에서 피해야 할 일반적인 실수와 함정",
        "8. 집중력과 생산성을 극대화하는 작업 환경 설정 방법",
        "9. 에너지 관리 및 인지적 효율성 극대화 전략",
        "10. 비상 상황을 위한 백업 계획 및 대안적 접근법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 시간별 작업 계획 및 스케줄링\n"
        "2. 연구 및 자료 수집 최적화 전략\n"
        "3. 효율적인 작성 및 편집 기법\n"
        "4. 집중력 및 생산성 극대화 방법\n"
        "5. 최소한의 시간으로 최대 효과를 위한 체크리스트\n\n"
        f"{field} 분야의 {report_type}에 특화된 시간 효율화 전략과 구체적인 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 시간 효율화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n시간 효율화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: time_efficiency_guide.md): ") or "time_efficiency_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{available_time} 내 {report_type} 작성 효율화 가이드")
        print(f"시간 효율화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()