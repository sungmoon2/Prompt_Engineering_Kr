"""
API 활용 웹 애플리케이션 개발 실습 모듈

Part 5 - 섹션 5.4.1 실습 코드: 외부 API를 활용한 웹 애플리케이션 개발 방법을 학습합니다.
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
API_WEB_APP_TOPICS = {
    "1": {"name": "날씨 대시보드", "topic": "날씨 API를 활용한 대시보드 애플리케이션 개발", "output_format": "개발 가이드"},
    "2": {"name": "영화 검색 앱", "topic": "영화 정보 API를 활용한 검색 및 추천 애플리케이션", "output_format": "구현 계획"},
    "3": {"name": "금융 데이터 시각화", "topic": "금융 API를 활용한 주식 및 암호화폐 데이터 시각화", "output_format": "개발 명세서"},
    "4": {"name": "뉴스 애그리게이터", "topic": "뉴스 API를 활용한 개인화된 뉴스 애그리게이터", "output_format": "아키텍처 문서"},
    "5": {"name": "소셜 미디어 대시보드", "topic": "소셜 미디어 API 통합 분석 대시보드", "output_format": "개발 로드맵"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["API 기반 웹 애플리케이션 개발에 대한 일반적 안내 요청"],
    "enhanced": [
        "구체적 API 명시: 사용할 API와 핵심 기능 명확화",
        "아키텍처 패턴: 적합한 API 통합 패턴 요청",
        "기술 스택: 프론트엔드/백엔드 기술 구체화", 
        "데이터 처리: 데이터 변환 및 시각화 전략 요청"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "외부 API 활용은 강력한 기능을 빠르게 통합하여 개발 시간을 단축할 수 있습니다",
    "API 키 보안, CORS 이슈 등을 고려한 적절한 아키텍처 패턴 선택이 중요합니다",
    "효과적인 오류 처리와 재시도 메커니즘은 API 기반 애플리케이션의 안정성을 높입니다",
    "데이터 캐싱과 최적화 전략은 API 호출 비용 절감과 성능 향상에 핵심적입니다",
    "AI를 활용하면 API 클라이언트 구현, 데이터 변환, UI 컴포넌트 개발을 가속화할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 역할 및 맥락 설정
    if "날씨 API" in topic:
        builder.add_role(
            "웹 애플리케이션 아키텍트", 
            "API 통합 웹 애플리케이션 개발 전문가로, 다양한 외부 API를 효과적으로 활용한 애플리케이션 설계와 구현에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 날씨 데이터를 시각화하는 대시보드 웹 애플리케이션을 개발하려고 합니다. "
            f"이 애플리케이션은 사용자가 지정한 위치의 현재 날씨, 일주일 예보, 기상 경보 등을 "
            f"시각적으로 표시하고, 과거 날씨 데이터를 분석하여 트렌드를 보여줄 예정입니다. "
            f"OpenWeatherMap API 또는 Weather API를 활용할 계획이며, 프론트엔드는 React, "
            f"백엔드는 필요한 경우 Node.js를 사용할 예정입니다."
        )
        
        builder.add_instructions([
            "날씨 API를 활용한 대시보드 애플리케이션 개발을 위한 체계적인 접근법을 제안해주세요",
            "API 통합 아키텍처 패턴(직접 호출, 백엔드 프록시 등) 중 이 프로젝트에 적합한 방식과 그 이유를 설명해주세요",
            "React를 사용한 날씨 데이터 시각화 전략과 추천 라이브러리를 제안해주세요",
            "API 호출 최적화, 데이터 캐싱, 오류 처리 전략을 상세히 설명해주세요",
            "개발 단계별 접근법과 함께 각 단계에서 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
        
    elif "영화 정보 API" in topic:
        builder.add_role(
            "영화 애플리케이션 개발자", 
            "영화 데이터 API를 활용한 웹 애플리케이션 개발 전문가로, 사용자 경험이 뛰어난 영화 정보 서비스 구축에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 영화 정보를 검색하고 추천해주는 웹 애플리케이션을 개발하려고 합니다. "
            f"이 애플리케이션은 영화 제목, 배우, 감독 등으로 검색 기능을 제공하고, "
            f"사용자의 선호도에 기반하여 영화를 추천하며, 상세 정보와 리뷰 등을 표시할 예정입니다. "
            f"The Movie Database(TMDB) API를 활용할 계획이며, React와 Material-UI를 사용하여 "
            f"프론트엔드를 개발하고, 필요한 경우 Next.js를 사용할 수 있습니다."
        )
        
        builder.add_instructions([
            "영화 정보 API를 활용한 검색 및 추천 애플리케이션 개발을 위한 체계적인 접근법을 제안해주세요",
            "TMDB API 통합 전략과 인증, 요청 관리, 응답 처리 방법을 설명해주세요",
            "영화 검색, 필터링, 추천 기능 구현을 위한 UI/UX 디자인과 컴포넌트 설계를 제안해주세요",
            "성능 최적화(지연 로딩, 무한 스크롤, 이미지 최적화 등)와 사용자 경험 향상 전략을 상세히 설명해주세요",
            "개발 단계별 구현 계획과 함께 각 단계에서 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
        
    elif "금융 API" in topic:
        builder.add_role(
            "금융 데이터 시각화 전문가", 
            "금융 API를 활용한 데이터 시각화 애플리케이션 개발 전문가로, 복잡한 금융 데이터를 직관적이고 유용한 시각적 정보로 변환하는 웹 애플리케이션 구축에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 주식 및 암호화폐 데이터를 시각화하는 금융 대시보드 애플리케이션을 개발하려고 합니다. "
            f"이 애플리케이션은 사용자가 선택한 주식이나 암호화폐의 가격 차트, 거래량, 기술적 지표 등을 "
            f"시각적으로 표시하고, 포트폴리오 추적 및 분석 기능을 제공할 예정입니다. "
            f"Alpha Vantage API 또는 Yahoo Finance API를 주식 데이터용으로, CoinGecko API를 "
            f"암호화폐 데이터용으로 활용할 계획이며, React와 D3.js 또는 Chart.js를 사용할 예정입니다."
        )
        
        builder.add_instructions([
            "금융 API를 활용한 주식 및 암호화폐 데이터 시각화 애플리케이션 개발을 위한 체계적인 접근법을 제안해주세요",
            "다양한 금융 API 통합 전략과 데이터 정규화, 변환 방법을 설명해주세요",
            "차트 및 그래프를 활용한 금융 데이터 시각화 전략과 추천 라이브러리를 제안해주세요",
            "실시간 데이터 업데이트, 대용량 히스토리 데이터 처리, 성능 최적화 전략을 상세히 설명해주세요",
            "개발 단계별 명세와 함께 각 단계에서 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
        
    elif "뉴스 API" in topic:
        builder.add_role(
            "뉴스 애플리케이션 아키텍트", 
            "뉴스 API를 활용한 콘텐츠 애그리게이션 애플리케이션 개발 전문가로, 개인화된 뉴스 경험을 제공하는 플랫폼 설계와 구현에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 다양한 소스의 뉴스를 통합하여 개인화된 뉴스 피드를 제공하는 애플리케이션을 개발하려고 합니다. "
            f"이 애플리케이션은 사용자 관심사에 따라 뉴스를 필터링하고, 카테고리별로 정리하며, "
            f"키워드 검색과 저장 기능을 제공할 예정입니다. NewsAPI 또는 Gnews API를 활용할 계획이며, "
            f"React와 Next.js를 프론트엔드로, Node.js를 백엔드로 사용할 예정입니다. "
            f"사용자 프로필 관리를 위해 Firebase 인증을 고려하고 있습니다."
        )
        
        builder.add_instructions([
            "뉴스 API를 활용한 개인화된 뉴스 애그리게이터 개발을 위한 체계적인 접근법을 제안해주세요",
            "뉴스 API 통합 아키텍처와 백엔드 프록시 활용 전략을 상세히 설명해주세요",
            "사용자 선호도 기반 개인화 및 추천 알고리즘 구현 방법을 제안해주세요",
            "콘텐츠 캐싱, 성능 최적화, 오프라인 지원 등의 기술적 전략을 설명해주세요",
            "개발 단계별 아키텍처 문서와 함께 각 단계에서 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
        
    elif "소셜 미디어 API" in topic:
        builder.add_role(
            "소셜 미디어 분석 전문가", 
            "다양한 소셜 미디어 API를 통합한 분석 대시보드 개발 전문가로, 소셜 데이터 수집, 분석, 시각화에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 여러 소셜 미디어 플랫폼(Twitter, Instagram, Facebook 등)의 데이터를 "
            f"통합 분석할 수 있는 대시보드 애플리케이션을 개발하려고 합니다. "
            f"이 애플리케이션은 계정 성과 지표, 게시물 참여도, 팔로워 분석, 해시태그 트렌드 등을 "
            f"시각화하고, 경쟁사 비교 및 인사이트 제공 기능이 필요합니다. "
            f"각 플랫폼의 공식 API를 활용할 계획이며, React와 Recharts 또는 D3.js를 프론트엔드로, "
            f"Node.js를 백엔드로 사용할 예정입니다."
        )
        
        builder.add_instructions([
            "소셜 미디어 API 통합 분석 대시보드 개발을 위한 체계적인 접근법을 제안해주세요",
            "다양한 소셜 미디어 API 통합 전략과 인증, 데이터 수집, 정규화 방법을 설명해주세요",
            "소셜 미디어 데이터 분석 및 시각화를 위한 대시보드 UI/UX 설계와 컴포넌트 구성을 제안해주세요",
            "API 요청 한도, 데이터 캐싱, 성능 최적화 등의 기술적 고려사항을 상세히 설명해주세요",
            "개발 단계별 로드맵과 함께 각 단계에서 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
        
    else:
        builder.add_role(
            "API 통합 웹 개발자", 
            "다양한 외부 API를 활용한 웹 애플리케이션 개발 전문가로, API 통합 아키텍처 설계와 구현에 깊은 경험을 가진 전문가입니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있는 개발자입니다. "
            f"외부 API를 활용한 웹 애플리케이션을 개발하려고 하며, "
            f"효과적인 API 통합 방법, 데이터 처리 전략, 사용자 인터페이스 설계에 대한 "
            f"체계적인 접근법을 알고 싶습니다."
        )
        
        builder.add_instructions([
            f"{topic}을 위한 체계적인 개발 접근법을 제안해주세요",
            "API 통합 아키텍처 패턴과 적합한 상황을 설명해주세요",
            "API 데이터 처리, 캐싱, 오류 처리 전략을 상세히 설명해주세요",
            "사용자 인터페이스 설계 및 데이터 시각화 방법을 제안해주세요",
            "개발 단계별 접근법과 AI를 활용한 개발 가속화 방법도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"코드 예시와 구현 패턴을 포함하여 실제 개발에 참고할 수 있게 해주세요. "
        f"API 통합 아키텍처, 데이터 처리 전략, UI 컴포넌트 설계 등에 대한 구체적인 접근법을 제시해주세요. "
        f"실제 개발 시 발생할 수 있는 문제점과 해결 방법, 최적화 전략도 포함해주세요. "
        f"가능한 경우 다이어그램이나 표를 사용하여 설명을 보완해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="API 활용 웹 애플리케이션 개발",
        topic_options=API_WEB_APP_TOPICS,
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