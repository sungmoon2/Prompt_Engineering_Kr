"""
프롬프트 엔지니어링 교안 메인 모듈

다양한 챕터의 실습 코드를 생성하고 실행하는 기능을 제공합니다.
"""

import os
import sys
import argparse
from typing import Dict, List, Any, Optional

from utils.config import load_config, get_setting
from utils.logger import setup_logger, get_logger
from utils.script_generator import create_project_structure
from utils.example_provider import get_sample_research_topics

# 교안 챕터 정보
COURSE_CHAPTERS = [
    # 1.1 리포트 품질 향상 기법
    {"chapter_id": "1.1", "title": "리포트 품질 향상 기법", 
     "description": "주제 분석, 논리적 구조 설계, 인용 최적화, 맞춤형 과제 작성을 위한 통합 도구"},
    {"chapter_id": "1.1.1", "title": "주제 분석 및 논점 도출을 위한 프롬프트", 
     "description": "주제를 깊이 있게 분석하고 핵심 논점을 도출하기 위한 프롬프트 기술"},
    {"chapter_id": "1.1.2", "title": "논리적 구조와 흐름 설계 프롬프트", 
     "description": "효과적인 리포트 구조와 논리적 흐름을 설계하는 프롬프트 패턴"},
    {"chapter_id": "1.1.3", "title": "참고문헌 및 인용 최적화 전략", 
     "description": "학술적 인용과 참고문헌 관리를 최적화하는 프롬프트 기법"},
    {"chapter_id": "1.1.4", "title": "교수 유형별 맞춤형 과제 작성 가이드", 
     "description": "다양한 교수 유형과 평가 스타일에 맞춘 과제 작성 전략"},
    
    # 1.2 전공별 맞춤형 리포트 작성
    {"chapter_id": "1.2", "title": "전공별 맞춤형 리포트 작성", 
     "description": "다양한 학문 분야별 최적화된 리포트 작성 도구"},
    {"chapter_id": "1.2.1", "title": "인문사회계열 리포트 작성 프롬프트", 
     "description": "인문학, 사회과학 분야의 리포트 작성을 위한 특화 프롬프트"},
    {"chapter_id": "1.2.2", "title": "이공계 실험 보고서 템플릿", 
     "description": "공학, 자연과학 분야의 실험 보고서 작성을 위한 템플릿"},
    
    # 2.1 코딩 개념 이해 및 학습
    {"chapter_id": "2.1", "title": "코딩 개념 이해 및 학습", 
     "description": "프로그래밍 개념 학습과 이해를 돕는 도구"},
    {"chapter_id": "2.1.1", "title": "프로그래밍 개념 설명 프롬프트", 
     "description": "복잡한 프로그래밍 개념을 이해하기 쉽게 설명받는 프롬프트 기법"},
    
    # 3.1 연구 계획 및 설계
    {"chapter_id": "3.1", "title": "연구 계획 및 설계", 
     "description": "효과적인 연구 계획과 방법론 설계를 위한 도구"},
    {"chapter_id": "3.1.1", "title": "연구 주제 구체화 프롬프트", 
     "description": "광범위한 관심사에서 구체적인 연구 주제로 좁혀나가는 프롬프트 기법"},
    
    # 4.1 이력서 및 자기소개서 작성
    {"chapter_id": "4.1", "title": "이력서 및 자기소개서 작성", 
     "description": "취업 준비를 위한 문서 작성 최적화 도구"},
    {"chapter_id": "4.1.1", "title": "직무별 이력서 최적화 프롬프트", 
     "description": "다양한 직무와 산업에 맞춘 이력서 작성을 위한 프롬프트 패턴"},
    
    # 5.1 역할 기반 프롬프팅
    {"chapter_id": "5.1", "title": "역할 기반 프롬프팅", 
     "description": "다양한 전문가 역할을 활용한 프롬프트 기법"},
    {"chapter_id": "5.1.1", "title": "학술/전문가 역할 지정 프롬프트", 
     "description": "특정 분야의 전문가 관점에서 응답을 유도하는 프롬프트 패턴"},
    
    # 5.2 단계적 사고 유도
    {"chapter_id": "5.2", "title": "단계적 사고 유도 (Chain-of-Thought)", 
     "description": "복잡한 문제를 단계별로 사고하는 프롬프트 패턴"},
    
    # 6.1 학기 과제 완벽 지원 시스템
    {"chapter_id": "6.1", "title": "학기 과제 완벽 지원 시스템", 
     "description": "과목별 과제 계획과 실행을 위한 통합 시스템"},
    
    # 7.1 AI 활용의 윤리적 경계
    {"chapter_id": "7.1", "title": "AI 활용의 윤리적 경계", 
     "description": "학업에서 AI 활용의 윤리적 가이드라인"}
]


def parse_arguments():
    """
    명령줄 인자 파싱
    
    Returns:
        파싱된 인자
    """
    parser = argparse.ArgumentParser(description="프롬프트 엔지니어링 교안 실행 도구")
    
    parser.add_argument('--setup', action='store_true', 
                        help='프로젝트 구조 초기 설정')
    parser.add_argument('--chapter', type=str, 
                        help='실행할 챕터 ID (예: 1.1.2)')
    parser.add_argument('--list', action='store_true', 
                        help='사용 가능한 챕터 목록 표시')
    parser.add_argument('--config', action='store_true', 
                        help='설정 파일 확인 및 수정')
    
    return parser.parse_args()


def setup_project():
    """
    프로젝트 초기 설정 (디렉토리 및 파일 생성)
    """
    logger = get_logger()
    logger.info("프로젝트 구조 초기화 중...")
    
    # 필요한 디렉토리 생성
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dirs = ["chapter1", "chapter2", "chapter3", "chapter4", 
           "chapter5", "chapter6", "chapter7", "results", "examples", "logs"]
    
    for d in dirs:
        dir_path = os.path.join(base_dir, d)
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"디렉토리 생성: {dir_path}")
    
    # 모든 챕터 스크립트 생성
    created_files = create_project_structure(COURSE_CHAPTERS, base_dir)
    
    logger.info(f"총 {len(created_files)} 개의 스크립트 파일이 생성되었습니다.")
    print(f"\n프로젝트 구조가 성공적으로 초기화되었습니다.")
    print(f"총 {len(created_files)} 개의 스크립트 파일이 생성되었습니다.")


def list_chapters():
    """
    사용 가능한 챕터 목록 표시
    """
    print("\n===== 프롬프트 엔지니어링 교안 챕터 =====\n")
    
    current_main_chapter = None
    
    for chapter in COURSE_CHAPTERS:
        chapter_id = chapter["chapter_id"]
        title = chapter["title"]
        description = chapter.get("description", "")
        
        # 메인 챕터 구분
        main_chapter = chapter_id.split('.')[0]
        if main_chapter != current_main_chapter:
            current_main_chapter = main_chapter
            print(f"\n[챕터 {main_chapter}]")
        
        # 들여쓰기로 계층 표현
        indent = "  " * (len(chapter_id.split('.')) - 1)
        print(f"{indent}● {chapter_id}: {title}")
        
        if description:
            print(f"{indent}  - {description}")
    
    print("\n실행 방법: python main.py --chapter <챕터ID>")


def run_chapter(chapter_id: str):
    """
    특정 챕터 스크립트 실행
    
    Args:
        chapter_id: 실행할 챕터 ID
    """
    # 챕터 유효성 검사
    valid_chapters = [c["chapter_id"] for c in COURSE_CHAPTERS]
    if chapter_id not in valid_chapters:
        print(f"오류: 챕터 '{chapter_id}'를 찾을 수 없습니다.")
        print("사용 가능한 챕터 목록을 확인하려면 --list 옵션을 사용하세요.")
        return
    
    # 챕터 정보 찾기
    chapter_info = next((c for c in COURSE_CHAPTERS if c["chapter_id"] == chapter_id), None)
    if not chapter_info:
        print(f"오류: 챕터 '{chapter_id}' 정보를 찾을 수 없습니다.")
        return
    
    # 스크립트 파일 경로 구성
    main_chapter = chapter_id.split('.')[0]
    safe_title = chapter_info["title"].lower()
    safe_title = ''.join(c if c.isalnum() else '_' for c in safe_title).replace('__', '_')
    
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f"chapter{main_chapter}",
        f"{chapter_id.replace('.', '_')}_{safe_title}.py"
    )
    
    # 파일 존재 확인
    if not os.path.exists(script_path):
        print(f"오류: 스크립트 파일을 찾을 수 없습니다: {script_path}")
        print("먼저 --setup 옵션으로 프로젝트를 초기화하세요.")
        return
    
    # 스크립트 실행
    print(f"\n===== 챕터 {chapter_id}: {chapter_info['title']} =====\n")
    
    try:
        # 상대 경로에서 모듈 import 문제 방지를 위해 해당 디렉토리로 이동
        original_dir = os.getcwd()
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        
        # 스크립트 실행 (exec 대신 import 사용)
        script_name = os.path.basename(script_path).replace('.py', '')
        sys.path.insert(0, script_dir)
        
        try:
            # 동적으로 모듈 import 및 main 함수 실행
            module = __import__(script_name)
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"주의: '{script_name}' 모듈에 main() 함수가 없습니다.")
        finally:
            # 원래 디렉토리로 복원
            os.chdir(original_dir)
            
    except Exception as e:
        print(f"스크립트 실행 중 오류 발생: {e}")


def edit_config():
    """
    설정 파일 확인 및 수정
    """
    config = load_config()
    
    print("\n===== 현재 설정 =====\n")
    print(f"AI 제공자: {get_setting('ai.provider')}")
    print(f"AI 모델: {get_setting('ai.model')}")
    print(f"기본 온도: {get_setting('ai.temperature')}")
    print(f"최대 토큰: {get_setting('ai.max_tokens')}")
    print(f"결과 저장: {get_setting('output.save_results')}")
    print(f"결과 디렉토리: {get_setting('output.results_dir')}")
    print(f"로깅 활성화: {get_setting('logging.enabled')}")
    
    while True:
        print("\n수정할 설정 선택 (종료하려면 q 입력):")
        print("1. AI 제공자 (openai/anthropic)")
        print("2. AI 모델")
        print("3. 응답 온도 (0.0-1.0)")
        print("4. 최대 토큰 수")
        print("5. 결과 저장 여부")
        print("6. 결과 디렉토리 경로")
        print("7. 로깅 활성화 여부")
        
        choice = input("\n선택 (1-7, q): ").strip().lower()
        
        if choice == 'q':
            break
            
        try:
            if choice == '1':
                value = input("AI 제공자 (openai/anthropic): ").strip()
                from utils.config import update_setting
                update_setting('ai.provider', value)
                
            elif choice == '2':
                value = input("AI 모델: ").strip()
                from utils.config import update_setting
                update_setting('ai.model', value)
                
            elif choice == '3':
                value = float(input("응답 온도 (0.0-1.0): ").strip())
                from utils.config import update_setting
                update_setting('ai.temperature', value)
                
            elif choice == '4':
                value = int(input("최대 토큰 수: ").strip())
                from utils.config import update_setting
                update_setting('ai.max_tokens', value)
                
            elif choice == '5':
                value = input("결과 저장 여부 (true/false): ").strip().lower() == 'true'
                from utils.config import update_setting
                update_setting('output.save_results', value)
                
            elif choice == '6':
                value = input("결과 디렉토리 경로: ").strip()
                from utils.config import update_setting
                update_setting('output.results_dir', value)
                
            elif choice == '7':
                value = input("로깅 활성화 여부 (true/false): ").strip().lower() == 'true'
                from utils.config import update_setting
                update_setting('logging.enabled', value)
                
            else:
                print("잘못된 선택입니다.")
                continue
                
            print("설정이 업데이트되었습니다.")
            
        except Exception as e:
            print(f"설정 업데이트 중 오류 발생: {e}")


def main():
    """
    메인 함수
    """
    # 로거 설정
    setup_logger()
    
    # 명령줄 인자 파싱
    args = parse_arguments()
    
    # 인자에 따른 동작 수행
    if args.setup:
        setup_project()
    elif args.list:
        list_chapters()
    elif args.config:
        edit_config()
    elif args.chapter:
        run_chapter(args.chapter)
    else:
        # 기본: 사용법 표시
        print("\n프롬프트 엔지니어링 교안 실행 도구\n")
        print("사용법:")
        print("  python main.py --setup       # 프로젝트 구조 초기화")
        print("  python main.py --list        # 챕터 목록 표시")
        print("  python main.py --chapter 1.1 # 특정 챕터 실행")
        print("  python main.py --config      # 설정 확인 및 수정")


if __name__ == "__main__":
    main()