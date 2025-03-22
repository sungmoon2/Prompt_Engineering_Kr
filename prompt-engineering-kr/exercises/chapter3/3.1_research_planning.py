"""
연구 계획 및 설계

효과적인 연구 계획과 방법론 설계를 위한 도구
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
    print("===== 연구 계획 및 설계 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    research_type = input("연구 유형을 입력하세요 (예: 정성적, 정량적, 혼합): ")
    time_resources = input("가용 시간과 자원을 입력하세요 (예: 1학기, 제한된 예산): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{research_topic}에 관한 {research_type} 연구를 어떻게 계획하고 설계해야 할까요?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 연구 계획 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 연구 방법론 전문가", 
        f"{field} 분야에서 다양한 {research_type} 연구를 설계하고 수행한 경험이 풍부한 연구자로, 연구 계획 수립과 방법론 설계에 관한 다수의 워크숍과 강의를 진행한 전문가입니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 정보:
- 주제: {research_topic}
- 학문 분야: {field}
- 연구 유형: {research_type}
- 가용 시간/자원: {time_resources}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 연구 주제 구체화 및 연구 질문 설정",
        f"   - {research_topic}을(를) 더 구체적이고 연구 가능한 질문으로 발전시키는 방법",
        "   - 명확하고 측정 가능한 연구 목표 설정 전략",
        "   - 연구의 범위와 한계 설정 방법",
        
        "2. 연구 방법론 선택 및 설계",
        f"   - {research_type} 연구에 적합한 방법론적 접근법 제안",
        f"   - {field} 분야에서 일반적으로 사용되는 연구 방법의 장단점",
        "   - 연구 질문과 방법론의 적합성 확보 전략",
        
        "3. 데이터 수집 및 분석 계획",
        "   - 필요한 데이터 유형 및 수집 방법 제안",
        "   - 표본 크기 및 선정 전략",
        "   - 적절한 분석 기법 및 도구 추천",
        
        "4. 연구 타임라인 및 자원 계획",
        f"   - {time_resources} 내에서 효과적인 연구 단계별 일정 계획",
        "   - 인적, 물적 자원 배분 전략",
        "   - 잠재적 위험 및 대안 계획",
        
        "5. 연구 윤리 및 타당성 고려사항",
        "   - 연구 윤리 준수를 위한 필요 조치",
        "   - 연구의 신뢰성과 타당성 확보 전략",
        "   - 필요한 승인 및 동의 절차"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **연구 개요**: {research_topic}에 대한 간략한 배경과 중요성

2. **연구 질문 및 목표 설정**:
   - 구체적인 연구 질문 예시
   - 측정 가능한 연구 목표
   - 연구의 범위와 한계

3. **연구 방법론 설계**:
   - 권장되는 {research_type} 연구 방법
   - 방법론적 접근법 정당화
   - 데이터 수집 및 분석 전략

4. **실행 계획**:
   - 단계별 연구 일정
   - 필요 자원 및 예산 계획
   - 잠재적 장애물 및 대안 전략

5. **연구 윤리 및 품질 보장**:
   - 윤리적 고려사항
   - 신뢰성 및 타당성 확보 전략
   - 품질 관리 절차

마크다운 형식으로 체계적인 연구 계획 템플릿과 구체적인 예시를 포함해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 연구 계획 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n연구 계획 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: research_planning_guide.md): ") or "research_planning_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} 연구 계획 가이드")
        print(f"연구 계획 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()