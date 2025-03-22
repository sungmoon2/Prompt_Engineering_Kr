"""
역량 진단 및 개발 계획

체계적인 자기 역량 진단과 경쟁력 있는 직무 역량 개발 로드맵 수립
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
    print("===== 역량 진단 및 개발 계획 =====")
    
    # 사용자 입력 받기
    current_skills = input("현재 보유한 역량/스킬을 입력하세요 (쉼표로 구분): ")
    target_job = input("목표 직무/직업을 입력하세요: ")
    education = input("학력 및 전공을 입력하세요: ")
    timeframe = input("역량 개발 기간을 입력하세요 (예: 6개월, 1년): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{target_job} 직무를 위해 필요한 역량을 알려주고, {current_skills} 역량을 가진 내가 어떻게 개발해야 할지 조언해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 역량 진단 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("역량 개발 및 경력 컨설턴트", 
                           f"{target_job} 분야의 역량 요구사항에 정통하고 개인 맞춤형 역량 개발 계획을 수립하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"현재 역량: {current_skills}\n"
        f"목표 직무: {target_job}\n"
        f"교육 배경: {education}\n"
        f"개발 기간: {timeframe}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 체계적인 현재 역량 진단 및 평가",
        f"   - {current_skills}의 현 직무 시장 가치 평가",
        "   - 보유 역량의 강점과 차별화 요소 식별",
        "   - 발전 잠재력과 개선 필요 영역 파악",
        
        f"2. {target_job} 직무에 필요한 핵심 역량 분석",
        "   - 필수 기술적/소프트 스킬 요구사항 분석",
        "   - 산업 트렌드와 미래 역량 수요 예측",
        "   - 역량별 중요도 및 우선순위 설정",
        
        "3. 역량 갭 분석 및 개발 목표 설정",
        "   - 현재 역량과 목표 역량 간의 갭 식별",
        "   - 구체적이고 측정 가능한 역량 개발 목표 설정",
        f"   - {timeframe} 기간 내 달성 가능한 단계별 목표 정의",
        
        "4. 맞춤형 역량 개발 로드맵 및 실행 계획",
        "   - 우선순위에 따른 단계별 역량 개발 전략",
        "   - 효과적인 학습 방법 및 자원 추천",
        "   - 비용-효과적인 역량 개발 접근법",
        
        "5. 역량 검증 및 입증 전략",
        "   - 개발된 역량을 증명하는 방법 (포트폴리오, 프로젝트, 자격증 등)",
        "   - 역량 가시화 및 잠재적 고용주에게 어필하는 전략",
        "   - 역량 개발 과정의 모니터링 및 성과 측정 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 현재 역량 진단 및 강점 분석\n"
        "2. 목표 직무 역량 요구사항 분석\n"
        "3. 역량 갭 분석 및 개발 우선순위\n"
        "4. 단계별 역량 개발 로드맵\n"
        "5. 추천 학습 자원 및 활동\n"
        "6. 역량 검증 및 입증 전략\n\n"
        f"{timeframe} 기간 동안 {target_job} 직무를 위한 구체적이고 실행 가능한 역량 개발 계획을 제시해주세요. 실제 시간과 자원 제약을 고려한 현실적인 접근법을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 역량 진단 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n역량 진단 및 개발 계획을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: capability_development.md): ") or "capability_development.md"
        save_markdown(enhanced_result, file_path, title=f"{target_job} 역량 개발 로드맵")
        print(f"역량 진단 및 개발 계획이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()