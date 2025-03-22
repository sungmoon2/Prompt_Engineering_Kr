"""
경험 강조 전략

이력서와 자기소개서에서 개인 경험을 효과적으로 강조하는 방법
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
    print("===== 경험 강조 전략 =====")
    
    # 사용자 입력 받기
    experience_type = input("강조하고 싶은 경험 유형을 입력하세요 (예: 프로젝트, 인턴십, 학생활동): ")
    target_position = input("목표 직무를 입력하세요: ")
    experience_details = input("경험에 대한 간략한 설명을 입력하세요: ")
    achievements = input("해당 경험에서의 성과나 배운 점을 입력하세요: ")
    challenges = input("경험 중 마주한 어려움이 있다면 입력하세요 (선택사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{experience_type} 경험을 이력서와 자기소개서에서 어떻게 효과적으로 강조할 수 있을까?

경험 내용: {experience_details}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 경험 강조 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("경력 개발 및 취업 컨설턴트", 
                           "다양한 배경을 가진 지원자들의 이력서와 자기소개서를 검토하고, 개인 경험을 채용담당자에게 효과적으로 어필하는 방법을 코칭하는 전문가입니다.")
    
    # 맥락 제공
    context = f"경험 유형: {experience_type}\n" \
             f"목표 직무: {target_position}\n" \
             f"경험 상세: {experience_details}\n" \
             f"주요 성과: {achievements}"
    
    if challenges:
        context += f"\n직면한 어려움: {challenges}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 경험-직무 연관성 분석",
        f"   - {experience_type} 경험과 {target_position} 직무 간의 관련성 도출",
        "   - 직무 요구사항에 맞춘 경험 재해석 방법",
        "   - 채용담당자 관점에서 본 경험의 가치 평가",
        
        "2. 이력서에서의 경험 강조 전략",
        "   - STAR 기법(상황-과제-행동-결과)을 활용한 경험 기술 방법",
        "   - 성과 중심의 글머리 기호(Bullet Points) 작성법",
        "   - 정량적 성과와 영향력을 부각시키는 표현 전략",
        "   - 관련 키워드 및 업계 용어 활용법",
        
        "3. 자기소개서에서의 경험 스토리텔링",
        "   - 경험을 통한 역량과 직무 적합성 증명 방법",
        f"   - {experience_details}를 매력적인 스토리로 구성하는 기법",
        "   - 경험을 통해 얻은 인사이트와 성장 강조 방법",
        "   - 미래 기여 가능성으로 연결하는 서술 전략"
    ]
    
    if challenges:
        instructions.append("4. 도전과 극복 스토리 활용")
        instructions.append(f"   - {challenges} 같은 어려움을 성장 기회로 재구성하는 방법")
        instructions.append("   - 문제 해결 능력과 회복 탄력성 부각 전략")
        instructions.append("   - 어려움 속에서 발휘된 강점과 역량 강조 방법")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 경험-직무 연관성 분석\n"
        "2. 이력서 최적화 전략 및 예시\n"
        "3. 자기소개서 작성 전략 및 예시\n"
        "4. 효과적인 경험 강조를 위한 표현 가이드\n"
        "5. 실제 적용 사례와 성공 포인트\n\n"
        f"구체적으로 {experience_type} 경험을 {target_position} 직무에 맞게 강조하는 방법에 중점을 두고, 실제 이력서와 자기소개서에 바로 적용할 수 있는 표현 예시와 템플릿을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 경험 강조 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n경험 강조 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: experience_highlighting.md): ") or "experience_highlighting.md"
        save_markdown(enhanced_result, file_path, title=f"{experience_type} 경험 강조 전략 가이드")
        print(f"경험 강조 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()