"""
진로 계획 설계

역량 진단, 직무 분석, 개인 브랜딩, 네트워킹 전략을 통합한 체계적 진로 계획 수립
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 진로 계획 설계 =====")
    
    # 사용자 입력 받기
    current_status = input("현재 상태/경력을 입력하세요: ")
    career_goals = input("진로 목표를 입력하세요 (단기/중기/장기): ")
    skills = input("보유 역량과 강점을 입력하세요: ")
    interests = input("관심 분야/산업을 입력하세요: ")
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("진로 계획 및 경력 개발 전문가", 
                         "개인 맞춤형 진로 설계와 경력 개발 전략을 통해 지속 가능한 성장 경로를 설계하는 전문 컨설턴트입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"현재 상태: {current_status}\n"
        f"진로 목표: {career_goals}\n"
        f"보유 역량/강점: {skills}\n"
        f"관심 분야/산업: {interests}"
    )
    
    # 지시사항 추가 - 하위 챕터 내용 통합
    prompt_builder.add_instructions([
        # 4.5.1 역량 진단 및 개발 계획 반영
        "1. 제공된 정보를 바탕으로 역량 진단과 개발 필요 영역을 분석해주세요.",
        f"   - {skills} 역량의 현재 가치와 발전 방향 평가",
        "   - 직무 목표 달성을 위한 역량 개발 로드맵",
        
        # 4.5.2 직무/산업 심층 분석 반영
        f"2. {interests} 분야/산업의 주요 직무와 요구 역량을 분석해주세요.",
        "   - 주요 직무 유형, 요구 자격, 성장 전망",
        "   - 직무별 진입 장벽과 차별화 전략",
        
        # 4.5.3 개인 브랜딩 전략 반영
        f"3. {career_goals}를 지원하는 개인 브랜딩 전략을 제안해주세요.",
        "   - 차별화된 개인 가치 제안(UVP) 개발",
        "   - 온/오프라인 브랜드 구축 방안",
        
        # 4.5.4 네트워킹 및 멘토십 전략 반영
        "4. 효과적인 네트워킹과 멘토십 구축 방법을 제시해주세요.",
        "   - 전략적 네트워킹 접근법과 관계 구축 방안",
        "   - 멘토 발굴 및 멘토십 활용 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 역량 진단 및 개발 계획\n"
        "2. 직무/산업 분석 및 진입 전략\n"
        "3. 개인 브랜딩 로드맵\n"
        "4. 네트워킹 및 멘토십 전략\n"
        "5. 단계별 진로 실행 계획\n\n"
        "구체적이고 실행 가능한 단계별 접근법을 제시하고, 실질적인 리소스와 도구를 추천해주세요."
    )
    
    # 프롬프트 실행
    enhanced_prompt = prompt_builder.build()
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 진로 계획 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n진로 계획을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: career_plan.md): ") or "career_plan.md"
        save_markdown(enhanced_result, file_path, title="맞춤형 진로 계획 및 경력 개발 로드맵")
        print(f"진로 계획이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()