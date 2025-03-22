"""
시각 자료 기획 및 내용 구성 전략

발표를 위한 효과적인 시각 자료 디자인과 콘텐츠 구성 방법
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
    print("===== 시각 자료 기획 및 내용 구성 전략 =====")
    
    # 사용자 입력 받기
    topic = input("발표 주제를 입력하세요: ")
    field = input("학문/전문 분야를 입력하세요: ")
    visual_tool = input("사용할 도구를 입력하세요 (예: PowerPoint, Prezi, Keynote): ")
    key_points = input("전달할 핵심 포인트를 입력하세요 (쉼표로 구분): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 발표 슬라이드를 어떻게 디자인하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 시각 자료 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("시각 커뮤니케이션 및 프레젠테이션 디자인 전문가", 
                           f"{field} 분야의 학술적/전문적 발표를 위한 효과적인 시각 자료 제작에 특화된 전문가로, 정보 디자인과 시각적 스토리텔링 분야에서 다년간의 경험을 가지고 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"발표 주제: {topic}\n"
        f"학문/전문 분야: {field}\n"
        f"사용 도구: {visual_tool}\n"
        f"핵심 포인트: {key_points}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {topic}에 대한 효과적인 시각 자료 전략 수립",
        "2. 핵심 메시지를 시각적으로 강화하는 디자인 원칙",
        f"3. {field} 분야에 적합한 시각적 표현과 전문성 확보 방법",
        f"4. {key_points}를 명확하게 전달하기 위한 슬라이드 구성",
        "5. 텍스트와 시각 요소의 최적 균형 및 배치 가이드",
        "6. 데이터 시각화 및 복잡한 정보의 효과적 표현 방법",
        f"7. {visual_tool}의 기능을 활용한 효과적인 프레젠테이션 기법",
        "8. 청중의 주의를 유지하고 이해를 돕는 시각적 계층 구조 설계",
        "9. 전문적이고 일관된 디자인 테마 및 스타일 가이드",
        "10. 흔히 발생하는 시각 자료 디자인 실수와 해결 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 슬라이드 구성 및 흐름 개요\n"
        "2. 주요 슬라이드별 내용 및 디자인 가이드\n"
        "3. 시각 요소 활용 전략 (차트, 다이어그램, 이미지 등)\n"
        "4. 텍스트 최적화 및 가독성 향상 방법\n"
        "5. 전체적인 디자인 원칙 및 체크리스트\n\n"
        f"{topic}에 대한 발표의 구체적인 슬라이드 구성 예시와 각 슬라이드 유형별 레이아웃 제안을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 시각 자료 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n시각 자료 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: visual_content_guide.md): ") or "visual_content_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 발표 시각 자료 디자인 가이드")
        print(f"시각 자료 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()