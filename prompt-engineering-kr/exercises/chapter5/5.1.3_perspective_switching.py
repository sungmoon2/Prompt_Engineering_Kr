"""
다중 관점 역할 프롬프트

여러 전문가 관점을 통합하여 균형 잡힌 분석을 유도하는 프롬프트 패턴
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
    print("===== 다중 관점 역할 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("다양한 관점에서 분석할 주제를 입력하세요: ")
    perspective_type = input("관점 유형을 선택하세요 (1: 학문 분야별, 2: 역할별, 3: 이해관계자별): ")
    
    # 관점 유형에 따른 관점 목록 설정
    if perspective_type == "1":  # 학문 분야별
        perspectives = input("분석에 포함할 학문 분야들을 쉼표로 구분하여 입력하세요: ").split(",")
        perspective_desc = "다양한 학문 분야의 렌즈를 통해"
    elif perspective_type == "2":  # 역할별
        perspectives = input("분석에 포함할 역할들을 쉼표로 구분하여 입력하세요: ").split(",")
        perspective_desc = "다양한 전문 역할의 관점에서"
    else:  # 이해관계자별
        perspectives = input("분석에 포함할 이해관계자들을 쉼표로 구분하여 입력하세요: ").split(",")
        perspective_desc = "다양한 이해관계자의 입장에서"
    
    # 관점 목록 정리
    perspectives = [p.strip() for p in perspectives]
    perspectives_str = ", ".join(perspectives)
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대해 {perspectives_str}의 관점에서 분석해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 다중 관점 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("통합적 분석 전문가", 
                          f"{topic}와 같은 복잡한 주제를 {perspective_desc} 종합적으로 분석하고, 다양한 관점을 균형 있게 통합하는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"분석 주제: {topic}\n"
        f"분석 관점: {perspectives_str}\n"
        f"관점 유형: {perspective_type}번 - " + 
        ("학문 분야별" if perspective_type == "1" else "역할별" if perspective_type == "2" else "이해관계자별")
    )
    
    # 지시사항 추가
    instructions = [
        f"1. {topic}에 대해 다음 관점들을 포함한 종합적 분석을 제공해주세요:"
    ]
    
    # 각 관점별 분석 지시사항 추가
    for i, perspective in enumerate(perspectives, 1):
        instructions.append(f"   - {perspective} 관점: 이 관점에서의 핵심 인사이트, 우려사항, 가치를 분석")
    
    # 추가 지시사항
    instructions.extend([
        f"2. 각 관점에서 {topic}을 어떻게 이해하고 평가하는지 명확히 구분해주세요.",
        "3. 각 관점의 강점과 한계점을 비교해주세요.",
        "4. 관점들 간의 공통점과 차이점을 분석해주세요.",
        "5. 관점들 간의 갈등과 상충을 파악하고 이를 조정하는 방법을 제안해주세요.",
        "6. 다양한 관점을 통합한 균형 잡힌 결론을 도출해주세요.",
        "7. 각 관점의 전문적 어투와 특성을 적절히 반영해주세요."
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_sections = ["1. 주제 소개 및 분석 접근법\n"]
    
    # 각 관점별 섹션 추가
    for i, perspective in enumerate(perspectives, 2):
        output_sections.append(f"{i}. {perspective} 관점 분석\n")
    
    # 추가 섹션
    next_section = len(perspectives) + 2
    output_sections.extend([
        f"{next_section}. 관점 간 비교 및 통합\n",
        f"{next_section+1}. 종합적 결론 및 제언\n"
    ])
    
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n" +
        "".join(output_sections) + "\n" +
        "각 관점의 특성을 반영하는 전문적 용어와 표현을 사용하면서도, 일반 독자가 이해할 수 있는 명확한 설명을 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 다중 관점 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n다중 관점 분석 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: multi_perspective_analysis.md): ") or "multi_perspective_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{topic}에 대한 다중 관점 분석")
        print(f"다중 관점 분석 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()