"""
코드 주석 및 문서화 최적화

코드 내 주석과 문서 문자열(docstring)을 효과적으로 작성하는 방법
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
    print("===== 코드 주석 및 문서화 최적화 =====")
    
    # 사용자 입력 받기
    code_sample = input("문서화가 필요한 코드 샘플을 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    doc_style = input("문서화 스타일을 입력하세요 (예: Google, NumPy, JSDoc, JavaDoc 등): ")
    team_context = input("팀/프로젝트 문서화 기준이 있다면 간략히 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
다음 {language} 코드를 더 잘 문서화해주세요:

```{language}
{code_sample}
```
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 코드 문서화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{language} 코드 문서화 전문가", 
        f"{language} 코드베이스의 가독성과 유지보수성을 향상시키는 최적의 문서화 관행에 정통한 전문가로, {doc_style} 스타일 가이드라인에 따른 주석과 docstring 작성에 특화되어 있습니다."
    )
    
    # 컨텍스트 추가
    context = f"""
대상 코드:
```{language}
{code_sample}
```

문서화 요구사항:
- 프로그래밍 언어: {language}
- 문서화 스타일: {doc_style}
"""
    
    if team_context:
        context += f"- 팀 문서화 기준: {team_context}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 코드 분석 및 목적 파악",
        "   - 코드의 주요 기능과 의도 식별",
        "   - 핵심 로직과 알고리즘 이해",
        "   - 잠재적인 복잡성과 혼란스러운 부분 식별",
        
        "2. 모듈/파일 수준 문서화",
        "   - 명확한 모듈 설명 및 목적 기술",
        "   - 사용 방법 및 의존성 정보 제공",
        "   - 라이센스, 저자, 버전 정보 (해당되는 경우)",
        
        "3. 함수/클래스 문서화",
        f"   - {doc_style} 스타일에 맞는 docstring 작성",
        "   - 매개변수, 반환값, 예외 상황 명확히 설명",
        "   - 사용 예시 및 제약사항 포함",
        
        "4. 인라인 주석 최적화",
        "   - 복잡한 로직이나 비자명한 부분에 주석 추가",
        "   - 주석 내용의 명확성과 간결성 유지",
        "   - 불필요한 주석 피하기 (코드가 자명한 경우)",
        
        "5. 코드와 함께 문서화된 버전 제공",
        "   - 원본 코드 구조 및 들여쓰기 유지",
        "   - 문서화가 추가된 완성된 코드 제공",
        "   - 주요 문서화 변경 사항 설명"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = """
다음 형식으로 응답해주세요:

1. **코드 분석**: 코드의 목적과 기능에 대한 간략한 분석

2. **문서화 접근 전략**: 해당 코드 문서화를 위한 전반적인 접근 방법

3. **문서화된 코드**:
   ```language
   // 문서화된 코드를 여기에 제공
   ```

4. **문서화 설명**: 추가한 문서화 요소와 선택한 이유

5. **문서화 모범 사례**: 이와 같은 코드 문서화를 위한 일반적인 지침과 권장사항

코드 블록은 적절한 언어 표시와 함께 마크다운 형식으로 제공해주세요. 원본 코드 구조를 유지하면서 효과적인 문서화를 추가해주세요.
"""
    
    output_format = output_format.replace("language", language)
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 코드 문서화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n코드 문서화 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: code_documentation.md): ") or "code_documentation.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 문서화 결과")
        print(f"코드 문서화 결과가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()