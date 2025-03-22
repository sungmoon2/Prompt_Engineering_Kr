"""
경력 계획 및 로드맵 수립 전략

체계적인 경력 개발 계획과 장기적 성장을 위한 로드맵 작성법
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
    print("===== 경력 계획 및 로드맵 수립 전략 =====")
    
    # 사용자 입력 받기
    current_status = input("현재 경력 상태를 입력하세요 (예: 대학생, 신입, 주니어 개발자): ")
    target_field = input("목표 분야/직무를 입력하세요: ")
    timeframe = input("목표 달성을 위한 기간을 입력하세요 (예: 1년, 3년, 5년): ")
    key_skills = input("개발하고 싶은 주요 역량/기술을 입력하세요 (쉼표로 구분): ")
    challenges = input("예상되는 도전 요소나 장애물이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
{current_status}에서 {target_field} 분야로 {timeframe} 내에 경력을 발전시키기 위한 계획을 세워주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 경력 계획 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("경력 개발 및 진로 컨설턴트", 
                           "다양한 분야의 전문가들의 경력 계획을 수립하고 코칭해온 경험이 풍부한 커리어 전략가로, 개인 맞춤형 경력 로드맵 설계에 전문성을 가지고 있습니다.")
    
    # 맥락 제공
    context = f"현재 상태: {current_status}\n" \
             f"목표 분야/직무: {target_field}\n" \
             f"목표 기간: {timeframe}\n" \
             f"개발 희망 역량: {key_skills}"
    
    if challenges:
        context += f"\n예상 도전 요소: {challenges}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 현재 상황 및 목표 분석",
        "   - 현재 상태에서의 강점과 개발 영역 평가",
        "   - 목표 분야/직무의 핵심 요구사항 및 트렌드 분석",
        "   - 현재 상태와 목표 간의 격차 식별",
        
        "2. 단계별 경력 발전 경로 수립",
        f"   - {timeframe} 내 달성 가능한 현실적 마일스톤 설정",
        "   - 단기, 중기, 장기 목표 세분화",
        "   - 필요한 경력 전환점 및 이정표 제안",
        
        "3. 역량 개발 계획",
        "   - 필수 기술/역량 우선순위화",
        "   - 역량별 구체적 개발 방법 및 자원 제안",
        "   - 실무 경험과 학습의 균형 전략",
        
        "4. 네트워킹 및 가시성 향상 전략",
        "   - 효과적인 네트워크 구축 방법",
        "   - 전문성 표현 및 브랜딩 전략",
        "   - 업계 참여 및 기여 기회 탐색"
    ]
    
    if challenges:
        instructions.append("5. 도전 요소 극복 전략")
        instructions.append("   - 예상되는 장애물별 대응 방안")
        instructions.append("   - 회복탄력성 유지 및 적응 전략")
    
    instructions.append(f"{'6' if challenges else '5'}. 진행 상황 평가 및 계획 조정 방법")
    instructions.append(f"   - 정기적 자기 평가 프레임워크")
    instructions.append(f"   - 유연한 계획 조정 및 피드백 반영 방법")
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = """
다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:

1. **현황 및 목표 분석**
   - 현재 상태 평가
   - 목표 분야/직무 요구사항
   - 격차 분석

2. **경력 로드맵**
   - 단계별 마일스톤
   - 주요 경력 전환점
   - 시간 프레임별 목표 (단기/중기/장기)

3. **역량 개발 계획**
   - 우선순위 역량 및 학습 경로
   - 추천 학습 자원 및 활동
   - 실무 경험 획득 전략

4. **네트워킹 및 전문성 개발**
   - 핵심 네트워킹 전략
   - 전문성 구축 및 표현 방법
   - 업계 참여 기회

5. **실행 계획 및 점검 체계**
   - 구체적 실행 일정표
   - 진행 상황 측정 방법
   - 계획 조정 및 피드백 통합 방법
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 경력 계획 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n경력 계획을 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: career_roadmap.md): ") or "career_roadmap.md"
        save_markdown(enhanced_result, file_path, title=f"{target_field} 경력 로드맵")
        print(f"경력 계획이 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()