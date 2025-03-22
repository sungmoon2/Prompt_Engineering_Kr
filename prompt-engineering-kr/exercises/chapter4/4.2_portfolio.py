"""
포트폴리오 개발 및 최적화

취업 경쟁력을 높이기 위한 효과적인 포트폴리오 제작 전략
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
    print("===== 포트폴리오 개발 및 최적화 =====")
    
    # 사용자 입력 받기
    field = input("전문 분야를 입력하세요 (예: 웹 개발, 그래픽 디자인, 마케팅): ")
    career_stage = input("경력 단계를 입력하세요 (예: 신입, 주니어, 시니어): ")
    key_skills = input("핵심 스킬을 입력하세요 (쉼표로 구분): ")
    project_types = input("포트폴리오에 포함할 프로젝트 유형을 입력하세요: ")
    target_audience = input("포트폴리오의 주요 대상을 입력하세요 (예: 채용담당자, 클라이언트): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{field} 분야의 포트폴리오를 어떻게 만들면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 포트폴리오 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{field} 분야 포트폴리오 전문가", 
                           f"{field} 분야에서 수많은 전문가들의 포트폴리오를 컨설팅하고, 채용 과정에서 포트폴리오를 평가해온 경험이 풍부한 전문가로, 취업과 경력 개발에 효과적인 포트폴리오 전략을 제시합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"전문 분야: {field}\n"
        f"경력 단계: {career_stage}\n"
        f"핵심 스킬: {key_skills}\n"
        f"프로젝트 유형: {project_types}\n"
        f"타겟 대상: {target_audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 포트폴리오 전략 수립",
        f"   - {field} 분야에서 효과적인 포트폴리오의 핵심 요소와 구성",
        f"   - {career_stage} 단계에 적합한 포트폴리오 범위와 깊이",
        f"   - {target_audience}의 관점에서 본 포트폴리오 평가 기준",
        "   - 차별화된 개인 브랜드 구축 방법",
        
        "2. 프로젝트 선정 및 구성",
        f"   - {key_skills}를 효과적으로 보여줄 수 있는 프로젝트 선정 기준",
        f"   - {project_types}와 같은 프로젝트의 효과적인 구성 및 설명 방법",
        "   - 다양성과 전문성의 균형을 갖춘 프로젝트 포트폴리오 구성",
        "   - 각 프로젝트의 문제 해결 과정과 결과를 효과적으로 제시하는 방법",
        
        "3. 포트폴리오 형식 및 플랫폼",
        f"   - {field} 분야에 적합한 포트폴리오 형식 (웹사이트, PDF, 비디오 등)",
        "   - 직관적이고 효과적인 네비게이션 및 레이아웃 설계",
        "   - 반응형 디자인 및 사용자 경험 최적화",
        "   - 적절한 플랫폼 선택 및 활용 전략",
        
        "4. 프로젝트 설명 및 스토리텔링",
        "   - 각 프로젝트의 맥락, 도전 과제, 해결책, 결과를 명확히 전달하는 구조",
        "   - 기술적 세부사항과 비즈니스 가치의 균형 있는 설명",
        "   - 개인의 기여도와 역할을 효과적으로 강조하는 방법",
        "   - 시각적 요소와 텍스트의 최적 조합",
        
        "5. 지속적인 관리 및 업데이트",
        "   - 정기적인 포트폴리오 업데이트 전략",
        "   - 피드백 수집 및 반영 방법",
        "   - 트렌드와 산업 변화에 따른 포트폴리오 조정",
        "   - 포트폴리오와 다른 취업 문서(이력서, LinkedIn 등)의 연계"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 포트폴리오의 핵심 원칙\n"
        "2. 포트폴리오 전략 및 구성 가이드\n"
        "3. 프로젝트 선정 및 설명 방법\n"
        "4. 시각적 표현 및 디자인 최적화\n"
        "5. 포트폴리오 플랫폼 선택 가이드\n"
        "6. 효과적인 프로젝트 설명 템플릿\n"
        "7. 포트폴리오 평가 및 개선 체크리스트\n\n"
        f"{field} 분야에 특화된 구체적인 예시와 실용적인 조언을 포함해주세요. {career_stage} 단계에 적합한 포트폴리오 개발 전략과 {target_audience}의 관점을 고려한 최적화 방법을 상세히 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 포트폴리오 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n포트폴리오 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: portfolio_guide.md): ") or "portfolio_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 포트폴리오 개발 및 최적화 가이드")
        print(f"포트폴리오 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()