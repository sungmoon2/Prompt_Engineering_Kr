"""
직무별 이력서 최적화 프롬프트

다양한 직무와 산업에 맞춘 이력서 작성을 위한 프롬프트 패턴
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
    print("===== 직무별 이력서 최적화 프롬프트 =====")
    
    # 사용자 입력 받기
    job_position = input("지원 직무를 입력하세요: ")
    industry = input("산업 분야를 입력하세요: ")
    skills = input("보유한 주요 스킬을 입력하세요 (쉼표로 구분): ")
    experience = input("주요 경력/경험을 간략히 입력하세요: ")
    target_companies = input("목표 기업들을 입력하세요 (쉼표로 구분): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{industry} 분야 {job_position} 직무에 지원하기 위한 이력서 작성 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 이력서 최적화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("채용 전문가 및 이력서 컨설턴트", 
                           f"{industry} 분야의 여러 기업에서 {job_position} 직무 채용 과정을 진행한 경험이 있으며, 수많은 지원자의 이력서를 검토하고 채용 결정에 참여한 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"지원 직무: {job_position}\n"
        f"산업 분야: {industry}\n"
        f"보유 스킬: {skills}\n"
        f"주요 경력/경험: {experience}\n"
        f"목표 기업: {target_companies}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {job_position} 직무에 대한 채용담당자의 기대 분석",
        f"   - {industry} 분야에서 {job_position} 직무의 핵심 책임과 요구 역량",
        f"   - {target_companies}와 같은 기업들이 {job_position} 지원자에게 중요시하는 요소",
        "   - 직무 기술서(Job Description)에서 자주 등장하는 키워드와 요구사항",
        
        "2. 이력서 구조 및 내용 최적화",
        f"   - {job_position} 직무에 최적화된 이력서 섹션 구성 및 우선순위",
        f"   - {skills}를 효과적으로 부각시키는 스킬 섹션 구성 방법",
        f"   - {experience}를 직무 관련성 높게 표현하는 경력 기술 방법",
        "   - 직무 관련 성과와 역량을 정량적으로 표현하는 전략",
        
        "3. ATS 최적화 및 키워드 전략",
        "   - 지원자 추적 시스템(ATS)을 통과하기 위한 핵심 전략",
        "   - 직무별 핵심 키워드 및 배치 전략",
        "   - 적절한 이력서 형식 및 파일 유형 선택",
        "   - 섹션별 최적화 포인트 및 주의사항",
        
        "4. 차별화 및 경쟁력 강화 전략",
        f"   - {job_position} 직무 지원자 중에서 돋보이기 위한 전략",
        "   - 직무 적합성을 강조하는 맞춤형 요약문(Summary) 작성법",
        "   - 관련 자격증, 프로젝트, 교육 경험의 효과적인 활용",
        "   - 직무 관련 포트폴리오 또는 추가 자료 연계 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 직무 분석 및 채용 트렌드\n"
        "2. 직무별 맞춤형 이력서 구조\n"
        "3. 핵심 섹션별 최적화 전략\n"
        "4. ATS 최적화 및 키워드 가이드\n"
        "5. 차별화 전략 및 사례\n"
        "6. 맞춤형 이력서 템플릿 및 예시\n\n"
        f"{industry} 분야의 {job_position} 직무에 특화된 구체적인 예시와 실용적인 조언을 포함해주세요. 현직 채용담당자 관점에서의 통찰력 있는 조언과 실제 성공 사례를 바탕으로 한 팁을 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 이력서 최적화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n이력서 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: job_specific_resume.md): ") or "job_specific_resume.md"
        save_markdown(enhanced_result, file_path, title=f"{industry} {job_position} 직무별 이력서 최적화 가이드")
        print(f"이력서 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()