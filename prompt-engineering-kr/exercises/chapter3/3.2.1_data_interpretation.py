"""
데이터 해석 및 의미 도출 프롬프트

분석 결과의 효과적인 해석과 의미 있는 통찰 도출을 위한 프롬프트 기법
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
    print("===== 데이터 해석 및 의미 도출 프롬프트 =====")
    
    # 사용자 입력 받기
    analysis_results = input("해석이 필요한 분석 결과를 입력하세요: ")
    research_questions = input("원래 연구 질문이나 가설을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    audience = input("결과를 발표할 대상을 입력하세요 (예: 학술 동료, 일반인, 의사결정자): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
다음 분석 결과의 의미를 해석해주세요: {analysis_results}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 데이터 해석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 데이터 해석 전문가", 
        f"{field} 분야에서 복잡한 데이터 분석 결과를 의미 있게 해석하고 다양한 대상에게 효과적으로 설명하는 데 특화된 전문가로, 연구 결과와 이론적 지식 사이의 연결고리를 구축하는 능력이 뛰어납니다."
    )
    
    # 컨텍스트 추가
    context = f"""
분석 정보:
- 분석 결과: {analysis_results}
- 연구 질문/가설: {research_questions}
- 학문 분야: {field}
- 대상 청중: {audience}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 분석 결과의 객관적 요약 및 정리",
        "   - 핵심 결과의 명확한 식별 및 구조화",
        "   - 통계적/분석적 의미의 객관적 설명",
        "   - 결과의 패턴, 관계, 추세 요약",
        
        "2. 연구 질문/가설과의 연결",
        f"   - {research_questions}와 결과 간의 관계 분석",
        "   - 가설 지지/기각 여부 및 그 정도 평가",
        "   - 예상했던 결과와 실제 결과의 차이점 설명",
        
        "3. 학문적/실용적 의미 해석",
        f"   - {field} 분야의 이론적 관점에서 결과 해석",
        "   - 선행 연구와의 일치/불일치 분석",
        "   - 실용적/응용적 함의 도출",
        
        "4. 결과의 한계 및 대안적 해석",
        "   - 결과 해석의 잠재적 한계 식별",
        "   - 대안적 설명 및 해석 가능성 탐색",
        "   - 결과의 일반화 가능성 및 제한사항 분석",
        
        "5. 청중 맞춤형 해석 전략",
        f"   - {audience}에게 적합한 해석 방식 및 표현",
        "   - 핵심 메시지 및 주요 통찰 강조 전략",
        "   - 복잡한 결과의 접근 가능한 설명 방법"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **분석 결과 요약 및 구조화**:
   - 핵심 결과 요약
   - 주요 패턴 및 관계 정리
   - 통계적/분석적 의미 설명

2. **연구 질문/가설 검증**:
   - {research_questions}에 대한 결과의 함의
   - 가설 검증 결과 평가
   - 예상과 실제 결과 비교

3. **이론적/실용적 의미 해석**:
   - {field} 분야 이론적 맥락에서의 해석
   - 선행 연구와의 관계
   - 실용적/응용적 함의

4. **한계 및 대안적 해석**:
   - 결과 해석의 한계점
   - 대안적 설명 가능성
   - 일반화 가능성 및 제한사항

5. **{audience}을 위한 핵심 통찰**:
   - 주요 발견점 및 의미
   - 접근 가능한 설명 및 비유
   - 의사결정/후속 연구를 위한 함의

6. **시각적 설명 전략**:
   - 결과 해석을 위한 시각화 제안
   - 핵심 메시지 전달을 위한 프레젠테이션 전략

마크다운 형식으로 체계적인 데이터 해석 가이드와 실제 사례를 통한 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 데이터 해석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n데이터 해석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: data_interpretation_guide.md): ") or "data_interpretation_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_questions} 데이터 해석 가이드")
        print(f"데이터 해석 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()