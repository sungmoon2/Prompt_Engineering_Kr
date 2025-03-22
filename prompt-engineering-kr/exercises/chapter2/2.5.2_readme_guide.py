"""
효과적인 README 파일 작성 가이드

프로젝트를 명확히 소개하고 사용법을 안내하는 README 최적화 방법
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
    print("===== 효과적인 README 파일 작성 가이드 =====")
    
    # 사용자 입력 받기
    project_name = input("프로젝트 이름을 입력하세요: ")
    project_description = input("프로젝트에 대한 간략한 설명을 입력하세요: ")
    project_type = input("프로젝트 유형을 입력하세요 (예: 라이브러리, 웹 앱, CLI 도구): ")
    target_audience = input("주요 대상 사용자를 입력하세요 (예: 개발자, 데이터 과학자, 일반 사용자): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{project_name} 프로젝트를 위한 좋은 README 파일을 작성하는 방법을 알려주세요.
프로젝트 설명: {project_description}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 README 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "오픈소스 문서화 전문가", 
        "성공적인 오픈소스 프로젝트들의 문서화를 컨설팅하고, 효과적인 README 파일 작성을 통해 사용자 참여와 기여를 증진시키는 전문가입니다."
    )
    
    # 컨텍스트 추가
    context = f"""
프로젝트 정보:
- 이름: {project_name}
- 설명: {project_description}
- 프로젝트 유형: {project_type}
- 대상 사용자: {target_audience}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. README 파일의 이상적인 구조와 섹션 제안",
        "2. 프로젝트를 명확하게 소개하는 효과적인 방법",
        f"3. {target_audience}에게 적합한 설치 및 시작하기 가이드 작성 전략",
        "4. 사용 예시와 코드 샘플을 제시하는 효과적인 방법",
        "5. 프로젝트 API 또는 기능을 문서화하는 접근법",
        "6. 기여 가이드라인 및 행동 강령 작성 방법",
        "7. 라이센스, 연락처, 감사의 글 등 추가 정보 섹션 구성",
        "8. 배지, 목차, 스크린샷 등을 활용한 가독성 향상 전략",
        f"9. {project_type} 프로젝트에 특화된 README 작성 팁",
        "10. GitHub, GitLab 등 플랫폼별 README 최적화 방법"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **README 모범 구조**: {project_type} 프로젝트에 적합한 README 구조와 필수 섹션

2. **주요 섹션별 작성 가이드**:
   - 제목 및 소개
   - 설치 방법
   - 사용 방법 및 예시
   - API/기능 설명
   - 기여 방법
   - 기타 필요 섹션

3. **{project_name} 프로젝트 맞춤 README 템플릿**:
   ```markdown
   # 템플릿 내용
   ```

4. **시각적 요소 활용법**: 배지, 스크린샷, 다이어그램 등의 효과적인 활용 방법

5. **README 최적화 체크리스트**: 완성도와 효과를 검증하기 위한 항목

마크다운 형식으로 실제 사용 가능한 템플릿과 구체적인 예시를 포함해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 README 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\nREADME 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: readme_guide.md): ") or "readme_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{project_name} README 작성 가이드")
        print(f"README 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()