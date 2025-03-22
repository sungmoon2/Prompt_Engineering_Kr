"""
발표 자료 기획 및 스크립트 작성

발표 구조 설계, 시각 자료 기획, 스크립트 작성, 팀 발표 최적화를 통합한 접근법
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
    print("===== 발표 자료 기획 및 스크립트 작성 =====")
    
    # 사용자 입력 받기
    topic = input("발표 주제를 입력하세요: ")
    presentation_type = input("발표 유형을 입력하세요 (예: 개인발표, 팀발표, 학술발표): ")
    duration = input("발표 시간을 입력하세요: ")
    audience = input("대상 청중을 입력하세요: ")
    visual_tool = input("사용할 시각 자료 도구를 입력하세요 (예: PowerPoint, Prezi): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {duration} 발표를 어떻게 준비하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 발표 준비 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("발표 전략 및 커뮤니케이션 마스터", 
                           "학술 및 전문 발표의 모든 측면(구조 설계, 시각화, 스크립트 작성, 팀 협업)에 대한 종합적인 전문성을 가진 발표 코치입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"발표 주제: {topic}\n"
        f"발표 유형: {presentation_type}\n"
        f"발표 시간: {duration}\n"
        f"대상 청중: {audience}\n"
        f"시각 자료 도구: {visual_tool}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 발표 구조 및 내용 설계",
        f"   - {topic}에 대한 효과적인 발표 구조 프레임워크",
        f"   - {audience}의 관심과 이해도를 고려한 내용 구성",
        f"   - {duration} 시간에 맞는 적절한 범위와 깊이 설정",
        
        "2. 시각 자료 기획 및 내용 구성",
        f"   - {visual_tool}을 활용한 효과적인 시각 자료 디자인 원칙",
        "   - 핵심 메시지를 강화하는 시각적 요소 활용 전략",
        "   - 텍스트와 시각 요소의 최적 균형 및 배치",
        
        "3. 발표 스크립트 작성 및 Q&A 준비",
        "   - 명확하고 설득력 있는 스크립트 작성 가이드",
        "   - 시각 자료와 스크립트의 통합 및 동기화 방법",
        "   - 예상 질문과 효과적인 응답 준비 전략",
        
        "4. 팀 프로젝트 발표 최적화 (해당시)",
        f"   - {presentation_type}이 팀 발표인 경우 역할 분담 및 조화 전략",
        "   - 발표자 간 전환과 일관성 유지 방법",
        "   - 팀 발표의 시너지를 극대화하는 기법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 발표 준비 종합 계획 및 일정\n"
        "2. 발표 구조 및 내용 설계 가이드\n"
        "3. 슬라이드별 내용 및 시각화 전략\n"
        "4. 발표 스크립트 템플릿과 전달 팁\n"
        "5. 발표 준비 종합 체크리스트\n\n"
        f"{topic}에 대한 구체적인 발표 준비 전략과 예시를 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 발표 준비 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n발표 준비 종합 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: presentation_master_guide.md): ") or "presentation_master_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 발표 준비 종합 가이드")
        print(f"발표 준비 종합 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()