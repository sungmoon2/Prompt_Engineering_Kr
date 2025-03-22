"""
경험 기반 구조화 답변 작성법

STAR 기법을 활용한 경험 중심 면접 답변 구조화 및 스토리텔링 최적화 전략
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
    print("===== 경험 기반 구조화 답변 작성법 =====")
    
    # 사용자 입력 받기
    experience = input("활용하고 싶은 경험/프로젝트/성과를 입력하세요: ")
    skills_demonstrated = input("이 경험을 통해 보여주고 싶은 역량/스킬을 입력하세요: ")
    target_questions = input("이 경험으로 답변하고 싶은 면접 질문 유형을 입력하세요: ")
    job_position = input("지원하는 직무/포지션을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{experience}에 대한 면접 답변을 STAR 기법으로 작성해줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 STAR 답변 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("면접 스토리텔링 전문가", 
                          "경험 기반 면접 답변을 구조화하고 후보자의 강점을 효과적으로 부각시키는 기법에 특화된 면접 코치입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"활용 경험: {experience}\n"
        f"보여주고 싶은 역량/스킬: {skills_demonstrated}\n"
        f"타겟 질문 유형: {target_questions}\n"
        f"지원 직무: {job_position}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. STAR 기법의 각 요소를 최적화하여 경험 기반 답변 구조화",
        "   - Situation(상황): 맥락과 배경을 간결하게 설정하는 방법",
        "   - Task(과제): 당면한 과제와 책임을 명확히 정의하는 방법",
        "   - Action(행동): 구체적인 행동과 접근법을 강조하는 방법",
        "   - Result(결과): 정량적/정성적 성과를 설득력 있게 제시하는 방법",
        
        f"2. {experience}를 STAR 구조에 맞게 재구성 및 최적화",
        f"3. {skills_demonstrated} 역량이 돋보이도록 핵심 요소 강조",
        f"4. {target_questions} 질문에 효과적으로 대응하는 답변 전략",
        f"5. {job_position} 직무와의 연관성을 강화하는 맞춤형 표현 기법",
        
        "6. 면접관의 관심을 끌고 기억에 남는 스토리텔링 기법",
        "7. 답변의 일관성과 논리적 흐름 유지 전략",
        "8. 면접 시간 제약을 고려한 최적의 답변 길이 및 구성",
        "9. 전문 용어와 업계 특화 표현의 효과적 활용법",
        "10. 자연스러운 전달을 위한 답변 연습 및 내재화 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. STAR 기법 핵심 원칙 및 최적화 전략\n"
        "2. 제공된 경험의 STAR 분석 및 구조화\n"
        "3. 완성된 STAR 기반 면접 답변\n"
        "4. 상황별 변형 및 응용 방법\n"
        "5. 질문 유형별 전환 전략\n"
        "6. 답변 강화 및 연습 가이드\n\n"
        f"제공된 {experience} 경험을 바탕으로 {skills_demonstrated} 역량을 효과적으로 보여주는 구체적인 STAR 답변 예시와 다양한 변형을 제공해주세요. 답변은 2-3분 내외의 면접 상황에 적합한 길이로 작성해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 STAR 답변 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\nSTAR 답변 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: star_response_guide.md): ") or "star_response_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{experience} 경험 기반 STAR 답변 가이드")
        print(f"STAR 답변 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()