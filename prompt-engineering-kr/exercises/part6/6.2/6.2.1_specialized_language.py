"""
비즈니스/경제 분야 프롬프트 최적화 실습 모듈

Part 6 - 섹션 6.2.1 실습 코드: 비즈니스와 경제 분야의 문제 해결과 의사결정을 위한
최적화된 프롬프트 작성법을 학습합니다.
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
BUSINESS_PROMPTS_TOPICS = {
    "1": {"name": "시장/산업 분석", "topic": "새로운 산업 진출을 위한 시장 분석", "output_format": "분석 보고서"},
    "2": {"name": "비즈니스 전략", "topic": "스타트업 성장 전략 수립", "output_format": "전략 계획서"},
    "3": {"name": "재무 의사결정", "topic": "투자 프로젝트 재무 타당성 분석", "output_format": "의사결정 메모"},
    "4": {"name": "마케팅 전략", "topic": "디지털 마케팅 캠페인 개발", "output_format": "마케팅 계획서"},
    "5": {"name": "운영 최적화", "topic": "공급망 효율성 향상 방안", "output_format": "프로세스 개선 계획"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 일반적인 분석 요청"],
    "enhanced": [
        "비즈니스 맥락 설정: 구체적인 상황과 목표 정의",
        "데이터 중심 요청: 정량적 분석과 지표 기반 접근 강조",
        "프레임워크 활용: 비즈니스 분석 도구와 모델 명시",
        "실행 가능성 요청: 구체적 단계와 KPI가 포함된 실용적 제안 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "비즈니스 분야는 데이터 중심적, 결과 지향적, 구조화된 접근을 중시하므로 이를 프롬프트에 반영해야 합니다",
    "주요 비즈니스 프레임워크(SWOT, Porter의 5가지 경쟁요인, 비즈니스 모델 캔버스 등)를 활용하면 체계적인 분석이 가능합니다",
    "다양한 비즈니스 상황(시장 분석, 전략 개발, 재무 의사결정 등)에 맞게 맞춤형 프롬프트를 구성하면 효과적입니다",
    "정량적 분석과 실행 가능한 권장사항을 요청하면 실무에 바로 활용할 수 있는 결과를 얻을 수 있습니다",
    "산업별 특화된 용어, KPI, 비즈니스 모델을 반영한 프롬프트를 개발하면 더 전문적인 분석이 가능합니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 분석해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 분야별 역할 및 맥락 설정
    if "시장/산업 분석" in purpose:
        builder.add_role(
            "시장 분석 컨설턴트",
            "데이터 기반 시장 조사와 산업 분석을 전문으로 하는 컨설턴트로, 기업의 새로운 시장 진출 의사결정을 지원하는 전략적 인사이트를 제공하는 전문가"
        )
        
        builder.add_context(
            f"저는 중견 기업의 사업 개발 매니저로 {topic}에 관한 분석이 필요합니다. "
            f"우리 회사는 현재 새로운 산업 진출을 고려하고 있으며, 시장 기회와 위험을 "
            f"포괄적으로 이해하기 위한 체계적인 분석이 필요합니다. 이 분석은 경영진에게 "
            f"제시될 예정이며, 투자 의사결정의 기초 자료로 활용될 것입니다."
        )
        
        builder.add_instructions([
            "해당 산업의 시장 규모, 성장률, 주요 세그먼트 등 핵심 시장 데이터를 포함해주세요",
            "Porter의 5가지 경쟁요인 프레임워크를 활용하여 산업의 경쟁 구도를 분석해주세요",
            "주요 시장 참여자, 그들의 시장 점유율, 비즈니스 모델, 경쟁 전략을 설명해주세요",
            "주요 시장 트렌드, 성장 동인, 잠재적 장벽과 위험 요소를 분석해주세요",
            "새로운 진입자에게 가장 유망한 시장 기회와 진입 전략을 제안해주세요",
            "향후 3-5년간의 시장 전망과 주요 성공 요인을 제시해주세요"
        ])
        
    elif "비즈니스 전략" in purpose:
        builder.add_role(
            "스타트업 전략 컨설턴트",
            "스타트업의 성장 전략과 확장 계획을 전문으로 하는 비즈니스 전략가로, 제한된 자원을 가진 기업의 확장과 시장 포지셔닝에 대한 실용적인 조언을 제공하는 전문가"
        )
        
        builder.add_context(
            f"저는 SaaS 스타트업의 공동 창업자로 {topic}에 관한 도움이 필요합니다. "
            f"우리 기업은 초기 시장 검증을 마치고 제품-시장 적합성을 확보했으며, "
            f"이제 본격적인 성장 단계로 진입하려고 합니다. 현재 월 반복 수익(MRR)은 "
            f"2만 달러이며, 10명의 팀과 50만 달러의 시드 투자를 확보한 상태입니다. "
            f"다음 18개월 동안의 체계적인 성장 전략이 필요합니다."
        )
        
        builder.add_instructions([
            "사용자 획득, 제품 개발, 팀 구축, 자금 조달 등 핵심 영역을 포함한 종합적인 성장 전략을 개발해주세요",
            "SaaS 비즈니스의 주요 성과 지표(KPI)와 목표 설정 방법을 제안해주세요",
            "제한된 자원(인력, 자금)을 고려한 우선순위 설정과 단계적 접근법을 제시해주세요",
            "고객 획득 비용(CAC)과 고객 생애 가치(LTV) 최적화를 위한 구체적인 전략을 포함해주세요",
            "경쟁사와의 차별화 전략과 지속 가능한 경쟁 우위 구축 방안을 설명해주세요",
            "다음 자금 조달 라운드를 위한 준비 사항과 핵심 마일스톤을 제안해주세요"
        ])
        
    elif "재무 의사결정" in purpose:
        builder.add_role(
            "투자 분석 전문가",
            "투자 프로젝트의 재무적 타당성을 평가하는 재무 분석 전문가로, 객관적인 데이터 분석과 위험 평가를 통해 투자 의사결정을 지원하는 전문가"
        )
        
        builder.add_context(
            f"저는 제조업체의 재무 분석가로 {topic}에 관한 분석이 필요합니다. "
            f"우리 회사는 생산 설비 확장을 위한 대규모 투자를 고려하고 있습니다. "
            f"초기 투자금은 약 500만 달러이며, 설비 수명은 10년으로 예상됩니다. "
            f"이 투자의 재무적 타당성을 종합적으로 평가하여 경영진에게 투자 권고안을 "
            f"제시해야 합니다."
        )
        
        builder.add_instructions([
            "NPV, IRR, 회수 기간, ROI 등 핵심 재무 지표를 활용한 종합적인 투자 분석을 수행해주세요",
            "투자에 대한 현금 흐름 예측과 할인율 설정에 대한 명확한 가정을 제시해주세요",
            "다양한 시나리오(낙관적, 현실적, 비관적)에 따른 민감도 분석을 포함해주세요",
            "투자와 관련된 주요 리스크 요소와 이를 완화하기 위한 전략을 분석해주세요",
            "재무적 분석 외에도 전략적, 운영적 측면의 영향을 종합적으로 고려해주세요",
            "투자 의사결정에 대한 명확한 권고안과 그 근거를 제시해주세요"
        ])
        
    elif "마케팅 전략" in purpose:
        builder.add_role(
            "디지털 마케팅 전략가",
            "데이터 기반 디지털 마케팅 캠페인을 설계하는 마케팅 전문가로, ROI 최적화와 고객 생애 가치 증대를 위한 통합적인 마케팅 전략을 개발하는 전문가"
        )
        
        builder.add_context(
            f"저는 온라인 패션 리테일 브랜드의 마케팅 매니저로 {topic}에 관한 도움이 필요합니다. "
            f"새로운 시즌 컬렉션 출시를 위한 종합적인 디지털 마케팅 캠페인을 개발해야 합니다. "
            f"주요 타겟은 25-40세 도시 거주 전문직 여성이며, 마케팅 예산은 10만 달러입니다. "
            f"매출 증대와 브랜드 인지도 향상이 주요 목표입니다."
        )
        
        builder.add_instructions([
            "고객 획득, 전환, 유지를 위한 종합적인 디지털 마케팅 전략을 개발해주세요",
            "각 마케팅 채널(소셜 미디어, 이메일, 검색, 디스플레이 등)별 구체적인 전략과 예산 할당 방안을 제안해주세요",
            "타겟 고객에 대한 페르소나 개발과 그에 맞는 메시징 전략을 포함해주세요",
            "마케팅 성과 측정을 위한 KPI와 분석 프레임워크를 설정해주세요",
            "경쟁사 대비 차별화된 콘텐츠 및 크리에이티브 전략을 제안해주세요",
            "캠페인 일정, 실행 계획, 주요 마일스톤을 포함한 구체적인 실행 로드맵을 제시해주세요"
        ])
        
    elif "운영 최적화" in purpose:
        builder.add_role(
            "공급망 최적화 컨설턴트",
            "기업의 공급망 효율성과 복원력을 향상시키는 운영 전문가로, 프로세스 최적화와 비용 절감을 통해 기업의 경쟁력을 강화하는 전문가"
        )
        
        builder.add_context(
            f"저는 글로벌 소비재 기업의 운영 매니저로 {topic}에 관한 분석이 필요합니다. "
            f"최근 공급망 중단과 비용 증가로 인해 운영 효율성이 저하되었습니다. "
            f"주요 문제점으로는 긴 리드타임, 재고 관리 문제, 물류 비용 증가, 공급업체 "
            f"리스크 등이 있습니다. 공급망 효율성을 개선하고 운영 비용을 절감하기 위한 "
            f"종합적인 접근법이 필요합니다."
        )
        
        builder.add_instructions([
            "공급망의 현재 비효율성과 병목 현상을 식별하고 근본 원인을 분석해주세요",
            "린(Lean) 원칙과 6시그마 방법론을 활용한 프로세스 최적화 방안을 제안해주세요",
            "재고 관리, 수요 예측, 공급업체 관리, 물류 최적화 등 주요 영역별 개선 전략을 개발해주세요",
            "공급망 복원력을 강화하기 위한 리스크 관리 전략을 포함해주세요",
            "제안된 개선 방안의 예상 비용과 효과(ROI, 비용 절감, 리드타임 단축 등)를 정량적으로 분석해주세요",
            "단기, 중기, 장기적 접근을 포함한 단계적 실행 계획을 제시해주세요"
        ])
        
    else:
        builder.add_role(
            f"{purpose} 전문가", 
            f"{topic}에 대한 심층적 분석과 전략적 인사이트를 제공하는 비즈니스 컨설턴트"
        )
        
        builder.add_context(
            f"저는 비즈니스 전문가로 {topic}에 관한 분석이 필요합니다. "
            f"이 주제에 대한 체계적이고 실용적인 분석을 통해 비즈니스 의사결정을 "
            f"지원할 수 있는 인사이트를 얻고자 합니다."
        )
        
        builder.add_instructions([
            f"{topic}에 대한 현재 상황과 주요 도전과제를 분석해주세요",
            "관련 시장 데이터와 산업 트렌드를 포함한 배경 정보를 제공해주세요",
            "SWOT 분석 등 적절한 비즈니스 프레임워크를 활용한 체계적인 분석을 수행해주세요",
            "실행 가능한 전략적 옵션과 각 옵션의 장단점을 제시해주세요",
            "권장 접근법과 구체적인 실행 단계를 제안해주세요",
            "성과 측정을 위한 KPI와 모니터링 방법을 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"다음과 같은 구조로 체계적으로 정리해주세요:\n\n"
        f"1. 개요: 핵심 요약과 주요 발견사항\n"
        f"2. 상황 분석: 현재 상황, 배경, 주요 도전과제\n"
        f"3. 주요 분석: 데이터와 프레임워크 기반 심층 분석\n"
        f"4. 전략적 옵션: 가능한 접근법과 각각의 장단점\n"
        f"5. 권장사항: 명확한 행동 계획과 우선순위\n"
        f"6. 실행 계획: 구체적인 단계, 타임라인, 필요 자원\n"
        f"7. 성과 측정: 주요 KPI와 모니터링 방법\n\n"
        f"가능한 경우 표, 차트, 다이어그램 등을 활용하여 정보를 시각화해주세요. "
        f"모든 분석과 권장사항은 데이터와 근거에 기반해야 하며, 실행 가능성을 고려한 "
        f"실용적인 접근법을 강조해주세요. 전문 용어를 적절히 사용하되, 명확하고 직관적인 "
        f"언어로 설명해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="비즈니스/경제 분야 프롬프트 최적화",
        topic_options=BUSINESS_PROMPTS_TOPICS,
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