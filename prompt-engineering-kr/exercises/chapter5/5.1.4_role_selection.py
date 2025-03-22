"""
상황별 최적 역할 선택 가이드

다양한 학습 및 분석 상황에 맞는 최적의 역할 선택 전략
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
    print("===== 상황별 최적 역할 선택 가이드 =====")
    
    # 사용자 입력 받기
    task_type = input("수행할 작업 유형을 선택하세요 (1: 학술 분석, 2: 실무 문제 해결, 3: 의사 결정, 4: 학습): ")
    task_desc = input("구체적인 작업 설명을 입력하세요: ")
    field = input("관련 분야를 입력하세요: ")
    goal = input("주요 목표나 기대 결과를 입력하세요: ")
    
    # 작업 유형에 따른 설정
    if task_type == "1":  # 학술 분석
        task_category = "학술 분석"
        suggested_roles = ["연구 교수", "학술 저널 편집자", "분야별 이론가", "학제간 연구자"]
    elif task_type == "2":  # 실무 문제 해결
        task_category = "실무 문제 해결"
        suggested_roles = ["산업 컨설턴트", "시니어 엔지니어", "제품 매니저", "운영 전문가"]
    elif task_type == "3":  # 의사 결정
        task_category = "의사 결정"
        suggested_roles = ["전략 컨설턴트", "리스크 분석가", "윤리적 고문", "다중 관점 통합자"]
    else:  # 학습
        task_category = "학습"
        suggested_roles = ["전문 교육자", "멘토", "커리큘럼 디자이너", "학습 코치"]
    
    # 추천 역할 표시
    roles_str = ", ".join(suggested_roles)
    print(f"\n{task_category} 작업에 추천되는 역할: {roles_str}")
    
    # 사용자가 역할 선택
    selected_role = input("사용할 역할을 입력하세요 (추천 목록에서 선택하거나 새로운 역할 입력): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{selected_role}로서 다음 작업을 수행해주세요: {task_desc}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 역할 기반 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정에 대한 메타 프롬프트 구성
    meta_prompt_builder = PromptBuilder()
    meta_prompt_builder.add_role("역할 프롬프트 설계 전문가", 
                               "다양한 작업 유형에 맞는 최적의 역할과 세부 특성을 정의하는 전문가입니다.")
    
    meta_prompt_builder.add_context(
        f"작업 유형: {task_category}\n"
        f"작업 설명: {task_desc}\n"
        f"관련 분야: {field}\n"
        f"목표/기대 결과: {goal}\n"
        f"선택된 역할: {selected_role}"
    )
    
    meta_prompt_builder.add_instructions([
        f"1. {selected_role} 역할에 대한 상세한 설명을 제공해주세요.",
        f"2. 이 역할이 {task_category} 유형의 작업에 적합한 이유를 설명해주세요.",
        f"3. 이 역할이 {field} 분야에서 가진 특별한 관점이나 전문성을 설명해주세요.",
        f"4. 이 역할이 {goal} 목표 달성에 어떻게 기여할 수 있는지 설명해주세요.",
        "5. 이 역할의 어투, 접근 방식, 분석 프레임워크 등의 특성을 설명해주세요."
    ])
    
    meta_prompt_builder.add_format_instructions(
        "다음 형식으로 응답해주세요:\n"
        "1. 역할 설명: [역할에 대한 1-2문장의 간결한 설명]\n"
        "2. 역할 특성: [이 역할의 주요 특성, 전문성, 관점 등 3-5가지 특징]\n"
        "3. 역할 스타일: [이 역할의 어투, 소통 방식, 접근법 등 2-3가지 특징]\n"
        "4. 적합성 분석: [이 역할이 현재 작업에 적합한 이유 2-3가지]"
    )
    
    # 메타 프롬프트 실행하여 역할 정의 가져오기
    meta_prompt = meta_prompt_builder.build()
    role_definition = get_completion(meta_prompt, temperature=0.7)
    
    print("\n===== 생성된 역할 정의 =====")
    print(role_definition)
    
    # 역할 정의를 기반으로 최종 프롬프트 구성
    prompt_builder.add_text(f"당신은 {field} 분야의 {selected_role}입니다.\n\n{role_definition}")
    
    prompt_builder.add_context(
        f"작업: {task_desc}\n"
        f"목표: {goal}"
    )
    
    prompt_builder.add_instructions([
        f"1. {selected_role}의 관점과 전문성을 활용하여 이 작업에 접근해주세요.",
        f"2. {task_category} 유형의 작업에 적합한 분석 프레임워크와 방법론을 적용해주세요.",
        "3. 역할에 맞는 전문 용어, 어투, 접근 방식을 일관되게 유지해주세요.",
        f"4. {goal} 목표를 달성하는 데 중점을 두고 응답해주세요.",
        "5. 필요한 경우 분야별 지식, 사례, 이론, 도구 등을 활용해주세요."
    ])
    
    # 작업 유형별 추가 지시사항
    if task_type == "1":  # 학술 분석
        prompt_builder.add_instructions([
            "6. 학술적 깊이와 엄밀성을 유지하면서 이론적 틀을 제공해주세요.",
            "7. 관련 연구와 문헌을 참조하여 근거 기반 분석을 제시해주세요."
        ])
    elif task_type == "2":  # 실무 문제 해결
        prompt_builder.add_instructions([
            "6. 실행 가능한 해결책과 구체적인 단계를 제시해주세요.",
            "7. 실무적 제약 조건과 자원을 고려한 현실적인 접근법을 제안해주세요."
        ])
    elif task_type == "3":  # 의사 결정
        prompt_builder.add_instructions([
            "6. 대안들의 장단점을 체계적으로 비교 분석해주세요.",
            "7. 의사 결정의 잠재적 영향과 리스크를 평가해주세요."
        ])
    else:  # 학습
        prompt_builder.add_instructions([
            "6. 개념을 단계별로 명확하게 설명하고 예시를 제공해주세요.",
            "7. 학습자의 이해도를 높이기 위한 교육적 접근법을 활용해주세요."
        ])
    
    # 출력 형식 지정 (작업 유형별 맞춤)
    if task_type == "1":  # 학술 분석
        prompt_builder.add_format_instructions(
            "학술적 분석 형식으로 마크다운 문서를 작성해주세요. 섹션 제목, 인용, 참고문헌 등 학술 문서의 구조를 따라주세요."
        )
    elif task_type == "2":  # 실무 문제 해결
        prompt_builder.add_format_instructions(
            "실무 보고서 형식으로 마크다운 문서를 작성해주세요. 요약, 문제 정의, 해결책, 실행 계획 등의 섹션을 포함해주세요."
        )
    elif task_type == "3":  # 의사 결정
        prompt_builder.add_format_instructions(
            "의사 결정 브리핑 형식으로 마크다운 문서를 작성해주세요. 상황 개요, 선택지 분석, 추천 사항, 근거 등의 섹션을 포함해주세요."
        )
    else:  # 학습
        prompt_builder.add_format_instructions(
            "교육 자료 형식으로 마크다운 문서를 작성해주세요. 학습 목표, 개념 설명, 예시, 연습 문제 등의 섹션을 포함해주세요."
        )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 역할 기반 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: role_based_output.md): ") or "role_based_output.md"
        save_markdown(enhanced_result, file_path, title=f"{selected_role}의 {task_desc} 결과")
        print(f"결과가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()