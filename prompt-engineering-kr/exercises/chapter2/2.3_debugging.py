"""
코드 디버깅 및 개선

오류 진단, 코드 최적화, 문서화, 스타일 개선을 통합한 종합적 코드 향상 접근법
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
    print("===== 코드 디버깅 및 개선 =====")
    
    # 사용자 입력 받기
    code = input("디버깅/개선이 필요한 코드를 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    issues = input("알려진 문제점이나 오류를 입력하세요 (없으면 '종합 개선'으로 입력): ")
    improvement_goals = input("개선 목표를 입력하세요 (예: 성능, 가독성, 유지보수성, 문서화): ")
    code_context = input("코드의 맥락이나 용도를 간략히 설명해주세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드를 디버깅하고 개선해줘:

```{language}
{code}
```

문제: {issues}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 디버깅 및 개선 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{language} 개발 및 코드 품질 전문가", 
                          f"{language} 코드의 디버깅, 최적화, 리팩토링, 문서화에 특화된 시니어 개발자로, 프로그래밍 문제를 진단하고 코드 품질을 종합적으로 개선하는 데 풍부한 경험을 보유하고 있습니다.")
    
    # 맥락 제공
    context = f"대상 코드:\n```{language}\n{code}\n```\n\n" \
             f"프로그래밍 언어: {language}\n" \
             f"알려진 문제/오류: {issues}\n" \
             f"개선 목표: {improvement_goals}\n" \
             f"코드 맥락/용도: {code_context}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 종합 코드 분석",
        "   - 코드의 기능 및 목적 파악",
        "   - 코드 구조, 로직, 패턴 분석",
        "   - 현재 코드의 강점과 약점 평가",
        
        "2. 오류 진단 및 해결",
        "   - 오류나 버그의 근본 원인 식별",
        "   - 잠재적인 에지 케이스 및 취약점 분석",
        "   - 단계별 문제 해결 접근법 제시",
        
        "3. 코드 최적화 및 개선",
        f"   - {improvement_goals}를 위한 최적화 전략",
        "   - 알고리즘 및 데이터 구조 개선",
        "   - 성능, 메모리 사용, 확장성 최적화",
        
        "4. 코드 문서화 및 설명",
        "   - 주요 기능 및 로직에 대한 명확한 설명",
        "   - 적절한 주석 및 문서화 추가",
        "   - API 및 사용법 문서화",
        
        "5. 스타일 및 가독성 향상",
        f"   - {language} 모범 사례 및 코딩 표준 적용",
        "   - 일관된 스타일 및 명명 규칙 적용",
        "   - 코드 구조 및 조직 개선"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 코드 분석 및 문제 진단\n"
        "2. 오류 해결 및 디버깅\n"
        "3. 코드 최적화 및 개선\n"
        "4. 문서화 및 주석 추가\n"
        "5. 스타일 및 가독성 향상\n"
        "6. 최종 개선 코드\n"
        "7. 개선 효과 및 추가 권장사항\n\n"
        f"코드 블록은 {language} 문법 하이라이팅을 사용하고, 단계별 변경 사항을 명확히 설명해주세요. 각 개선 영역에 대해 변경 이유와 기대 효과를 설명하고, 최종 개선 코드는 모든 수정사항이 통합된 완성된 형태로 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 디버깅 및 개선 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n디버깅 및 개선 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_improvement.md): ") or "code_improvement.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 디버깅 및 개선")
        print(f"디버깅 및 개선 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()