"""
문헌 검토 작성 가이드

효과적인 문헌 검토 방법, 비판적 분석, 통합적 접근법
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
    print("===== 문헌 검토 작성 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    review_purpose = input("문헌 검토 목적을 입력하세요 (예: 연구 격차 식별, 이론적 배경 구축, 방법론 검토): ")
    review_scope = input("검토 범위를 입력하세요 (예: 출판 연도 범위, 주요 키워드, 학문적 영역): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 문헌 검토를 어떻게 작성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 문헌 검토 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("문헌 검토 및 학술 연구 전문가", 
                           f"{field} 분야의 체계적 문헌 검토 방법론 전문가로, 우수 학술지에 다수의 리뷰 논문을 출판하고, 연구자들의 문헌 검토 작성을 지도한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"문헌 검토 목적: {review_purpose}\n"
        f"검토 범위: {review_scope}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 효과적인 문헌 검토 구조 및 조직화 전략",
        f"2. {field} 분야에서 주요 문헌 식별 및 선별 방법",
        "3. 비판적이고 분석적인 문헌 평가 방법",
        "4. 문헌 간 연결과 통합적 접근법",
        f"5. {review_purpose}에 부합하는 특화 검토 전략",
        "6. 연구 동향, 패턴, 격차 식별 방법",
        "7. 이론적 프레임워크와 기존 연구 연결하는 방법",
        "8. 효과적인 인용 패턴 및 문헌 정리 방법",
        "9. 문헌 검토에서 자주 발생하는 오류와 피해야 할 사항",
        "10. 체계적이고 재현 가능한 검토 프로세스 설계"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 문헌 검토 계획 및 준비 단계\n"
        "2. 문헌 검색 및 선별 전략\n"
        "3. 문헌 분석 및 통합 방법\n"
        "4. 구조화 및 조직화 가이드\n"
        "5. 비판적 평가 및 분석 기법\n"
        "6. 문헌 검토 작성 체크리스트\n\n"
        f"{research_topic}에 대한 문헌 검토 구조 예시와 주요 섹션별 작성 가이드를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 문헌 검토 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n문헌 검토 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: literature_review_guide.md): ") or "literature_review_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 문헌 검토 작성 가이드")
        print(f"문헌 검토 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()