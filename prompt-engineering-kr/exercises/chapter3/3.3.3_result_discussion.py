"""
결과 논의 작성 가이드

연구 결과의 효과적인 해석과 의미 있는 논의 전개 방법
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
    print("===== 결과 논의 작성 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    key_findings = input("주요 연구 결과를 간략히 입력하세요: ")
    audience = input("주요 독자층을 입력하세요 (예: 연구자, 실무자, 일반 대중): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 연구 결과의 논의 섹션을 어떻게 작성하면 좋을까?
주요 결과: {key_findings}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 결과 논의 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 논문 작성 및 학술 커뮤니케이션 전문가", 
                           f"{field} 분야의 저명한 학술지 편집자이자 연구자로서, 연구 결과의 해석과 효과적인 논의 작성에 전문성을 갖추고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"주요 연구 결과: {key_findings}\n"
        f"주요 독자층: {audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 효과적인 논의 섹션의 구조와 구성 요소",
        "2. 연구 결과의 명확한 해석 및 의미 부여 방법",
        "3. 연구 질문 및 가설과 결과 연결하기",
        "4. 기존 문헌과의 비교 및 대조 전략",
        "5. 예상치 못한 결과 또는 모순의 처리 방법",
        "6. 연구의 이론적, 실무적 함의 도출 방법",
        "7. 연구의 한계점을 건설적으로 제시하는 방법",
        "8. 미래 연구 방향 제안 전략",
        f"9. {audience}의 관심과 필요에 맞는 논의 맞춤화 방법",
        "10. 논의 섹션에서 흔히 발생하는 실수와 해결 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 논의 섹션 구조 및 구성 요소\n"
        "2. 결과 해석 및 의미 부여 전략\n"
        "3. 기존 문헌과의 연결 및 비교 방법\n"
        "4. 이론적/실무적 함의 도출 가이드\n"
        "5. 한계점 및 미래 연구 제안 작성법\n"
        "6. 논의 섹션 작성 체크리스트\n\n"
        f"{research_topic}에 대한 구체적인 논의 섹션 예시 구조와 각 부분에 대한 작성 가이드를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 결과 논의 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n결과 논의 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: result_discussion_guide.md): ") or "result_discussion_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 연구 결과 논의 작성 가이드")
        print(f"결과 논의 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()