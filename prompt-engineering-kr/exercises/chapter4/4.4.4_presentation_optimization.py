"""
발표 최적화

공모전 제안서 발표를 위한 효과적인 피칭 전략과 시각 자료 최적화 기법
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
    print("===== 발표 최적화 =====")
    
    # 사용자 입력 받기
    presentation_topic = input("발표 주제/프로젝트명을 입력하세요: ")
    presentation_format = input("발표 형식과 제한 시간을 입력하세요 (예: 5분 피칭, 15분 프레젠테이션): ")
    key_points = input("전달하고자 하는 핵심 포인트를 입력하세요 (쉼표로 구분): ")
    audience = input("청중/심사위원의 특성을 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
{presentation_topic}에 대한 {presentation_format} 발표를 어떻게 준비하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 발표 최적화 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role("프레젠테이션 및 피칭 전문가", 
                           "TED 스타일의 발표와 스타트업 피칭 코칭 경험이 풍부한 전문가로, 제한된 시간 내에 청중을 사로잡고 핵심 메시지를 효과적으로 전달하는 전략을 제공합니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"발표 주제: {presentation_topic}\n"
        f"발표 형식: {presentation_format}\n"
        f"핵심 포인트: {key_points}\n"
        f"청중/심사위원: {audience}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 발표 구조 최적화 전략",
        f"   - {presentation_format}에 최적화된 발표 구조와 시간 배분",
        "   - 강력한 시작과 기억에 남는 마무리 설계",
        "   - 핵심 메시지를 명확히 전달하는 논리적 흐름 구성",
        
        "2. 시각 자료 디자인 및 활용 전략",
        "   - 효과적인 슬라이드 구성 및 디자인 원칙",
        "   - 텍스트와 시각 요소의 최적 균형 설계",
        "   - 데이터 시각화와 스토리텔링의 통합 방법",
        
        "3. 발표 전달 및 퍼포먼스 최적화",
        "   - 목소리, 자세, 제스처 등 비언어적 요소 활용법",
        "   - 청중과의 상호작용 및 연결 구축 전략",
        "   - 자신감 있고 설득력 있는 발표 기법",
        
        "4. 시간 제약 극복 및 핵심 메시지 강조",
        f"   - {presentation_format} 내에서 {key_points}를 효과적으로 전달하는 방법",
        "   - 복잡한 개념을 간결하게 설명하는 기법",
        "   - 시간 효율성을 높이는 발표 연습 전략",
        
        f"5. {audience} 맞춤형 설득 전략",
        "   - 청중/심사위원의 관심사와 기대에 부합하는 접근법",
        "   - 잠재적 질문과 이의에 대한 준비 및 대응 방법",
        "   - 제안의 가치와 차별성을 효과적으로 부각시키는 방법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 발표 구조 및 시간 배분 전략\n"
        "2. 시각 자료 최적화 가이드\n"
        "3. 발표 전달 및 퍼포먼스 기법\n"
        "4. 핵심 메시지 강조 전략\n"
        "5. Q&A 대비 및 설득 전략\n"
        "6. 발표 준비 체크리스트\n\n"
        f"{presentation_topic}에 대한 {presentation_format} 발표를 위한 구체적인 전략과 실용적인 팁을 제공해주세요. 발표 전, 중, 후 단계별 최적화 방법을 포함해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 발표 최적화 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n발표 최적화 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: presentation_optimization.md): ") or "presentation_optimization.md"
        save_markdown(enhanced_result, file_path, title=f"{presentation_topic} 발표 최적화 가이드")
        print(f"발표 최적화 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()