"""
이력서 및 자기소개서 작성

취업 준비를 위한 문서 작성 최적화 도구
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
    print("===== 이력서 및 자기소개서 작성 =====")
    
    # 사용자 입력 받기
    job_position = input("지원 직무를 입력하세요: ")
    industry = input("산업 분야를 입력하세요: ")
    experience_level = input("경력 수준을 입력하세요 (예: 신입, 경력 3년차): ")
    strengths = input("자신의 주요 강점이나 스킬을 입력하세요 (쉼표로 구분): ")
    company_preference = input("지원하고 싶은 기업 유형을 입력하세요 (선택 사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{industry} 분야 {job_position} 직무에 지원하는 {experience_level} 지원자의 이력서와 자기소개서 작성 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 취업 서류 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("취업 문서 전문가 및 채용 컨설턴트", 
                           f"{industry} 분야의 채용 과정에 정통하고, 수많은 지원자의 이력서와 자기소개서를 검토하며 채용 결정에 참여한 경험이 있는 전문가입니다.")
    
    # 맥락 제공
    context = f"지원 직무: {job_position}\n" \
             f"산업 분야: {industry}\n" \
             f"경력 수준: {experience_level}\n" \
             f"주요 강점/스킬: {strengths}"
    
    if company_preference:
        context += f"\n선호 기업 유형: {company_preference}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 이력서 최적화 전략",
        f"   - {industry} 분야의 {job_position} 직무에 최적화된 이력서 구조",
        f"   - {experience_level} 수준에 적합한 내용 구성 및 강조점",
        "   - ATS(지원자 추적 시스템) 최적화를 위한 키워드 활용법",
        f"   - {strengths}를 효과적으로 부각시키는 표현 방법",
        
        "2. 자기소개서 작성 전략",
        f"   - {job_position} 직무에 특화된 자기소개서 핵심 구성 요소",
        "   - 차별화된 자기소개서를 위한 스토리텔링 접근법",
        f"   - {industry} 분야 기업의 가치와 연결하는 방법",
        "   - 구체적인 성과와 경험을 설득력 있게 제시하는 전략",
        
        "3. 직무 적합성 강조 전략",
        "   - 직무 요구사항과 개인 역량을 연결하는 방법",
        "   - 전문성과 성장 가능성을 효과적으로 표현하는 기법",
        f"   - {experience_level} 수준에서 기대하는 역량을 강조하는 방법",
        "   - 약점을 보완하고 강점을 부각시키는 전략"
    ]
    
    if company_preference:
        instructions.append("4. 기업 맞춤형 접근법")
        instructions.append(f"   - {company_preference} 유형 기업에 적합한 가치 제안")
        instructions.append("   - 기업 연구를 통한 맞춤형 내용 구성 방법")
        instructions.append("   - 기업 문화와의 적합성 강조 전략")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 이력서 작성 가이드\n"
        "2. 설득력 있는 자기소개서 작성 전략\n"
        "3. 직무 적합성 강조 방법\n"
        "4. 실제 적용 예시 및 템플릿\n"
        "5. 제출 전 최종 체크리스트\n\n"
        f"{industry} 분야의 {job_position} 직무에 특화된 구체적인 예시와 실용적인 조언을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 취업 서류 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n취업 서류 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: career_document_guide.md): ") or "career_document_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{industry} {job_position} 취업 서류 작성 가이드")
        print(f"취업 서류 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()