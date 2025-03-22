"""
명확한 지시문 작성하기 실습 모듈

Part 1 - 섹션 1.1 실습 코드: 기본 프롬프트와 향상된 프롬프트의 차이 비교를 통해
효과적인 지시문 작성법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.ui_helpers import (
    print_header, print_step, get_user_input, 
    display_results_comparison, print_prompt_summary,
    print_learning_points, print_next_steps, print_comparison_points
)
from utils.example_data import get_examples_by_category

# 예제 주제 목록 (utils/example_data.py를 사용할 수도 있음)
INSTRUCTION_TOPICS = {
    "1": {"name": "여행 계획", "topic": "3박 4일 제주도 여행 계획", "output_format": "일정표"},
    "2": {"name": "레시피 요청", "topic": "초보자를 위한 파스타 레시피", "output_format": "단계별 가이드"},
    "3": {"name": "개념 설명", "topic": "블록체인 기술의 기본 원리", "output_format": "초보자용 설명"},
    "4": {"name": "기술 비교", "topic": "Python과 JavaScript의 주요 차이점", "output_format": "비교표"},
    "5": {"name": "역사 요약", "topic": "산업혁명의 주요 영향과 결과", "output_format": "시간순 요약"}
}

def main():
    """메인 함수"""
    print_header("명확한 지시문 작성하기")
    print("효과적인 지시문을 작성하는 방법을 배우고 연습합니다.\n")
    print("모호하고 일반적인 프롬프트와 명확하고 구체적인 프롬프트의 차이를 비교해봅시다.")
    
    # 1. 주제 선택 단계
    print_step(1, "주제 선택")
    
    # 옵션 표시
    print("\n지시문 작성 연습을 위한 주제 옵션:")
    for key, value in INSTRUCTION_TOPICS.items():
        print(f"  {key}. {value['name']}")
    print("  0. 직접 주제 입력하기")
    
    choice = get_user_input("\n선택하세요", "1")
    
    if choice == "0":
        topic = get_user_input("주제를 입력하세요", "여름 휴가 계획")
        output_format = get_user_input("원하는 출력 형식을 입력하세요", "일정표")
        purpose = get_user_input("이 정보를 사용할 목적을 입력하세요", "휴가 계획 수립")
    else:
        selected = INSTRUCTION_TOPICS.get(choice, INSTRUCTION_TOPICS["1"])
        topic = selected["topic"]
        output_format = selected["output_format"]
        purpose = f"{selected['name']} 작성"
    
    print(f"\n선택한 주제: {topic}")
    print(f"출력 형식: {output_format}")
    print(f"사용 목적: {purpose}")
    
    # 2. 기본 프롬프트 실행 단계
    print_step(2, "기본 프롬프트로 요청하기")
    
    # 기본 프롬프트 생성
    basic_prompt = f"{topic}에 대해 알려주세요."
    
    print("\n기본 프롬프트:")
    print(f"'{basic_prompt}'")
    
    # AI 응답 요청
    print("\n응답 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n✅ 기본 프롬프트 응답이 생성되었습니다.")
    
    # 3. 향상된 프롬프트 실행 단계
    print_step(3, "향상된 프롬프트로 요청하기")
    
    # PromptBuilder를 사용한 향상된 프롬프트 작성
    builder = PromptBuilder()
    
    # 사용 맥락 정보 추가
    builder.add_context(
        f"저는 {purpose}을 위해 {topic}에 대한 정보가 필요합니다. "
        f"이 정보는 {output_format} 형식으로 정리되면 가장 유용할 것 같습니다."
    )
    
    # 구체적인 지시사항 추가
    builder.add_instructions([
        f"{topic}에 대한 핵심 정보를 명확하고 구체적으로 제공해주세요",
        "중요한 요소나 고려사항을 빠짐없이 포함해주세요",
        "가능한 단계별로 구분하여 체계적으로 설명해주세요",
        "실제 예시나 사례를 포함해주면 더 이해하기 쉬울 것 같습니다",
        "일반적인 내용보다는 구체적이고 실용적인 정보에 중점을 두어주세요"
    ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 체계적으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요."
    )
    
    enhanced_prompt = builder.build()
    
    # 프롬프트 요약 정보 출력
    print_prompt_summary("향상된", [
        "사용 맥락 제공: 목적과 활용 방법 명시",
        "구체적 지시사항: 5가지 세부 요청 추가",
        "출력 형식 지정: 원하는 형식과 구조 요청"
    ])
    
    # AI 응답 요청
    print("\n응답 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n✅ 향상된 프롬프트 응답이 생성되었습니다.")
    
    # 4. 결과 비교 및 저장 단계
    print_step(4, "결과 비교 및 저장")
    
    # 결과 비교 표시
    display_results_comparison(basic_result, enhanced_result, 300)
    
    # 프롬프트 개선 효과 설명
    print_comparison_points({
        "1. 기본 프롬프트의 한계:": [
            "모호하고 일반적인 요청",
            "목적과 활용 방법이 명시되지 않음",
            "원하는 출력 형식이 지정되지 않음"
        ],
        "2. 향상된 프롬프트의 장점:": [
            "명확한 맥락과 목적 제시",
            "구체적인 요구사항 명시",
            "원하는 출력 형식과 구조 지정",
            "실제 사용 목적에 맞는 정보 요청"
        ]
    })
    
    # 결과 저장
    save_option = get_user_input("\n결과를 파일로 저장하시겠습니까? (y/n)", "y")
    if save_option.lower() in ['y', 'yes']:
        # 파일명 생성 및 저장 경로 설정
        safe_topic = topic.replace(' ', '_').lower()
        results_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "results")
        os.makedirs(results_dir, exist_ok=True)
        
        # 기본 응답 저장
        basic_filename = os.path.join(results_dir, f"basic_{safe_topic}.md")
        save_markdown(basic_result, basic_filename, title=f"{topic} - 기본 프롬프트 결과")
        print(f"기본 응답이 '{basic_filename}'에 저장되었습니다.")
        
        # 향상된 응답 저장
        enhanced_filename = os.path.join(results_dir, f"enhanced_{safe_topic}.md")
        save_markdown(enhanced_result, enhanced_filename, title=f"{topic} - 향상된 프롬프트 결과")
        print(f"향상된 응답이 '{enhanced_filename}'에 저장되었습니다.")
        
        # 프롬프트 비교 저장
        comparison_filename = os.path.join(results_dir, f"comparison_{safe_topic}.md")
        save_markdown(f"""# {topic} 프롬프트 비교

## 기본 프롬프트
```
{basic_prompt}
```

## 향상된 프롬프트
```
{enhanced_prompt}
```

## 주요 개선점
1. **맥락 제공**: 목적과 활용 방법 명시
2. **구체적 지시사항**: 5가지 세부 요청 추가
3. **출력 형식 지정**: 원하는 형식과 구조 요청

## 효과
향상된 프롬프트는 더 구체적이고 맥락에 맞는 응답을 생성합니다.
기본 프롬프트는 일반적인 정보를 제공하는 반면, 향상된 프롬프트는
실제 사용 목적에 맞는 구조화된 정보를 제공합니다.
""", comparison_filename)
        print(f"프롬프트 비교가 '{comparison_filename}'에 저장되었습니다.")
    
    # 5. 학습 내용 정리 단계
    print_step(5, "학습 내용 정리")
    
    # 학습 포인트 출력
    print_learning_points([
        "명확한 맥락과 목적을 제공하면 더 관련성 높은 응답을 얻을 수 있습니다",
        "구체적인 지시사항이 모호한 요청보다 훨씬 효과적입니다",
        "원하는 출력 형식을 명시하면 응답의 구조가 개선됩니다",
        "실제 사용 목적을 공유하면 AI가 더 적합한 정보를 제공할 수 있습니다"
    ])
    
    # 다음 단계 제안
    print_next_steps([
        "다른 주제에 동일한 프롬프트 구조를 적용해보세요",
        "지시사항의 세부 항목을 변경하면서 응답의 변화를 관찰해보세요",
        "더 다양한 출력 형식을 요청해보세요 (표, 목록, 단계별 가이드 등)",
        "여러 종류의 맥락 정보를 추가하면서 응답의 변화를 확인해보세요"
    ])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")