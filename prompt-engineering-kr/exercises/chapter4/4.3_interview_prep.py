"""
면접 준비 및 전략 최적화

직무별 질문 분석, 경험 기반 답변 구조화, 압박 질문 대응, 시뮬레이션을 통합한 접근법
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown

def main():
    """실습 코드 메인 함수"""
    print("===== 면접 준비 통합 전략 =====")
    
    # 사용자 입력 받기
    job_position = input("지원하는 직무/포지션을 입력하세요: ")
    company = input("지원하는 회사명을 입력하세요: ")
    key_experience = input("주요 경험이나 역량을 입력하세요: ")
    challenge = input("면접시 어려움이 예상되는 부분을 입력하세요: ")
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("면접 준비 전문가", 
                         f"{job_position} 직무의 면접 전략을 컨설팅하는 전문가로서, 후보자의 강점을 극대화하고 성공적인 면접을 위한 종합적인 접근법을 제공합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"지원 직무: {job_position}\n"
        f"지원 회사: {company}\n"
        f"핵심 역량/경험: {key_experience}\n"
        f"예상 어려움: {challenge}"
    )
    
    # 지시사항 추가 - 하위 챕터 내용 통합
    prompt_builder.add_instructions([
        # 4.3.1 직무별 면접 질문 준비 반영
        f"1. {job_position} 직무와 {company}에 특화된 주요 면접 질문 유형과 패턴을 분석해주세요.",
        "   - 직무 적합성, 기술적 역량, 문화적 적합성 평가 질문 각 3개씩",
        
        # 4.3.2 경험 기반 구조화 답변 작성법 반영
        f"2. {key_experience}를 STAR 기법으로 구조화하는 방법을 보여주세요.",
        "   - 상황(S), 과제(T), 행동(A), 결과(R) 구조의 답변 템플릿",
        
        # 4.3.3 압박 질문 대응 전략 반영
        f"3. {challenge}와 관련된 압박 질문에 대처하는 전략을 제시해주세요.",
        "   - 약점 질문, 갭 설명, 경험 부족 관련 질문 대응법",
        
        # 4.3.4 면접 시뮬레이션 반영
        "4. 핵심 질문 1-2개에 대한 간단한 시뮬레이션과 피드백을 제공해주세요.",
        "   - 예상 질문, 모범 답변, 개선점 분석"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 직무 맞춤형 핵심 면접 질문 리스트\n"
        "2. STAR 기법을 활용한 경험 구조화 템플릿\n"
        "3. 압박 질문 대응 전략\n"
        "4. 미니 면접 시뮬레이션\n"
        "5. 면접 준비 종합 체크리스트\n\n"
        "구체적이고 실용적인 조언을 제공하되, 각 섹션을 간결하게 유지해주세요."
    )
    
    # 프롬프트 실행
    enhanced_prompt = prompt_builder.build()
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 면접 준비 통합 전략 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n면접 준비 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: interview_guide.md): ") or "interview_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{company} {job_position} 면접 준비 통합 가이드")
        print(f"면접 준비 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()