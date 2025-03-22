"""
중간/기말 보고서 마스터하기

보고서 유형, 범위 설정, 피드백 활용, 시간 관리를 통합한 보고서 작성 전략
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
    print("===== 중간/기말 보고서 마스터하기 =====")
    
    # 사용자 입력 받기
    topic = input("보고서 주제를 입력하세요: ")
    report_type = input("보고서 유형을 입력하세요 (예: 중간고사, 기말고사, 학기 프로젝트): ")
    field = input("학문 분야를 입력하세요: ")
    deadline = input("제출 기한을 입력하세요: ")
    previous_feedback = input("이전 피드백이 있다면 입력하세요 (없으면 Enter): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대한 {report_type} 보고서를 어떻게 효과적으로 작성할 수 있을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 보고서 마스터 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("학술 글쓰기 및 보고서 전략 전문가", 
                           f"{field} 분야에서 수많은 학생들의 보고서 작성을 지도하고, 평가해 온 대학 교수입니다.")
    
    # 맥락 제공
    context = f"주제: {topic}\n" \
             f"보고서 유형: {report_type}\n" \
             f"학문 분야: {field}\n" \
             f"제출 기한: {deadline}"
    
    if previous_feedback:
        context += f"\n이전 피드백:\n\"{previous_feedback}\""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 보고서 유형별 맞춤 접근법",
        f"   - {report_type}의 특성과 평가 기준 분석",
        f"   - {field} 분야에서 {report_type}에 적합한 구조와 내용",
        "   - 교수자의 기대치와 평가 요소 고려",
        
        "2. 주제 범위와 깊이 최적화",
        f"   - {topic}의 범위 설정 및 초점화 전략",
        "   - 적절한 분석 깊이 확보 방법",
        f"   - {report_type}에 맞는 균형 잡힌 범위와 깊이 설정",
        
        "3. 피드백 분석 및 반영",
        "   - 이전 피드백의 체계적 분석 및 우선순위 설정",
        "   - 개선 영역 식별 및 전략적 접근",
        "   - 지속적인 발전을 위한 피드백 활용법",
        
        "4. 시간 제약 상황에서의 효율적 작성",
        f"   - {deadline}까지 효과적인 시간 관리 계획",
        "   - 연구, 작성, 편집 단계별 시간 최적화 전략",
        "   - 압박 상황에서의 품질 유지 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 보고서 계획 및 준비 단계\n"
        "2. 효과적인 연구 및 자료 수집 전략\n"
        "3. 보고서 구조 및 내용 구성 가이드\n"
        "4. 작성 및 편집 최적화 방법\n"
        "5. 제출 전 최종 검토 체크리스트\n\n"
        f"{topic}에 대한 {report_type} 보고서 작성을 위한 구체적인 단계별 가이드와 전략을 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 보고서 마스터 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n보고서 마스터 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: report_master_guide.md): ") or "report_master_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} {report_type} 보고서 마스터 가이드")
        print(f"보고서 마스터 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()