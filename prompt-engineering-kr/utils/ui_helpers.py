"""
사용자 인터페이스 관련 도우미 함수 모듈

실습 코드에서 사용되는 공통 UI 관련 기능을 제공합니다.
"""

from typing import Dict, List, Any, Optional

def print_header(title: str) -> None:
    """
    제목 출력 함수
    
    Args:
        title: 출력할 제목
    """
    print("\n" + "=" * 70)
    print(f"{title}".center(70))
    print("=" * 70 + "\n")

def print_step(num: int, desc: str) -> None:
    """
    단계 출력 함수
    
    Args:
        num: 단계 번호
        desc: 단계 설명
    """
    print(f"\n📍 [단계 {num}] {desc}")

def get_user_input(prompt: str, default: str = "") -> str:
    """
    사용자 입력 함수 (기본값 제공)
    
    Args:
        prompt: 사용자에게 표시할 메시지
        default: 기본값
        
    Returns:
        사용자 입력 또는 기본값
    """
    user_input = input(f"{prompt} [기본값: {default}]: ").strip()
    return user_input if user_input else default

def display_results_comparison(basic_result: str, enhanced_result: str, preview_length: int = 200) -> None:
    """
    두 결과의 비교 표시 함수
    
    Args:
        basic_result: 기본 프롬프트 결과
        enhanced_result: 향상된 프롬프트 결과
        preview_length: 미리보기 길이
    """
    print("\n" + "-" * 35 + " 결과 비교 " + "-" * 35)
    print("\n🔹 기본 프롬프트 결과 (처음 " + str(preview_length) + "자):")
    print("-------------------------------------------")
    print(basic_result[:preview_length] + "..." if len(basic_result) > preview_length else basic_result)
    
    print("\n🔹 향상된 프롬프트 결과 (처음 " + str(preview_length) + "자):")
    print("-------------------------------------------")
    print(enhanced_result[:preview_length] + "..." if len(enhanced_result) > preview_length else enhanced_result)
    
    print("\n" + "-" * 80)
    print("* 전체 결과는 저장된 파일에서 확인할 수 있습니다.")

def print_prompt_summary(prompt_type: str, summary_points: List[str]) -> None:
    """
    프롬프트 요약 출력 함수
    
    Args:
        prompt_type: 프롬프트 유형 (기본/향상된)
        summary_points: 요약 포인트 목록
    """
    print(f"\n{prompt_type} 프롬프트 (요약):")
    
    for i, point in enumerate(summary_points, 1):
        print(f"{i}. {point}")

def print_learning_points(points: List[str]) -> None:
    """
    학습 포인트 출력 함수
    
    Args:
        points: 학습 포인트 목록
    """
    print("\n[이번 실습에서 배운 핵심 포인트]")
    
    for i, point in enumerate(points, 1):
        print(f"{i}. {point}")

def print_next_steps(steps: List[str]) -> None:
    """
    다음 단계 제안 출력 함수
    
    Args:
        steps: 다음 단계 제안 목록
    """
    print("\n다음 단계 제안:")
    
    for step in steps:
        print(f"- {step}")

def print_comparison_points(points: Dict[str, List[str]]) -> None:
    """
    비교 포인트 출력 함수
    
    Args:
        points: 비교 포인트 딕셔너리
    """
    print("\n[프롬프트 개선 효과]")
    
    for title, details in points.items():
        print(f"{title}")
        for detail in details:
            print(f"   - {detail}")