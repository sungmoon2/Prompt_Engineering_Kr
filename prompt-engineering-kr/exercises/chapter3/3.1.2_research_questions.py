"""
효과적인 연구 질문 설계 프롬프트

명확하고 연구 가능한 질문을 설계하고 평가하는 프롬프트 기법
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
    print("===== 효과적인 연구 질문 설계 프롬프트 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    research_purpose = input("연구의 주요 목적을 입력하세요 (예: 탐색적, 설명적, 기술적): ")
    draft_questions = input("현재 고려 중인 연구 질문이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{research_topic}에 관한 좋은 연구 질문을 어떻게 설계할 수 있을까요?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 연구 질문 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 연구 방법론 전문가", 
        f"{field} 분야의 저명한 연구자로, 학술 논문 심사와 연구 설계 컨설팅을 통해 수많은 연구 질문을 평가하고 개선한 경험이 있습니다. 특히 {research_purpose} 연구의 질문 설계에 정통합니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 정보:
- 주제: {research_topic}
- 학문 분야: {field}
- 연구 목적: {research_purpose}
"""
    
    if draft_questions:
        context += f"- 현재 고려 중인 연구 질문: {draft_questions}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 효과적인 연구 질문의 특성 설명",
        "   - 연구 가능성, 명확성, 중요성, 독창성 등의 기준",
        f"   - {field} 분야의 연구 질문 특성 및 고려사항",
        f"   - {research_purpose} 연구 목적에 적합한 질문 구조",
        
        "2. 연구 질문 설계 프레임워크 제시",
        "   - 단계별 연구 질문 개발 과정",
        "   - 개념적 명확화 및 조작적 정의 방법",
        "   - 변수 간 관계 명시 전략",
        
        "3. 구체적인 연구 질문 예시 제안",
        f"   - {research_topic}에 대한 5-7개의 구체적 연구 질문 후보",
        "   - 각 질문의 강점, 약점, 연구 접근법 분석",
        "   - 주요 질문과 부차적 질문의 계층적 구성 방법",
        
        "4. 연구 질문 평가 및 정제 방법",
        "   - 질문의 범위, 실행 가능성, 윤리적 측면 평가 기준",
        "   - 모호하거나 편향된 질문 식별 및 개선 방법",
        "   - 연구 질문과 방법론적 접근의 일치성 확보 전략"
    ]
    
    if draft_questions:
        instructions.append(
            "5. 제공된 연구 질문 분석 및 개선",
            f"   - '{draft_questions}'의 강점과 약점 평가",
            "   - 구체적인 개선 제안 및 재구성 방법",
            "   - 대안적 연구 질문 형식 제시"
        )
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **효과적인 연구 질문의 기준**: {field} 분야에서 좋은 연구 질문의 특성과 평가 기준

2. **연구 질문 설계 프로세스**:
   - 광범위한 관심사에서 구체적 질문으로 발전시키는 단계
   - 개념적 명확화와 조작적 정의 방법
   - 변수 관계 및 가설 형성 전략

3. **{research_topic}에 대한 연구 질문 예시**:
   - 주요 연구 질문:
     - 연구 질문 1
     - 연구 질문 2
     ...
   - 각 질문별 분석 (강점, 약점, 연구 접근법)

4. **연구 질문 평가 체크리스트**:
   - 연구 가능성
   - 학술적 중요성
   - 윤리적 고려사항
   - 방법론적 적합성
   ...

5. **연구 질문 정제 실습 가이드**:
   - 단계별 연구 질문 개선 과정
   - 일반적인 실수와 개선 방법
   - 연구 목적별 질문 형식 템플릿
"""
    
    if draft_questions:
        output_format += """
6. **제공된 연구 질문 분석 및 개선**:
   - 기존 질문 평가
   - 개선된 버전 제안
   - 개선 이유 및 이점 설명
"""
    
    output_format += """
마크다운 형식으로 체계적인 연구 질문 설계 가이드와 실제 적용 가능한 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 연구 질문 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n연구 질문 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: research_questions_guide.md): ") or "research_questions_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 연구 질문 설계 가이드")
        print(f"연구 질문 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()