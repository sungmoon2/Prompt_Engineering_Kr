"""
데이터 시각화 전략 및 도구

연구 결과를 효과적으로 시각화하고 적절한 시각화 유형을 선택하는 방법
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
    print("===== 데이터 시각화 전략 및 도구 =====")
    
    # 사용자 입력 받기
    data_type = input("시각화할 데이터 유형을 입력하세요 (예: 시계열, 분포, 관계, 비교): ")
    research_field = input("연구 분야를 입력하세요: ")
    viz_purpose = input("시각화 목적을 입력하세요 (예: 논문, 발표, 대시보드, 탐색적 분석): ")
    audience = input("대상 독자/청중을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{data_type} 데이터를 {viz_purpose}를 위해 어떻게 시각화하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 시각화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("데이터 시각화 전문가 및 연구 커뮤니케이션 컨설턴트", 
                           f"{research_field} 분야의 연구 데이터 시각화에 특화된 전문가로, 효과적인 데이터 스토리텔링과 시각적 표현 방법에 관한 다수의 저서와 강의를 제공했습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"데이터 유형: {data_type}\n"
        f"연구 분야: {research_field}\n"
        f"시각화 목적: {viz_purpose}\n"
        f"대상 독자/청중: {audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {data_type} 데이터에 가장 적합한 시각화 유형과 그 선택 이유",
        f"2. {research_field} 분야에서 많이 사용되는 표준적인 시각화 방법 및 관행",
        f"3. {viz_purpose}를 위한 시각화 최적화 전략 (포맷, 크기, 해상도, 색상 등)",
        f"4. {audience}의 특성과 필요를 고려한 시각화 접근법",
        "5. 주요 시각화 도구 및 소프트웨어 추천 (R, Python, Tableau, 기타 도구)",
        "6. 효과적인 데이터 스토리텔링을 위한 시각화 구성 및 배치 전략",
        "7. 일반적인 시각화 오류와 피해야 할 사항",
        "8. 복잡한 데이터를 명확하게 전달하기 위한 단순화 전략",
        "9. 시각화에 적절한 텍스트 요소 (제목, 라벨, 주석, 범례) 활용법",
        "10. 윤리적이고 정확한 데이터 표현을 위한 고려사항"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 최적 시각화 유형 선택 및 근거\n"
        "2. 시각화 디자인 원칙 및 모범 사례\n"
        "3. 추천 도구 및 구현 방법\n"
        "4. 시각화 예시 및 템플릿\n"
        "5. 효과적인 데이터 스토리텔링 전략\n"
        "6. 시각화 체크리스트 및 평가 기준\n\n"
        f"{data_type} 데이터에 대한 구체적인 시각화 예시와 설명을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 시각화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n시각화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: data_visualization_guide.md): ") or "data_visualization_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{data_type} 데이터 시각화 가이드: {viz_purpose}용")
        print(f"시각화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()