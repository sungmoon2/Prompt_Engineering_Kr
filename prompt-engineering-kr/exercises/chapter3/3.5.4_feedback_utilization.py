"""
학술 발표 피드백 활용 전략

학술 발표 후 받은 피드백을 효과적으로 분석하고 향후 연구와 발표에 통합하는 방법
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
    print("===== 학술 발표 피드백 활용 전략 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    received_feedback = input("받은 피드백을 간략히 입력하세요: ")
    research_stage = input("연구 단계를 입력하세요 (예: 초기, 중간, 최종): ")
    future_goal = input("향후 연구나 발표 목표를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
학술 발표 후 받은 피드백을 어떻게 활용하면 좋을까?

피드백: {received_feedback}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 피드백 활용 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 멘토 및 연구 개발 컨설턴트", 
                           f"{field} 분야에서 연구자들의 학술적 발전을 지원하고, 피드백을 통한 연구 개선 과정을 체계적으로 안내하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"받은 피드백: {received_feedback}\n"
        f"연구 단계: {research_stage}\n"
        f"향후 목표: {future_goal}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 학술 발표 피드백의 다양한 유형과 가치 분석",
        "2. 피드백을 체계적으로 수집하고 기록하는 효과적인 방법",
        f"3. {received_feedback}을 객관적으로 분류하고 우선순위를 설정하는 프레임워크",
        "4. 건설적인 비판과 부정적 평가를 구분하고 활용하는 전략",
        f"5. {research_stage} 단계에서 피드백을 연구에 통합하는 실질적인 접근법",
        f"6. {future_goal}을 위해 피드백을 활용한 연구 및 발표 개선 방안",
        "7. 피드백을 통해 연구의 잠재적 약점을 강점으로 전환하는 전략",
        "8. 후속 연구 계획 및 방향성 설정에 피드백을 활용하는 방법",
        "9. 피드백 제공자와의 지속적인 학술적 대화 및 네트워킹 전략",
        "10. 다양한 관점의 피드백을 균형 있게 통합하기 위한 의사결정 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 학술 피드백의 가치와 접근 방식\n"
        "2. 피드백 분석 및 분류 프레임워크\n"
        "3. 구체적인 피드백 통합 전략\n"
        "4. 연구 및 발표 개선을 위한 실행 계획\n"
        "5. 장기적 학술 발전을 위한 피드백 활용 방법\n\n"
        f"특히 {received_feedback}과 같은 구체적인 피드백을 {research_stage} 단계의 연구에 통합하는 단계별 접근법과 {future_goal}을 달성하기 위한 전략적 활용 방안을 상세히 제시해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 피드백 활용 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n피드백 활용 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: feedback_utilization_guide.md): ") or "feedback_utilization_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 학술 발표 피드백 활용 가이드")
        print(f"피드백 활용 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()