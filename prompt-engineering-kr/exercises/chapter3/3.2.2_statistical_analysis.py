"""
통계 분석 선택 및 해석 프롬프트

연구 질문에 적합한 통계 분석 방법 선택과 결과 해석을 위한 프롬프트 기법
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
    print("===== 통계 분석 선택 및 해석 프롬프트 =====")
    
    # 사용자 입력 받기
    research_question = input("연구 질문을 입력하세요: ")
    data_description = input("데이터 특성을 입력하세요 (예: 변수 유형, 표본 크기): ")
    hypothesis = input("검증하려는 가설이 있다면 입력하세요: ")
    stats_knowledge = input("통계 지식 수준을 입력하세요 (기초/중급/고급): ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
"{research_question}" 연구 질문을 위한 적절한 통계 분석 방법을 추천해주세요.
데이터 특성: {data_description}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 통계 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        "통계 분석 및 연구 방법론 전문가", 
        "다양한 연구 맥락에서 적절한 통계적 접근법을 선택하고 적용하는 데 전문성을 가진 통계학자로, 복잡한 통계 개념을 다양한 배경의 연구자들이 이해할 수 있도록 설명하는 능력이 뛰어납니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 정보:
- 연구 질문: {research_question}
- 데이터 특성: {data_description}
- 통계 지식 수준: {stats_knowledge}
"""
    
    if hypothesis:
        context += f"- 검증할 가설: {hypothesis}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 연구 질문 및 데이터 특성 분석",
        f"   - '{research_question}'의 통계적 분석 요구사항 파악",
        f"   - {data_description}에 따른 적절한 분석 접근법 평가",
        "   - 변수 유형, 관계, 분포 등 고려사항 분석",
        
        "2. 적합한 통계 분석 방법 추천",
        "   - 3-5가지 가능한 통계 분석 방법 제안",
        "   - 각 방법의 적합성, 장단점, 가정 설명",
        "   - 최적의 방법 추천 및 선택 근거 제시",
        
        "3. 분석 실행 및 해석 가이드",
        f"   - {stats_knowledge} 수준에 맞는 단계별 분석 절차 안내",
        "   - 필요한 통계 소프트웨어 및 명령어/코드 예시",
        "   - 결과 해석을 위한 주요 통계량 및 의미 설명",
        
        "4. 잠재적 문제 및 대안 전략",
        "   - 통계적 가정 위반 시 대처 방법",
        "   - 일반적인 통계적 오류 및 방지법",
        "   - 표본 크기, 검정력, 효과 크기 고려사항",
        
        "5. 결과 보고 및 시각화 전략",
        "   - 분석 결과의 학술적 보고 방법",
        "   - 효과적인 통계 결과 시각화 기법",
        "   - 통계 결과와 연구 질문 연결 전략"
    ]
    
    if hypothesis:
        instructions.append(
            "6. 가설 검증 전략",
            f"   - '{hypothesis}' 검증을 위한 최적의 접근법",
            "   - 귀무가설 및 대립가설 명확화 방법",
            "   - 가설 검증 결과 해석 및 결론 도출 프레임워크"
        )
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **연구 질문 및 데이터 분석**:
   - '{research_question}'의 통계적 분석 요구사항
   - {data_description}에 기반한 주요 고려사항
   - 변수 관계 및 분석 목표 정리

2. **추천 통계 분석 방법**:
   - 방법 1: [이름 및 설명]
     - 적합성 평가
     - 주요 가정 및 요구사항
     - 장단점
   - 방법 2: [이름 및 설명]
     ...
   (3-5개 방법)
   - 최적 방법 추천 및 근거

3. **단계별 분석 실행 가이드**:
   - 데이터 준비 및 가정 검토 단계
   - 분석 실행 단계별 지침
   - 주요 통계량 및 결과 해석 방법
   - 소프트웨어/코드 예시

4. **결과 해석 프레임워크**:
   - 주요 통계량의 의미 설명
   - 통계적 유의성 및 효과 크기 해석
   - 결과의 실질적 의미 도출 방법

5. **결과 보고 및 시각화 가이드**:
   - 통계 결과 보고 모범 사례
   - 추천 시각화 방법 및 예시
   - 효과적인 결과 커뮤니케이션 전략
"""
    
    if hypothesis:
        output_format += """
6. **가설 검증 전략 및 해석**:
   - 가설 검증을 위한 통계적 접근법
   - 가설 검증 결과 해석 가이드
   - 결론 도출 프레임워크
"""
    
    output_format += f"""
7. **{stats_knowledge} 수준을 위한 학습 자료**:
   - 핵심 개념 설명
   - 추천 학습 자료
   - 향후 학습 경로

마크다운 형식으로 체계적인 통계 분석 가이드와 실제 적용 가능한 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 통계 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n통계 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: statistical_analysis_guide.md): ") or "statistical_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_question} 통계 분석 가이드")
        print(f"통계 분석 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()