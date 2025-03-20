"""
주제 분석 및 논점 도출을 위한 프롬프트

학술 리포트의 기초가 되는 주제 분석과 핵심 논점 도출을 위한 프롬프트 엔지니어링 기법
"""

import os
import sys

# 상위 디렉토리 추가하여 utils 모듈 import 가능하게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.file_handler import save_markdown

def main():
    # 사용자 입력
    topic = input("분석할 주제를 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{topic}에 대해 알려줘.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 분석 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트
    enhanced_prompt = f"""
당신은 {field} 분야의 저명한 학자로, 30년 이상의 연구 경력을 가지고 있습니다.

다음 주제에 대해 심층적인 학술 분석을 제공해주세요:

주제: {topic}
학문 분야: {field}
목적: 대학원 수준의 학술 리포트 작성

다음 내용을 포함해주세요:
1. 주제의 학술적 중요성과 현재의 연구 동향
2. 이 주제에 대한 주요 이론적 패러다임과 접근 방식
3. 핵심 논점 5가지와 각각의 학문적 의의 및 논쟁점
4. 각 논점에 대한 상반된 학파들의 관점
5. 이 주제 연구에 적합한 방법론적 접근법들
6. 필수 참고문헌 5-7개와 각 문헌의 주요 기여
7. 연구 시 주의해야 할 방법론적, 윤리적 고려사항

마크다운 형식으로 구조화된 응답을 제공해주세요.
"""
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 분석 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n분석 결과를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: topic_analysis.md): ") or "topic_analysis.md"
        save_markdown(enhanced_result, file_path, title=f"{topic} 분석")
        print(f"분석 결과가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()