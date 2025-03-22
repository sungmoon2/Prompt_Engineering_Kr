"""
평가 기준 최적화 제안서

공모전 평가 기준에 맞춰 제안서를 최적화하고 심사위원 관점에서 완성도를 높이는 전략
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
    print("===== 평가 기준 최적화 제안서 =====")
    
    # 사용자 입력 받기
    competition_name = input("공모전 이름을 입력하세요: ")
    evaluation_criteria = input("공모전 평가 기준을 입력하세요 (쉼표로 구분): ")
    proposal_concept = input("제안서/아이디어 개요를 입력하세요: ")
    current_challenges = input("현재 제안서의 약점이나 도전 과제가 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{competition_name} 공모전의 평가 기준({evaluation_criteria})에 맞게 제안서를 최적화하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 평가 기준 최적화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("공모전 심사위원 및 제안서 최적화 전문가", 
                           "다수의 공모전 심사 경험과 수상작 컨설팅 경험을 바탕으로 평가 기준에 최적화된 제안서 작성법을 코칭하는 전문가입니다.")
    
    # 맥락 제공
    context = f"공모전 정보: {competition_name}\n" \
             f"평가 기준: {evaluation_criteria}\n" \
             f"제안 개요: {proposal_concept}"
    
    if current_challenges:
        context += f"\n현재 도전 과제: {current_challenges}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 평가 기준 심층 분석 및 이해",
        f"   - {evaluation_criteria}의 각 항목이 의미하는 바와 심사위원 관점의 기대치",
        "   - 명시적/암묵적 평가 요소 파악 및 우선순위 설정",
        
        "2. 각 평가 기준별 제안서 최적화 전략",
        "   - 평가 요소별 제안서 구성과 내용 최적화 방법",
        "   - 평가 기준을 충족하는 핵심 메시지와 증거 제시 전략",
        "   - 각 섹션의 균형과 일관성 확보 방법"
    ]
    
    if current_challenges:
        instructions.append("3. 현재 도전 과제 해결 및 약점 보완 전략")
        instructions.append(f"   - {current_challenges}를 보완하는 구체적 방안")
        instructions.append("   - 약점을 강점으로 전환하는 접근법")
    else:
        instructions.append("3. 잠재적 약점 식별 및 선제적 보완 전략")
        instructions.append("   - 심사위원이 의문을 제기할 수 있는 영역 예측")
        instructions.append("   - 잠재적 약점에 대한 선제적 대응 방안")
    
    instructions.extend([
        "4. 심사위원 관점에서의 제안서 완성도 향상 기법",
        "   - 심사 과정과 심리를 고려한 구성 및 디자인 전략",
        "   - 시각적 요소와 데이터 활용을 통한 설득력 강화",
        "   - 심사위원의 관심을 끌고 기억에 남는 차별화 요소",
        
        "5. 평가 기준 충족 증명을 위한 구체적 방법론",
        "   - 명확한 성과 지표와 검증 가능한 결과 제시 방법",
        "   - 실현 가능성과 지속 가능성 입증 전략",
        "   - 혁신성과 창의성을 효과적으로 전달하는 기법"
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 평가 기준 분석 및 해석\n"
        "2. 각 평가 기준별 최적화 전략\n"
        "3. 약점 보완 및 강점 강화 방안\n"
        "4. 심사위원 관점의 차별화 전략\n"
        "5. 제안서 최종 점검 체크리스트\n\n"
        f"{competition_name} 공모전의 특성과 {evaluation_criteria} 평가 기준에 맞춘 구체적인 최적화 방안과 예시를 제공해주세요. 실제 심사 과정에서 적용할 수 있는 실용적인 조언을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 평가 기준 최적화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n평가 기준 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: criteria_optimization.md): ") or "criteria_optimization.md"
        save_markdown(enhanced_result, file_path, title=f"{competition_name} 평가 기준 최적화 가이드")
        print(f"평가 기준 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()