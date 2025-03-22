"""
팀 프로젝트 발표 내용 최적화 방법

팀 발표의 기여자 간 일관성 및 효과적인 협업 발표 전략
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
    print("===== 팀 프로젝트 발표 내용 최적화 방법 =====")
    
    # 사용자 입력 받기
    project_topic = input("팀 프로젝트 주제를 입력하세요: ")
    team_size = input("팀원 수를 입력하세요: ")
    project_components = input("프로젝트의 주요 구성 요소를 입력하세요 (쉼표로 구분): ")
    audience = input("대상 청중을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{project_topic}에 대한 {team_size}명의 팀 발표를 어떻게 구성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 팀 발표 최적화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("팀 프레젠테이션 전략가 및 협업 커뮤니케이션 전문가", 
                           "다수의 성공적인 팀 프로젝트 발표를 기획하고 코칭한 경험이 있으며, 다양한 분야에서 팀 발표의 효과성을 극대화하는 방법론을 연구해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"팀 프로젝트 주제: {project_topic}\n"
        f"팀원 수: {team_size}명\n"
        f"프로젝트 구성 요소: {project_components}\n"
        f"대상 청중: {audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {project_topic}에 대한 효과적인 팀 발표 구조 설계",
        f"2. {team_size}명의 발표자 간 역할 분담 및 전환 전략",
        "3. 발표의 일관성과 통일성 확보를 위한 방법",
        f"4. {project_components} 요소들의 논리적 연결 및 통합 방안",
        "5. 각 팀원의 전문성과 강점을 활용한 발표 최적화 방법",
        "6. 효과적인 팀 발표를 위한 시각 자료 통합 전략",
        "7. 발표자 간 원활한 전환과 흐름 유지 방법",
        "8. 팀 발표 준비 과정에서의 협업 및 연습 전략",
        "9. 질의응답 시간의 팀 대응 전략",
        "10. 팀 발표에서 흔히 발생하는 문제점과 해결 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 팀 발표 전체 구조 및 흐름 설계\n"
        "2. 팀원별 역할 분담 및 내용 할당 가이드\n"
        "3. 통일성과 일관성 확보 전략\n"
        "4. 발표자 간 전환 및 협업 기법\n"
        "5. 팀 발표 준비 및 연습 체크리스트\n\n"
        f"{project_topic}에 대한 구체적인 팀 발표 구성 예시와 각 팀원의 역할 제안을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 팀 발표 최적화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n팀 발표 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: team_presentation_guide.md): ") or "team_presentation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{project_topic} 팀 발표 최적화 가이드")
        print(f"팀 발표 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()