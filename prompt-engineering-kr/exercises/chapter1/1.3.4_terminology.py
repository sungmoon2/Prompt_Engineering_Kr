"""
전문 용어 및 개념 활용 최적화

학술적 글쓰기에서 전문 용어와 개념을 효과적으로 활용하는 방법
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
    print("===== 전문 용어 및 개념 활용 최적화 =====")
    
    # 사용자 입력 받기
    topic = input("주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    audience = input("대상 독자 수준을 입력하세요 (예: 학부생, 대학원생, 전문가): ")
    text_sample = input("전문 용어 활용을 개선할 텍스트 샘플을 입력하세요 (없으면 Enter): ")
    
    if not text_sample:
        text_sample = f"{topic}는 중요한 연구 분야입니다. 많은 연구자들이 이 주제에 관심을 가지고 있으며, 다양한 측면에서 연구되고 있습니다. 하지만 여전히 많은 부분이 불분명하고 더 연구가 필요합니다."
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 텍스트에 {field} 분야의 전문 용어를 추가해줘:

{text_sample}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 전문 용어 활용 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{field} 분야 용어학 및 학술 커뮤니케이션 전문가", 
                           f"{field} 분야의 전문 용어 사전 편찬에 참여하고, 학술 글쓰기에서의 전문 용어 활용에 관한 워크숍을 진행해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"학문 분야: {field}\n"
        f"대상 독자: {audience}\n"
        f"텍스트 샘플:\n\n{text_sample}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. 제공된 텍스트를 {field} 분야의 적절한 전문 용어와 개념으로 최적화해주세요.",
        f"2. {audience} 수준에 적합한 전문성과 접근성의 균형을 유지해주세요.",
        "3. 각 전문 용어를 처음 도입할 때 적절한 정의나 설명을 제공해주세요.",
        "4. 일반적 표현을 분야 특화 용어로 대체할 수 있는 부분을 식별해주세요.",
        "5. 전문 용어의 과도한 사용이나 불필요한 전문용어병(jargon)을 피해주세요.",
        "6. 전문 용어 간의 논리적 연결과 개념적 일관성을 유지해주세요.",
        "7. 각 용어의 적절한 맥락과 범위를 고려하여 활용해주세요.",
        "8. 용어 사용의 정확성과 최신성을 확보해주세요.",
        "9. 최적화된 텍스트와 원본 텍스트를 비교하며 변경 사항을 설명해주세요.",
        f"10. {field} 분야에서 효과적인 전문 용어 활용을 위한 일반 원칙과 지침을 제공해주세요."
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 전문 용어가 최적화된 텍스트\n"
        "2. 용어 활용 전후 비교 분석\n"
        "3. 주요 용어 해설 및 선택 이유\n"
        "4. 용어 활용 원칙 및 지침\n"
        "5. 대상 독자별 용어 수준 조정 전략\n\n"
        f"{field} 분야의 핵심 개념과 용어를 효과적으로 설명하는 구체적인 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 전문 용어 활용 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n전문 용어 활용 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: terminology_guide.md): ") or "terminology_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 분야 전문 용어 활용 가이드")
        print(f"전문 용어 활용 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()