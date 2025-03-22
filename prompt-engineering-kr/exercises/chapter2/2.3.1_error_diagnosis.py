"""
오류 진단 및 해결 프롬프트

코드의 오류를 효과적으로 진단하고 해결책을 얻기 위한 프롬프트 기법
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
    print("===== 오류 진단 및 해결 프롬프트 =====")
    
    # 사용자 입력 받기
    problematic_code = input("오류가 있는 코드를 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    error_message = input("오류 메시지나 문제 설명을 입력하세요: ")
    code_purpose = input("코드의 목적을 간략히 설명해주세요: ")
    learning_level = input("프로그래밍 수준을 입력하세요 (초급/중급/고급): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드에 오류가 있어. 고쳐줘:

```{language}
{problematic_code}
```

오류 메시지: {error_message}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 오류 진단 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{language} 디버깅 전문가", 
                         f"{language} 코드의 오류를 진단하고 해결하는 데 특화된 개발자로, 초보자부터 전문가까지 다양한 수준의 프로그래머를 지원한 풍부한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"문제 코드:\n```{language}\n{problematic_code}\n```\n\n"
        f"오류 메시지/문제 설명: {error_message}\n"
        f"코드 목적: {code_purpose}\n"
        f"프로그래밍 수준: {learning_level}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 오류 식별 및 진단",
        "   - 코드의 오류 유형과 정확한 위치 식별",
        "   - 오류의 근본 원인 심층 분석",
        "   - 오류 메시지 해석 및 의미 설명",
        
        "2. 단계별 해결 과정",
        "   - 오류 해결을 위한 체계적 접근법 제시",
        "   - 다양한 해결 가능성 및 장단점 분석",
        "   - 가장 효과적인 해결책 제안 및 정당화",
        
        "3. 수정된 코드 제공",
        "   - 명확한 주석과 함께 수정된 코드 제공",
        "   - 수정 사항을 명확히 강조하여 표시",
        f"   - {language} 모범 사례를 따르는 코드 작성",
        
        "4. 학습 및 예방 가이드",
        f"   - {learning_level} 수준에 맞는 설명 및 학습 자료 제공",
        "   - 유사한 오류의 향후 예방을 위한 팁",
        "   - 디버깅 기술 및 도구 추천"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 오류 요약 및 진단\n"
        "2. 근본 원인 분석\n"
        "3. 해결 접근법\n"
        "4. 수정된 코드 (변경 사항 강조)\n"
        "5. 설명 및 학습 포인트\n"
        "6. 향후 예방 팁\n\n"
        f"코드 블록은 {language} 문법 하이라이팅을 사용하고, 오류가 있는 라인과 수정된 부분을 명확히 식별할 수 있게 해주세요. {learning_level} 수준의 학습자가 개념을 이해할 수 있도록 적절한 설명과 예시를 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 오류 진단 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n오류 진단 및 해결 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: error_diagnosis.md): ") or "error_diagnosis.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 오류 진단 및 해결")
        print(f"오류 진단 및 해결 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()