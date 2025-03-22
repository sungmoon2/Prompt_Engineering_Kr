"""
자기소개서 실적 부분 작성 전략

성과와 역량을 효과적으로 전달하는 자기소개서 실적 작성법
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
    print("===== 자기소개서 실적 부분 작성 전략 =====")
    
    # 사용자 입력 받기
    achievement_type = input("작성할 실적 유형을 입력하세요 (예: 학업성취, 프로젝트, 직무경험, 수상경력): ")
    target_position = input("지원하는 직무/포지션을 입력하세요: ")
    achievement_detail = input("실적에 대한 간략한 설명을 입력하세요: ")
    company_values = input("지원 기업/조직의 핵심 가치나 문화가 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{achievement_type} 관련 자기소개서 실적을 어떻게 작성하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 실적 작성 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("취업 전략 및 자기소개서 작성 전문가", 
                           "주요 기업의 채용 과정을 분석하고 수많은 지원자들의 자기소개서 작성을 코칭해온 경력을 가진 전문가입니다.")
    
    # 맥락 제공
    context = f"실적 유형: {achievement_type}\n" \
             f"지원 직무: {target_position}\n" \
             f"실적 내용: {achievement_detail}"
    
    if company_values:
        context += f"\n기업/조직 가치: {company_values}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        f"1. {achievement_type} 유형의 실적을 효과적으로 구조화하는 방법",
        "   - STAR 기법 또는 다른 효과적인 프레임워크 적용 방법",
        "   - 명확한 성과 중심 서술 전략",
        "   - 실적의 맥락, 과정, 결과를 균형있게 표현하는 방법",
        
        f"2. {target_position} 직무와 실적의 연관성 강화 전략",
        "   - 직무 관련 핵심 역량 강조 방법",
        "   - 직무 적합성을 드러내는 키워드와 표현",
        "   - 실적을 통해 직무 적합성 입증하는 논리적 연결",
        
        "3. 객관적 증명과 정량적 표현 기법",
        "   - 구체적인 수치와 성과 지표 활용법",
        "   - 모호한 표현을 구체적 증거로 대체하는 방법",
        "   - 신뢰성을 높이는 표현 기법",
        
        "4. 개인 역량과 기여도 부각 전략",
        "   - 팀 성과에서 개인 기여 명확히 하는 방법",
        "   - 직무 관련 강점과 역량 연결짓기",
        "   - 문제 해결 능력과 성장 스토리 통합 방법"
    ]
    
    if company_values:
        instructions.append(f"5. {company_values} 가치와 실적 연계 방법")
        instructions.append("   - 조직 가치와 개인 실적의 연결점 강조")
        instructions.append("   - 문화적 적합성 드러내는 표현 전략")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = """
다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:

1. **효과적인 실적 서술 구조 및 프레임워크**
   - 이상적인 구성과 흐름
   - 주요 포함 요소

2. **직무 연관성 강화 전략**
   - 핵심 역량 연결 방법
   - 관련 키워드 및 표현

3. **구체적 작성 예시**
   - 제공된 실적을 활용한 작성 예시
   - 좋은 예시/나쁜 예시 비교

4. **실적 서술 체크리스트**
   - 작성 완료 후 점검 사항
   - 개선을 위한 질문들

5. **맞춤형 작성 전략**
   - 제공된 실적 유형에 특화된 조언
   - 지원 직무/기업에 최적화하는 방법

구체적이고 실용적인 조언과 함께 실제 적용 가능한 예시와 템플릿을 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 실적 작성 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n실적 작성 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: achievement_guide.md): ") or "achievement_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{achievement_type} 실적 작성 가이드")
        print(f"실적 작성 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()