import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 프로젝트 구조 및 파일 구성 가이드 =====")
    
    # 사용자 입력 받기
    project_type = input("프로젝트 유형을 입력하세요 (예: 웹앱, 모바일앱, CLI 도구): ")
    language = input("주요 프로그래밍 언어를 입력하세요: ")
    framework = input("사용할 프레임워크를 입력하세요 (없으면 '없음'): ")
    scale = input("프로젝트 규모를 입력하세요 (소규모/중규모/대규모): ")
    features = input("주요 기능을 입력하세요 (쉼표로 구분): ")
    
    # 기본 프롬프트
    basic_prompt = f"{language} {project_type} 프로젝트의 디렉토리 구조를 어떻게 만들면 좋을까?"
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 프로젝트 구조 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    framework_text = framework if framework and framework.lower() != "없음" else f"{language} 생태계"
    prompt_builder.add_role("프로젝트 아키텍처 및 구조화 전문가", 
                           f"{language}와 {framework_text}에 대한 깊은 이해를 바탕으로 다양한 규모의 프로젝트 구조를 최적화하는 시니어 개발자입니다.")
    
    # 맥락 제공
    fw_context = f"프레임워크: {framework}" if framework and framework.lower() != "없음" else ""
    prompt_builder.add_context(
        f"프로젝트 유형: {project_type}\n"
        f"프로그래밍 언어: {language}\n"
        f"{fw_context}\n"
        f"프로젝트 규모: {scale}\n"
        f"주요 기능: {features}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 최적화된 프로젝트 구조 설계",
        f"   - {language}와 {framework_text}의 모범 사례 기반 구조",
        f"   - {scale} 규모 {project_type}에 적합한 디렉토리 계층",
        "   - 확장성과 유지보수성을 고려한 구성",
        
        "2. 세부 디렉토리 및 파일 구성",
        "   - 주요 디렉토리의 목적과 내용 설명",
        "   - 핵심 파일 및 설정 파일 구성",
        "   - 명명 규칙 및 조직 원칙",
        
        "3. 주요 기능별 모듈 조직화",
        f"   - {features}와 같은 기능들의 적절한 배치",
        "   - 모듈 간 의존성 관리 전략",
        
        "4. 개발 환경 및 빌드 구성",
        "   - 개발, 테스트, 배포를 위한 구성 파일",
        "   - 의존성 관리 및 패키징 전략",
        
        "5. 확장성 및 유지보수 고려사항",
        "   - 미래 기능 추가를 위한 유연한 구조",
        "   - 코드 재사용성과 모듈화 최적화"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 프로젝트 구조 개요\n"
        "2. 디렉토리 및 파일 구조 (트리 형식)\n"
        "3. 주요 디렉토리 및 파일 설명\n"
        "4. 구성 파일 및 설정 가이드\n"
        "5. 개발 워크플로우 지원 전략\n"
        "6. 확장 및 유지보수 고려사항\n\n"
        "디렉토리 구조는 ASCII 트리 형식으로 표현하고, 각 디렉토리와 주요 파일의 목적을 명확히 설명해주세요. 샘플 파일 구조나 주요 설정 파일의 예시 내용도 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 프로젝트 구조 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n프로젝트 구조 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: project_structure.md): ") or "project_structure.md"
        save_markdown(enhanced_result, file_path, title=f"{language} {project_type} 프로젝트 구조 가이드")
        print(f"프로젝트 구조 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()