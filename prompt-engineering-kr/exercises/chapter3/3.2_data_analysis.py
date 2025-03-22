"""
데이터 분석 지원

연구 데이터 분석 및 해석을 위한 도구와 기법
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
    print("===== 데이터 분석 지원 =====")
    
    # 사용자 입력 받기
    data_description = input("분석할 데이터의 특성을 입력하세요 (예: 유형, 크기, 변수): ")
    research_goals = input("데이터 분석의 주요 목표를 입력하세요: ")
    analysis_method = input("고려하고 있는 분석 방법이 있다면 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{data_description} 데이터를 분석하여 {research_goals}을(를) 달성하는 방법을 알려주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 데이터 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 데이터 분석 전문가", 
        f"{field} 분야에서 다양한 유형의 데이터를 분석한 풍부한 경험을 가진 연구자로, 복잡한 데이터셋에서 의미 있는 통찰을 도출하고 연구 질문에 답하기 위한 최적의 분석 방법을 적용하는 전문가입니다."
    )
    
    # 컨텍스트 추가
    context = f"""
데이터 분석 정보:
- 데이터 특성: {data_description}
- 분석 목표: {research_goals}
- 학문 분야: {field}
"""
    
    if analysis_method:
        context += f"- 고려 중인 분석 방법: {analysis_method}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 데이터 특성 및 분석 목표 평가",
        f"   - {data_description} 데이터의 특성과 구조 분석",
        f"   - {research_goals}를 달성하기 위한 분석 접근법 평가",
        "   - 데이터와 목표 간의 적합성 및 제한사항 식별",
        
        "2. 적합한 분석 방법 제안",
        f"   - {field} 분야에 적합한 데이터 분석 방법 추천",
        "   - 각 방법의 장단점 및 적용 조건 설명",
        "   - 방법론적 결정에 대한 정당화 및 근거 제시",
        
        "3. 데이터 전처리 및 준비 전략",
        "   - 필요한 데이터 정제 및 변환 절차",
        "   - 결측치, 이상치, 중복 데이터 처리 방법",
        "   - 변수 선택, 변환, 생성 전략",
        
        "4. 분석 실행 단계별 가이드",
        "   - 체계적인 분석 워크플로우 제안",
        "   - 주요 분석 단계 및 기법 상세 설명",
        "   - 잠재적 문제점 및 해결 전략",
        
        "5. 결과 해석 및 시각화 방법",
        "   - 분석 결과의 효과적인 해석 프레임워크",
        "   - 적절한 시각화 방법 및 도구 추천",
        "   - 결과를 연구 질문과 연결하는 전략"
    ]
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **데이터 특성 및 분석 목표 평가**:
   - {data_description} 데이터의 특성과 구조
   - {research_goals}를 위한 분석 접근법 요구사항
   - 데이터와 목표 간의 적합성 평가

2. **분석 방법 추천 및 평가**:
   - 권장 분석 방법
   - 각 방법의 장단점
   - 방법론적 결정의 근거
   - 대안적 접근법 비교

3. **데이터 전처리 및 준비 가이드**:
   - 필요한 전처리 단계
   - 자료 정제 및 변환 기법
   - 변수 관리 전략

4. **분석 실행 단계별 가이드**:
   - 주요 분석 단계
   - 적용 기법 및 코드 예시
   - 잠재적 문제 및 해결책

5. **결과 해석 및 시각화 전략**:
   - 주요 결과 해석 프레임워크
   - 권장 시각화 방법
   - 연구 질문과의 연결 전략

6. **분석 품질 보장 체크리스트**:
   - 분석의 타당성 및 신뢰성 확보 방법
   - 결과 검증 전략
   - 연구 윤리 고려사항

마크다운 형식으로 체계적인 데이터 분석 가이드와 실제 적용 가능한 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 데이터 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n데이터 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: data_analysis_guide.md): ") or "data_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_goals} 데이터 분석 가이드")
        print(f"데이터 분석 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()