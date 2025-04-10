"""
분야별 프롬프트 패턴 실습 모듈

Part 6 - 섹션 6.2 실습 코드: 다양한 학문/전문 분야별 최적화된 프롬프트 패턴을 이해하고 적용하는 방법을 학습합니다.
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
DOMAIN_PATTERNS_TOPICS = {
    "1": {"name": "비즈니스/경제", "topic": "시장 진입 전략 분석", "output_format": "전략 보고서"},
    "2": {"name": "이공계 연구", "topic": "실험 데이터 분석 및 해석", "output_format": "연구 분석 보고서"},
    "3": {"name": "인문/사회과학", "topic": "문화 현상의 비판적 분석", "output_format": "학술 에세이"},
    "4": {"name": "법률", "topic": "법적 사례 분석 및 의견", "output_format": "법률 메모"},
    "5": {"name": "의학/보건", "topic": "임상 사례 평가 및 치료 계획", "output_format": "임상 보고서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["주제에 대한 직접적인 질문"],
    "enhanced": [
        "분야별 맞춤 구조: 각 학문 분야에 최적화된 프롬프트 구조 적용",
        "전문적 프레임워크: 분야별 분석 도구와 방법론 명시",
        "맥락 설정: 분야 특성에 맞는 배경 및 상황 정보 제공",
        "출력 형식 지정: 해당 분야의 전문적 문서 형식 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "각 학문/전문 분야는 고유한 사고방식과 접근 방법을 가지고 있어 이에 맞춘 프롬프트가 더 효과적입니다",
    "비즈니스 분야는 데이터 기반 의사결정과 실행 가능한 전략을 중시하므로 이를 반영한 구조가 필요합니다",
    "이공계 분야는 과학적 방법론과 실증적 데이터를 강조하는 프롬프트 패턴이 적합합니다",
    "인문/사회과학은 다양한 관점과 맥락적 이해를 중시하는 해석적 프레임워크를 활용하는 것이 좋습니다",
    "분야별 특성을 반영한 템플릿을 개발하여 재사용하면 프롬프트 작성 효율과 응답 품질이 향상됩니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 분석해주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 분야별 역할 및 맥락 설정
    if "비즈니스" in purpose:
        builder.add_role(
            "비즈니스 전략 컨설턴트",
            "주요 경영 컨설팅 기업 출신으로 다양한 산업의 시장 진입 전략, 비즈니스 모델 혁신, 경쟁 분석을 전문으로 하는 전략 컨설턴트"
        )
        
        builder.add_context(
            f"저는 경영학 전공 학생으로 {topic}에 관한 프로젝트를 진행 중입니다. "
            f"가상의 기술 스타트업이 새로운 시장에 진입하는 전략을 수립하는 과제를 작성하고 있습니다. "
            f"다음과 같은 상황에서 체계적인 시장 진입 전략 분석이 필요합니다:\n\n"
            f"기업 상황: 인공지능 기반 개인화 학습 솔루션을 제공하는 에듀테크 스타트업\n"
            f"목표 시장: 고등교육(대학) 시장, 현재는 K-12 시장에서만 운영 중\n"
            f"가용 자원: 투자금 500만 달러, 핵심 기술 팀 보유, 제한된 영업/마케팅 역량\n"
            f"경쟁 상황: 대형 교육 플랫폼 기업들이 시장 장악, 일부 틈새 스타트업 존재"
        )
        
        builder.add_instructions([
            "산업 및 시장 분석: 고등교육 시장의 규모, 성장성, 주요 트렌드, 진입 장벽 분석",
            "경쟁 환경 평가: 주요 경쟁사 프로필, 강점/약점, 시장 포지셔닝 분석",
            "시장 진입 옵션: 가능한 진입 전략(직접 진출, 파트너십, 인수 등) 최소 3가지 제시 및 비교 분석",
            "각 옵션의 리스크-리워드 프로필과 자원 요구사항 평가",
            "추천 전략: 최적의 진입 전략 제안 및 선택 근거 설명",
            "실행 계획: 추천 전략의 단계별 실행 계획, 타임라인, 주요 마일스톤, KPI 제시"
        ])
        
    elif "이공계" in purpose:
        builder.add_role(
            "연구 방법론 전문가",
            "이공계 연구 데이터 분석 및 해석 전문가로, 다양한 실험 설계와 데이터 분석 기법에 정통한 연구 방법론 컨설턴트"
        )
        
        builder.add_context(
            f"저는 물리학과 대학원생으로 {topic}에 대한 도움이 필요합니다. "
            f"다음과 같은 실험 데이터를 수집했으며, 이에 대한 체계적인 분석과 해석이 필요합니다:\n\n"
            f"연구 주제: 나노입자 코팅이 태양전지 효율에 미치는 영향\n"
            f"가설: 특정 나노입자 코팅 처리가 태양전지의 에너지 변환 효율을 유의미하게 향상시킨다\n"
            f"실험 설계: 4가지 다른 나노입자 코팅(A, B, C, D)과 대조군(무코팅)으로 구성된 태양전지 샘플 각 10개씩 제작\n"
            f"측정 데이터: 각 샘플의 에너지 변환 효율(%), 광 흡수율(%), 내구성 테스트 결과(시간)"
        )
        
        builder.add_instructions([
            "데이터 분석 방법론: 이 실험 데이터에 적합한 통계적 분석 방법 제안 및 적용",
            "기술 통계 및 시각화: 핵심 측정치의 평균, 표준편차, 분포 등 분석 및 시각화",
            "가설 검정: 나노입자 코팅과 태양전지 효율 간의 관계에 대한 통계적 검정 수행",
            "그룹 간 비교: 다양한 코팅 유형 간의 성능 차이 분석 및 최적 조건 식별",
            "상관관계 분석: 측정된 변수 간의 상관관계 및 인과관계 가능성 탐색",
            "결론 및 한계: 데이터에 기반한 결론 도출과 실험의 제한점 및 개선 방향 제시"
        ])
        
    elif "인문" in purpose or "사회과학" in purpose:
        builder.add_role(
            "문화 분석 학자",
            "문화 연구, 미디어 이론, 사회학적 분석 방법론에 전문성을 갖춘 학자로, 다양한 문화 현상에 대한 비판적 분석과 해석을 수행하는 전문가"
        )
        
        builder.add_context(
            f"저는 미디어 문화학과 대학원생으로 {topic}에 관한 연구를 진행 중입니다. "
            f"현대 소셜 미디어 플랫폼에서의 셀프 브랜딩(self-branding) 현상을 비판적으로 분석하고자 합니다. "
            f"특히 인플루언서 문화, 진정성의 상품화, 디지털 자아의 형성과 관련된 문화적, 사회적 함의를 탐구하고 있습니다. "
            f"포스트모더니즘, 소비 문화 이론, 디지털 정체성 이론 등의 관점에서 이 현상을 분석하는 데 도움이 필요합니다."
        )
        
        builder.add_instructions([
            "이론적 프레임워크: 셀프 브랜딩 현상을 분석하기 위한 주요 이론적 관점(최소 3가지) 제시 및 설명",
            "현상의 맥락화: 역사적, 사회경제적, 기술적 맥락에서 셀프 브랜딩의 발전과 의미 분석",
            "비판적 분석: 권력, 젠더, 계급, 인종 등의 측면에서 인플루언서 문화와 셀프 브랜딩의 함의 고찰",
            "담론 분석: 셀프 브랜딩과 관련된 주요 담론(진정성, 성공, 개인주의 등)의 구성과 작동 방식 탐구",
            "상충되는 해석: 이 현상에 대한 다양한(때로는 모순되는) 학술적 해석과 관점 비교",
            "반성적 결론: 분석의 함의와 한계, 그리고 향후 연구 방향 제시"
        ])
        
    elif "법률" in purpose:
        builder.add_role(
            "법률 분석 전문가",
            "기업법 및 계약법 분야의 변호사로, 복잡한 법적 사례를 분석하고 실용적인 법률 조언을 제공하는 전문가"
        )
        
        builder.add_context(
            f"저는 법학과 학생으로 {topic}에 관한 과제를 수행 중입니다. "
            f"다음과 같은 가상의 법적 사례에 대한 분석과 법률 의견이 필요합니다:\n\n"
            f"사례 개요: 기술 스타트업 A사가 경쟁사 B사의 전 직원을 채용한 후, B사는 해당 직원이 기밀 정보를 A사에 유출했다고 주장하며 소송을 제기\n"
            f"쟁점 사항: (1) 비밀유지계약(NDA)의 범위와 효력, (2) 영업비밀의 정의와 보호 요건, (3) 경업금지 조항의 합리성, (4) 손해배상의 범위\n"
            f"관련 정보: 해당 직원은 B사에서 2년간 근무했으며, A사 입사 후 유사한 제품 개발에 참여, B사와의 계약에는 2년간 경업금지 조항 포함"
        )
        
        builder.add_instructions([
            "법적 쟁점 분석: 사례에 내포된 주요 법적 쟁점의 체계적 식별 및 정의",
            "관련 법률 및 판례: 각 쟁점과 관련된 주요 법률, 규정, 판례 분석",
            "사실관계 평가: 제공된 정보를 기반으로 법적으로 중요한 사실관계 분석",
            "양측 주장 분석: 원고(B사)와 피고(A사) 측의 가능한 법적 주장과 항변 분석",
            "위험 평가: A사 입장에서의 법적 위험과 잠재적 결과 평가",
            "권고 사항: A사를 위한 법적 전략, 협상 옵션, 위험 완화 방안 제안"
        ])
        
    elif "의학" in purpose or "보건" in purpose:
        builder.add_role(
            "임상 의학 전문가",
            "내과 전문의이자 의과대학 교수로, 복잡한 임상 사례의 진단, 평가, 치료 계획 수립에 폭넓은 경험을 가진 의료 전문가"
        )
        
        builder.add_context(
            f"저는 의과대학 학생으로 {topic}에 관한 임상 실습 과제를 진행 중입니다. "
            f"다음과 같은 가상의 환자 사례에 대한 평가와 치료 계획이 필요합니다:\n\n"
            f"환자 정보: 58세 남성, 고혈압과 제2형 당뇨병 병력 10년\n"
            f"주 호소: 3개월간 지속된 운동 시 호흡 곤란과 가슴 압박감, 최근 악화\n"
            f"검사 결과: 심전도에서 ST 분절 하강, 심장 효소 약간 상승, 지질 프로필 이상\n"
            f"현재 약물: 메트포민, 리시노프릴, 심바스타틴"
        )
        
        builder.add_instructions([
            "임상 평가: 제시된 병력, 증상, 검사 결과에 기반한 체계적 평가",
            "감별 진단: 가능성 있는 주요 진단명 나열 및 각각에 대한 근거와 가능성 평가",
            "추가 검사: 진단 확정을 위해 필요한 추가 검사 및 그 근거 제시",
            "치료 계획: 가장 가능성 높은 진단에 대한 증거 기반 치료 계획 수립",
            "약물 요법: 현재 약물을 고려한 적절한 약물 치료 방안 제안",
            "모니터링 계획: 치료 효과 및 질병 진행 모니터링을 위한 계획 수립"
        ])
        
    else:
        builder.add_role(
            f"{purpose} 전문가", 
            f"{topic}에 대한 심층적 분석과 전문적 인사이트를 제공하는 전문가"
        )
        
        builder.add_context(
            f"저는 학생으로 {topic}에 관한 분석이 필요합니다. "
            f"이 주제에 대한 체계적이고 전문적인 분석을 통해 깊이 있는 이해를 얻고자 합니다."
        )
        
        builder.add_instructions([
            f"{topic}의 핵심 측면과 주요 구성 요소 분석",
            "관련 이론적 프레임워크와 방법론 적용",
            "다양한 관점과 입장에서의 비교 분석",
            "주요 쟁점과 도전 과제 식별",
            "실용적 적용 방안 및 향후 발전 방향 제안"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"해당 분야의 전문적 문서 스타일과 구조를 따라 체계적으로 작성해주세요. "
        f"필요한 경우 표, 프레임워크, 분석 모델 등을 활용하여 정보를 시각적으로 구조화해주세요. "
        f"전문 용어를 적절히 사용하되, 필요시 간략한 설명을 병행해주세요. "
        f"결론과 권장사항은 명확하고 실행 가능하게 제시해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="분야별 프롬프트 패턴",
        topic_options=DOMAIN_PATTERNS_TOPICS,
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