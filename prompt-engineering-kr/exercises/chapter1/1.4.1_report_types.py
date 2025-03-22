"""
보고서 유형별 맞춤 프롬프트

다양한 보고서 유형에 최적화된 프롬프트 작성 기법
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
    print("===== 보고서 유형별 맞춤 프롬프트 =====")
    
    # 사용자 입력 받기
    topic = input("보고서 주제를 입력하세요: ")
    report_type = input("보고서 유형을 입력하세요 (예: 문헌 연구, 실험 보고서, 사례 연구, 정책 분석): ")
    field = input("학문 분야를 입력하세요: ")
    scope = input("보고서 범위를 입력하세요 (예: 중간고사, 기말고사, 학기 프로젝트): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {report_type} 보고서 작성 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 보고서 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{field} 분야 교수 및 학술 자문", 
                           f"대학에서 {report_type} 보고서 작성법을 가르치고, 수많은 학생 보고서를 평가해온 경험이 있는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"보고서 유형: {report_type}\n"
        f"학문 분야: {field}\n"
        f"보고서 범위: {scope}"
    )
    
    # 보고서 유형별 특화 지시사항
    report_specific_instructions = {
        "문헌 연구": [
            "1. 문헌 검토의 효과적인 범위 설정 및 조직화 방법",
            "2. 문헌 선별 및 평가 기준 설정 전략",
            "3. 주요 연구 동향, 패턴, 격차 식별 방법",
            "4. 다양한 관점을 통합적으로 분석하는 기법"
        ],
        "실험 보고서": [
            "1. 명확한 실험 목적과 가설 설정 방법",
            "2. 실험 방법론 및 절차의 정확한 기술법",
            "3. 실험 결과의 체계적 제시 및 시각화 전략",
            "4. 결과에 대한 객관적 해석 및 논의 방법"
        ],
        "사례 연구": [
            "1. 대표적 사례 선정 기준 및 정당화 방법",
            "2. 사례 배경 및 맥락의 효과적 설명 기법",
            "3. 사례 분석을 위한 프레임워크 개발 방법",
            "4. 사례에서 일반화 가능한 통찰 도출 전략"
        ],
        "정책 분석": [
            "1. 정책 문제의 명확한 정의 및 범위 설정 방법",
            "2. 다양한 정책 대안 개발 및 평가 기준 설정",
            "3. 정책 대안의 비용-편익 분석 방법",
            "4. 근거 기반 정책 제안 및 실행 전략 수립"
        ]
    }
    
    # 기본 지시사항 설정
    default_instructions = [
        f"1. {report_type} 보고서의 표준 구조와 핵심 구성요소",
        f"2. {field} 분야에서 {report_type} 보고서 작성 시 고려할 특수 요소",
        "3. 학술적 문체와 표현 최적화 방법",
        "4. 효과적인 논증 구조 및 근거 제시 전략"
    ]
    
    # 보고서 유형에 맞는 특화 지시사항 선택
    type_specific = report_specific_instructions.get(report_type, [
        f"1. {report_type} 보고서의 고유한 특성과 요구사항",
        "2. 내용 구성 및 전개 전략",
        "3. 자료 활용 및 제시 방법",
        "4. 분석 및 논의 접근법"
    ])
    
    # 공통 지시사항
    common_instructions = [
        f"5. {scope}에 적합한 범위와 깊이 설정 방법",
        "6. 평가 기준을 충족하기 위한 핵심 전략",
        "7. 시간 관리 및 효율적 작성 계획",
        "8. 자기 평가 및 검토 체크리스트",
        f"9. {report_type} 보고서의 우수 사례 및 특징",
        "10. 흔히 발생하는 실수와 피해야 할 사항"
    ]
    
    # 지시사항 통합
    all_instructions = type_specific + common_instructions
    
    # 지시사항 추가
    prompt_builder.add_instructions(all_instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        f"1. {report_type} 보고서 개요 및 핵심 특성\n"
        "2. 효과적인 구조 및 내용 구성 가이드\n"
        "3. 작성 단계별 팁과 전략\n"
        "4. 평가 기준 및 품질 향상 방법\n"
        "5. 시간 관리 및 자원 활용 전략\n\n"
        f"{topic}에 대한 {report_type} 보고서 작성을 위한 구체적인 예시와 템플릿을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 보고서 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n보고서 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: report_guide.md): ") or "report_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic}에 대한 {report_type} 보고서 작성 가이드")
        print(f"보고서 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()