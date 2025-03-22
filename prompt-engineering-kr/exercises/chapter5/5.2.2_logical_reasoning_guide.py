"""
논리적 추론 과정 유도 방법

단계적인 논리적 추론을 통해 결론에 도달하는 프롬프트 기법
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
    print("===== 논리적 추론 과정 유도 방법 =====")
    
    # 사용자 입력 받기
    reasoning_topic = input("추론이 필요한 주제/문제를 입력하세요: ")
    reasoning_type = input("추론 유형을 선택하세요 (1: 연역적, 2: 귀납적, 3: 가설적, 4: 비판적): ")
    premises = input("알려진 전제나 사실을 입력하세요 (쉼표로 구분): ")
    
    # 추론 유형 텍스트 변환
    reasoning_types = {
        "1": "연역적 추론",
        "2": "귀납적 추론",
        "3": "가설적 추론",
        "4": "비판적 추론"
    }
    
    reasoning_type_text = reasoning_types.get(reasoning_type, "논리적 추론")
    
    # 전제 목록 변환
    premises_list = [p.strip() for p in premises.split(",")]
    premises_text = "\n".join([f"- {p}" for p in premises_list])
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
다음 전제를 바탕으로 {reasoning_topic}에 대해 추론해주세요:
{premises_text}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 추론 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정 (추론 유형에 따라)
    if reasoning_type == "1":  # 연역적
        prompt_builder.add_role("논리학자", 
                             "주어진 전제로부터 필연적인 결론을 도출하는 연역적 추론의 전문가로, 명확한 논리적 단계와 타당한 논증 구조를 통해 결론에 도달하는 능력을 가지고 있습니다.")
    elif reasoning_type == "2":  # 귀납적
        prompt_builder.add_role("귀납적 추론 전문가", 
                             "특정 관찰이나 사례로부터 일반적 패턴과 원칙을 도출하는 전문가로, 데이터 기반 추론과 확률적 사고를 통해 유용한 일반화에 도달하는 능력을 가지고 있습니다.")
    elif reasoning_type == "3":  # 가설적
        prompt_builder.add_role("가설 추론 전문가", 
                             "현상을 설명하기 위한 가설을 세우고 검증하는 전문가로, 창의적 가설 생성과 체계적인 가설 평가를 통해 최선의 설명에 도달하는 능력을 가지고 있습니다.")
    else:  # 비판적
        prompt_builder.add_role("비판적 사고 전문가", 
                             "주장과 증거를 평가하고 다양한 관점에서 분석하는 전문가로, 가정을 검토하고 오류를 식별하며 균형 잡힌 결론에 도달하는 능력을 가지고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"추론 주제/문제: {reasoning_topic}\n"
        f"추론 유형: {reasoning_type_text}\n"
        f"알려진 전제/사실:\n{premises_text}"
    )
    
    # 추론 유형별 지시사항 설정
    if reasoning_type == "1":  # 연역적
        instructions = [
            "1. 주어진 전제들의 논리적 구조와 의미를 명확히 분석해주세요.",
            "2. 전제들 사이의 논리적 관계를 파악해주세요.",
            "3. 연역적 추론 규칙(삼단논법, 조건부 추론 등)을 적용해주세요.",
            "4. 전제로부터 반드시 따라오는 필연적 결론을 도출해주세요.",
            "5. 각 추론 단계가 유효한(valid) 논증 형식을 따르는지 확인해주세요.",
            "6. 도출된 결론이 전제에서 필연적으로 따라오는지 검증해주세요."
        ]
    elif reasoning_type == "2":  # 귀납적
        instructions = [
            "1. 주어진 사례나 관찰 데이터의 패턴을 식별해주세요.",
            "2. 관찰된 패턴이 어떤 일반화를 시사하는지 분석해주세요.",
            "3. 귀납적 일반화의 강도를 평가해주세요 (사례의 수, 다양성, 대표성 등).",
            "4. 잠재적 예외나 반례의 가능성을 검토해주세요.",
            "5. 관찰에 기반한 확률적 결론을 제시해주세요.",
            "6. 귀납적 추론의 한계와 불확실성을 명시해주세요."
        ]
    elif reasoning_type == "3":  # 가설적
        instructions = [
            "1. 주어진 현상이나 관찰을 설명할 수 있는 다양한 가설을 생성해주세요.",
            "2. 각 가설의 설명력과 그럴듯함(plausibility)을 평가해주세요.",
            "3. 경쟁 가설들을 비교하고 최선의 설명을 찾아주세요.",
            "4. 선택한 가설을 지지하거나 반박하는 증거를 분석해주세요.",
            "5. 가설의 예측력과 검증 가능성을 평가해주세요.",
            "6. 최종 선택한 가설의 함의와 한계를 논의해주세요."
        ]
    else:  # 비판적
        instructions = [
            "1. 주제와 관련된 다양한 주장과 관점을 식별해주세요.",
            "2. 각 주장의 전제와 가정을 명시적으로 드러내주세요.",
            "3. 주장을 지지하는 증거와 반대하는 증거를 균형 있게 평가해주세요.",
            "4. 논증의 강점과 약점, 잠재적 논리적 오류를 분석해주세요.",
            "5. 다양한 관점을 통합하여 균형 잡힌 결론을 도출해주세요.",
            "6. 추가 정보나 고려사항이 결론에 어떤 영향을 미칠 수 있는지 논의해주세요."
        ]
    
    # 공통 지시사항 추가
    common_instructions = [
        f"7. 전체 추론 과정을 명확한 단계로 나누어 설명해주세요.",
        "8. 각 단계에서의 사고 과정과 근거를 명시적으로 보여주세요.",
        "9. 핵심 개념이나 용어를 명확히 정의해주세요.",
        "10. 추론의 한계와 대안적 해석 가능성을 고려해주세요."
    ]
    
    prompt_builder.add_instructions(instructions + common_instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 추론 과제 분석\n"
        "2. 전제 및 사실 검토\n"
        "3. 단계별 추론 과정\n"
        "4. 도출된 결론\n"
        "5. 추론의 강도 및 한계\n"
        "6. 대안적 해석 및 추가 고려사항\n\n"
        f"{reasoning_type_text}의 특성을 반영하여 체계적이고 명확한 단계별 추론 과정을 보여주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 추론 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n추론 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: logical_reasoning.md): ") or "logical_reasoning.md"
        save_markdown(enhanced_result, file_path, title=f"{reasoning_topic}에 대한 {reasoning_type_text}")
        print(f"추론 결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()