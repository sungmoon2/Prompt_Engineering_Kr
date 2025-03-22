import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 기능 명세 및 요구사항 정의 지원 =====")
    
    # 사용자 입력 받기
    project_idea = input("프로젝트 아이디어/개념을 입력하세요: ")
    target_users = input("목표 사용자 그룹을 입력하세요: ")
    project_goals = input("프로젝트의 주요 목표를 입력하세요: ")
    constraints = input("제약 조건이나 가정이 있다면 입력하세요: ")
    doc_format = input("원하는 문서 형식을 입력하세요 (예: 유저 스토리, 기능 명세서, 요구사항 정의서): ")
    
    # 기본 프롬프트
    basic_prompt = f"{project_idea} 프로젝트의 요구사항을 작성해줘."
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 요구사항 정의 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("제품 요구사항 및 기능 명세 전문가", 
                           "요구사항 수집, 분석, 문서화에 전문성을 가진 제품 관리자로, 사용자 중심 요구사항과 개발자를 위한 명확한 기능 명세를 작성하는 데 풍부한 경험을 보유하고 있습니다.")
    
    # 맥락 제공
    context = f"프로젝트 아이디어: {project_idea}\n" \
             f"목표 사용자: {target_users}\n" \
             f"프로젝트 목표: {project_goals}\n" \
             f"원하는 문서 형식: {doc_format}"
    
    if constraints:
        context += f"\n제약 조건/가정: {constraints}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 사용자 요구사항 및 문제점 분석",
        f"   - {target_users}의 주요 문제점 및 요구사항 식별",
        "   - 사용자 관점에서의 핵심 가치 및 이점 정의",
        "   - 사용자 여정 및 시나리오 설계",
        
        "2. 기능적 요구사항 정의",
        "   - 핵심 기능 및 특징 상세 명세",
        "   - 기능 우선순위 및 의존성 정의",
        "   - 시스템 행동 및 상호작용 명세",
        
        "3. 비기능적 요구사항 정의",
        "   - 성능, 보안, 확장성, 사용성 요구사항",
        "   - 품질 기준 및 제약 조건",
        "   - 규정 준수 및 표준 요구사항",
        
        "4. 요구사항 검증 기준",
        "   - 성공 기준 및 검증 방법",
        "   - 테스트 시나리오 및 사용자 수용 기준",
        
        "5. 문서 형식화 및 구조화",
        f"   - {doc_format} 형식에 맞는 체계적 문서화",
        "   - 명확하고 측정 가능한 요구사항 작성",
        "   - 개발팀과 이해관계자를 위한 이해하기 쉬운 형식"
    ])
    
    # 출력 형식 지정
    sections = [
        "1. 개요 및 배경",
        "2. 사용자 요구사항 분석",
        "3. 기능적 요구사항"
    ]
    
    if doc_format.lower() in ["유저 스토리", "user stories"]:
        sections.append("   - 에픽 및 유저 스토리 형식")
    else:
        sections.append("   - 기능별 상세 명세")
    
    sections.extend([
        "4. 비기능적 요구사항",
        "5. 제약 조건 및 가정",
        "6. 우선순위 및 로드맵",
        "7. 검증 및 수용 기준"
    ])
    
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n" + 
        "\n".join(sections) + 
        f"\n\n{doc_format} 형식에 맞게 요구사항을 체계적으로 구조화하고, 각 요구사항은 고유 ID, 설명, 우선순위, 검증 기준을 포함해주세요. 명확하고 측정 가능하며 테스트 가능한 방식으로 작성해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 요구사항 정의 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n요구사항 정의 문서를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: requirements.md): ") or "requirements.md"
        save_markdown(enhanced_result, file_path, title=f"{project_idea} 요구사항 정의서")
        print(f"요구사항 정의 문서가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()