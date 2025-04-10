"""
다양한 학문 분야 탐험 실습 모듈

Part 6 - 섹션 6.4 실습 코드: 다양한 학문 분야별 특화된 프롬프트 패턴과 접근법을 학습합니다.
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
ACADEMIC_DOMAINS_TOPICS = {
    "1": {"name": "경영학 케이스 스터디", "topic": "경영학 사례 분석 방법론", "output_format": "분석 프레임워크"},
    "2": {"name": "심리학 실험 설계", "topic": "심리학 연구 방법론과 실험 설계", "output_format": "실험 설계 가이드"},
    "3": {"name": "컴퓨터과학 알고리즘 최적화", "topic": "알고리즘 분석 및 최적화 접근법", "output_format": "분석 방법론"},
    "4": {"name": "문학 비평과 텍스트 분석", "topic": "문학 작품의 비평적 분석 방법", "output_format": "분석 템플릿"},
    "5": {"name": "법학 판례 분석", "topic": "법률 사례 및 판례 분석 방법론", "output_format": "법적 분석 프레임워크"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["분야에 대한 일반적인 지식 요청"],
    "enhanced": [
        "분야 전문가 역할 설정: 특정 학문 분야 전문가 페르소나 정의",
        "분야 특화 용어: 해당 분야의 핵심 개념과 전문 용어 활용",
        "분야별 사고방식: 해당 학문의 특징적 사고 패턴과 방법론 반영",
        "맞춤형 구조화: 분야에 적합한 구조와 형식 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "각 학문 분야는 고유한 용어, 방법론, 사고방식을 가지고 있어 이를 프롬프트에 반영하는 것이 중요합니다",
    "분야 전문가 역할 설정은 해당 도메인에 특화된 지식과 관점을 이끌어내는 효과적인 방법입니다",
    "분야별 특화된 프레임워크와 구조는 결과물의 전문성과 활용성을 높입니다",
    "여러 학문 분야를 탐색함으로써 다양한 접근법과 사고방식을 배울 수 있습니다",
    "분야별 맞춤형 템플릿을 개발하면 유사한 과제에 반복적으로 활용할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 설명해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 분야별 특화된 역할 및 맥락 설정
    if "경영학" in topic:
        builder.add_role(
            "경영학 사례 분석 전문가", 
            "세계적인 비즈니스 스쿨 교수이자 다양한 기업 케이스 스터디를 개발한 컨설턴트로, 하버드 비즈니스 리뷰 등에 다수의 사례 연구를 게재하고 기업 전략 분석 프레임워크를 개발한 전문가입니다."
        )
        
        builder.add_context(
            f"저는 경영학과 학생으로 {topic}에 관심이 있습니다. "
            f"기업 사례 분석 과제가 있는데, 체계적인 접근법과 분석 프레임워크를 익히고 싶습니다. "
            f"교수님께서는 SWOT, Porter의 5가지 경쟁요인, Value Chain 등 다양한 분석 도구를 활용하라고 하셨지만, "
            f"실제로 이러한 도구들을 어떻게 통합적으로 적용해야 하는지 감이 잘 잡히지 않습니다."
        )
        
        builder.add_instructions([
            "경영학 사례 분석의 핵심 목적과 체계적 접근법을 설명해주세요",
            "주요 전략 분석 프레임워크(SWOT, PEST, Porter의 5가지 경쟁요인, 가치 사슬, 비즈니스 모델 캔버스 등)의 적용 방법을 설명해주세요",
            "사례 분석 과정을 '상황 분석 → 문제 정의 → 대안 탐색 → 의사결정 → 실행 계획'의 단계로 구조화하여 설명해주세요",
            "정량적 분석(재무지표, 시장점유율 등)과 정성적 분석(리더십, 조직문화 등)을 균형 있게 통합하는 방법을 제시해주세요",
            "경영학 사례 분석 보고서의 전문적인 구성과 작성 방법, 그리고 흔히 범하는 실수와 극복 방법도 포함해주세요"
        ])
        
    elif "심리학" in topic:
        builder.add_role(
            "심리학 연구 방법론 전문가", 
            "유수의 대학에서 실험심리학과 연구방법론을 가르치는 교수로, 다수의 피어 리뷰 저널에 연구를 발표하고 심리학 실험 설계의 모범 사례와 방법론적 엄격성에 관한 저서를 집필한 전문가입니다."
        )
        
        builder.add_context(
            f"저는 심리학과 학생으로 {topic}에 관심이 있습니다. "
            f"학부 연구 프로젝트를 위한 실험을 설계해야 하는데, 방법론적으로 타당하고 윤리적인 실험을 "
            f"설계하는 과정에서 어려움을 겪고 있습니다. 특히 변수 통제, 참가자 모집, 측정 도구 선택, "
            f"그리고 연구 가설 검증을 위한 적절한 통계 분석 방법을 선택하는 데 도움이 필요합니다."
        )
        
        builder.add_instructions([
            "심리학 실험 설계의 핵심 원칙과 단계별 접근법을 설명해주세요",
            "내적/외적 타당도 확보를 위한 실험 설계 전략과 변수 통제 방법을 설명해주세요",
            "연구 질문에서 가설 도출, 변수 조작화, 측정 도구 선택까지의 과정을 단계별로 안내해주세요",
            "무작위 할당, 대조군 설정, 혼입변수 통제 등 실험적 엄격성을 높이는 방법을 설명해주세요",
            "심리학 연구의 윤리적 고려사항, IRB 승인 과정, 참가자 권리 보호 방법도 포함해주세요"
        ])
        
    elif "컴퓨터과학" in topic:
        builder.add_role(
            "알고리즘 분석 및 최적화 전문가", 
            "컴퓨터 과학과 교수이자 알고리즘 설계와 성능 최적화 분야의 연구자로, 대규모 시스템의 효율성 개선을 위한 알고리즘 분석 및 최적화 방법론을 개발하고 주요 기술 기업과 협업한 전문가입니다."
        )
        
        builder.add_context(
            f"저는 컴퓨터과학과 학생으로 {topic}에 관심이 있습니다. "
            f"알고리즘 수업에서 주어진 문제에 대한 솔루션은 구현할 수 있지만, 그 솔루션의 효율성을 분석하고 "
            f"최적화하는 과정에서 어려움을 겪고 있습니다. 시간 복잡도와 공간 복잡도의 균형, 다양한 자료구조 선택의 "
            f"트레이드오프, 그리고 실제 환경에서의 성능 측정과 개선 방법에 대해 체계적으로 이해하고 싶습니다."
        )
        
        builder.add_instructions([
            "알고리즘 분석 및 최적화의 핵심 원칙과 단계별 접근법을 설명해주세요",
            "알고리즘의 시간 복잡도와 공간 복잡도를 체계적으로 분석하는 방법을 설명해주세요",
            "알고리즘 병목 현상을 식별하고 성능을 개선하기 위한 구체적인 전략과 기법을 제시해주세요",
            "다양한 알고리즘 패러다임(분할 정복, 동적 계획법, 탐욕 알고리즘 등)의 최적화 원칙과 적용 사례를 설명해주세요",
            "알고리즘 성능 측정을 위한 벤치마킹 방법과 분석 도구, 그리고 실제 환경에서의 최적화 고려사항도 포함해주세요"
        ])
        
    elif "문학" in topic:
        builder.add_role(
            "문학 비평 및 텍스트 분석 전문가", 
            "유명 대학의 비교문학과 교수이자 문학 이론가로, 다양한 문학 작품에 대한 비평적 분석 방법론을 개발하고 현대 및 고전 문학에 대한 다수의 학술서와 비평을 출판한 전문가입니다."
        )
        
        builder.add_context(
            f"저는 문학과 학생으로 {topic}에 관심이 있습니다. "
            f"학기말 과제로 문학 작품 분석 에세이를 작성해야 하는데, 표면적인 줄거리 요약이나 단순한 감상문이 아닌 "
            f"깊이 있는 비평적 분석을 수행하는 방법을 익히고 싶습니다. 형식적 요소, 주제, 상징, 사회적 맥락 등을 "
            f"통합적으로 분석하여 설득력 있는 문학 비평을 작성하는 체계적인 접근법이 필요합니다."
        )
        
        builder.add_instructions([
            "문학 비평과 텍스트 분석의 핵심 원칙과 주요 비평 이론(형식주의, 구조주의, 포스트모더니즘, 페미니즘 등)을 간략히 소개해주세요",
            "문학 작품 분석을 위한 체계적 접근법과 비평적 읽기 전략을 단계별로 설명해주세요",
            "텍스트의 형식적 요소(서술 구조, 시점, 언어적 장치 등)와 내용적 요소(주제, 인물, 배경, 상징 등)를 분석하는 방법을 설명해주세요",
            "사회적, 역사적, 문화적 맥락을 텍스트 분석에 통합하는 방법과 간텍스트성(intertextuality) 분석 기법을 제시해주세요",
            "설득력 있는 문학 비평 에세이의 구조와 작성 방법, 그리고 효과적인 텍스트 인용과 해석 전략도 포함해주세요"
        ])
        
    elif "법학" in topic:
        builder.add_role(
            "법률 사례 분석 전문가", 
            "저명한 로스쿨 교수이자 법률 분석 방법론 연구자로, 판례 분석과 법적 추론 기술을 가르치고 법률 교육을 위한 사례 연구 방법론을 개발한 전문가입니다."
        )
        
        builder.add_context(
            f"저는 법학과 학생으로 {topic}에 관심이 있습니다. "
            f"법률 사례 분석 과제가 있는데, 복잡한 판례를 체계적으로 분석하고 법적 추론을 발전시키는 과정에서 "
            f"어려움을 겪고 있습니다. 특히 사실관계 정리, 법적 쟁점 식별, 적용 가능한 법리 분석, "
            f"그리고 논리적인 법적 주장 구성에 관한 체계적인 접근법을 배우고 싶습니다."
        )
        
        builder.add_instructions([
            "법률 사례 및 판례 분석의 핵심 원칙과 단계별 접근법을 설명해주세요",
            "IRAC(Issue, Rule, Application, Conclusion) 방법론과 같은 법적 분석 프레임워크의 적용 방법을 설명해주세요",
            "사실관계 분석, 법적 쟁점 식별, 관련 법리 연구, 법적 추론 및 결론 도출의 과정을 체계적으로 안내해주세요",
            "선례 구속의 원칙(stare decisis), 유추(analogy), 구별(distinguishing) 등 판례 분석에 중요한 법적 개념과 그 적용 방법을 설명해주세요",
            "법률 사례 분석 보고서나 법적 메모의 전문적인 구성과 작성 방법, 그리고 법적 문헌(판례, 법령, 학술 자료 등)의 효과적인 인용 방법도 포함해주세요"
        ])
        
    else:
        builder.add_role(
            "학문 분야 연구 방법론 전문가", 
            "다양한 학문 분야의 연구 방법론을 연구하고 가르치는 학제간 전문가로, 각 분야별 특화된 접근법과 방법론적 엄격성을 강조하는 전문가입니다."
        )
        
        builder.add_context(
            f"저는 대학생으로 {topic}에 관심이 있습니다. "
            f"이 분야의 연구 방법론과 분석 접근법을 체계적으로 이해하고 적용하는 방법을 배우고 싶습니다. "
            f"특히 이 분야의 특화된 사고방식, 주요 개념과 이론, 그리고 연구 및 분석의 실질적인 접근법에 "
            f"대한 통찰력 있는 안내가 필요합니다."
        )
        
        builder.add_instructions([
            f"{topic}의 핵심 원칙과 주요 이론적 프레임워크를 소개해주세요",
            "이 분야의 연구 방법론과 분석 기법을 체계적으로 설명해주세요",
            "실제 연구나 분석 과정에서 필요한 단계별 접근법을 안내해주세요",
            "이 분야에서 중요한 방법론적 고려사항과 일반적인 도전과제를 설명해주세요",
            "학부생 수준에서 이 분야의 연구나 분석을 수행하기 위한 실용적인 가이드와 팁을 제공해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"해당 학문 분야의 주요 개념과 전문 용어를 적절히 사용하되, 학부생이 이해할 수 있는 수준으로 설명해주세요. "
        f"가능한 경우 시각적 요소(표, 다이어그램 등)를 포함하여 이해를 돕고, "
        f"분석 또는 연구 프로세스를 단계별로 구조화하여 실용적으로 활용할 수 있게 작성해주세요. "
        f"학생이 실제 과제나 연구에 바로 적용할 수 있는 템플릿이나 체크리스트도 포함해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="다양한 학문 분야 탐험",
        topic_options=ACADEMIC_DOMAINS_TOPICS,
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