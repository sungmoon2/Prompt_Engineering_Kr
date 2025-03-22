"""
압박 질문 대응 전략

면접에서 마주하는 까다로운 질문이나 압박 상황에 침착하게 대응하는 전략과 기법
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
    print("===== 압박 질문 대응 전략 =====")
    
    # 사용자 입력 받기
    job_position = input("지원하는 직무/포지션을 입력하세요: ")
    tough_questions = input("염려되는 압박 질문이나 약점 관련 질문을 입력하세요 (쉼표로 구분): ")
    weaknesses = input("본인의 약점이나 경력 갭이 있다면 입력하세요: ")
    industry = input("산업 분야를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
면접에서 압박 질문이 나왔을 때 어떻게 대응하면 좋을까?
예를 들어 이런 질문들: {tough_questions}
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 압박 질문 대응 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("면접 위기 관리 전문가", 
                          "고난도 면접 상황과 압박 질문에 대응하는 전략을 교육하는 전문가로, 후보자들이 어려운 순간에도 자신감과 전문성을 유지할 수 있도록 지원합니다.")
    
    # 맥락 제공
    context = f"지원 직무: {job_position}\n" \
             f"산업 분야: {industry}\n" \
             f"압박 질문 예시: {tough_questions}"
    
    if weaknesses:
        context += f"\n개인적 약점/경력 갭: {weaknesses}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 압박 질문의 유형 및 면접관의 의도 분석",
        "   - 약점/단점 관련 질문의 실제 의도 파악",
        "   - 경력 갭이나 실패 경험에 대한 질문의 평가 포인트",
        "   - 역량 검증을 위한 깊이 있는 기술 질문의 목적",
        "   - 가치관과 윤리적 판단을 테스트하는 압박 질문 유형",
        
        "2. 압박 상황에서의 심리적 안정 유지 전략",
        "   - 압박감 관리 및 침착성 유지 기법",
        "   - 답변을 위한 시간 확보 방법",
        "   - 비언어적 요소 관리 (시선, 목소리 톤, 자세)",
        
        "3. 질문 유형별 효과적인 대응 프레임워크",
        f"   - '{tough_questions}' 질문에 대한 구체적 대응 방안",
        "   - 약점을 강점으로 전환하는 리프레이밍 기법",
        "   - 경험 부족 관련 질문에 대한 대안적 역량 제시 방법",
        "   - 모호하거나 함정이 있는 질문 명확화 전략"
    ]
    
    if weaknesses:
        instructions.append(f"4. 개인 약점 '{weaknesses}'를 효과적으로 다루는 전략")
        instructions.append("   - 약점 인정과 극복 노력을 설득력 있게 제시하는 방법")
        instructions.append("   - 약점에 대한 자기인식과 성장 마인드셋 표현 기법")
        instructions.append("   - 약점 관련 개선 노력과 발전 과정 설명 방법")
    else:
        instructions.append("4. 일반적인 약점 관련 질문 대응 전략")
        instructions.append("   - 전략적으로 적절한 약점 선택하기")
        instructions.append("   - 약점에 대한 자기인식과 개선 노력 강조")
    
    instructions.extend([
        "5. 예상치 못한 질문이나 모르는 내용에 대한 대처법",
        "6. 공격적이거나 부정적인 면접관에 대한 대응 방법",
        "7. 압박 면접 상황에서의 자신감 표현과 전문성 유지 전략",
        "8. 압박 질문 대응을 위한 사전 준비 및 연습 방법"
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 압박 질문의 심리학 및 면접관 의도 분석\n"
        "2. 질문 유형별 대응 전략 및 프레임워크\n"
        "3. 제시된 압박 질문에 대한 구체적 답변 예시\n"
        "4. 약점 관련 질문 대응 전략\n"
        "5. 심리적 안정 유지 및 자신감 표현 기법\n"
        "6. 압박 상황 대비 사전 준비 체크리스트\n\n"
        f"{job_position} 직무와 {industry} 산업에 특화된 압박 질문 대응 사례와 구체적인 스크립트를 포함해주세요. 실제 면접 상황에서 활용할 수 있는 실용적인 팁과 즉시 적용 가능한 대응 방식을 제시해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 압박 질문 대응 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n압박 질문 대응 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: pressure_question_guide.md): ") or "pressure_question_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{job_position} 면접 압박 질문 대응 가이드")
        print(f"압박 질문 대응 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()