"""
연구 주제 구체화 프롬프트

광범위한 관심사에서 구체적인 연구 주제로 좁혀나가는 프롬프트 기법
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.example_provider import get_sample_research_topics

def main():
    """
    실습 코드 메인 함수
    """
    print("===== 연구 주제 구체화 프롬프트 =====")
    
    # 사용자 입력 받기
    broad_topic = input("관심 있는 광범위한 주제 영역을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    interest_aspects = input("특별히 관심 있는 측면이나 요소가 있다면 입력하세요: ")
    academic_level = input("학술 수준을 입력하세요 (예: 학부 논문, 석사 논문, 박사 논문): ")
    
    # 샘플 연구 주제 예시 제공 (선택 사항)
    print("\n참고할 수 있는 샘플 연구 주제:")
    sample_topics = get_sample_research_topics()
    for i, topic in enumerate(sample_topics[:5], 1):
        print(f"{i}. {topic}")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{broad_topic}에 관한 구체적인 연구 주제를 제안해주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 주제 구체화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 연구 방법론 전문가 및 지도교수", 
        f"{field} 분야에서 다양한 수준의 연구를 지도한 경험이 풍부한 학자로, 광범위한 관심사에서 연구할 만한 가치가 있는 구체적인 주제를 도출하는 데 전문성을 갖고 있습니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 관심사 정보:
- 광범위한 주제 영역: {broad_topic}
- 학문 분야: {field}
- 특별 관심 측면: {interest_aspects if interest_aspects else '특별히 명시되지 않음'}
- 학술 수준: {academic_level}
"""
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 주제 영역 분석 및 세분화",
        f"   - {broad_topic}의 주요 하위 영역 및 현재 연구 동향 파악",
        f"   - {field} 분야에서 {broad_topic}과 관련된 연구 격차 식별",
        "   - 연구 가능성과 학술적 중요성 기준으로 하위 영역 평가",
        
        "2. 구체적인 연구 주제 후보 도출",
        f"   - {academic_level} 수준에 적합한 5-7개의 구체적 연구 주제 제안",
        "   - 각 주제의 핵심 연구 질문 및 잠재적 가설 제시",
        "   - 주제별 독창성과 학술적 기여도 평가",
        
        "3. 주제 구체화 및 범위 설정 전략",
        "   - 시간적, 공간적, 개념적 범위 설정 방법 제안",
        "   - 측정 가능하고 실행 가능한 연구 질문으로 변환하는 기법",
        "   - 연구 주제의 명확한 경계 설정 전략",
        
        "4. 연구 가능성 및 실행 분석",
        f"   - {academic_level} 수준에서의 자원과 시간 제약 고려",
        "   - 데이터 접근성 및 연구 방법론 적용 가능성 평가",
        "   - 잠재적 장애물 및 해결 전략"
    ]
    
    if interest_aspects:
        instructions.append(
            "5. 관심 측면 중심의 주제 발전",
            f"   - {interest_aspects}와 관련된 특화된 연구 가능성 탐색",
            f"   - {interest_aspects}를 중심으로 한 독창적 접근법 제안",
            "   - 개인적 관심과 학술적 가치의 균형 전략"
        )
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **주제 영역 분석**: {broad_topic}의 현재 연구 동향 및 하위 영역 분석

2. **구체적 연구 주제 후보**:
   - 주제 1: [제목]
     - 핵심 연구 질문
     - 학술적 중요성
     - 연구 가능성
   - 주제 2: [제목]
     ...
   (총 5-7개 주제)

3. **우선 추천 주제 심층 분석**:
   - 연구 질문 정제 방법
   - 범위 설정 전략
   - 방법론적 접근 제안
   - 예상되는 학술적 기여

4. **주제 구체화 단계별 접근법**:
   - 관심 영역에서 구체적 주제로 발전시키는 체계적 절차
   - 효과적인 연구 질문 형성 프레임워크
   - 주제 평가 기준

마크다운 형식으로 체계적인 주제 구체화 가이드와 실제 적용 가능한 예시를 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 주제 구체화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n주제 구체화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: topic_refinement_guide.md): ") or "topic_refinement_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{broad_topic} 연구 주제 구체화 가이드")
        print(f"주제 구체화 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()