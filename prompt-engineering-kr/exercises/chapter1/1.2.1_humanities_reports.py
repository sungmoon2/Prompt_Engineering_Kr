"""
인문사회계열 리포트 작성 프롬프트

인문학, 사회과학 분야의 리포트 작성을 위한 특화 프롬프트
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
    print("===== 인문사회계열 리포트 작성 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("리포트 주제를 입력하세요: ")
    specific_field = input("구체적인 인문사회 분야를 입력하세요 (예: 철학, 역사학, 사회학, 문학): ")
    report_type = input("리포트 유형을 입력하세요 (예: 문헌 분석, 비교 연구, 사례 연구): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{specific_field} 분야에서 {topic}에 대한 {report_type} 리포트를 작성하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 인문사회계열 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{specific_field} 교수", 
                          f"저명한 대학의 {specific_field} 교수로서 학술지 편집위원이며 우수 강의상을 여러 차례 수상한 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"학문 분야: {specific_field} (인문사회계열)\n"
        f"리포트 유형: {report_type}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {specific_field} 분야에서 {topic}의 학술적 중요성과 맥락 설명",
        f"2. {specific_field}에 특화된 접근 방법과 이론적 프레임워크 제안",
        f"3. 인문사회계열, 특히 {specific_field}에 적합한 {report_type} 리포트의 구조와 구성요소",
        "4. 효과적인 논증 구성 및 근거 제시 방법 (인문사회계열 특화)",
        f"5. {specific_field}에서 주로 사용되는 연구 방법론 및 적용 방법",
        "6. 인문사회계열에서 중요한 비판적 사고와 다양한 관점 통합 방법",
        "7. 인용 및 참고문헌 관리 (인문사회계열 표준 형식)",
        "8. 인문사회계열 리포트에서 흔히 발생하는 오류와 피해야 할 사항",
        f"9. {specific_field} 분야의 우수 리포트 사례 및 특징"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 체계적으로 구조화된 안내서를 제공해주세요. "
        "각 섹션별로 명확한 제목과 하위 제목을 사용하고, "
        "인문사회계열 리포트 작성의 특수성을 반영한 실질적인 조언과 구체적인 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 인문사회계열 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n인문사회계열 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: humanities_guide.md): ") or "humanities_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{specific_field}분야 {topic} 리포트 작성 가이드")
        print(f"인문사회계열 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()