"""
연구 제안서 작성 프롬프트

효과적인 연구 제안서 작성을 위한 구조화된 프롬프트 기법
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
    print("===== 연구 제안서 작성 프롬프트 =====")
    
    # 사용자 입력 받기
    research_title = input("연구 제목을 입력하세요: ")
    field = input("학문 분야를 입력하세요: ")
    target_audience = input("제안서 대상(예: 교수, 연구비 지원 기관, 윤리 위원회)을 입력하세요: ")
    key_aims = input("주요 연구 목표를 입력하세요: ")
    proposal_length = input("제안서 길이 제한이 있다면 입력하세요: ")
    
    # 기본 프롬프트 - 간단한 버전
    basic_prompt = f"""
"{research_title}" 연구를 위한 제안서 작성 방법을 알려주세요.
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    print("\n기본 프롬프트 결과 생성 중...")
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 제안서 작성 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 구성
    prompt_builder = PromptBuilder()
    prompt_builder.add_role(
        f"{field} 연구 제안서 전문가", 
        f"{field} 분야에서 다수의 성공적인 연구비 지원 및 연구 승인을 받은 경험이 있는 시니어 연구자로, 연구 제안서 평가 위원으로도 활동하며 {target_audience}를 대상으로 한 제안서 작성에 정통합니다."
    )
    
    # 컨텍스트 추가
    context = f"""
연구 정보:
- 연구 제목: {research_title}
- 학문 분야: {field}
- 제안서 대상: {target_audience}
- 주요 연구 목표: {key_aims}
"""
    
    if proposal_length:
        context += f"- 제안서 길이 제한: {proposal_length}\n"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 효과적인 연구 제안서의 구조와 구성요소",
        f"   - {field} 분야의 제안서 표준 구조",
        f"   - {target_audience}가 중요시하는 요소 강조",
        "   - 각 섹션의 목적과 포함해야 할 핵심 내용",
        
        "2. 제안서 각 섹션별 작성 전략",
        "   - 매력적이고 명확한 제목과 초록 작성법",
        "   - 설득력 있는 연구 배경 및 중요성 서술 방법",
        "   - 명확한 연구 질문, 목표, 가설 제시 방법",
        "   - 체계적인 방법론 및 연구 설계 설명 전략",
        "   - 실현 가능한 일정 및 예산 계획 수립",
        "   - 예상 결과 및 영향 설명 기법",
        
        "3. 연구의 중요성 및 혁신성 강조 전략",
        "   - 학술적, 실용적 중요성 설득력 있게 표현하는 방법",
        "   - 기존 연구와의 차별점 및 혁신성 강조 기법",
        "   - 잠재적 영향 및 기여도 효과적으로 설명하는 전략",
        
        "4. 제안서 품질 향상 기법",
        "   - 명확하고 전문적인 언어 사용 전략",
        "   - 설득력 있는 논증 구조 구축 방법",
        "   - 시각적 요소(표, 그림 등) 효과적 활용법",
        "   - 편집 및 형식 최적화 전략"
    ]
    
    if proposal_length:
        instructions.append(
            "5. 제한된 길이 내 효과적인 내용 압축 전략",
            f"   - {proposal_length} 제한 내에서 핵심 내용 포함 방법",
            "   - 간결하면서도 충분한 정보 제공 기법",
            "   - 우선순위 설정 및 내용 최적화 전략"
        )
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    output_format = f"""
다음 형식으로 응답해주세요:

1. **연구 제안서 성공 요소**: {target_audience}에게 효과적인 제안서의 핵심 특성

2. **제안서 구조 및 섹션 가이드**:
   - 제목 및 초록
   - 연구 배경 및 중요성
   - 연구 질문 및 목표
   - 방법론 및 연구 설계
   - 일정 및 자원 계획
   - 예상 결과 및 영향
   - 참고문헌
   - 부록(해당되는 경우)

3. **"{research_title}" 연구 제안서 템플릿**:
   ```markdown
   # 제안서 템플릿 (주요 섹션과 내용 포함)
   ```

4. **섹션별 작성 전략 및 팁**:
   - 각 섹션별 구체적인 작성 가이드
   - 효과적인 표현 방법과 예시
   - 피해야 할 일반적인 실수

5. **설득력 강화 전략**:
   - 중요성 및 혁신성 강조 방법
   - 학술적/실용적 가치 표현 기법
   - 제안서 평가자 관점에서의 핵심 고려사항
"""
    
    if proposal_length:
        output_format += f"""
6. **{proposal_length} 제한 내 최적화 전략**:
   - 간결성과 완전성의 균형 유지법
   - 우선순위 설정 방법
   - 효과적인 내용 압축 기법
"""
    
    output_format += """
마크다운 형식으로 체계적인 연구 제안서 작성 가이드와 실제 적용 가능한 템플릿을 제공해주세요.
"""
    
    prompt_builder.add_format_instructions(output_format)
    
    # 최종 프롬프트 생성
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    print("\n향상된 프롬프트 결과 생성 중...")
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 제안서 작성 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n제안서 작성 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: research_proposal_guide.md): ") or "research_proposal_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{research_title} 연구 제안서 작성 가이드")
        print(f"제안서 작성 가이드가 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    main()