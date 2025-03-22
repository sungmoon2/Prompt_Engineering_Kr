"""
이공계 실험 보고서 템플릿

공학, 자연과학 분야의 실험 보고서 작성을 위한 템플릿
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
    print("===== 이공계 실험 보고서 템플릿 =====")
    
    # 사용자 입력 받기
    experiment_topic = input("실험 주제를 입력하세요: ")
    science_field = input("구체적인 이공계 분야를 입력하세요 (예: 화학, 물리학, 컴퓨터공학, 생물학): ")
    experiment_type = input("실험 유형을 입력하세요 (예: 정량분석, 비교실험, 데이터 수집, 시뮬레이션): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{science_field} 분야에서 {experiment_topic}에 대한 {experiment_type} 실험 보고서를 작성하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 이공계 보고서 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{science_field} 연구원 및 교수", 
                          f"최고 수준의 연구 기관에서 {science_field} 분야 연구를 수행하고 학생들의 실험 보고서를 평가해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"실험 주제: {experiment_topic}\n"
        f"학문 분야: {science_field} (이공계)\n"
        f"실험 유형: {experiment_type}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 이공계 실험 보고서의 표준 구조와 각 섹션의 목적 설명",
        f"2. {science_field} 분야에 특화된 실험 보고서 형식과 요구사항",
        "3. 제목 페이지 및 초록 작성 가이드 (명확하고 간결한 내용 요약 방법)",
        "4. 서론 작성법 (실험 목적, 이론적 배경, 선행 연구 및 가설 제시)",
        "5. 재료 및 방법 섹션 작성법 (재현 가능성 확보를 위한 상세 기술 방법)",
        "6. 실험 결과 표현 가이드 (데이터 테이블, 그래프, 도표 활용법)",
        "7. 결과 논의 및 분석 작성법 (데이터 해석, 가설 검증, 오차 분석)",
        "8. 결론 및 참고문헌 작성 가이드",
        f"9. {science_field}에서 중요한 데이터 시각화 및 통계 분석 방법",
        "10. 실험 보고서에서 흔히 발생하는 오류와 주의사항"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 체계적이고 실용적인 템플릿을 제공해주세요. "
        "각 섹션마다 구체적인 지침과 예시, 그리고 적용 가능한 템플릿 문구를 포함해주세요. "
        "테이블, 그래프, 수식 등의 표현 방법도 마크다운으로 예시해주세요. "
        f"{science_field} 분야의 특수성을 반영한 실질적인 조언을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 이공계 보고서 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n이공계 보고서 템플릿을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: science_report_template.md): ") or "science_report_template.md"
        save_markdown(enhanced_result, file_path, title=f"{science_field} {experiment_topic} 실험 보고서 템플릿")
        print(f"이공계 보고서 템플릿이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()