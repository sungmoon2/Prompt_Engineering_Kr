"""
타겟 대상자 맞춤 디자인

채용 담당자 및 클라이언트 유형별 포트폴리오 최적화 전략
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
    print("===== 타겟 대상자 맞춤 디자인 =====")
    
    # 사용자 입력 받기
    audience_type = input("주요 포트폴리오 대상자 유형을 입력하세요 (예: 채용담당자, 클라이언트, 에이전시): ")
    industry = input("목표 산업이나 분야를 입력하세요: ")
    portfolio_content = input("포트폴리오의 주요 콘텐츠 유형을 입력하세요 (예: 웹 디자인, 개발 프로젝트, UX 연구): ")
    audience_characteristics = input("대상자의 특성이나 선호도를 입력하세요 (알고 있는 경우): ")
    goals = input("포트폴리오를 통해 달성하고자 하는 목표를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{audience_type}을 위한 포트폴리오는 어떻게 디자인해야 할까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 타겟 대상자 맞춤 디자인 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("타겟 마케팅 및 포트폴리오 전략 전문가", 
                           f"{industry} 산업에서 다양한 대상자를 위한 포트폴리오를 컨설팅하고, 대상자의 심리와 의사결정 과정을 이해하여 효과적인 커뮤니케이션 전략을 설계하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"대상자 유형: {audience_type}\n"
        f"목표 산업: {industry}\n"
        f"포트폴리오 콘텐츠: {portfolio_content}\n"
        f"대상자 특성: {audience_characteristics}\n"
        f"달성 목표: {goals}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 대상자 심리 및 니즈 분석",
        f"   - {audience_type}의 의사결정 과정 및 우선순위 이해",
        f"   - {industry} 산업의 {audience_type}이 중요시하는 요소와 평가 기준",
        f"   - {audience_characteristics}와 같은 특성을 고려한 접근 전략",
        "   - 대상자의 시간 제약과 주의력 패턴 분석",
        
        "2. 콘텐츠 구성 및 강조점 전략",
        f"   - {audience_type}의 관심을 끄는 핵심 정보 위계 설정",
        f"   - {portfolio_content}를 대상자 관점에서 가장 효과적으로 구성하는 방법",
        f"   - {goals} 달성을 위해 강조해야 할 핵심 요소와 증명 포인트",
        "   - 기술적 정보와 비즈니스 가치의 균형 설정",
        
        "3. 시각적 커뮤니케이션 최적화",
        f"   - {audience_type}에게 어필하는 시각적 언어와 스타일",
        f"   - {industry} 분야에 적합한 전문성과 창의성의 균형",
        "   - 효과적인 첫인상 형성을 위한 시각적 전략",
        "   - 대상자의 스크리닝 패턴을 고려한 정보 배치",
        
        "4. 상호작용 및 사용자 경험 설계",
        "   - 대상자의 포트폴리오 탐색 경로 설계",
        "   - 핵심 정보 접근성 최적화 전략",
        "   - 대상자 참여도를 높이는 인터랙션 요소",
        "   - 다양한 기기 및 환경에서의 접근성 고려",
        
        "5. 차별화 및 기억 전략",
        "   - 경쟁 속에서 돋보이는 독특한 가치 제안(UVP) 전달 방법",
        "   - 대상자 기억에 남는 핵심 메시지 설정",
        "   - 후속 조치를 유도하는 전략적 행동 유도(CTA)",
        "   - 브랜드 일관성과 전문성 강화 요소"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 대상자 중심 포트폴리오 전략 개요\n"
        "2. 대상자 유형별 특성 및 선호도 분석\n"
        "3. 콘텐츠 최적화 및 강조점 가이드\n"
        "4. 시각적 커뮤니케이션 전략\n"
        "5. 상호작용 및 경험 설계 원칙\n"
        "6. 차별화 및 인상적 요소 구축 방법\n"
        "7. 대상자 맞춤형 포트폴리오 체크리스트\n\n"
        f"{audience_type} 대상자를 위한 포트폴리오 최적화에 초점을 맞추고, {industry} 산업의 특성과 {portfolio_content} 콘텐츠를 효과적으로 제시하는 구체적인 전략과 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 타겟 대상자 맞춤 디자인 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n타겟 대상자 맞춤 디자인 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: target_audience_design.md): ") or "target_audience_design.md"
        save_markdown(enhanced_result, file_path, title=f"{audience_type}을 위한 포트폴리오 디자인 가이드")
        print(f"타겟 대상자 맞춤 디자인 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()