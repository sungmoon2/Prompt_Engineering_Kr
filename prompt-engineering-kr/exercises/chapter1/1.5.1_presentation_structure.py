"""
발표 구조 및 내용 설계 프롬프트

효과적인 학술 및 전문 발표의 구조와 내용을 설계하는 프롬프트 기법
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
    print("===== 발표 구조 및 내용 설계 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("발표 주제를 입력하세요: ")
    presentation_type = input("발표 유형을 입력하세요 (예: 학술 발표, 프로젝트 제안, 연구 결과 발표): ")
    audience = input("대상 청중을 입력하세요 (예: 교수진, 학생, 전문가): ")
    duration = input("발표 시간을 입력하세요 (예: 10분, 20분): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {duration} 발표를 어떻게 구성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 발표 구조 설계 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("발표 전략 및 커뮤니케이션 전문가", 
                           "수많은 학술 및 전문 발표를 기획하고 코칭해온 경험이 있으며, 효과적인 발표 구조와 내용 설계에 관한 다수의 저서를 집필했습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"발표 주제: {topic}\n"
        f"발표 유형: {presentation_type}\n"
        f"대상 청중: {audience}\n"
        f"발표 시간: {duration}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {topic}에 대한 {duration} 발표에 최적화된 전체 구조 설계",
        "2. 청중의 관심을 사로잡는 효과적인 도입부 전략",
        "3. 핵심 메시지의 명확한 정의 및 전달 방법",
        f"4. {audience}에게 적합한 내용 수준과 접근 방식",
        f"5. {duration} 시간 내에 효과적으로 전달할 수 있는 적절한 내용량 설정",
        "6. 핵심 포인트의 효과적인 조직화 및 연결 방법",
        "7. 발표의 논리적 흐름과 일관성 확보 전략",
        "8. 각 섹션별 적절한 시간 배분 가이드",
        "9. 청중의 기억에 남는 효과적인 결론 전략",
        "10. 발표 후 질의응답을 위한 준비 지침"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 발표 전체 구조 및 시간 배분\n"
        "2. 각 섹션별 세부 내용 가이드\n"
        "3. 청중 참여 및 집중력 유지 전략\n"
        "4. 발표 준비 체크리스트\n"
        "5. 발표 내용 템플릿\n\n"
        f"{topic}에 대한 {presentation_type} 발표의 구체적인 내용 구성과 각 섹션별 목표를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 발표 구조 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n발표 구조 설계 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: presentation_structure_guide.md): ") or "presentation_structure_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} {presentation_type} 발표 구조 설계")
        print(f"발표 구조 설계 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()