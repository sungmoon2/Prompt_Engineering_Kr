"""
결론의 한계와 불확실성 다루기 실습 모듈

Part 2 - 섹션 2.3.3 실습 코드: 결론 도출 과정에서 한계와 불확실성을 적절히 인정하고 표현하는 방법을 학습합니다.
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
UNCERTAINTY_TOPICS = {
    "1": {"name": "과학적 예측", "topic": "기후변화의 장기적 영향 예측", "output_format": "정책 브리핑"},
    "2": {"name": "의학적 권고", "topic": "새로운 건강 가이드라인의 한계와 적용", "output_format": "공중 보건 안내서"},
    "3": {"name": "경제 전망", "topic": "향후 5년간 경제 전망과 불확실성 요인", "output_format": "경제 분석 보고서"},
    "4": {"name": "기술 발전", "topic": "인공지능 기술의 미래 발전과 한계", "output_format": "기술 평가 보고서"},
    "5": {"name": "교육 방법론", "topic": "새로운 교육 방법론의 효과와 제한점", "output_format": "교육 연구 리뷰"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 단순한 결론 요청"],
    "enhanced": [
        "한계 명시: 현재 지식과 증거의 한계 인정",
        "불확실성 표현: 확률적 언어와 조건부 표현 사용",
        "균형적 관점: 다양한 가능성과 대안적 관점 포함"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "결론의 한계와 불확실성을 인정하는 것은 과학적 엄격함과 지적 정직성의 표현입니다",
    "확률적 언어와 조건부 표현을 사용하면 과도한 확신이나 단순화를 피할 수 있습니다",
    "증거의 질과 범위에 따라 결론의 신뢰도를 차등화하는 것이 중요합니다",
    "향후 연구나 정보가 결론을 어떻게 변화시킬 수 있는지 고려하는 것이 포괄적 분석에 필수적입니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대한 결론을 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 역할 및 맥락 설정
    builder.add_role(
        "과학적 불확실성 전문가", 
        "복잡한 주제에 대한 결론을 도출할 때 한계와 불확실성을 투명하게 다루는 전문가"
    )
    
    # 맥락 정보 추가
    builder.add_context(
        f"저는 {topic}에 관한 보고서를 작성 중인 대학생입니다. "
        f"관련 자료를 수집하고 분석했지만, 많은 불확실성과 제한된 증거가 있습니다. "
        f"현재의 한계를 인정하면서도 유용한 결론을 도출하고, 이를 적절하게 표현하는 방법을 배우고 싶습니다. "
        f"과도한 확신이나 지나친 회의주의 없이 균형 잡힌 관점을 제시하고 싶습니다."
    )
    
    # 구체적인 지시사항 추가
    if "기후변화" in topic:
        builder.add_instructions([
            "기후변화의 장기적 영향 예측에 관한 현재 과학적 합의와 주요 예측 모델을 요약해주세요",
            "기후 모델링의 주요 한계와 불확실성 요인(데이터 한계, 복잡한 피드백 메커니즘 등)을 설명해주세요",
            "다양한 시나리오와 확률 범위를 활용하여 예측의 불확실성을 표현해주세요",
            "정책 결정에 필요한 '충분히 확실한' 결론과 여전히 높은 불확실성이 있는 영역을 구분해주세요",
            "불확실성에도 불구하고 현재 증거에 기반한 합리적인 정책 방향을 제안해주세요"
        ])
    elif "건강 가이드라인" in topic:
        builder.add_instructions([
            "새로운 건강 가이드라인의 핵심 권고사항과 그 근거가 되는 연구를 요약해주세요",
            "연구 설계, 표본 크기, 연구 기간 등 근거의 강도와 질에 관한 제한점을 분석해주세요",
            "다양한 인구 집단(나이, 성별, 건강 상태 등)에 따른 가이드라인 적용의 한계와 변이를 설명해주세요",
            "연구 결과 간의 불일치나 상충되는 증거에 대해 투명하게 논의해주세요",
            "불확실성을 인정하면서도 현재 증거에 기반한 실용적인 건강 권고를 제시해주세요"
        ])
    elif "경제 전망" in topic:
        builder.add_instructions([
            "향후 5년간 경제 전망에 대한 주요 예측과 가정을 설명해주세요",
            "경제 예측의 근본적 한계와 주요 불확실성 요인(정책 변화, 글로벌 사건, 기술 발전 등)을 분석해주세요",
            "다양한 시나리오와 확률 범위를 통해 경제 전망의 불확실성을 표현해주세요",
            "경제 지표별로 예측 신뢰도의 차이를 설명하고, 더 확실한 전망과 더 불확실한 영역을 구분해주세요",
            "불확실성 속에서도 개인, 기업, 정책 입안자에게 도움이 될 수 있는 실용적 통찰을 제공해주세요"
        ])
    elif "인공지능" in topic:
        builder.add_instructions([
            "인공지능 기술의 현재 상태와 주요 발전 트렌드를 요약해주세요",
            "기술 예측의 한계와 AI 발전에 영향을 미치는 주요 불확실성 요인을 분석해주세요",
            "다양한 시나리오와 시간 프레임에 따른 AI 발전 가능성을 설명해주세요",
            "기술적, 사회적, 윤리적 관점에서 AI 발전의 한계와 도전과제를 논의해주세요",
            "불확실성을 인정하면서도, 현재 증거에 기반한 AI 기술의 발전 방향과 준비 전략을 제시해주세요"
        ])
    elif "교육 방법론" in topic:
        builder.add_instructions([
            "새로운 교육 방법론의 주요 원리와 기존 연구 결과를 요약해주세요",
            "교육 연구의 방법론적 한계와 결과 해석에 영향을 미치는 요인들을 분석해주세요",
            "다양한 학습자 집단, 교육 환경, 과목 영역에 따른 효과 차이와 적용 한계를 설명해주세요",
            "상충되는 연구 결과와 아직 충분히 연구되지 않은 영역을 투명하게 논의해주세요",
            "불확실성과 한계를 인정하면서도, 현재 증거에 기반한 교육 실천에 대한 제안을 제공해주세요"
        ])
    else:
        builder.add_instructions([
            f"{topic}에 관한 현재 지식 상태와 주요 연구 결과를 요약해주세요",
            "현재 증거와 연구의 주요 한계와 제한점을 분석해주세요",
            "결론에 영향을 미치는 불확실성 요인과 가정을 명확히 해주세요",
            "다양한 시나리오와 가능성을 고려한 균형 잡힌 관점을 제시해주세요",
            "현재 한계를 인정하면서도 증거에 기반한 합리적인 결론과 제안을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"확률적 언어('가능성이 높음', '~일 수 있음', '증거가 시사함' 등)를 적절히 사용하여 확실성의 정도를 표현해주세요. "
        f"현재 지식의 한계와 불확실성에 대한 섹션을 명시적으로 포함해주세요. "
        f"시각적 요소(표, 확률 범위, 신뢰 구간 등)를 활용하여 불확실성을 효과적으로 전달해주세요. "
        f"추가 연구나 정보가 필요한 영역을 명확히 지정해주세요. "
        f"현재 증거 상태에 따라 결론의 신뢰도를 차등화하여 표현해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="결론의 한계와 불확실성 다루기",
        topic_options=UNCERTAINTY_TOPICS,
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
