"""
학술 발표 통합 가이드

효과적인 학술 발표를 위한 구조 설계, 시각 자료 제작, Q&A 준비의 통합적 접근법
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
    print("===== 학술 발표 통합 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    presentation_type = input("발표 유형을 입력하세요 (예: 학회 발표, 포스터 발표, 세미나): ")
    audience = input("대상 청중을 입력하세요 (예: 전문 연구자, 학생, 다학제 청중): ")
    time_limit = input("발표 시간 제한을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 {presentation_type} 발표를 어떻게 준비하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 학술 발표 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 발표 및 커뮤니케이션 전문가", 
                           f"{field} 분야에서 수많은 학술 발표를 진행하고 지도한 경험이 있는 연구자로, 복잡한 연구 내용을 다양한 청중에게 효과적으로 전달하는 방법에 정통합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"발표 유형: {presentation_type}\n"
        f"대상 청중: {audience}\n"
        f"시간 제한: {time_limit}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        # 발표 구조 설계
        f"1. {presentation_type}에 적합한 전체적인 발표 구조 설계",
        f"2. {time_limit} 내에서 효과적인 내용 배분 및 시간 관리 전략",
        f"3. {audience}의 관심과 이해도를 고려한 발표 내용 맞춤화 방법",
        "4. 강력한 시작과 기억에 남는 결론 구성 전략",
        
        # 시각 자료 설계
        "5. 효과적인 슬라이드/포스터 디자인 원칙과 레이아웃",
        "6. 데이터 시각화 및 복잡한 정보의 명확한 표현 방법",
        "7. 시각 자료와 구두 발표의 조화로운 통합 방법",
        
        # 발표 전달
        "8. 발표 전달 기술 및 비언어적 커뮤니케이션 요소",
        "9. 학술적 명확성과 청중 참여 사이의 균형 유지 방법",
        
        # Q&A 및 피드백
        "10. 효과적인 Q&A 세션 준비 및 진행 전략",
        "11. 잠재적 질문 예측 및 대응 방법",
        "12. 발표 피드백 수집 및 활용 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 학술 발표 준비 통합 프레임워크\n"
        "2. 발표 구조 및 내용 설계\n"
        "3. 시각 자료 개발 및 디자인\n"
        "4. 발표 전달 및 프레젠테이션 기술\n"
        "5. Q&A 및 피드백 활용 전략\n"
        "6. 발표 준비 체크리스트 및 타임라인\n\n"
        f"{research_topic}에 대한 {presentation_type} 발표의 구체적인 구성 예시와 준비 가이드를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 학술 발표 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n학술 발표 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: academic_presentation_guide.md): ") or "academic_presentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} {presentation_type} 발표 가이드")
        print(f"학술 발표 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()