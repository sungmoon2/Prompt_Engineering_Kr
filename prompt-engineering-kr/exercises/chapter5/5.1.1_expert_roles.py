"""
학술/전문가 역할 지정 프롬프트

특정 분야의 전문가 관점에서 응답을 유도하는 프롬프트 패턴
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.templates import get_pattern_examples

def main():
    """
    실습 코드 메인 함수
    """
    print("===== 학술/전문가 역할 지정 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("분석할 주제를 입력하세요: ")
    academic_field = input("학문/전문 분야를 입력하세요 (예: 경제학, 심리학, 컴퓨터과학): ")
    expertise_level = input("전문성 수준을 입력하세요 (예: 교수, 연구원, 박사): ")
    specific_approach = input("특정 접근법이나 이론적 관점이 있다면 입력하세요 (선택사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{academic_field} {expertise_level}로서 {topic}에 대해 분석해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 학술 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    role_description = f"{academic_field} 분야에서 오랜 연구 경력을 가진 저명한 {expertise_level}"
    if specific_approach:
        role_description += f"로, 특히 {specific_approach} 접근법에 정통한 전문가"
    
    prompt_builder.add_role(f"{academic_field} {expertise_level}", role_description)
    
    # 맥락 제공
    context = f"분석 주제: {topic}\n학문 분야: {academic_field}"
    if specific_approach:
        context += f"\n특정 접근법: {specific_approach}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {topic}에 대해 {academic_field} 분야의 전문적 관점에서 심층 분석해주세요.",
        f"2. {academic_field}의 주요 개념, 이론, 프레임워크를 활용하여 분석해주세요.",
        "3. 관련 연구 및 학술적 증거를 참조하여 논의를 뒷받침해주세요.",
        "4. 주제와 관련된 학술적 논쟁이나 다양한 이론적 관점을 소개해주세요.",
        "5. 분석에 적절한 전문 용어와 개념을 사용해주세요."
    ]
    
    if specific_approach:
        instructions.append(f"6. {specific_approach} 관점에서 주제를 특별히 조명해주세요.")
        instructions.append(f"7. {specific_approach}의 강점과 한계점을 고려한 균형 잡힌 분석을 제공해주세요.")
    else:
        instructions.append("6. 다양한 이론적 관점을 비교하고 통합하는 균형 잡힌 분석을 제공해주세요.")
        instructions.append("7. 현재 연구 동향과 향후 방향성에 대해 논의해주세요.")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 주제 소개 및 학술적 중요성\n"
        "2. 이론적 프레임워크 및 핵심 개념\n"
        "3. 주요 분석 및 논의\n"
        "4. 비판적 검토 및 대안적 관점\n"
        "5. 결론 및 함의\n"
        "6. 참고 문헌 및 추가 자료\n\n"
        f"{academic_field} {expertise_level}의 전문적 어투와 분석 스타일을 일관되게 유지해주세요."
    )
    
    # 역할 기반 프롬프팅 예시 활용
    try:
        examples = get_pattern_examples("role_prompting")
        if examples and len(examples) > 0:
            example = examples[0]  # 첫 번째 예시 사용
            prompt_builder.add_text("\n\n참고 예시:")
            prompt_builder.add_text(f"역할: {example.get('role')}")
            prompt_builder.add_text(f"역할 설명: {example.get('role_description')}")
            prompt_builder.add_text(f"주제: {example.get('topic')}")
            prompt_builder.add_text(f"예시 출력 미리보기: {example.get('output')[:200]}...")
    except Exception as e:
        print(f"예시 로드 중 오류 발생: {e}")
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 학술 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n학술 분석 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: academic_analysis.md): ") or "academic_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{academic_field} 관점에서의 {topic} 분석")
        print(f"학술 분석 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()