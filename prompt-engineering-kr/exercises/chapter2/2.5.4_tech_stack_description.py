"""
기술 스택 설명 및 아키텍처 문서화

프로젝트의 기술 스택과 아키텍처를 효과적으로 설명하고 문서화하는 방법
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
    print("===== 기술 스택 설명 및 아키텍처 문서화 =====")
    
    # 사용자 입력 받기
    tech_stack = input("주요 기술 스택을 쉼표로 구분하여 입력하세요: ")
    project_type = input("프로젝트 유형을 입력하세요 (예: 웹 앱, 마이크로서비스, 데이터 파이프라인): ")
    target_audience = input("문서의 주요 대상 독자를 입력하세요 (예: 신규 개발자, 프로젝트 관리자, 경영진): ")
    arch_complexity = input("아키텍처 복잡성 수준을 입력하세요 (단순/중간/복잡): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{tech_stack} 기술을 사용하는 {project_type}의 기술 스택과 아키텍처를 설명하는 문서를 작성하는 방법을 알려주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 기술 스택 문서화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "기술 아키텍처 문서화 전문가", 
        f"복잡한 기술 아키텍처와 스택을 다양한 독자층에게 명확하게 설명할 수 있는 능력을 가진 기술 작가로, {project_type} 유형의 프로젝트에서 사용되는 {tech_stack}와 같은 기술 스택의 문서화에 특화되어 있습니다."
    )
    
    # 컨텍스트 추가
    context = f"""
프로젝트 정보:
- 기술 스택: {tech_stack}
- 프로젝트 유형: {project_type}
- 대상 독자: {target_audience}
- 아키텍처 복잡성: {arch_complexity}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 기술 스택 설명 전략",
        "   - 개별 기술의 역할과 목적 설명 방법",
        "   - 기술 선택 이유와 대안 비교 방식",
        "   - 기술 간 상호작용 및 의존성 설명 기법",
        "   - 각 기술의 버전 및 호환성 정보 문서화",
        
        "2. 아키텍처 문서화 접근법",
        f"   - {project_type}에 적합한 아키텍처 표현 방식",
        f"   - {arch_complexity} 수준의 복잡성 적절히 설명하는 방법",
        "   - 컴포넌트, 모듈, 서비스 간 관계 표현 전략",
        "   - 데이터 흐름 및 통신 방식 설명 기법",
        
        "3. 시각적 표현 방법",
        "   - 적절한 다이어그램 유형 선택 가이드",
        "   - 아키텍처 다이어그램 작성 모범 사례",
        "   - 텍스트와 다이어그램의 효과적인 조합",
        "   - 복잡성 수준별 적절한 추상화 방법",
        
        "4. 대상자별 문서화 전략",
        f"   - {target_audience}에게 적합한 기술적 깊이와 용어 선택",
        "   - 기술적/비기술적 독자를 위한 정보 구성 방법",
        "   - 다양한 지식 수준을 고려한 계층적 정보 제공",
        "   - 핵심 개념과 세부 사항의 균형 유지 방법"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **기술 스택 문서화 모범 사례**: {project_type}의 기술 스택 문서화를 위한 핵심 원칙과 접근법

2. **기술 스택 설명 템플릿**:
   ```markdown
   # 기술 스택 설명 문서 구조
   ```

3. **아키텍처 문서화 가이드**:
   - 효과적인 아키텍처 설명 방법
   - 다이어그램 유형 및 활용법
   - 복잡성 관리 전략

4. **{tech_stack} 기반 {project_type} 예시 문서**:
   ```markdown
   # 예시 기술 스택 및 아키텍처 문서
   ```

5. **{target_audience}을 위한 맞춤형 전략**:
   - 이해도 증진을 위한 구체적 접근법
   - 주요 관심사와 연결하는 방법

6. **유지보수 및 업데이트 전략**: 기술 스택 변화에 따른 문서 최신화 방법

마크다운 형식으로 실제 적용 가능한 템플릿과 예시를 제공해주세요. ASCII 다이어그램이나 마크다운으로 표현할 수 있는 시각적 예시도 포함해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 기술 스택 문서화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n기술 스택 문서화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: tech_stack_guide.md): ") or "tech_stack_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{project_type} 기술 스택 및 아키텍처 문서화 가이드")
        print(f"기술 스택 문서화 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()