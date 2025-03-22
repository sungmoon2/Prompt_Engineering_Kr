"""
자기소개서 최적화 전략

지원 기업과 직무에 맞춘 효과적인 자기소개서 작성 방법
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
    print("===== 자기소개서 최적화 전략 =====")
    
    # 사용자 입력 받기
    company_name = input("지원 기업명을 입력하세요: ")
    job_position = input("지원 직무를 입력하세요: ")
    background = input("자신의 배경을 간략히 입력하세요 (전공, 경력 등): ")
    motivation = input("지원 동기나 관심 분야를 입력하세요: ")
    company_values = input("해당 기업의 핵심 가치나 문화가 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{company_name}의 {job_position} 직무에 지원하는 자기소개서를 어떻게 작성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 자기소개서 최적화 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("채용 컨설턴트 및 기업 문화 전문가", 
                           f"{company_name}와 같은 기업의 채용 과정과 기업 문화를 깊이 이해하고, 지원자들의 자기소개서를 검토하며 성공적인 취업 전략을 제시해온 전문가입니다.")
    
    # 맥락 제공
    context = f"지원 기업: {company_name}\n" \
             f"지원 직무: {job_position}\n" \
             f"지원자 배경: {background}\n" \
             f"지원 동기: {motivation}"
    
    if company_values:
        context += f"\n기업 가치/문화: {company_values}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 자기소개서 구조 최적화",
        f"   - {company_name}의 자기소개서 형식 및 특성 분석",
        "   - 효과적인 자기소개서 구조 및 섹션 구성",
        "   - 분량 배분 및 우선순위 설정 전략",
        "   - 시선을 사로잡는 시작과 기억에 남는 마무리 기법",
        
        "2. 기업 맞춤형 내용 구성",
        f"   - {company_name}의 비전, 미션, 가치와 연결하는 자기소개서 작성법",
        f"   - {job_position} 직무에 필요한 핵심 역량 중심의 내용 구성",
        f"   - {background}를 {company_name}에 적합한 인재로 부각시키는 방법",
        f"   - {motivation}을 설득력 있게 표현하는 전략",
        
        "3. 차별화 및 진정성 강화 전략",
        "   - 다른 지원자들과 차별화되는 고유한 가치 제안(UVP) 개발",
        "   - 구체적인 사례와 경험을 통한 설득력 강화",
        "   - 진정성 있는 열정과 태도를 표현하는 방법",
        "   - 과장이나 클리셰 없이 자신만의 스토리 전달하기",
        
        "4. 표현 및 문체 최적화",
        "   - 기업 문화에 맞는 적절한 어조와 문체 선택",
        "   - 명확하고 간결한 문장 구성 전략",
        "   - 추상적 표현보다 구체적 표현 활용법",
        "   - 전문성과 성장 가능성을 보여주는 언어 선택"
    ]
    
    if company_values:
        instructions.append("5. 기업 가치 연결 전략")
        instructions.append(f"   - {company_values}와 같은 기업 가치를 자신의 경험과 연결하는 방법")
        instructions.append("   - 기업 문화 적합성(Culture Fit)을 보여주는 사례 선택 전략")
        instructions.append("   - 기업의 사회적 미션에 기여할 수 있는 방안 제시")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 자기소개서 전략적 접근법\n"
        "2. 기업 맞춤형 구조 및 내용 가이드\n"
        "3. 핵심 섹션별 작성 전략\n"
        "4. 차별화 및 진정성 강화 방법\n"
        "5. 맞춤형 자기소개서 템플릿 및 예시\n"
        "6. 최종 점검 체크리스트\n\n"
        f"{company_name}의 {job_position} 직무에 특화된 구체적인 예시와 표현을 포함해주세요. 실제 적용 가능한 템플릿과 차별화 전략에 중점을 두고 안내해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 자기소개서 최적화 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n자기소개서 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: cover_letter_optimization.md): ") or "cover_letter_optimization.md"
        save_markdown(enhanced_result, file_path, title=f"{company_name} {job_position} 자기소개서 최적화 가이드")
        print(f"자기소개서 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()