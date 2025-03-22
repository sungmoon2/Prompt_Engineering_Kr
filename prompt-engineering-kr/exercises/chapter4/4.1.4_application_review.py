"""
지원서류 최종 검토 전략

이력서와 자기소개서의 완성도를 높이기 위한 체계적인 검토 방법
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
    print("===== 지원서류 최종 검토 전략 =====")
    
    # 사용자 입력 받기
    document_type = input("검토할 문서 유형을 입력하세요 (이력서/자기소개서/전체): ")
    job_position = input("지원 직무를 입력하세요: ")
    industry = input("산업 분야를 입력하세요: ")
    key_requirements = input("직무 핵심 요구사항을 입력하세요: ")
    submission_deadline = input("제출 마감일을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{document_type}를 제출하기 전에 어떻게 검토해야 할까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 지원서류 검토 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("취업 서류 품질 관리 전문가", 
                           f"{industry} 분야의 채용 프로세스에 대한 깊은 이해를 바탕으로 수천 개의 지원 서류를 검토하고 개선해온 전문가로, 취업 성공률을 높이는 최종 검토 전략을 제시합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"문서 유형: {document_type}\n"
        f"지원 직무: {job_position}\n"
        f"산업 분야: {industry}\n"
        f"직무 핵심 요구사항: {key_requirements}\n"
        f"제출 마감일: {submission_deadline}"
    )
    
    # 지시사항 추가
    instructions = [
        "1. 직무 적합성 검토",
        f"   - {job_position} 직무에 필수적인 키워드와 역량 포함 여부 확인",
        f"   - {key_requirements}와 같은 핵심 요구사항 반영 정도 평가",
        "   - 직무 관련 경험과 성과의 명확한 제시 여부 점검",
        "   - 기업 및 산업 특성에 맞는 용어와 표현 사용 확인",
        
        "2. 구조 및 가독성 검토",
        "   - 논리적 흐름과 일관성 평가",
        "   - 적절한 여백, 폰트, 포맷팅 점검",
        "   - 섹션 간 균형과 중요도에 따른 배치 최적화",
        "   - 스캔 가능성(scanability) 및 핵심 정보 돋보이게 하기",
        
        "3. 내용의 구체성 및 증명력 검토",
        "   - 추상적/일반적 표현 vs 구체적/증명 가능한 성과 비교",
        "   - 정량적 성과와 수치 활용 최적화",
        "   - 주장을 뒷받침하는 근거 충분성 평가",
        "   - 성과 중심 서술(accomplishment statements) 효과성 점검",
        
        "4. 오류 및 완성도 검토",
        "   - 맞춤법, 문법, 구두점 오류 식별",
        "   - 일관된 시제와 표현 스타일 확인",
        "   - 중복 내용 및 불필요한 정보 제거",
        "   - 전문적 어조와 적절한 공식성 유지 확인"
    ]
    
    if document_type.lower() in ["전체", "all", "both"]:
        instructions.append("5. 이력서-자기소개서 연계성 검토")
        instructions.append("   - 두 문서 간 정보의 일관성 및 상호보완성 점검")
        instructions.append("   - 각 문서의 고유 목적 달성 여부 확인")
        instructions.append("   - 중복 내용의 전략적 활용 평가")
    
    if submission_deadline:
        instructions.append("6. 최종 제출 전 체크리스트")
        instructions.append(f"   - {submission_deadline} 마감일을 고려한 검토 일정 계획")
        instructions.append("   - 제출 형식 및 파일 요구사항 준수 확인")
        instructions.append("   - 피드백 반영 및 최종 검토 프로세스")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 지원서류 검토의 중요성\n"
        "2. 단계별 체계적 검토 전략\n"
        "3. 영역별 세부 검토 체크리스트\n"
        "4. 피어 리뷰 및 피드백 활용법\n"
        "5. 최종 제출 전 확인 사항\n"
        "6. 일반적인 실수 및 주의점\n\n"
        f"{document_type}에 특화된 구체적인 검토 포인트와 체크리스트를 제공하고, {job_position} 직무 지원에 최적화된 검토 전략을 상세히 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 지원서류 검토 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n지원서류 검토 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: application_review_guide.md): ") or "application_review_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{document_type} 지원서류 최종 검토 가이드")
        print(f"지원서류 검토 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()