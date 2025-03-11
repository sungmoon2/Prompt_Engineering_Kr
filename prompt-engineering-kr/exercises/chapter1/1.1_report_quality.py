"""
1.1 리포트 품질 향상 기법 - 학업 보고서 작성 최적화 실습

이 실습은 기본적인 보고서 작성 프롬프트와 향상된 프롬프트의 차이를 보여줍니다.
"""

from utils.api_utils import generate_text
from utils.prompt_utils import format_prompt

# 실습 주제: 인공지능의 교육적 활용에 관한 학술 보고서 작성

# 1. 기본 프롬프트 (부실한 프롬프트)
basic_prompt = """
인공지능의 교육적 활용에 대한 보고서를 작성해주세요.
"""

# 2. 향상된 프롬프트 (구조화, 구체적 지시, 평가 기준 포함)
enhanced_prompt = """
당신은 교육공학 전문가입니다. 대학원 수준의 학술 보고서를 작성해주세요.

주제: 인공지능 기술의 교육적 활용과 그 영향

다음 구조를 따라 작성해주세요:
1. 서론 (배경, 중요성, 연구 질문)
2. 이론적 배경 (AI 교육 도구의 발전과 현황)
3. 적용 사례 분석 (최소 3가지 구체적 사례)
4. 효과 및 한계점 (긍정적/부정적 측면 모두 포함)
5. 미래 방향 및 제언
6. 결론

요구사항:
- 학술적 문체와 용어 사용
- 최신 연구(2020년 이후)를 포함한 참고문헌 최소 5개 인용
- 각 섹션에서 제시된 주장에 대한 근거 포함
- 총 2000단어 내외로 작성
- 교육 평등성, 접근성, 윤리적 측면을 반드시 다룰 것

평가 기준:
- 내용의 깊이와一관련성
- 논리적 구성과 흐름
- 근거 기반 논증
- 비판적 분석력
"""

# 3. 두 프롬프트 실행 및 결과 비교
print("\n===== 기본 프롬프트와 향상된 프롬프트 비교 =====\n")
print(f"기본 프롬프트 글자 수: {len(basic_prompt)}")
print(f"향상된 프롬프트 글자 수: {len(enhanced_prompt)}")

# 기본 프롬프트 실행
print("\n----- 기본 프롬프트 실행 중... -----")
basic_result = generate_text(basic_prompt)

# 향상된 프롬프트 실행
print("\n----- 향상된 프롬프트 실행 중... -----")
enhanced_result = generate_text(enhanced_prompt)

# 4. 결과 비교 및 출력
print("\n===== 결과 비교 =====\n")

# 기본 프롬프트 결과 미리보기 (처음 300자)
print("----- 기본 프롬프트 결과 (일부) -----")
print(basic_result[:300] + "...\n")
print(f"총 글자 수: {len(basic_result)}")
print(f"구조화된 섹션 수: {basic_result.count('#') + basic_result.count('##')}")

# 향상된 프롬프트 결과 미리보기 (처음 300자)
print("\n----- 향상된 프롬프트 결과 (일부) -----")
print(enhanced_result[:300] + "...\n")
print(f"총 글자 수: {len(enhanced_result)}")
print(f"구조화된 섹션 수: {enhanced_result.count('#') + enhanced_result.count('##')}")

# 5. 간단한 분석
print("\n===== 분석 =====")
print(f"글자 수 증가율: {(len(enhanced_result) / len(basic_result) * 100 - 100):.1f}%")
print(f"구조화 개선율: {(enhanced_result.count('#') - basic_result.count('#')) / max(1, basic_result.count('#')) * 100:.1f}%")
