"""
초록 및 결론 작성 가이드

연구의 첫인상과 마지막 인상을 결정짓는 초록과 결론의 효과적인 작성법
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
    print("===== 초록 및 결론 작성 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    paper_type = input("논문 유형을 입력하세요 (예: 실증 연구, 문헌 검토, 질적 연구): ")
    main_contributions = input("연구의 주요 기여점을 간략히 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 연구 논문의 초록과 결론을 어떻게 작성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 초록 및 결론 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 논문 작성 및 편집 전문가", 
                           f"{field} 분야의 학술지 편집위원으로 활동하며, 수많은 논문의 초록과 결론을 심사하고 개선한 경험을 가진 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"논문 유형: {paper_type}\n"
        f"주요 기여점: {main_contributions}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        # 초록 작성 지침
        "1. 효과적인 초록의 구조 및 필수 구성 요소",
        f"2. {field} 분야에서 선호되는 초록 스타일 및 특성",
        f"3. {paper_type} 논문에 특화된 초록 작성 전략",
        "4. 독자의 관심을 끌고 연구의 가치를 전달하는 초록 작성법",
        "5. 키워드 선택 및 최적화 방법",
        
        # 결론 작성 지침
        "6. 효과적인 결론의 구조 및 핵심 구성 요소",
        "7. 연구의 주요 발견점을 간결하게 요약하는 방법",
        "8. 연구의 기여도와 의의를 강조하는 전략",
        "9. 학문적/실용적 함의를 효과적으로 제시하는 방법",
        "10. 초록과 결론 사이의 일관성 유지 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 초록 작성 가이드\n"
        "2. 초록 구조 및 구성 요소\n"
        "3. 효과적인 결론 작성 가이드\n"
        "4. 결론 구조 및 구성 요소\n"
        "5. 초록과 결론의 연계 전략\n"
        "6. 초록 및 결론 작성 체크리스트\n\n"
        f"{research_topic}에 대한 {paper_type} 논문의 초록 및 결론 예시와 템플릿을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 초록 및 결론 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n초록 및 결론 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: abstract_conclusion_guide.md): ") or "abstract_conclusion_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 초록 및 결론 작성 가이드")
        print(f"초록 및 결론 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()