"""
코드 문서화 및 주석 생성 기법 실습 모듈

Part 5 - 섹션 5.3.3 실습 코드: 효과적인 코드 문서화와 주석 작성 기법을 학습합니다.
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
CODE_DOCUMENTATION_TOPICS = {
    "1": {"name": "Python 패키지 문서화", "topic": "Python 패키지의 효과적인 문서화 전략", "output_format": "문서화 가이드"},
    "2": {"name": "JavaScript 라이브러리 문서화", "topic": "JavaScript 라이브러리의 API 문서화 방법", "output_format": "JSDoc 템플릿"},
    "3": {"name": "자동화된 문서 생성", "topic": "CI/CD 파이프라인과 연동된 자동 문서 생성 전략", "output_format": "설정 가이드"},
    "4": {"name": "복잡한 알고리즘 주석", "topic": "복잡한 알고리즘 및 비즈니스 로직 주석 작성법", "output_format": "주석 예시"},
    "5": {"name": "팀 문서화 표준", "topic": "개발팀을 위한 코드 문서화 표준 및 가이드라인", "output_format": "표준 문서"}
}

# 프롬프트 요약 정보
PROMPT_SUMMARY = {
    "basic": ["코드 문서화에 대한 일반적 안내 요청"],
    "enhanced": [
        "역할 정의: 문서화 전문가 역할 부여",
        "상세 요구사항: 구체적인 문서화 요구사항 명시",
        "코드 컨텍스트: 프로젝트/코드의 목적과 맥락 제공", 
        "형식 지정: 원하는 문서화 형식과 스타일 명시"
    ]
}

# 학습 포인트
LEARNING_POINTS = [
    "효과적인 코드 문서화는 지식 공유, 유지보수 효율성, 온보딩 가속화에 핵심적입니다",
    "각 프로그래밍 언어별 문서화 컨벤션(Docstrings, JSDoc, Javadoc 등)을 따르는 것이 중요합니다",
    "문서화는 코드의 '무엇'이 아닌 '왜'에 초점을 맞추어 가치를 더합니다",
    "자동화된 문서 생성 도구를 활용하면 문서의 최신성과 일관성을 유지할 수 있습니다",
    "AI를 활용하면 기존 코드에 대한 문서화를 효율적으로 생성하고 개선할 수 있습니다"
]

def get_basic_prompt(topic: str) -> str:
    """기본 프롬프트 생성"""
    return f"{topic}에 대해 알려주세요."

def get_enhanced_prompt(topic: str, purpose: str, output_format: str) -> str:
    """향상된 프롬프트 생성"""
    builder = PromptBuilder()
    
    # 주제별 역할 및 맥락 설정
    if "Python 패키지" in topic:
        builder.add_role(
            "Python 문서화 전문가", 
            "다양한 규모의 Python 프로젝트에서 효과적인 문서화 전략을 설계하고 구현한 풍부한 경험을 가진 전문가입니다. Sphinx, Read the Docs, NumPy/Google 스타일 docstring에 대한 깊은 이해를 보유하고 있습니다."
        )
        
        builder.add_context(
            f"저는 데이터 분석 및 시각화를 위한 중규모 Python 패키지를 개발하고 있습니다. "
            f"이 패키지는 데이터 과학자와 분석가들이 사용할 예정이며, 효과적인 문서화가 필수적입니다. "
            f"현재 코드는 기본적인 docstring이 있지만, 체계적이고 포괄적인 문서화 전략이 필요합니다. "
            f"특히 API 참조, 튜토리얼, 사용 예제를 포함한 문서화 접근법을 수립하고 싶습니다."
        )
        
        builder.add_instructions([
            "Python 패키지의 효과적인 문서화 전략을 설계해주세요",
            "다음 문서화 요소를 포함해주세요: docstring 표준(Google/NumPy 스타일 등), 모듈/패키지 수준 문서, API 참조 문서, 튜토리얼 및 사례",
            "Sphinx, Read the Docs 등 문서 생성 및 호스팅 도구 통합 방법을 설명해주세요",
            "코드 변경 시 문서를 최신 상태로 유지하는 전략을 제안해주세요",
            "다양한 수준의 사용자(초보자부터 전문가까지)를 위한 문서화 접근법을 포함해주세요"
        ])
        
    elif "JavaScript 라이브러리" in topic:
        builder.add_role(
            "JavaScript 문서화 전문가", 
            "JavaScript 라이브러리 및 프레임워크의 API 문서화 전문가로, JSDoc, TypeDoc, Docusaurus 등 다양한 문서화 도구와 접근법에 깊은 경험이 있습니다."
        )
        
        builder.add_context(
            f"저는 데이터 시각화를 위한 JavaScript 라이브러리를 개발하고 있습니다. "
            f"이 라이브러리는 다양한 차트 유형, 데이터 처리 기능, 사용자 정의 옵션을 제공합니다. "
            f"개발자들이 쉽게 이해하고 사용할 수 있도록 명확하고 포괄적인 API 문서가 필요합니다. "
            f"TypeScript로 작성된 코드에 대한 문서화 방법과 예제를 포함한 접근법이 필요합니다."
        )
        
        builder.add_instructions([
            "JavaScript 라이브러리의 API 문서화 방법을 설계해주세요",
            "JSDoc을 활용한 효과적인 문서화 접근법과 모범 사례를 설명해주세요",
            "TypeScript 타입 정의와 문서화를 통합하는 방법을 포함해주세요",
            "주요 클래스, 메서드, 이벤트에 대한 문서화 템플릿과 예시를 제공해주세요",
            "대화형 예제, 샌드박스, 데모 등 API 사용법을 보여주는 방법을 제안해주세요"
        ])
        
    elif "자동화된 문서 생성" in topic:
        builder.add_role(
            "문서화 자동화 전문가", 
            "CI/CD 파이프라인과 연동된 자동화된 문서 생성 시스템 구축 전문가로, 다양한 프로그래밍 언어와 프레임워크에서 문서 생성 자동화 경험이 풍부합니다."
        )
        
        builder.add_context(
            f"저는 여러 마이크로서비스로 구성된 시스템의 개발 팀장입니다. "
            f"코드 변경 시 문서가 자동으로 업데이트되지 않아 문서와 코드의 불일치 문제가 발생하고 있습니다. "
            f"CI/CD 파이프라인과 연동된 자동화된 문서 생성 시스템을 구축하여 "
            f"코드 변경 시 문서가 자동으로 업데이트되고 배포되는 방식을 구현하고자 합니다."
        )
        
        builder.add_instructions([
            "CI/CD 파이프라인과 연동된 자동 문서 생성 전략을 설계해주세요",
            "다양한 언어(Python, JavaScript, Java 등)에 대한 문서 생성 도구와 통합 방법을 설명해주세요",
            "GitHub Actions, Jenkins, GitLab CI 등의 CI/CD 도구에서 문서 생성 파이프라인 구성 방법을 제안해주세요",
            "문서 호스팅 옵션(GitHub Pages, Read the Docs 등)과 연동 방법을 포함해주세요",
            "문서 버전 관리, 코드 변경에 따른 문서 변경 추적 전략을 제시해주세요"
        ])
        
    elif "복잡한 알고리즘" in topic:
        builder.add_role(
            "코드 주석 전문가", 
            "복잡한 알고리즘과 비즈니스 로직에 대한 효과적인 주석 작성 전문가로, 명확하고 유지보수하기 쉬운 코드 설명 방법에 깊은 경험이 있습니다."
        )
        
        builder.add_context(
            f"저는 금융 리스크 분석 시스템을 개발하는 팀의 리더입니다. "
            f"시스템에는 복잡한 통계 알고리즘, 데이터 처리 파이프라인, 비즈니스 규칙 등이 포함되어 있습니다. "
            f"코드는 기술적으로 우수하지만, 주석과 설명이 부족하여 새로운 팀원이 이해하기 어렵습니다. "
            f"복잡한 알고리즘과 비즈니스 로직에 대한 효과적인 주석 작성 방법이 필요합니다."
        )
        
        builder.add_instructions([
            "복잡한 알고리즘 및 비즈니스 로직 주석 작성법을 설계해주세요",
            "알고리즘의 목적, 작동 원리, 가정, 제약사항을 명확히 설명하는 주석 패턴을 제안해주세요",
            "수학적 개념, 비즈니스 규칙, 도메인 지식을 코드 주석에 효과적으로 통합하는 방법을 설명해주세요",
            "코드의 '무엇'이 아닌 '왜'에 초점을 맞춘 주석 작성 전략을 제시해주세요",
            "다양한 프로그래밍 언어에서의 실제 주석 예시를 복잡한 알고리즘 사례와 함께 제공해주세요"
        ])
        
    elif "팀 문서화 표준" in topic:
        builder.add_role(
            "기술 문서화 관리자", 
            "여러 개발팀에 걸쳐 일관된 코드 문서화 표준을 수립하고 구현한 경험이 풍부한 전문가로, 문서화 프로세스 개선과 팀 문화 조성에 전문성을 갖고 있습니다."
        )
        
        builder.add_context(
            f"저는 50명 규모의 개발팀을 이끄는 기술 책임자입니다. "
            f"팀은 여러 프로젝트와 다양한 기술 스택(Python, JavaScript, Java 등)을 다루고 있습니다. "
            f"현재 각 개발자가 자신의 방식대로 문서화를 하고 있어 일관성이 부족하고 품질 차이가 큽니다. "
            f"모든 프로젝트와 언어에 걸쳐 적용할 수 있는 통합된 문서화 표준과 가이드라인이 필요합니다."
        )
        
        builder.add_instructions([
            "개발팀을 위한 코드 문서화 표준 및 가이드라인을 설계해주세요",
            "다양한 프로그래밍 언어(Python, JavaScript, Java 등)에 걸친 일관된 문서화 원칙을 제안해주세요",
            "프로젝트, 모듈, 클래스, 함수 수준에서의 문서화 요구사항과 템플릿을 포함해주세요",
            "문서화 품질 평가, 코드 리뷰 프로세스, 지속적 개선 방법을 설명해주세요",
            "팀에 문서화 문화를 정착시키는 전략과 모범 사례/나쁜 사례 예시를 제공해주세요"
        ])
        
    else:
        builder.add_role(
            "코드 문서화 전문가", 
            "효과적인 코드 문서화 전략과 기법에 대한 깊은 이해를 가진 전문가로, 다양한 프로그래밍 언어와 프로젝트 유형에서 문서화 모범 사례를 구현한 경험이 풍부합니다."
        )
        
        builder.add_context(
            f"저는 {topic}에 관심이 있는 개발자입니다. "
            f"프로젝트의 문서화를 개선하여 코드 이해도를 높이고 유지보수성을 향상시키고자 합니다. "
            f"효과적인 문서화 전략과 구체적인 지침이 필요합니다."
        )
        
        builder.add_instructions([
            f"{topic}에 대한 포괄적인 가이드를 제공해주세요",
            "효과적인 문서화의 기본 원칙과 모범 사례를 설명해주세요",
            "다양한 수준(프로젝트, 모듈, 함수)의 문서화 접근법을 제안해주세요",
            "실제 예시와 템플릿을 통해 적용 방법을 보여주세요",
            "문서화 유지보수 및 지속적 개선 전략도 포함해주세요"
        ])
    
    # 출력 형식 지정
    builder.add_format_instructions(
        f"응답은 {output_format} 형식으로 구성해주세요. "
        f"마크다운 형식을 사용하여 제목, 소제목, 목록 등을 명확히 구분해주세요. "
        f"실제 코드 예시와 주석/문서화 샘플을 포함하여 실용적인 적용 방법을 보여주세요. "
        f"다양한 상황과 난이도에 맞는 문서화 전략을 제시해주세요. "
        f"초보 개발자도 쉽게 따라할 수 있는 단계별 지침과 모범 사례를 포함해주세요. "
        f"가능한 경우 좋은 예시와 나쁜 예시를 비교하여 효과적인 문서화의 특징을 강조해주세요."
    )
    
    return builder.build()

def main():
    """메인 함수"""
    # 실행 결과를 저장할 때 챕터별 폴더 구조를 사용
    run_exercise(
        title="코드 문서화 및 주석 생성 기법",
        topic_options=CODE_DOCUMENTATION_TOPICS,
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