"""
학술 발표 Q&A 준비 전략

학술 발표 후 효과적인 질의응답 세션을 위한 준비 및 대응 전략
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
    print("===== 학술 발표 Q&A 준비 전략 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    methodology = input("연구 방법론을 간략히 입력하세요: ")
    key_findings = input("주요 연구 결과를 간략히 입력하세요: ")
    potential_issues = input("연구의 잠재적 약점이나 논쟁점이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 학술 발표 후 Q&A 준비 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 Q&A 준비 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 커뮤니케이션 및 발표 전문가", 
                           f"{field} 분야에서 수많은 학술 발표와 질의응답 세션을 성공적으로 진행하고, 연구자들의 발표 역량을 향상시키는 워크숍을 진행해온 전문가입니다.")
    
    # 맥락 제공
    context = f"연구 주제: {research_topic}\n" \
             f"학문 분야: {field}\n" \
             f"연구 방법론: {methodology}\n" \
             f"주요 연구 결과: {key_findings}"
    
    if potential_issues:
        context += f"\n잠재적 약점/논쟁점: {potential_issues}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 학술 발표 Q&A 세션의 목적과 중요성",
        "2. 발표 전 Q&A 준비를 위한 체계적인 접근법",
        f"3. {field} 분야에서 자주 제기되는 질문 유형과 대응 전략",
        f"4. {research_topic}에 관해 예상되는 핵심 질문 목록",
        f"5. {methodology}에 관한 잠재적 질문과 명확한 답변 전략",
        "6. 연구 한계와 미래 연구 방향에 관한 질문 대응법",
        "7. 도전적이거나 비판적인 질문에 대처하는 전략",
        "8. 질문을 명확히 이해하지 못했을 때의 대응 방법",
        "9. 발표 자료 내에 Q&A 지원 요소를 통합하는 방법",
        "10. Q&A 세션에서 자신감과 전문성을 유지하는 커뮤니케이션 기법"
    ]
    
    if potential_issues:
        instructions.append(f"11. {potential_issues}에 관한 질문에 효과적으로 대응하는 방법")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. Q&A 세션 준비의 중요성\n"
        "2. 예상 질문 및 모범 답변 템플릿\n"
        "3. 질문 유형별 대응 전략\n"
        "4. 도전적 질문 처리 기법\n"
        "5. Q&A 준비 체크리스트\n\n"
        f"{research_topic}에 관한 구체적인 예상 질문과 효과적인 답변 예시를 포함해주세요. 또한 여러 상황에 적용할 수 있는 실용적인 커뮤니케이션 전략을 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 Q&A 준비 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\nQ&A 준비 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: qa_preparation_guide.md): ") or "qa_preparation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 학술 발표 Q&A 준비 가이드")
        print(f"Q&A 준비 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()