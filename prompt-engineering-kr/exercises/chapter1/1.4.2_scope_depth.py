"""
주제 범위와 깊이 최적화 전략

보고서의 주제 범위 설정과 분석 깊이 최적화를 위한 프롬프트 기법
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
    print("===== 주제 범위와 깊이 최적화 전략 =====")
    
    # 사용자 입력 받기
    broad_topic = input("넓은 주제 영역을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    report_length = input("보고서 길이/워드 수 제한을 입력하세요: ")
    time_limit = input("작성 가능한 시간을 입력하세요 (예: 2주, 1개월): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{broad_topic}이라는 넓은 주제를 {report_length} 길이의 보고서로 어떻게 좁힐 수 있을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 범위 최적화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("연구 방법론 전문가", 
                           f"{field} 분야의 교수로서 학술 연구 설계와 주제 범위 설정에 관한 여러 워크숍과 세미나를 진행한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"넓은 주제 영역: {broad_topic}\n"
        f"학문 분야: {field}\n"
        f"보고서 길이 제한: {report_length}\n"
        f"가용 시간: {time_limit}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {broad_topic}의 하위 주제 및 접근 가능한 범위 매핑",
        "2. 효과적인 주제 범위 좁히기(scoping) 전략 제안",
        f"3. {report_length} 길이에 적합한 주제 범위와 깊이 균형 설정 방법",
        "4. 연구 질문 구체화 및 초점 설정 기법",
        "5. 체계적인 주제 범위 설정을 위한 의사결정 프레임워크",
        "6. 시간 및 자원 제약 하에서의 현실적 범위 설정 방법",
        f"7. {field} 분야에서 적절한 분석 깊이를 확보하는 전략",
        "8. 주제 범위 축소와 깊이 확보 사이의 균형점 찾기",
        "9. 범위가 과도하게 넓거나 좁은 경우의 위험 신호와 대처법",
        "10. 범위 및 깊이 최적화를 위한 자가 점검 질문"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        f"1. {broad_topic}에 대한 주제 매핑 및 범위 분석\n"
        "2. 추천 하위 주제 및 구체적 접근법 (3-5개)\n"
        "3. 각 하위 주제별 범위와 깊이 최적화 전략\n"
        "4. 주제 범위 설정을 위한 단계별 가이드\n"
        "5. 자가 진단 체크리스트\n\n"
        f"{field} 분야에 특화된 접근법과 구체적인 예시를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 범위 최적화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n범위 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: scope_optimization_guide.md): ") or "scope_optimization_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{broad_topic} 주제 범위 및 깊이 최적화 가이드")
        print(f"범위 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()