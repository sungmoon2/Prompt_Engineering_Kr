"""
API 문서화 전략 및 도구

효과적인 API 명세와 참조 문서 작성을 위한 방법론과 도구
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
    print("===== API 문서화 전략 및 도구 =====")
    
    # 사용자 입력 받기
    api_type = input("API 유형을 입력하세요 (예: REST, GraphQL, 라이브러리/SDK): ")
    language_framework = input("사용 언어/프레임워크를 입력하세요 (예: Python/FastAPI, Node/Express): ")
    api_sample = input("API 엔드포인트/함수 예시를 입력하세요: ")
    target_users = input("주요 API 사용자 유형을 입력하세요 (예: 외부 개발자, 내부 팀): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{api_type} API를 위한 효과적인 문서 작성 방법을 설명해주세요.
API 예시: {api_sample}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 API 문서화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "API 문서화 전문가", 
        f"{api_type} API 문서화에 특화된 테크니컬 라이터로, {language_framework} 기반 API의 명확하고 이해하기 쉬운 문서 작성과 최신 문서화 도구 활용에 전문성을 보유하고 있습니다."
    )
    
    # 컨텍스트 추가
    context = f"""
API 정보:
- 유형: {api_type}
- 기술 스택: {language_framework}
- 예시 엔드포인트/함수: {api_sample}
- 주요 사용자: {target_users}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. API 문서화 모범 사례 및 표준",
        f"   - {api_type} API에 특화된 문서화 접근법",
        f"   - {language_framework}에 적합한 문서화 형식",
        "   - 문서화 규약 및 일관성 유지 전략",
        
        "2. API 참조 문서 구조 및 내용",
        "   - 효과적인 API 개요 및 소개 작성법",
        "   - 엔드포인트/함수 명세 작성 방법",
        "   - 매개변수, 응답, 오류 코드 문서화",
        "   - 요청/응답 예제 및 샘플 코드 제공 전략",
        
        "3. 문서화 도구 및 자동화 방법",
        f"   - {api_type} API 문서화에 적합한 도구 추천",
        f"   - {language_framework}에서 문서 자동 생성 방법",
        "   - API 명세 표준(OpenAPI, RAML 등) 활용법",
        "   - 문서와 코드 동기화 유지 전략",
        
        "4. 사용자 경험 최적화",
        f"   - {target_users}에게 적합한 문서 수준과 접근법",
        "   - 검색성과 탐색성 향상 전략",
        "   - 인터랙티브 문서(예: Try-it-out) 구현 방법",
        "   - 사용 안내서, 튜토리얼, 시작하기 가이드 작성법"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **API 문서화 모범 사례 개요**: {api_type} API 문서화를 위한 핵심 원칙과 접근법

2. **API 문서 구조 템플릿**:
   ```markdown
   # API 문서 구조 예시
   ```

3. **{api_sample} 예시 문서**:
   ```markdown
   # 예시 API 엔드포인트/함수 문서
   ```

4. **문서화 도구 및 자동화 추천**:
   - {language_framework}에 적합한 도구
   - 설정 및 활용 방법
   - 지속적 통합 전략

5. **사용자 경험 최적화 전략**: 
   - 접근성 향상을 위한 구체적 기법
   - 인터랙티브 문서 요소 구현 방법
   - 다양한 이해 수준의 사용자를 위한 접근법

6. **체크리스트**: API 문서 품질 평가를 위한 검증 항목

마크다운 형식으로 실제 API 문서화에 적용할 수 있는 구체적인 템플릿과 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 API 문서화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\nAPI 문서화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: api_documentation_guide.md): ") or "api_documentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{api_type} API 문서화 가이드")
        print(f"API 문서화 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()