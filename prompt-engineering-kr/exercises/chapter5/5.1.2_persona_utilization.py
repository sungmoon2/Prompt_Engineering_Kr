"""
산업 전문가 역할 지정 프롬프트

실무 경험과 산업 지식을 활용한 응답을 유도하는 프롬프트 패턴
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
    print("===== 산업 전문가 역할 지정 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("분석할 주제나 문제를 입력하세요: ")
    industry = input("산업 분야를 입력하세요 (예: 금융, IT, 헬스케어): ")
    role = input("구체적인 직무/역할을 입력하세요 (예: 마케팅 이사, 제품 관리자, 데이터 과학자): ")
    experience = input("경력 수준을 입력하세요 (예: 시니어, 10년 경력, 스타트업 창업자): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{industry} 산업의 {role}로서 {topic}에 대해 조언해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 산업 전문가 조언 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{industry} {role}", 
                          f"{industry} 산업에서 {experience} 경력을 가진 전문가로, 실제 비즈니스 환경에서 {topic}과 같은 문제를 다수 해결한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제/문제: {topic}\n"
        f"산업 분야: {industry}\n"
        f"전문 역할: {role}\n"
        f"경력 수준: {experience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {topic}에 대해 {industry} 산업의 실무적 관점에서 분석해주세요.",
        f"2. {role}로서의 경험과 전문 지식을 바탕으로 현실적인 인사이트를 제공해주세요.",
        "3. 업계 트렌드, 실제 사례, 성공/실패 시나리오를 참조해주세요.",
        "4. 실무에서 직면하는 구체적인 도전과 해결 전략을 제시해주세요.",
        "5. 산업 특화 용어와 개념을 적절히 활용해주세요.",
        "6. 실행 가능한 전략, 팁, 권장사항을 제공해주세요.",
        "7. ROI, 자원 효율성, 시장 경쟁력 등 비즈니스 영향을 고려한 분석을 해주세요."
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 상황 개요 및 산업 맥락\n"
        "2. 핵심 도전 및 기회 분석\n"
        "3. 실무적 인사이트 및 전략\n"
        "4. 실제 사례 및 교훈\n"
        "5. 실행 가능한 권장사항\n"
        "6. ROI 및 비즈니스 영향 분석\n\n"
        f"{industry} {role}의 실무적 어투와 관점을 일관되게 유지하며, 이론보다 실용적인 지식에 중점을 두세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 산업 전문가 조언 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n산업 전문가 조언을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: industry_expert_advice.md): ") or "industry_expert_advice.md"
        save_markdown(enhanced_result, file_path, title=f"{industry} {role}의 {topic} 전문가 조언")
        print(f"산업 전문가 조언이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()