"""
예체능계 작품 분석 및 설명 최적화

예술, 음악, 무용, 디자인 등 예체능 분야의 작품 분석 및 설명을 위한 프롬프트
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
    print("===== 예체능계 작품 분석 및 설명 최적화 =====")
    
    # 사용자 입력 받기
    artwork_type = input("작품 유형을 입력하세요 (예: 회화, 조각, 음악, 무용, 영화, 디자인): ")
    specific_work = input("분석할 특정 작품이나 주제를 입력하세요: ")
    arts_field = input("구체적인 예체능 분야를 입력하세요 (예: 미술사, 음악이론, 영화평론, 공연예술학): ")
    analysis_purpose = input("분석 목적을 입력하세요 (예: 학술 논문, 비평문, 작품 해설, 포트폴리오): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{arts_field} 분야에서 {specific_work} {artwork_type}을(를) 분석하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 예체능 분석 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{arts_field} 전문 비평가 및 교수", 
                          f"유명 예술 기관과 대학에서 {artwork_type} 분석 및 비평을 수행하고 가르쳐온 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"작품 유형: {artwork_type}\n"
        f"분석 대상: {specific_work}\n"
        f"학문 분야: {arts_field} (예체능계)\n"
        f"분석 목적: {analysis_purpose}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        f"1. {artwork_type} 작품 분석을 위한 이론적 프레임워크와 접근 방식",
        f"2. {arts_field} 분야에서 작품 분석의 주요 구성요소와 고려사항",
        f"3. {specific_work}와 같은 {artwork_type}의 형식적 요소 분석 방법 (구조, 형태, 기법 등)",
        "4. 내용적 요소 분석 방법 (주제, 메시지, 의미, 상징 등)",
        "5. 맥락적 요소 분석 방법 (역사적, 사회적, 문화적 배경)",
        "6. 작품의 미학적, 기술적 특성을 효과적으로 설명하는 언어와 표현",
        f"7. {artwork_type} 분석에 특화된 전문 용어와 개념의 적절한 활용법",
        f"8. {analysis_purpose}에 적합한 분석 구조와 서술 방식",
        "9. 시각적/청각적 요소 설명을 위한 묘사 기법과 비유적 표현",
        "10. 주관적 해석과 객관적 분석의 균형 유지 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 체계적이고 통찰력 있는 분석 가이드를 제공해주세요. "
        "구체적인 분석 예시와 실제 적용 가능한 템플릿 문구를 포함해주세요. "
        f"{artwork_type} 작품의 특성을 효과적으로 설명하는 표현 기법과 예시를 포함해주세요. "
        "필요한 경우 섹션별로 체크리스트와 핵심 질문을 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 예체능 분석 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n예체능 분석 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: arts_analysis_guide.md): ") or "arts_analysis_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{specific_work} {artwork_type} 분석 가이드")
        print(f"예체능 분석 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()