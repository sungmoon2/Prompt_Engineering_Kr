"""
연구 발표 전략 가이드

효과적인 학술 발표 구조화 및 내용 설계를 위한 접근법
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
    print("===== 연구 발표 전략 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    key_findings = input("주요 연구 결과를 간략히 입력하세요: ")
    audience = input("대상 청중을 입력하세요 (예: 전문가, 학생, 다학제 청중): ")
    time_limit = input("발표 시간 제한을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 연구 발표를 어떻게 구성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 연구 발표 전략 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 커뮤니케이션 및 발표 전략 전문가", 
                           f"{field} 분야의 저명한 연구자로서, 수많은 학술 발표를 진행하고 코칭한 경험이 있으며, 복잡한 연구 내용을 명확하고 설득력 있게 전달하는 방법에 전문성을 갖추고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"주요 연구 결과: {key_findings}\n"
        f"대상 청중: {audience}\n"
        f"시간 제한: {time_limit}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 연구 발표의 전체적인 구조 및 흐름 설계",
        f"2. {time_limit} 시간 제한에 최적화된 내용 선별 및 배분 전략",
        f"3. {audience}의 배경 및 관심사를 고려한 발표 내용 맞춤화 방법",
        "4. 청중의 관심을 사로잡는 효과적인 시작 전략",
        "5. 연구 배경과 중요성을 간결하게 전달하는 방법",
        "6. 연구 방법론을 명확하고 설득력 있게 설명하는 전략",
        f"7. {key_findings}를 강조하는 효과적인 결과 제시 방법",
        "8. 결과의 의미와 함의를 명확히 전달하는 논의 구성 방법",
        "9. 핵심 메시지를 강화하는 강력한 결론 설계",
        "10. 발표 전달력을 높이는 스토리텔링 및 수사적 기법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 발표 구조 프레임워크 및 전략\n"
        "2. 발표 섹션별 내용 구성 가이드\n"
        "3. 청중 참여 및 관심 유지 전략\n"
        "4. 핵심 메시지 전달 최적화 방법\n"
        "5. 시간 관리 및 내용 우선순위 설정\n"
        "6. 발표 스크립트 작성 가이드\n"
        "7. 발표 구성 체크리스트\n\n"
        f"{research_topic}에 대한 구체적인 발표 구성 예시와 각 섹션별 시간 배분 계획을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 연구 발표 전략 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n연구 발표 전략 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: research_presentation_guide.md): ") or "research_presentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 연구 발표 전략 가이드")
        print(f"연구 발표 전략 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()