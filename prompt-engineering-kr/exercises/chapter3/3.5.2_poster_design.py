"""
포스터 디자인 가이드

효과적인 학술 포스터 설계 및 제작 방법
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
    print("===== 포스터 디자인 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    key_elements = input("포함할 주요 요소를 입력하세요 (예: 방법, 결과, 그래프): ")
    target_conference = input("목표 학회나 행사를 입력하세요: ")
    size_format = input("포스터 크기 형식을 입력하세요 (예: A0, 36x48 인치): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 학술 포스터를 어떻게 디자인하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 포스터 디자인 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 포스터 디자인 및 시각 커뮤니케이션 전문가", 
                           f"{field} 분야의 학술 포스터 디자인과 시각적 정보 전달에 특화된 전문가로, 다수의 성공적인 학술 포스터를 제작하고 지도한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"연구 주제: {research_topic}\n"
        f"학문 분야: {field}\n"
        f"주요 요소: {key_elements}\n"
        f"목표 학회/행사: {target_conference}\n"
        f"포스터 크기/형식: {size_format}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 효과적인 학술 포스터의 핵심 구성 요소 및 레이아웃",
        f"2. {field} 분야의 포스터 디자인 관행 및 특성",
        "3. 시선을 사로잡는 제목 및 헤더 디자인 전략",
        "4. 연구 내용의 논리적 흐름 설계 및 시각적 계층 구조",
        f"5. {key_elements}의 효과적인 배치 및 강조 방법",
        "6. 텍스트 양 최적화 및 가독성 향상 전략",
        "7. 데이터 시각화 및 그래프 디자인 최적화",
        "8. 색상, 폰트, 이미지 선택 및 활용 전략",
        f"9. {size_format} 크기에 맞춘 디자인 조정 방법",
        "10. 인쇄 및 제작 시 고려사항",
        "11. 포스터 세션에서의 효과적인 프레젠테이션 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 포스터 디자인 기본 원칙 및 레이아웃\n"
        "2. 섹션별 콘텐츠 구성 및 시각적 표현\n"
        "3. 시각 요소 최적화 (그래프, 이미지, 다이어그램)\n"
        "4. 텍스트 디자인 및 타이포그래피\n"
        "5. 색상 전략 및 시각적 계층 구조\n"
        "6. 포스터 제작 및 인쇄 가이드\n"
        "7. 포스터 발표 전략\n"
        "8. 디자인 체크리스트\n\n"
        f"{research_topic}에 대한 구체적인 포스터 레이아웃 예시와 디자인 요소별 권장사항을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 포스터 디자인 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n포스터 디자인 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: poster_design_guide.md): ") or "poster_design_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 학술 포스터 디자인 가이드")
        print(f"포스터 디자인 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()