"""
아이디어 차별화 전략

공모전에서 주목받는 독창적 아이디어 개발과 경쟁자와의 차별화 전략
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
    print("===== 아이디어 차별화 전략 =====")
    
    # 사용자 입력 받기
    idea_concept = input("현재 아이디어/컨셉을 입력하세요: ")
    competition_field = input("공모전/경쟁 분야를 입력하세요: ")
    competitors = input("주요 경쟁자나 기존 유사 아이디어가 있다면 입력하세요: ")
    target_impact = input("아이디어를 통해 달성하고자 하는 임팩트/목표를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{idea_concept} 아이디어를 어떻게 더 독창적이고 차별화할 수 있을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 아이디어 차별화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("창의적 혁신 전략가", 
                           f"{competition_field} 분야에서 독창적 아이디어와 혁신 전략을 개발하는 전문가로, 다수의 혁신적 프로젝트와 공모전 우승작을 컨설팅한 경험이 있습니다.")
    
    # 맥락 제공
    context = f"아이디어/컨셉: {idea_concept}\n" \
             f"경쟁 분야: {competition_field}\n" \
             f"목표 임팩트: {target_impact}"
    
    if competitors:
        context += f"\n주요 경쟁자/유사 아이디어: {competitors}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 현재 아이디어의 강점과 차별화 가능성 분석",
        f"   - {idea_concept}의 고유한 가치와 현재 차별점 식별",
        "   - 잠재적 독창성 요소와 발전 방향 탐색",
        
        "2. 경쟁 환경과 유사 아이디어 분석",
        f"   - {competition_field} 분야의 주요 트렌드와 경쟁 패턴",
        "   - 경쟁자들의 접근법과 현재 한계점 파악"
    ]
    
    if competitors:
        instructions.append(f"   - {competitors}와의 구체적 차별점 개발 전략")
    
    instructions.extend([
        "3. 차별화를 위한 창의적 사고 프레임워크",
        "   - 기존 아이디어의 재구성 및 확장 방법",
        "   - 역발상과 경계 허물기를 통한 혁신적 접근법",
        "   - 다른 분야의 원리와 방법론 적용 전략",
        
        "4. 아이디어 차별화를 위한 구체적 전략",
        "   - 핵심 가치 제안(UVP) 명확화 및 강화 방법",
        "   - 아이디어의 실행 방식과 구현 전략 차별화",
        f"   - {target_impact}를 달성하기 위한 독창적 접근법",
        
        "5. 차별화된 아이디어 검증 및 정제 방법",
        "   - 독창성과 실현 가능성의 균형 확보 전략",
        "   - 피드백 수렴을 통한 아이디어 발전 방법",
        "   - 차별화 포인트 강조를 위한 프레젠테이션 전략"
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 현재 아이디어 분석 및 차별화 포인트\n"
        "2. 경쟁 환경 및 유사 아이디어 평가\n"
        "3. 차별화를 위한 창의적 확장 방향\n"
        "4. 실행 가능한 차별화 전략\n"
        "5. 아이디어 검증 및 발전 방법\n\n"
        f"{idea_concept}을 기반으로 구체적이고 실행 가능한 차별화 전략을 제시해주세요. 각 전략에 대한 실제 적용 예시와 독창적 요소를 명확히 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 아이디어 차별화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n아이디어 차별화 전략을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: idea_differentiation.md): ") or "idea_differentiation.md"
        save_markdown(enhanced_result, file_path, title=f"{idea_concept} 아이디어 차별화 전략")
        print(f"아이디어 차별화 전략이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()