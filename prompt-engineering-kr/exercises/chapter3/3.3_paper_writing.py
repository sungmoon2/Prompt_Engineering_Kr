"""
논문 작성 통합 가이드

학술 논문의 구조 설계부터 각 섹션별 작성 전략까지 포괄하는 통합적 접근법
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
    print("===== 논문 작성 통합 가이드 =====")
    
    # 사용자 입력 받기
    research_topic = input("연구 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    paper_type = input("논문 유형을 입력하세요 (예: 실증 연구, 문헌 검토, 이론 개발): ")
    target_journal = input("목표 학술지가 있다면 입력하세요 (선택사항): ")
    main_findings = input("주요 연구 결과가 있다면 간략히 입력하세요 (선택사항): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{research_topic}에 대한 {paper_type} 논문 작성 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 논문 작성 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    role_desc = f"{field} 분야의 저명한 학술지 편집자이자 연구자로서, 수많은 논문을 작성, 검토, 지도한 경험을 가진 학술 출판 전문가입니다."
    if target_journal:
        role_desc += f" {target_journal}와 같은 우수 저널의 출판 기준과 요구사항에 정통합니다."
    
    prompt_builder.add_role("학술 논문 작성 및 출판 전문가", role_desc)
    
    # 맥락 제공
    context = f"연구 주제: {research_topic}\n" \
             f"학문 분야: {field}\n" \
             f"논문 유형: {paper_type}"
    
    if target_journal:
        context += f"\n목표 학술지: {target_journal}"
    
    if main_findings:
        context += f"\n주요 연구 결과: {main_findings}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        # 통합적 접근법
        f"1. {paper_type} 논문의 전체 구조 및 각 섹션의 목적 설명",
        f"2. {field} 분야의 논문 작성 관행 및 특성 고려",
        
        # 주요 섹션별 작성 전략
        "3. 효과적인 제목과 초록 작성 전략",
        "4. 설득력 있는 서론 구성 및 연구 동기 제시 방법",
        "5. 체계적이고 비판적인 문헌 검토 작성법",
        "6. 명확한 연구 방법론 설명 전략",
        "7. 연구 결과의 객관적이고 정확한 제시 방법",
        "8. 결과에 대한 통찰력 있는 논의 전개 방법",
        "9. 강력한 결론 작성 및 연구의 기여도 강조 전략",
        
        # 추가 고려사항
        "10. 인용 및 참고문헌 관리 최적화 방법",
        "11. 학술적 글쓰기 스타일 및 표현 향상 전략",
        "12. 효과적인 테이블, 그림, 부록 활용법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 논문 작성 통합 접근법\n"
        "2. 논문 전체 구조 및 흐름 설계\n"
        "3. 섹션별 작성 가이드\n"
        "   - 제목 및 초록\n"
        "   - 서론\n"
        "   - 문헌 검토\n"
        "   - 연구 방법\n"
        "   - 결과 제시\n"
        "   - 논의\n"
        "   - 결론\n"
        "4. 학술적 글쓰기 스타일 및 표현\n"
        "5. 논문 작성 프로세스 및 워크플로우\n"
        "6. 논문 완성도 체크리스트\n\n"
        f"{research_topic}에 대한 {paper_type} 논문의 구체적인 작성 예시와 템플릿을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 논문 작성 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n논문 작성 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: paper_writing_guide.md): ") or "paper_writing_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_topic} {paper_type} 논문 작성 가이드")
        print(f"논문 작성 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()