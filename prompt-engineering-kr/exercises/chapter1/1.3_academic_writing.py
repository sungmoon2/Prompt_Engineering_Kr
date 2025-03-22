"""
학술적 글쓰기 향상 전략

학술적 어투, 논증 구조, 비판적 분석, 전문 용어 활용을 통합한 학술 글쓰기 향상 방법
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
    print("===== 학술적 글쓰기 향상 전략 =====")
    
    # 사용자 입력 받기
    topic = input("학술적 글쓰기 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    audience = input("대상 독자를 입력하세요 (예: 학부생, 대학원생, 전문가): ")
    text_sample = input("개선할 글쓰기 샘플을 입력하세요 (없으면 Enter): ")
    
    if not text_sample:
        text_sample = f"{topic}에 대해 연구하는 것은 중요합니다. 많은 사람들이 이것의 중요성을 인식하고 있지만, 아직 제대로 이해하지 못하는 부분도 많습니다. 이 글에서는 이 주제에 대해 알아보고, 왜 중요한지, 그리고 어떤 의미가 있는지 생각해보겠습니다."
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 텍스트를 학술적으로 더 좋게 개선해줘:

{text_sample}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 학술 글쓰기 개선 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 글쓰기 전문가", 
                           f"{field} 분야의 저명한 학술지 편집자이자 대학의 학술 글쓰기 센터 디렉터로, 수많은 논문과 학술서의 집필 및 편집 경험을 갖고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"학문 분야: {field}\n"
        f"대상 독자: {audience}\n"
        f"글쓰기 샘플:\n\n{text_sample}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 학술적 어투와 표현 최적화",
        "   - 주관적 표현을 객관적 표현으로 변환",
        "   - 구어체를 학술적 문어체로 개선",
        "   - 적절한 헤지 표현(hedging)과 한정어 활용",
        
        "2. 논증 구조 강화",
        "   - 명확한 주장(thesis) 설정",
        "   - 논리적 흐름과 결속성 향상",
        "   - 주장과 근거의 연결 강화",
        
        "3. 비판적 분석 요소 통합",
        "   - 다양한 관점과 해석 고려",
        "   - 주장의 한계 및 대안적 견해 검토",
        "   - 균형 잡힌 평가와 판단",
        
        f"4. {field} 분야 전문 용어 및 개념 최적화",
        "   - 적절한 전문 용어 도입 및 설명",
        "   - 개념적 정확성과 일관성 확보",
        "   - 독자 수준에 맞는 용어 활용"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 통합적으로 개선된 학술 텍스트\n"
        "2. 개선 사항 상세 분석 (네 가지 향상 전략별)\n"
        "3. 학술적 글쓰기 개선을 위한 체크리스트\n"
        "4. 대상 독자별 조정 방법\n"
        "5. 추가 개선을 위한 제안\n\n"
        "각 개선 전략별로 구체적인 예시와 비교를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 학술 글쓰기 개선 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n학술 글쓰기 개선 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: academic_writing_guide.md): ") or "academic_writing_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{field} 분야 학술적 글쓰기 향상 가이드")
        print(f"학술 글쓰기 개선 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()