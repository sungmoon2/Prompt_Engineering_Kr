"""
공모전 제안서 작성법

목적과 구성에 맞는 효과적인 공모전 제안서 작성 전략 및 프레임워크 개발
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
    print("===== 공모전 제안서 작성법 =====")
    
    # 사용자 입력 받기
    competition_name = input("공모전 이름/주제를 입력하세요: ")
    competition_type = input("공모전 유형을 입력하세요 (예: 아이디어, 사업계획서, 디자인): ")
    project_concept = input("프로젝트/아이디어 컨셉을 간략히 입력하세요: ")
    target_audience = input("심사위원/타겟 청중을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{competition_name} 공모전을 위한 제안서를 어떻게 작성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 제안서 작성 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("공모전 제안서 작성 전문가", 
                           f"다양한 {competition_type} 공모전에서 수상 경력이 있고, 심사위원으로도 활동한 경험이 있는 전문가로서 효과적인 제안서 작성법에 관한 다수의 워크숍을 진행했습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"공모전 정보: {competition_name}\n"
        f"공모전 유형: {competition_type}\n"
        f"프로젝트 컨셉: {project_concept}\n"
        f"타겟 청중: {target_audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {competition_type} 공모전에 적합한 제안서 구조와 핵심 구성요소 설명",
        "2. 강력한 서두와 문제 정의 작성 방법 제시",
        "3. 컨셉과 솔루션 설명을 위한 효과적인 구조화 전략",
        "4. 데이터와 증거 활용을 통한 논리적 설득 방법",
        "5. 실행 계획 및 타당성 제시 전략",
        f"6. {target_audience}의 관심을 끌고 기억에 남는 제안서 작성 기법",
        "7. 시각적 요소(도표, 그래프, 이미지 등)의 효과적인 활용법",
        "8. 명확하고 간결한 언어 사용과 스토리텔링 기법",
        "9. 제안서 편집 및 마무리를 위한 체크리스트",
        "10. 제안서 검토 및 피드백 수렴 전략"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 제안서 구조 및 프레임워크\n"
        "2. 핵심 구성요소별 작성 가이드\n"
        "3. 시각적 요소 활용 전략\n"
        "4. 문체 및 표현 최적화 방법\n"
        "5. 제안서 작성 체크리스트\n\n"
        f"{competition_name} 공모전의 특성과 {competition_type} 유형에 특화된 구체적인 가이드와 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 제안서 작성 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n제안서 작성 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: proposal_writing_guide.md): ") or "proposal_writing_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{competition_name} 공모전 제안서 작성 가이드")
        print(f"제안서 작성 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()