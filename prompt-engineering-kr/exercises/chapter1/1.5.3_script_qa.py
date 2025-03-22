"""
발표 스크립트 작성 및 Q&A 준비

효과적인 발표 스크립트 작성과 질의응답 준비를 위한 전략
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
    print("===== 발표 스크립트 작성 및 Q&A 준비 =====")
    
    # 사용자 입력 받기
    topic = input("발표 주제를 입력하세요: ")
    presentation_outline = input("발표 개요를 간략히 입력하세요: ")
    audience = input("대상 청중을 입력하세요: ")
    duration = input("발표 시간을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 발표 스크립트를 작성해줘. 그리고 예상 질문과 답변도 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 스크립트 작성 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("발표 스크립트 작가 및 발표 코치", 
                           "다양한 학술 및 전문 발표를 위한 스크립트 작성과, 효과적인 질의응답 준비에 특화된 전문가로서 발표자들의 자신감과 명확한 메시지 전달을 지원합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"발표 주제: {topic}\n"
        f"발표 개요: {presentation_outline}\n"
        f"대상 청중: {audience}\n"
        f"발표 시간: {duration}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {topic}에 대한 효과적인 발표 스크립트 작성",
        "2. 청중의 관심을 사로잡는 강력한 시작과 기억에 남는 결론",
        "3. 자연스럽고 명확한 구어체 표현으로 작성",
        f"4. {audience}에 맞는 적절한 언어 수준과 톤 설정",
        f"5. {duration} 시간에 맞는 적절한 내용량과 속도 고려",
        "6. 슬라이드 전환 및 시각 자료 참조를 위한 큐 포함",
        "7. 강조해야 할 핵심 포인트와 어조 변화 표시",
        "8. 발표 후 예상되는 질문 목록 작성",
        "9. 각 질문에 대한 명확하고 간결한 답변 준비",
        "10. 난이도가 높거나 도전적인 질문에 대처하는 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 완성된 발표 스크립트 (시작, 본론, 결론 포함)\n"
        "2. 스크립트 전달 팁 (속도, 강조, 쉼 등)\n"
        "3. 예상 질문 및 모범 답변 (최소 8개)\n"
        "4. 까다로운 질문 대처법\n"
        "5. 발표 전 준비 체크리스트\n\n"
        "발표 스크립트에는 슬라이드 전환 시점과 시각 자료 참조 지점을 명확히 표시해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 스크립트 작성 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n발표 스크립트와 Q&A 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: presentation_script.md): ") or "presentation_script.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 발표 스크립트 및 Q&A 가이드")
        print(f"발표 스크립트와 Q&A 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()