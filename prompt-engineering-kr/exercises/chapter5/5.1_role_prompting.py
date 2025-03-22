"""
역할 기반 프롬프팅

다양한 전문가 역할을 활용한 프롬프트 기법
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
    print("===== 역할 기반 프롬프팅 =====")
    
    # 사용자 입력 받기
    topic = input("분석할 주제를 입력하세요: ")
    role_type = input("적용할 역할 유형을 선택하세요 (1: 학술/전문가, 2: 산업 전문가, 3: 다중 관점): ")
    field = input("관련 분야나 학문을 입력하세요: ")
    
    # 역할 유형에 따른 설정
    if role_type == "1":
        role_name = input("학술/전문가 역할명을 입력하세요 (예: 역사학자, 심리학 교수): ")
        role_desc = f"{field} 분야의 저명한 학자로서 수십 년간의 연구 경험을 가진 {role_name}"
    elif role_type == "2":
        role_name = input("산업 전문가 역할명을 입력하세요 (예: UX 디자이너, 데이터 과학자): ")
        role_desc = f"{field} 업계에서 오랜 실무 경험을 가진 시니어 {role_name}"
    else:
        role_name = "다중 관점 분석가"
        role_desc = f"{field}를 다양한 관점(학술적, 실용적, 비판적, 윤리적)에서 분석할 수 있는 통합적 사고의 전문가"
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{role_name}로서 {topic}에 대해 분석해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 역할 기반 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(role_name, role_desc)
    
    # 맥락 제공 및 지시사항 추가
    prompt_builder.add_context(f"분석 주제: {topic}\n관련 분야: {field}")
    
    # 역할 유형에 따른 지시사항 조정
    if role_type == "1":  # 학술/전문가
        prompt_builder.add_instructions([
            f"1. {topic}에 대한 학술적/이론적 분석을 제공해주세요.",
            f"2. {field} 분야의 주요 개념과 이론을 적용해주세요.",
            "3. 관련 연구와 문헌을 참조하여 근거 기반 분석을 제시해주세요.",
            "4. 학술적 용어와 전문적 어투를 적절히 활용해주세요.",
            "5. 다양한 이론적 관점을 비교하고 통합해주세요."
        ])
    elif role_type == "2":  # 산업 전문가
        prompt_builder.add_instructions([
            f"1. {topic}에 대한 실무적/현장 중심 분석을 제공해주세요.",
            f"2. {field} 산업의 현재 트렌드와 실제 사례를 활용해주세요.",
            "3. 실용적인 인사이트와 적용 가능한 전략을 제시해주세요.",
            "4. 업계 용어와 전문적 어투를 적절히 활용해주세요.",
            "5. 실무에서 직면하는 도전과 해결책을 논의해주세요."
        ])
    else:  # 다중 관점
        prompt_builder.add_instructions([
            f"1. {topic}에 대해 다음 관점들을 통합한 분석을 제공해주세요:",
            "   - 학술적/이론적 관점",
            "   - 실용적/현실적 관점",
            "   - 비판적/대안적 관점",
            "   - 윤리적/사회적 관점",
            "2. 각 관점별 핵심 인사이트를 제시해주세요.",
            "3. 관점들 간의 충돌과 조화를 분석해주세요.",
            "4. 통합적이고 균형 잡힌 결론을 도출해주세요."
        ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 다음 섹션을 포함해주세요:\n"
        "1. 개요 및 접근법\n"
        "2. 주요 분석 및 인사이트\n"
        "3. 핵심 개념 및 원칙\n"
        "4. 실제 적용 및 사례\n"
        "5. 결론 및 추가 고려사항\n\n"
        f"{role_name}의 전문적 관점을 일관되게 유지하며 분석해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 역할 기반 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n분석 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: role_based_analysis.md): ") or "role_based_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{role_name}의 {topic} 분석")
        print(f"분석 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()