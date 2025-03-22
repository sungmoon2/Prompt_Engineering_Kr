"""
면접 시뮬레이션

실제 면접 환경을 모방한 시뮬레이션을 통해 답변 완성도와 자신감을 향상시키는 실습
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
    print("===== 면접 시뮬레이션 =====")
    
    # 사용자 입력 받기
    job_position = input("지원하는 직무/포지션을 입력하세요: ")
    company = input("지원하는 회사명을 입력하세요: ")
    interview_type = input("면접 유형을 입력하세요 (예: 1차면접, 기술면접, 임원면접): ")
    background = input("본인의 경력 및 배경을 간략히 입력하세요: ")
    focus_areas = input("특별히 연습하고 싶은 질문 영역이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{company}의 {job_position} 면접 상황을 가정하고 몇 가지 질문을 해줘. 내가 답변하면 피드백도 줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 면접 시뮬레이션 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("면접관 및 면접 코치", 
                          f"{company}와 같은 기업의 {job_position} 채용 면접을 수년간 진행해왔으며, 후보자들의 면접 준비를 돕는 전문 코치입니다.")
    
    # 맥락 제공
    context = f"지원 직무: {job_position}\n" \
             f"지원 회사: {company}\n" \
             f"면접 유형: {interview_type}\n" \
             f"지원자 배경: {background}"
    
    if focus_areas:
        context += f"\n연습 희망 영역: {focus_areas}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 실제 면접 환경과 유사한 시뮬레이션 구성",
        f"   - {company}의 {job_position} 실제 면접 과정 및 분위기 재현",
        f"   - {interview_type}에 적합한 질문 구성 및 난이도 설정",
        "   - 일반적 질문부터 시작해 점진적으로 심화된 질문으로 전환",
        
        f"2. {job_position} 직무에 특화된 다양한 유형의 면접 질문 포함",
        "   - 경력 및 경험 검증 질문",
        "   - 직무 관련 기술 및 지식 평가 질문",
        "   - 상황 대처 능력과 문제 해결 역량 평가 질문",
        "   - 문화적 적합성 및 팀워크 관련 질문",
        "   - 동기 부여 및 커리어 계획 탐색 질문"
    ]
    
    if focus_areas:
        instructions.append(f"3. '{focus_areas}' 영역에 중점을 둔 심층 질문 및 시나리오")
    else:
        instructions.append("3. 균형 잡힌 다양한 주제의 질문 구성")
    
    instructions.extend([
        "4. 각 질문 후 상세한 피드백 및 개선 가이드 제공",
        "   - 답변의 강점과 개선점 분석",
        "   - 면접관 관점에서의 인상과 평가 포인트",
        "   - 구체적인 개선 방향 및 대안 제시",
        "   - 효과적인 답변 구조와 핵심 요소 가이드",
        
        "5. 실전 면접 상황의 상호작용 시뮬레이션",
        "   - 추가 질문이나 명확화 요청 포함",
        "   - 답변에 따른 면접관의 반응 및 후속 질문 예시",
        "   - 면접 상황에서의 예상치 못한 요소 대응 연습",
        
        "6. 마무리 평가 및 종합 피드백 제공",
        "   - 전반적인 인상과 강점 분석",
        "   - 우선적 개선 영역 제안",
        "   - 실제 면접 준비를 위한 추가 조언"
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 구조로 완전한 면접 시뮬레이션을 진행하는 마크다운 형식의 응답을 제공해주세요:\n\n"
        "1. 면접 시뮬레이션 안내 및 설정\n"
        "2. 시뮬레이션 시작 (면접관 소개 및 첫 질문)\n"
        "3. 각 질문별 섹션 (최소 8-10개의 다양한 질문):\n"
        "   - 면접관 질문\n"
        "   - [예상 답변 가이드] (괄호 안에 지원자를 위한 답변 가이드)\n"
        "   - [피드백 및 개선점] (괄호 안에 상세한 피드백)\n"
        "4. 후속/심화 질문 및 시나리오\n"
        "5. 면접 마무리 질문 (지원자의 질문 기회)\n"
        "6. 종합 평가 및 최종 피드백\n\n"
        f"{company}의 {job_position} 면접 과정과 실제 면접관의 질문 스타일을 최대한 사실적으로 재현해주세요. 지원자가 실제로 답변을 준비하고 연습할 수 있도록 충분한 맥락과 가이드를 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 면접 시뮬레이션 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n면접 시뮬레이션을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: interview_simulation.md): ") or "interview_simulation.md"
        save_markdown(enhanced_result, file_path, title=f"{company} {job_position} 면접 시뮬레이션")
        print(f"면접 시뮬레이션이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()