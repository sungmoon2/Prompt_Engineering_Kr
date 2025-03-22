"""
프로젝트 설명 작성법

포트폴리오에 포함할 프로젝트를 효과적으로 소개하고 설명하는 방법
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
    print("===== 프로젝트 설명 작성법 =====")
    
    # 사용자 입력 받기
    project_type = input("프로젝트 유형을 입력하세요 (예: 웹사이트, 앱, 디자인, 연구): ")
    field = input("전문 분야를 입력하세요: ")
    role = input("프로젝트에서 본인의 역할을 입력하세요: ")
    key_features = input("프로젝트의 주요 특징/성과를 입력하세요: ")
    target_position = input("이 프로젝트로 어필하고자 하는 직무를 입력하세요: ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
포트폴리오에 들어갈 {project_type} 프로젝트를 어떻게 설명하면 좋을까?
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 프로젝트 설명 가이드 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    prompt_builder.add_role(f"{field} 포트폴리오 전문가", 
                           f"다양한 {field} 분야 전문가들의 포트폴리오를 검토하고 컨설팅해온 경험이 있으며, 채용 담당자들이 프로젝트 설명에서 중요하게 보는 요소들을 깊이 이해하고 있는 전문가입니다.")
    
    # 맥락 제공
    prompt_builder.add_context(
        f"프로젝트 유형: {project_type}\n"
        f"전문 분야: {field}\n"
        f"담당 역할: {role}\n"
        f"주요 특징/성과: {key_features}\n"
        f"목표 직무: {target_position}"
    )
    
    # 지시사항 추가
    prompt_builder.add_instructions([
        "1. 프로젝트 설명 구조 최적화",
        f"   - {project_type} 프로젝트에 최적화된 설명 구조 및 포맷",
        "   - 주의를 끄는 제목과 간결한 요약문 작성법",
        "   - 시각적 요소와 텍스트의 효과적인 조합",
        "   - 가독성과 스캔 가능성을 고려한 정보 구성",
        
        "2. 핵심 내용 요소",
        "   - 프로젝트 배경 및 목적 설명 전략",
        "   - 문제 정의와 해결 과정 서술 방법",
        f"   - {role}과 같은 본인의 역할과 기여도 강조 전략",
        f"   - {key_features}와 같은 주요 특징과 성과의 효과적인 제시",
        
        "3. 기술적 깊이와 비즈니스 가치 균형",
        f"   - {field} 분야의 전문성을 보여주는 기술적 세부사항 제시 수준",
        "   - 비즈니스 및 사용자 가치 강조 방법",
        "   - 전문용어와 일반적 설명의 적절한 균형",
        f"   - {target_position} 직무와 관련된 역량 강조 전략",
        
        "4. 스토리텔링 접근법",
        "   - 몰입감 있는 프로젝트 내러티브 구성 방법",
        "   - 도전 과제와 극복 과정을 흥미롭게 전달하는 기법",
        "   - 학습 및 성장 과정을 보여주는 효과적인 서술 방식",
        "   - 진정성과 전문성을 동시에 전달하는 어조와 표현",
        
        "5. 결과 및 영향력 제시",
        "   - 정량적/정성적 결과의 효과적인 제시 방법",
        "   - 사용자 피드백 및 평가 활용 전략",
        "   - 프로젝트의 장기적 영향 및 지속가능성 설명",
        "   - 학습된 교훈 및 향후 개선 방향 공유 접근법"
    ])
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 효과적인 프로젝트 설명의 핵심 원칙\n"
        "2. 프로젝트 설명 구조 및 템플릿\n"
        "3. 주요 내용 요소별 작성 가이드\n"
        "4. 임팩트 있는 사례와 표현 예시\n"
        "5. 흔한 실수와 개선 방법\n"
        "6. 프로젝트 유형별 맞춤 접근법\n\n"
        f"{project_type} 프로젝트 유형에 특화된 구체적인 작성 예시와 {target_position} 직무에 효과적인 어필 전략을 포함해주세요. 실제 포트폴리오에 바로 적용할 수 있는 템플릿과 구체적인 문구 예시를 제공해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 프로젝트 설명 가이드 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n프로젝트 설명 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: project_description_guide.md): ") or "project_description_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{project_type} 프로젝트 설명 작성 가이드")
        print(f"프로젝트 설명 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()