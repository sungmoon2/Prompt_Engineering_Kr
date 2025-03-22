"""
프로그래밍 스타일 향상 가이드

코드 가독성, 일관성, 유지보수성을 위한 스타일 개선 및 코딩 표준 적용 기법
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
    print("===== 프로그래밍 스타일 향상 가이드 =====")
    
    # 사용자 입력 받기
    code = input("스타일 개선이 필요한 코드를 입력하세요: ")
    language = input("프로그래밍 언어를 입력하세요: ")
    style_guide = input("적용하고 싶은 스타일 가이드나 코딩 표준을 입력하세요 (예: PEP8, Google Style Guide): ")
    team_context = input("팀/프로젝트 맥락이 있다면 입력하세요: ")
    experience_level = input("프로그래밍 경험 수준을 입력하세요 (초급/중급/고급): ")
    
    # 기본 프롬프트 - 매우 단순하고 빈약한 버전
    basic_prompt = f"""
이 코드의 스타일을 더 좋게 개선해줘:

```{language}
{code}
```
"""
    
    print("\n===== 기본 프롬프트 =====")
    print(basic_prompt)
    
    # 기본 프롬프트 실행
    basic_result = get_completion(basic_prompt, temperature=0.7)
    
    print("\n===== 기본 스타일 개선 결과 =====")
    print(basic_result)
    
    print("\n" + "-"*60)
    
    # 향상된 프롬프트 - PromptBuilder 활용
    prompt_builder = PromptBuilder()
    
    # 역할 설정
    style_guide_desc = style_guide if style_guide else f"{language} 모범 사례"
    prompt_builder.add_role("코드 품질 및 스타일 컨설턴트", 
                          f"{language} 코드베이스의 가독성, 일관성, 유지보수성을 향상시키는 전문가로, {style_guide_desc}에 정통하며 다양한 규모의 프로젝트에서 코드 품질 개선을 지원한 경험이 있습니다.")
    
    # 맥락 제공
    context = f"대상 코드:\n```{language}\n{code}\n```\n\n" \
             f"프로그래밍 언어: {language}\n" \
             f"프로그래밍 경험: {experience_level}"
    
    if style_guide:
        context += f"\n적용 스타일 가이드: {style_guide}"
    
    if team_context:
        context += f"\n팀/프로젝트 맥락: {team_context}"
    
    prompt_builder.add_context(context)
    
    # 지시사항 추가
    instructions = [
        "1. 스타일 분석 및 평가",
        "   - 현재 코드의 스타일 특성 및 패턴 식별",
        "   - 스타일 가이드/표준 준수 여부 평가",
        "   - 주요 스타일 이슈 및 개선 영역 식별",
        
        "2. 스타일 개선 권장사항",
        f"   - {language} 언어 특화 스타일 모범 사례 적용",
        f"   - {style_guide if style_guide else '업계 표준'} 기반 코딩 표준 적용",
        "   - 명명 규칙, 들여쓰기, 주석 등 개선 방향 제안",
        
        "3. 개선된 코드 제공",
        "   - 명확한 설명과 함께 리팩토링된 코드 제공",
        "   - 변경 사항을 명확히 강조하여 표시",
        "   - 일관된 스타일 적용 및 유지 방법 설명",
        
        "4. 스타일 유지 전략"
    ]
    
    if experience_level.lower() in ["초급", "beginner"]:
        instructions.append(f"   - {language} 스타일 가이드 이해를 위한 학습 자료 추천")
    
    instructions.extend([
        "   - 자동화 도구 및 린터 설정 가이드",
        "   - 코드 리뷰 체크리스트 및 모범 사례",
        "   - 지속적인 스타일 유지를 위한 팀 전략"
    ])
    
    prompt_builder.add_instructions(instructions)
    
    # 출력 형식 지정
    prompt_builder.add_format_instructions(
        "다음 섹션들을 포함하여 마크다운 형식으로 응답해주세요:\n"
        "1. 스타일 분석 및 개선 필요 영역\n"
        "2. 스타일 가이드 적용 전략\n"
        "3. 개선된 코드 (변경 사항 강조)\n"
        "4. 주요 스타일 규칙 설명\n"
        "5. 스타일 유지 및 자동화 도구 설정\n\n"
        f"코드 블록은 {language} 문법 하이라이팅을 사용하고, 변경된 부분을 명확히 식별할 수 있게 해주세요. {experience_level} 수준의 개발자가 이해하기 쉽도록 설명의 깊이와 기술적 상세함을 조정해주세요. 가능한 경우 스타일 향상이 가독성과 유지보수성에 미치는 긍정적 영향을 설명해주세요."
    )
    
    # 프롬프트 빌드
    enhanced_prompt = prompt_builder.build()
    
    print("\n===== 향상된 프롬프트 =====")
    print(enhanced_prompt)
    
    # 향상된 프롬프트 실행
    enhanced_result = get_completion(enhanced_prompt, temperature=0.5)
    
    print("\n===== 향상된 스타일 개선 결과 =====")
    print(enhanced_result)
    
    # 결과 저장 (선택 사항)
    save = input("\n스타일 가이드를 파일로 저장하시겠습니까? (y/n): ")
    if save.lower() == 'y':
        file_path = input("저장할 파일명을 입력하세요 (기본: style_guide.md): ") or "style_guide.md"
        save_markdown(enhanced_result, file_path, title=f"{language} 코드 스타일 향상 가이드")
        print(f"스타일 가이드가 {file_path}에 저장되었습니다.")


if __name__ == "__main__":
    main()