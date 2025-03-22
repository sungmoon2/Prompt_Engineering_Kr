"""
경쟁 공모전 제안서 작성

제안서 작성, 아이디어 차별화, 평가 기준 최적화, 발표 전략을 통합한 공모전 준비 기법
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 경쟁 공모전 제안서 작성 =====")
    
    # 사용자 입력 받기
    competition_name = input("공모전 이름/주제를 입력하세요: ")
    main_idea = input("주요 아이디어/컨셉을 입력하세요: ")
    criteria = input("공모전 평가 기준을 입력하세요 (쉼표로 구분): ")
    target_audience = input("심사위원/타겟 청중을 입력하세요: ")
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("공모전 제안서 전략 컨설턴트", 
                         "다수의 공모전 수상 경험과 심사 경험을 바탕으로 경쟁력 있는 제안서 작성과 효과적인 발표 전략을 제공하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"공모전 정보: {competition_name}\n"
        f"주요 아이디어: {main_idea}\n"
        f"평가 기준: {criteria}\n"
        f"심사위원/타겟: {target_audience}"
    )
    
    # 지시사항 추가 - 하위 챕터 내용 통합
    prompt_builder.add_instructions([
        # 4.4.1 공모전 제안서 작성법 반영
        "1. 공모전 제안서 구조와 핵심 구성요소를 제시해주세요.",
        "   - 효과적인 제안서 프레임워크와 주요 섹션 구성",
        "   - 제안서 작성 시 핵심 원칙과 접근법",
        
        # 4.4.2 아이디어 차별화 전략 반영
        f"2. {main_idea}를 경쟁자들과 차별화하는 전략을 제시해주세요.",
        "   - 독창성과 혁신성을 부각시키는 방법",
        "   - 차별화 포인트 명확화 및 강조 기법",
        
        # 4.4.3 평가 기준 최적화 전략 반영
        f"3. {criteria} 평가 기준에 맞춘 제안서 최적화 방법을 설명해주세요.",
        "   - 각 평가 요소별 대응 전략과 강조점",
        "   - 심사위원 관점에서의 제안서 평가 요소",
        
        # 4.4.4 제안서 발표 최적화 반영
        f"4. {target_audience}를 고려한 효과적인 발표 전략을 제안해주세요."
        "   - 주요 메시지 전달 방법 및 시각 자료 활용법",
        "   - 질의응답 대비 및 발표 임팩트 극대화 기법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 제안서 구조 및 작성 프레임워크\n"
        "2. 아이디어 차별화 전략\n"
        "3. 평가 기준별 최적화 접근법\n"
        "4. 효과적인 발표 및 피칭 전략\n"
        "5. 공모전 준비 종합 체크리스트\n\n"
        f"{competition_name} 공모전에 특화된 실용적인 전략과 구체적인 예시를 제공해주세요."
    )
    
    # 프롬프트 실행
    enhanced_prompt = prompt_builder.build()
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 공모전 제안서 전략 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n공모전 제안서 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: competition_guide.md): ") or "competition_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{competition_name} 공모전 제안서 작성 가이드")
        print(f"공모전 제안서 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()