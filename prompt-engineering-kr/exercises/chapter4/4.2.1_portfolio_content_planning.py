"""
포트폴리오 콘텐츠 기획

취업 목표에 맞는 효과적인 포트폴리오 콘텐츠 구성 및 기획 전략
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
    print("===== 포트폴리오 콘텐츠 기획 =====")
    
    # 사용자 입력 받기
    field = input("전문 분야를 입력하세요 (예: 웹 개발, UX 디자인, 마케팅): ")
    career_goal = input("취업 목표를 입력하세요 (구체적인 직무/회사 유형): ")
    skills = input("보유 스킬을 입력하세요 (쉼표로 구분): ")
    available_projects = input("포함 가능한 프로젝트/작업물을 입력하세요 (쉼표로 구분): ")
    target_employers = input("목표 고용주/기업의 특성을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{field} 분야의 포트폴리오에 어떤 내용을 넣으면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 포트폴리오 콘텐츠 기획 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{field} 커리어 전략가 및 포트폴리오 컨설턴트", 
                           f"{field} 분야에서 다양한 전문가들의 포트폴리오를 기획하고 성공적인 취업 전략을 수립해온 전문가로, 취업 목표에 최적화된 포트폴리오 콘텐츠 전략을 제시합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"전문 분야: {field}\n"
        f"취업 목표: {career_goal}\n"
        f"보유 스킬: {skills}\n"
        f"가용 프로젝트: {available_projects}\n"
        f"목표 고용주: {target_employers}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 전략적 포트폴리오 콘텐츠 계획",
        f"   - {career_goal}에 최적화된 포트폴리오 콘텐츠 전략",
        f"   - {target_employers}와 같은 고용주가 중요시하는 역량과 증명 방법",
        "   - 타겟 직무와 산업에 맞는 콘텐츠 우선순위 설정",
        "   - 개인 브랜드 구축을 위한 일관된 콘텐츠 메시지",
        
        "2. 핵심 콘텐츠 영역 및 구성",
        "   - 포트폴리오에 포함할 필수 섹션 및 컴포넌트",
        "   - 소개/자기 소개 섹션 최적화 전략",
        f"   - {skills}와 같은 스킬을 효과적으로 보여주는 콘텐츠 구성",
        f"   - {available_projects} 중 포함할 프로젝트 선정 기준 및 구성",
        
        "3. 프로젝트 콘텐츠 기획",
        "   - 각 프로젝트 설명을 위한 최적 구조 및 포맷",
        "   - 문제 해결 과정과 결과를 효과적으로 서술하는 방법",
        "   - 기술적 세부사항과 비즈니스 가치의 균형 있는 제시",
        "   - 프로젝트별 핵심 메시지 및 강조점 설정",
        
        "4. 보조 콘텐츠 요소",
        "   - 전문성과 신뢰도를 강화하는 추가 콘텐츠 유형",
        "   - 추천서, 인증, 수상 내역 등의 효과적인 활용",
        "   - 개인 블로그, 기고문, 오픈 소스 기여 등의 연계",
        "   - 콘텐츠 간 상호 연결 및 시너지 창출 방법",
        
        "5. 콘텐츠 발전 계획",
        "   - 포트폴리오 콘텐츠의 지속적인 개선 및 업데이트 전략",
        "   - 시장 피드백을 반영한 콘텐츠 조정 방법",
        "   - 경력 발전에 따른 콘텐츠 진화 계획",
        "   - 새로운 프로젝트 및 스킬 통합 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 포트폴리오 콘텐츠 전략 개요\n"
        "2. 핵심 섹션 및 콘텐츠 구성 가이드\n"
        "3. 프로젝트 선정 및 효과적인 설명 방법\n"
        "4. 스킬 및 역량 제시 전략\n"
        "5. 차별화를 위한 추가 콘텐츠 요소\n"
        "6. 포트폴리오 콘텐츠 기획 워크시트\n\n"
        f"{field} 분야에 특화된 구체적인 예시와 실용적인 조언을 포함해주세요. {career_goal}에 적합한 포트폴리오 콘텐츠 기획 전략을 중심으로 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 포트폴리오 콘텐츠 기획 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n포트폴리오 콘텐츠 기획 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: portfolio_content_planning.md): ") or "portfolio_content_planning.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 포트폴리오 콘텐츠 기획 가이드")
        print(f"포트폴리오 콘텐츠 기획 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()