"""
피드백 분석 및 반영 프롬프트

교수자 피드백을 체계적으로 분석하고 효과적으로 반영하는 방법
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
    print("===== 피드백 분석 및 반영 프롬프트 =====")
    
    # 사용자 입력 받기
    feedback = input("받은 피드백을 입력하세요: ")
    report_type = input("보고서 유형을 입력하세요 (예: 에세이, 연구 논문, 실험 보고서): ")
    field = input("학문 분야를 입력하세요: ")
    improvement_goal = input("개선 목표를 입력하세요 (예: 다음 과제 준비, 최종 제출물 수정): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 피드백을 어떻게 반영하면 좋을까?

피드백: {feedback}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 피드백 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 코치 및 교육 심리학자", 
                           f"{field} 분야에서 학생들의 학업 발전을 지원하고 피드백의 효과적인 활용을 연구해온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"교수자 피드백:\n\"{feedback}\"\n\n"
        f"보고서 유형: {report_type}\n"
        f"학문 분야: {field}\n"
        f"개선 목표: {improvement_goal}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 제공된 피드백을 핵심 요소로 분류하고 체계적으로 분석",
        "2. 각 피드백 요소의 우선순위와 중요도 평가",
        "3. 명시적 피드백 뿐만 아니라 잠재적/암묵적 의견 파악",
        "4. 피드백이 지적하는 근본적인 문제점 및 패턴 식별",
        f"5. {report_type}의 품질 향상을 위한 구체적인 개선 전략 제안",
        "6. 피드백을 통합적으로 반영하기 위한 단계별 접근법",
        f"7. {field} 분야의 학술적 기대와 연계한 개선 방향 제시",
        "8. 즉각적 개선과 장기적 역량 개발을 위한 균형 있는 접근",
        "9. 유사한 피드백의 재발을 방지하기 위한 예방 전략",
        "10. 향후 과제를 위한 자기 점검 체크리스트와 반성적 학습 도구"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 피드백 요소 분류 및 분석\n"
        "2. 우선순위 및 중요도 평가\n"
        "3. 개선을 위한 구체적 전략 및 단계\n"
        "4. 장기적 학습 및 역량 개발 방안\n"
        "5. 자기 점검 체크리스트\n\n"
        f"{field} 분야의 {report_type}에 특화된 개선 예시와 구체적인 수정 접근법을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 피드백 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n피드백 분석 및 개선 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: feedback_analysis_guide.md): ") or "feedback_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{report_type} 피드백 분석 및 개선 가이드")
        print(f"피드백 분석 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()