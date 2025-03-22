"""
전공별 맞춤형 리포트 작성

다양한 학문 분야별 최적화된 리포트 작성 도구
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
    print("===== 전공별 맞춤형 리포트 작성 =====")
    
    # 사용자 입력 받기
    topic = input("리포트 주제를 입력하세요: ")
    major_category = input("전공 계열을 선택하세요 (1: 인문사회계열, 2: 이공계열, 3: 예체능계열, 4: 경영/경제계열): ")
    specific_field = input("구체적인 전공 분야를 입력하세요: ")
    report_type = input("리포트 유형을 입력하세요 (예: 학술논문, 실험보고서, 작품분석, 사례연구): ")
    
    # 전공 계열에 따른 설정
    major_categories = {
        "1": "인문사회계열",
        "2": "이공계열",
        "3": "예체능계열",
        "4": "경영/경제계열"
    }
    
    major = major_categories.get(major_category, "학술")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{major} {specific_field} 분야에서 {topic}에 대한 {report_type}을 작성하는 방법을 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 전공별 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 전공별 특화 역할 및 지시사항 설정
    role_descriptions = {
        "1": f"{specific_field} 교수 및 학술 저널 편집자",
        "2": f"{specific_field} 연구원 및 실험 프로토콜 전문가",
        "3": f"{specific_field} 분야의 비평가 및 작품 분석 전문가",
        "4": f"{specific_field} 분야의 비즈니스 컨설턴트 및 사례 연구 전문가"
    }
    
    # 역할 설정
    prompt_builder.add_role(role_descriptions.get(major_category, "학술 전문가"), 
                           f"{specific_field} 분야에서 수년간의 교육, 연구, 출판 경험을 가진 전문가로서 학생들의 리포트 작성 지도에 풍부한 경험이 있습니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"주제: {topic}\n"
        f"전공 계열: {major}\n"
        f"구체적 분야: {specific_field}\n"
        f"리포트 유형: {report_type}"
    )
    
    # 전공별 특화 지시사항
    field_specific_instructions = {
        "1": [  # 인문사회계열
            f"1. {specific_field} 분야에서 {topic}의 학술적 중요성과 맥락",
            "2. 인문사회계열 특화 연구 방법론 및 적용 방법",
            "3. 비판적 사고와 다양한 관점 통합 전략",
            "4. 효과적인 논증 구성 및 근거 제시 방법"
        ],
        "2": [  # 이공계열
            f"1. {specific_field} 분야의 {report_type} 표준 구조와 요구사항",
            "2. 실험/연구 방법론 설명 및 데이터 표현 최적화",
            "3. 객관적이고 명확한 과학적 서술 방법",
            "4. 데이터 시각화 및 분석 방법"
        ],
        "3": [  # 예체능계열
            f"1. {specific_field} 분야에서 작품/현상 분석을 위한 이론적 프레임워크",
            "2. 시각적/청각적/체험적 요소의 효과적인 묘사 기법",
            "3. 미학적, 기술적 분석의 균형 있는 접근법",
            "4. 창의적 표현과 학술적 정확성의 조화"
        ],
        "4": [  # 경영/경제계열
            f"1. {specific_field} 분야의 사례/현상 분석 프레임워크",
            "2. 비즈니스 인사이트 도출 및 실용적 제안 전략",
            "3. 경제적/재무적 데이터 분석 및 표현 방법",
            "4. 전략적 사고와 실행 가능한 솔루션 제시 방법"
        ]
    }
    
    # 공통 지시사항
    common_instructions = [
        f"5. {major} {report_type}의 효과적인 구조와 형식",
        f"6. {specific_field} 분야의 전문 용어 및 개념 활용법",
        "7. 적합한 인용 스타일 및 참고문헌 관리",
        "8. 리포트 품질 향상을 위한 자기 검토 체크리스트",
        f"9. {major} 분야에서 우수한 {report_type} 예시와 특징",
        "10. 전공별 교수진이 중요시하는 평가 요소와 대응 전략"
    ]
    
    # 전공별 특화 지시사항과 공통 지시사항 결합
    specific_instructions = field_specific_instructions.get(major_category, [])
    all_instructions = specific_instructions + common_instructions
    
    # 지시사항 추가
    prompt_builder.add_instructions(all_instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "마크다운 형식으로 체계적이고 전공 특화된 리포트 작성 가이드를 제공해주세요. "
        f"{major} {specific_field} 분야의 특수성을 반영한 실용적인 조언과 구체적인 예시를 포함해주세요. "
        "각 섹션별 작성 요령, 구조적 특징, 표현 방식에 대한 명확한 가이드를 제공해주세요. "
        "학생들이 실제로 활용할 수 있는 템플릿과 체크리스트를 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 전공별 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n전공별 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: major_specific_guide.md): ") or "major_specific_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{specific_field} {topic} {report_type} 작성 가이드")
        print(f"전공별 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()