"""
직무별 면접 질문 준비

직무와 산업 특성에 맞춘 예상 면접 질문 및 효과적인 답변 전략 개발
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
    print("===== 직무별 면접 질문 준비 =====")
    
    # 사용자 입력 받기
    job_position = input("지원하는 직무/포지션을 입력하세요: ")
    industry = input("산업 분야를 입력하세요: ")
    experience_level = input("경력 수준을 입력하세요 (예: 신입, 경력 3년차, 관리자급): ")
    skills = input("주요 스킬이나 역량을 입력하세요 (쉼표로 구분): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{industry} 분야의 {job_position} 면접에서 어떤 질문이 나올까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 면접 질문 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("면접 질문 전문가 및 직무 컨설턴트", 
                          f"{industry} 산업의 {job_position} 채용 면접을 다수 진행해온 전문가로, 각 직무별 핵심 역량을 평가하는 질문 전략과 효과적인 답변법에 정통합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"직무/포지션: {job_position}\n"
        f"산업 분야: {industry}\n"
        f"경력 수준: {experience_level}\n"
        f"주요 스킬/역량: {skills}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {industry} 산업의 {job_position} 면접에서 자주 등장하는 질문 유형 분석",
        f"2. {experience_level} 수준에 특화된 직무 관련 전문 지식 질문 예시",
        f"3. {skills}와 관련된 기술적/실무적 역량 평가 질문",
        "4. 상황 기반 질문(Situational questions)과 행동 기반 질문(Behavioral questions) 구분 및 예시",
        "5. 문제 해결 능력 및 비판적 사고를 평가하는 질문 전략",
        "6. 직무 적합성 및 동기 부여를 평가하는 질문 기법",
        "7. 각 질문 유형별 답변 구조화 방법 및 STAR 기법 적용 예시",
        "8. 면접관의 의도 파악 및 핵심 키워드 중심 답변 전략",
        "9. 질문별 주의해야 할 함정과 회피해야 할 답변 패턴",
        "10. 차별화된 답변을 위한 사전 준비 전략 및 체크리스트"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 직무 면접 질문 패턴 분석\n"
        "2. 질문 카테고리별 예상 질문 목록 (최소 25개)\n"
        "3. 주요 질문별 모범 답변 구조 및 핵심 포인트\n"
        "4. 답변 작성 템플릿 및 가이드라인\n"
        "5. 질문 준비 및 연습 전략\n"
        "6. 면접관 관점에서의 평가 요소\n\n"
        f"{job_position} 직무의 실제 면접 상황을 고려한 구체적인 질문과 효과적인 답변 전략을 제공해주세요. 질문은 직무 기술적 측면, 행동 역량, 문화 적합성을 균형 있게 다루어야 합니다."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 면접 질문 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n면접 질문 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: job_interview_questions.md): ") or "job_interview_questions.md"
        save_markdown(enhanced_result, file_path, title=f"{industry} {job_position} 면접 질문 가이드")
        print(f"면접 질문 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()