"""
코드 개선 및 최적화 요청 방법

기능적으로 작동하는 코드의 성능, 가독성, 유지보수성을 향상시키기 위한 프롬프트 기법
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
    print("===== 코드 개선 및 최적화 요청 방법 =====")
    
    # 사용자 입력 받기
    working_code = input("개선하고 싶은 코드를 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    improvement_goals = input("개선하고 싶은 측면을 입력하세요 (예: 성능, 가독성, 유지보수성): ")
    constraints = input("고려해야 할 제약 조건이 있다면 입력하세요: ")
    code_context = input("코드가 사용되는 맥락/환경을 간략히 설명해주세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드를 더 좋게 개선해줘:

```{language}
{working_code}
```
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 개선 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{language} 코드 최적화 전문가", 
                          f"{language} 코드의 성능, 가독성, 유지보수성을 분석하고 개선하는 데 특화된 시니어 개발자로, 코드 리팩토링과 최적화에 관한 다년간의 경험을 보유하고 있습니다.")
    
    # 맥락 제공
    context = f"개선할 코드:\n```{language}\n{working_code}\n```\n\n" \
             f"프로그래밍 언어: {language}\n" \
             f"개선 목표: {improvement_goals}\n" \
             f"코드 사용 맥락: {code_context}"
    
    if constraints:
        context += f"\n제약 조건: {constraints}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 코드 분석 및 평가",
        "   - 현재 코드의 강점과 약점 식별",
        "   - 코드 구조, 알고리즘, 패턴 분석",
        f"   - {improvement_goals} 측면에서의 현재 상태 평가",
        
        "2. 개선 전략 및 권장사항",
        "   - 주요 개선 영역 식별 및 우선순위 설정",
        "   - 구체적이고 실행 가능한 개선 제안",
        "   - 각 제안의 이점과 잠재적 트레이드오프 설명",
        
        "3. 최적화된 코드 제공",
        "   - 명확한 주석과 함께 개선된 코드 제공",
        "   - 변경 사항을 명확히 강조하여 표시",
        f"   - {language} 모범 사례 및 관행 준수",
        
        "4. 성능 및 품질 비교",
        "   - 원본 코드와 개선된 코드의 비교 분석",
        "   - 개선 효과의 정량적/정성적 평가",
        "   - 추가 개선 가능성 및 방향 제안"
    ]
    
    if constraints:
        instructions.append("5. 제약 조건 준수 확인")
        instructions.append(f"   - {constraints}를 고려한 최적화 접근")
        instructions.append("   - 제약 조건 내에서의 최선의 해결책 제시")
        instructions.append("   - 제약 조건 완화 시 추가 개선 가능성 탐색")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 코드 분석 및 개선 기회\n"
        "2. 주요 개선 전략\n"
        "3. 최적화된 코드 (변경 사항 강조)\n"
        "4. 개선 효과 분석\n"
        "5. 추가 개선 제안\n\n"
        f"코드 블록은 {language} 문법 하이라이팅을 사용하고, 변경된 부분을 명확히 식별할 수 있게 해주세요. 각 개선 사항에 대해 그 이유와 이점을 명확히 설명하고, 가능한 경우 성능이나 유지보수성에 미치는 영향을 정량적으로 평가해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 개선 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 개선 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_improvement.md): ") or "code_improvement.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 개선 및 최적화")
        print(f"코드 개선 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()