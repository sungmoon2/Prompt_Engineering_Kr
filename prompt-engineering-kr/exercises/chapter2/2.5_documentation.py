"""
코드 문서화 및 기술 문서 작성

코드와 프로젝트에 대한 효과적인 문서화 전략 및 도구
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
    print("===== 코드 문서화 및 기술 문서 작성 =====")
    
    # 사용자 입력 받기
    project_name = input("프로젝트 이름을 입력하세요: ")
    code_language = input("사용 중인 프로그래밍 언어를 입력하세요: ")
    doc_type = input("필요한 문서 유형을 입력하세요 (예: 코드 주석, README, API 문서, 기술명세서): ")
    audience = input("대상 독자를 입력하세요 (예: 개발자, 비개발자, 신입 팀원): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{project_name} 프로젝트를 위한 {doc_type} 문서를 작성하는 방법을 알려주세요.
프로젝트는 {code_language} 언어로 작성되었습니다.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 문서화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "기술 문서화 전문가", 
        f"{code_language} 프로젝트를 위한 다양한 문서화 작업에 전문성을 갖춘 시니어 테크니컬 라이터로, 개발자와 비개발자 모두를 위한 명확하고 이해하기 쉬운 문서를 작성하는 전문가입니다."
    )
    
    # 컨텍스트 추가
    context = f"""
문서화 요청 정보:
- 프로젝트명: {project_name}
- 프로그래밍 언어: {code_language}
- 필요한 문서 유형: {doc_type}
- 대상 독자: {audience}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {code_language} 프로젝트를 위한 {doc_type} 문서화 모범 사례와 표준 제시",
        f"2. {audience}에게 적합한 문서 스타일, 깊이, 기술 수준 가이드",
        "3. 효과적인 문서 구조와 섹션 구성 제안",
        "4. 명확하고 이해하기 쉬운 설명 작성 방법",
        "5. 코드 예제, 다이어그램, 스크린샷 등 시각적 요소 활용 방안",
        "6. 문서 유지보수와 지속적인 업데이트 전략",
        "7. 자동화 도구를 활용한 문서화 효율성 향상 방법",
        "8. 일관된 용어, 포맷, 스타일 유지 전략"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = """
다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:

1. **문서화 모범 사례 개요**: 해당 문서 유형과 프로그래밍 언어 관련 표준
2. **대상 독자별 접근 방식**: 독자에 맞춘 설명 방식과 기술 수준 조정
3. **문서 구조 템플릿**: 효과적인 섹션 구성과 포함할 내용
4. **작성 스타일 가이드**: 명확성, 일관성, 가독성을 위한 작성 지침
5. **예시와 템플릿**: 실제 적용할 수 있는 코드와 예시
6. **자동화 및 도구**: 문서화 효율성을 위한 도구와 방법론
7. **유지보수 전략**: 문서 최신 상태 유지를 위한 워크플로우
8. **평가 체크리스트**: 문서 품질 검증을 위한 점검 항목

예시와 템플릿을 포함하여 구체적이고 실용적인 가이드를 제공해주세요.
"""
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 문서화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n문서화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: documentation_guide.md): ") or "documentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{project_name} {doc_type} 문서화 가이드")
        print(f"문서화 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()