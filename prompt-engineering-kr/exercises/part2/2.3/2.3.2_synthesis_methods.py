"""
통합적 결론 도출하기 실습 모듈

Part 2 - 섹션 2.3.2 실습 코드: 다양한 관점과 정보를 종합하여 일관성 있는 결론을 도출하는 방법을 학습합니다.
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(project_root)

from utils.prompt_builder import PromptBuilder
from utils.exercise_template import run_exercise

# 주제 옵션 정의
CONCLUSION_TOPICS = {
    "1": {"name": "사회 이슈", "topic": "소셜 미디어가 청소년 정신 건강에 미치는 영향", "output_format": "통합적 분석"},
    "2": {"name": "기술 평가", "topic": "자율주행차의 사회적, 경제적, 윤리적 영향", "output_format": "영향 평가 보고서"},
    "3": {"name": "정책 분석", "topic": "기본소득 정책의 실현 가능성과 예상 효과", "output_format": "정책 분석 보고서"},
    "4": {"name": "윤리적 딜레마", "topic": "인공지능의 의사결정 과정에서 발생하는 윤리적 문제", "output_format": "윤리적 분석"},
    "5": {"name": "학술 논쟁", "topic": "기후변화 대응 전략에 관한 다양한 관점", "output_format": "종합 리뷰"},
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 결론 요청"],
    "enhanced": [
        "다양한 관점 인정: 상충되는 견해 포함",
        "증거 기반 평가: 각 관점의 근거 검토 요청",
        "결론 구조화: 체계적인 결론 도출 방식 제시"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "통합적 결론은 단일 관점이 아닌 여러 관점을 포괄하는 균형 잡힌 시각을 제공합니다",
    "증거의 질과 관련성을 평가하여 각 관점의 타당성을 판단하는 것이 중요합니다",
    "상충되는 관점들 사이의 합리적 중간점을 찾거나 맥락에 따른 조건부 결론을 도출할 수 있습니다",
    "통합적 결론은 복잡한 문제의 다양한 측면을 포괄하여 더 풍부한 이해를 제공합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대한 결론을 도출해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "통합적 분석 전문가", 
        "복잡한 주제에 대한 다양한 관점과 증거를 분석하여 균형 잡힌 결론을 도출하는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관한 연구 보고서를 작성 중인 대학생입니다. "
        f"다양한 자료를 수집했지만, 상충되는 관점들이 많아 일관성 있는 결론을 도출하기 어렵습니다. "
        f"다양한 관점을 존중하면서도 증거에 기반한 통합적 결론을 도출하는 방법을 알고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "소셜 미디어" in topic:
        builder.add_instructions([
            "소셜 미디어가 청소년 정신 건강에 미치는 긍정적 영향과 부정적 영향을 균형 있게 제시해주세요",
            "각 영향에 대한 주요 연구 증거와 그 신뢰성을 평가해주세요",
            "다양한 관점(심리학, 사회학, 신경과학, 교육학 등)에서 이 문제를 어떻게 바라보는지 분석해주세요",
            "상충되는 증거와 관점들을 어떻게 조화시킬 수 있는지 설명해주세요",
            "증거의 강도와 일관성을 고려한 균형 잡힌 결론을 도출해주세요"
        ])
    elif "자율주행차" in topic:
        builder.add_instructions([
            "자율주행차의 사회적, 경제적, 윤리적 영향에 대한 다양한 이해관계자의 관점을 분석해주세요",
            "각 영향 영역(안전, 일자리, 접근성, 환경 등)에 대한 핵심 증거와 전망을 평가해주세요",
            "자율주행차 기술에 대한 낙관적 전망과 비관적 전망을 비교 분석해주세요",
            "불확실성이 큰 영역을 명확히 하고, 현재 증거로는 결론을 내리기 어려운 부분을 인정해주세요",
            "증거에 기반하여 자율주행차의 균형 잡힌 영향 평가와 정책적 고려사항을 제시해주세요"
        ])
    elif "기본소득" in topic:
        builder.add_instructions([
            "기본소득에 대한 경제학, 사회복지학, 철학, 정치학 등 다양한 분야의 관점을 분석해주세요",
            "기본소득 도입의 찬성 논거와 반대 논거를 증거와 함께 제시해주세요",
            "다양한 기본소득 실험과 파일럿 프로그램의 결과를 비교 분석해주세요",
            "기본소득의 재정적 실현 가능성과 장기적 지속가능성을 평가해주세요",
            "증거의 강도와 맥락적 조건을 고려한 균형 잡힌 정책 제안을 도출해주세요"
        ])
    elif "인공지능" in topic:
        builder.add_instructions([
            "인공지능의 의사결정에서 발생하는 주요 윤리적 문제(편향, 투명성, 책임, 프라이버시 등)를 분석해주세요",
            "다양한 윤리적 프레임워크에서 이 문제를 어떻게 접근하는지 비교해주세요",
            "윤리적 AI 개발을 위한 기술적 해결책과 정책적 접근법을 평가해주세요",
            "상충되는 가치들(효율성 vs 공정성, 혁신 vs 안전 등) 사이의 균형을 어떻게 맞출 수 있는지 논의해주세요",
            "다양한 관점을 통합한 윤리적 가이드라인이나 원칙을 제안해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 다양한 관점과 견해를 종합적으로 분석해주세요",
            "각 관점의 핵심 주장과 이를 뒷받침하는 주요 증거를 평가해주세요",
            "상충되는 관점들 사이의 공통점과 차이점을 명확히 해주세요",
            "증거의 질과 일관성을 기준으로 각 관점의 타당성을 평가해주세요",
            "다양한 관점을 존중하면서도 증거에 기반한 통합적 결론이나 제안을 도출해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"서론에서는 주제의 배경과 중요성, 다양한 관점이 존재하는 이유를 설명해주세요. "
        f"본론에서는 다양한 관점과 증거를 체계적으로 분석하고, 각 관점의 타당성을 평가해주세요. "
        f"결론에서는 증거를 기반으로 통합적 시각을 제시하되, 확실하지 않은 부분은 솔직히 인정해주세요. "
        f"필요하다면 맥락이나 조건에 따른 차별화된 결론도 제시해주세요. "
        f"색상, 굵은 글씨 등을 적절히 활용하여 핵심 내용을 강조해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="통합적 결론 도출하기",
        topic_options=CONCLUSION_TOPICS,
        get_basic_prompt=get_basic_prompt,
        get_enhanced_prompt=get_enhanced_prompt,
        prompt_summary=PROMPT_SUMMARY,
        learning_points=LEARNING_POINTS
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\n오류 발생: {err}")
        print("API 키나 네트워크 연결을 확인하세요.")
