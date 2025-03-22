"""
직무별 분석

직무 요구사항, 성장 전망, 진입 전략에 대한 체계적 분석과 진로 의사결정 지원
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
    print("===== 직무별 분석 =====")
    
    # 사용자 입력 받기
    job_title = input("분석할 직무/직책을 입력하세요: ")
    industry = input("관련 산업/분야를 입력하세요: ")
    career_stage = input("진로 단계를 입력하세요 (예: 신입, 경력 전환, 승진 준비): ")
    interests = input("관심 있는 직무 특성이나 선호사항을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{industry} 분야의 {job_title} 직무에 대해 분석해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 직무 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("직무 분석 및 경력 개발 전문가", 
                           f"{industry} 산업의 직무 요구사항과 경력 경로에 정통한 전문가로, 개인의 경력 목표와 산업 트렌드를 연계한 심층 분석을 제공합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"대상 직무: {job_title}\n"
        f"산업/분야: {industry}\n"
        f"진로 단계: {career_stage}\n"
        f"관심/선호: {interests}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {job_title} 직무의 핵심 책임과 역할 분석",
        "   - 주요 업무 영역 및 책임 범위 정의",
        "   - 일상적 업무 활동과 프로젝트 유형",
        "   - 조직 내 위치 및 타 부서와의 협업 관계",
        
        "2. 필수 역량 및 자격 요건 심층 분석",
        "   - 기술적 스킬 및 지식 요구사항",
        "   - 소프트 스킬 및 성격 특성 요구사항",
        "   - 교육, 자격증, 경험 요건의 필수/선호 구분",
        
        f"3. {industry} 산업에서의 직무 전망 및 동향",
        "   - 수요 전망 및 성장 가능성",
        "   - 산업 변화가 직무에 미치는 영향",
        "   - 급여 범위 및 보상 패키지 분석",
        
        f"4. {career_stage} 단계에 맞는 진입/성장 전략",
        "   - 직무 진입을 위한 효과적인 접근법",
        "   - 경쟁력 있는 차별화 요소 개발 방안",
        f"   - {interests}와 일치하는 특화 영역 식별",
        
        "5. 경력 경로 및 발전 가능성 탐색",
        "   - 일반적인 경력 발전 경로 및 단계",
        "   - 관련 직무로의 전환 및 확장 가능성",
        "   - 장기적 성장을 위한 핵심 마일스톤"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 직무 개요 및 핵심 책임\n"
        "2. 필수 및 선호 역량/자격 분석\n"
        "3. 산업 동향 및 직무 전망\n"
        "4. 진입 전략 및 차별화 방안\n"
        "5. 경력 경로 및 성장 기회\n"
        "6. 추천 자원 및 네트워킹 전략\n\n"
        f"{industry} 산업의 {job_title} 직무에 대한 구체적이고 실용적인 정보를 제공해주세요. 현실적인 시장 상황과 {career_stage} 단계에 맞는 맞춤형 인사이트를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 직무 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n직무 분석을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: job_analysis.md): ") or "job_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{industry} {job_title} 직무 분석")
        print(f"직무 분석이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()