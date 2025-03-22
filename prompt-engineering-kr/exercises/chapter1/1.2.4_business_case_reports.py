"""
경영/경제 사례 분석 보고서 작성법

경영학, 경제학 분야의 사례 분석 보고서 작성을 위한 프롬프트
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
    print("===== 경영/경제 사례 분석 보고서 작성법 =====")
    
    # 사용자 입력 받기
    case_type = input("사례 유형을 입력하세요 (예: 기업 전략, 마케팅 캠페인, 재무 분석, 경제 정책): ")
    specific_case = input("분석할 특정 사례나 기업을 입력하세요: ")
    business_field = input("구체적인 경영/경제 분야를 입력하세요 (예: 마케팅, 재무, 인사, 국제경제): ")
    report_purpose = input("보고서 목적을 입력하세요 (예: 학술 과제, 비즈니스 제안, 투자 분석): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{business_field} 분야에서 {specific_case}의 {case_type} 사례 분석 보고서를 작성하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 경영/경제 사례 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{business_field} 컨설턴트 및 교수", 
                          f"유명 경영대학원 교수이자 {business_field} 분야의 전문 컨설턴트로서 다수의 사례 분석과 컨설팅 프로젝트를 수행한 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"사례 유형: {case_type}\n"
        f"분석 대상: {specific_case}\n"
        f"학문 분야: {business_field} (경영/경제계열)\n"
        f"보고서 목적: {report_purpose}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {business_field} 분야의 {case_type} 사례 분석을 위한 프레임워크와 접근 방식",
        "2. 경영/경제 사례 분석 보고서의 표준 구조와 각 섹션의 목적",
        "3. 효과적인 사례 배경 및 현황 분석 방법",
        f"4. {case_type}에 적합한 분석 모델과 도구 (예: SWOT, PEST, 5 Forces, 재무비율 등)",
        "5. 데이터 활용 및 증거 기반 분석 방법",
        "6. 경영/경제 사례의 문제점 식별 및 명확한 원인 분석 기법",
        "7. 실행 가능한 해결책 및 전략적 대안 제시 방법",
        "8. 정량적/정성적 데이터의 효과적인 시각화 및 표현 방법",
        f"9. {specific_case}와 같은 사례에 대한 비즈니스 인사이트 도출 방법",
        f"10. {report_purpose}에 적합한 전문적 용어와 표현 활용법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 체계적이고 실용적인 사례 분석 가이드를 제공해주세요. "
        "실제 비즈니스 상황에서 활용할 수 있는 구체적인 템플릿과 예시를 포함해주세요. "
        f"{business_field} 분야의 특수성을 반영한 분석 프레임워크와 접근법을 상세히 설명해주세요. "
        "경영/경제 보고서에 적합한 데이터 표현 방식과 시각화 예시도 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 경영/경제 사례 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n경영/경제 사례 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: business_case_guide.md): ") or "business_case_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{specific_case} {case_type} 사례 분석 가이드")
        print(f"경영/경제 사례 분석 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()