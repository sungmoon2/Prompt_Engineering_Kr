"""
포트폴리오 디자인 방향 설정

개인 브랜드와 목표 직군에 적합한 포트폴리오 디자인 전략 수립
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
    print("===== 포트폴리오 디자인 방향 설정 =====")
    
    # 사용자 입력 받기
    field = input("전문 분야를 입력하세요 (예: 웹 디자인, UX/UI, 그래픽 디자인): ")
    personal_style = input("본인의 디자인 스타일이나 선호를 입력하세요: ")
    target_industry = input("목표 산업이나 분야를 입력하세요: ")
    portfolio_format = input("포트폴리오 형식을 입력하세요 (예: 웹사이트, PDF, 인쇄물): ")
    career_level = input("경력 수준을 입력하세요 (예: 신입, 주니어, 시니어): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{field} 분야의 포트폴리오 디자인은 어떻게 하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 포트폴리오 디자인 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("디자인 디렉터 및 포트폴리오 전략가", 
                           f"{field} 분야의 수많은 전문가 포트폴리오를 디자인하고 컨설팅한 경험이 있으며, 효과적인 개인 브랜딩과 시각적 커뮤니케이션 전략에 정통한 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"전문 분야: {field}\n"
        f"디자인 스타일/선호: {personal_style}\n"
        f"목표 산업/분야: {target_industry}\n"
        f"포트폴리오 형식: {portfolio_format}\n"
        f"경력 수준: {career_level}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 포트폴리오 디자인 전략 수립",
        f"   - {field} 분야에 효과적인 포트폴리오 디자인 방향 및 접근법",
        f"   - {personal_style}과 같은 개인 스타일과 전문적 아이덴티티 조화 방법",
        f"   - {target_industry} 산업의 디자인 트렌드와 기대에 부합하는 전략",
        "   - 시각적 일관성과 독창성의 균형 확보 방법",
        
        "2. 시각적 아이덴티티 개발",
        "   - 개인 브랜드를 반영한 색상 팔레트, 타이포그래피, 그래픽 요소 선정",
        "   - 로고 및 시그니처 스타일 개발 접근법",
        "   - 일관된 시각적 언어 구축 및 적용 방법",
        "   - 차별화된 개성과 전문성을 동시에 표현하는 시각적 전략",
        
        "3. 레이아웃 및 구조 최적화",
        f"   - {portfolio_format} 형식에 최적화된 레이아웃 및 정보 구조",
        "   - 가독성과 시각적 흐름을 고려한 콘텐츠 배치",
        "   - 화면 크기 및 매체 특성에 따른 적응형 디자인 전략",
        "   - 효과적인 네비게이션 및 사용자 경험 설계",
        
        "4. 시각적 계층 구조 및 포커스",
        "   - 중요 정보와 프로젝트 하이라이트를 강조하는 디자인 기법",
        "   - 시각적 리듬과 다양성을 통한 몰입도 유지 방법",
        "   - 화이트스페이스와 여백의 전략적 활용",
        "   - 시선 흐름과 정보 처리 순서를 고려한 설계",
        
        "5. 미디어 및 비주얼 요소 활용",
        "   - 프로젝트 이미지, 비디오, 애니메이션의 효과적인 활용",
        "   - 작업물 프레젠테이션을 위한 최적의 포맷 및 해상도",
        "   - 시각적 일관성을 유지하면서 다양한 프로젝트 유형 통합 방법",
        "   - 작업 과정과 결과물을 균형 있게 보여주는 비주얼 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 포트폴리오 디자인 전략 개요\n"
        "2. 개인 브랜드 시각화 가이드\n"
        "3. 포맷별 최적화 전략\n"
        "4. 시각적 요소 및 디자인 시스템 구축 방법\n"
        "5. 레이아웃 및 구조 설계 원칙\n"
        "6. 산업 및 경력 수준별 디자인 접근법\n"
        "7. 디자인 방향 설정 워크시트\n\n"
        f"{field} 분야와 {portfolio_format} 형식에 특화된 구체적인 디자인 전략과 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 포트폴리오 디자인 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n포트폴리오 디자인 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: portfolio_design_guide.md): ") or "portfolio_design_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 포트폴리오 디자인 방향 가이드")
        print(f"포트폴리오 디자인 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()