import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 소프트웨어 설계 지원 프롬프트 =====")
    
    # 사용자 입력 받기
    project_desc = input("프로젝트 설명을 입력하세요: ")
    requirements = input("주요 요구사항을 입력하세요: ")
    tech_stack = input("사용할 기술 스택을 입력하세요: ")
    constraints = input("제약 조건이 있다면 입력하세요: ")
    level = input("프로젝트 복잡성 수준을 입력하세요 (초급/중급/고급): ")
    
    # 기본 프롬프트
    basic_prompt = f"{project_desc} 프로젝트를 어떻게 설계할까?"
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 설계 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("소프트웨어 아키텍트", 
                           f"다양한 규모의 소프트웨어 시스템 설계와 {tech_stack} 기술 스택 활용에 전문성을 갖춘 시니어 아키텍트입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"프로젝트 설명: {project_desc}\n"
        f"주요 요구사항: {requirements}\n"
        f"기술 스택: {tech_stack}\n"
        f"복잡성 수준: {level}" +
        (f"\n제약 조건: {constraints}" if constraints else "")
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 요구사항 분석 및 정제",
        "   - 기능적 요구사항과 비기능적 요구사항 구분",
        "   - 핵심 기능 및 우선순위 식별",
        
        "2. 아키텍처 설계",
        "   - 적합한 아키텍처 패턴 선택 및 정당화",
        "   - 주요 컴포넌트 및 서브시스템 정의",
        "   - 컴포넌트 간 관계 및 인터페이스 설계",
        
        "3. 기술 스택 활용 전략",
        f"   - {tech_stack} 기술의 효과적 활용 방안",
        "   - 각 기술의 장단점 및 적합성 분석",
        
        "4. 데이터 모델 및 관리",
        "   - 주요 데이터 엔티티 및 관계 설계",
        "   - 데이터 저장 및 처리 전략",
        
        "5. 비기능적 요구사항 대응",
        "   - 확장성, 성능, 보안, 유지보수성 고려사항",
        "   - 잠재적 위험 및 대응 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 시스템 개요 및 목표\n"
        "2. 아키텍처 설계 및 주요 컴포넌트\n"
        "3. 기술 스택 활용 전략\n"
        "4. 데이터 모델링 및 데이터 흐름\n"
        "5. 비기능적 요구사항 충족 전략\n"
        "6. 주요 인터페이스 설계\n"
        "7. 잠재적 위험 및 완화 전략\n\n"
        "다이어그램은 텍스트로 표현하고, 필요한 경우 표를 활용하여 정보를 구조화해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 설계 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n설계 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: software_design.md): ") or "software_design.md"
        save_markdown(enhanced_result, file_path, title=f"{project_desc} 소프트웨어 설계")
        print(f"설계 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()