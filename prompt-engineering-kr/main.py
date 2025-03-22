"""
프롬프트 엔지니어링 교안 메인 모듈

다양한 파트의 실습 코드를 실행하고 관리하는 기능을 제공합니다.
"""

import os
import sys
import argparse
from typing import Dict, List, Any, Optional
import shutil

# 교안 파트 및 섹션 정보
COURSE_PARTS = [
    # Part 0: 프롬프트 엔지니어링 입문
    {"part_id": "0", "title": "프롬프트 엔지니어링 입문", 
     "description": "생성형 AI와 프롬프트 엔지니어링의 기본 개념 이해"},
    {"part_id": "0.1", "title": "생성형 AI와 프롬프트 엔지니어링 이해하기", 
     "description": "생성형 AI의 기본 개념과 프롬프트 엔지니어링의 중요성"},
    {"part_id": "0.2", "title": "대화 모델로 접근하기", 
     "description": "AI와의 대화를 통한 직관적 이해 및 실험 마인드셋"},
    {"part_id": "0.3", "title": "실습 환경 준비 및 기본 팁", 
     "description": "API 연결 설정 및 효과적인 사용 팁"},
    
    # Part 1: 기초 프롬프트 작성법
    {"part_id": "1", "title": "기초 프롬프트 작성법", 
     "description": "효과적인 지시문 작성과 정보 수집 방법"},
    {"part_id": "1.1", "title": "명확한 지시문 작성하기", 
     "description": "구체적인 요청과 명확한 지시로 원하는 응답 얻기"},
    {"part_id": "1.2", "title": "배경 지식 없이 질문하기", 
     "description": "낯선 주제에 대해 단계적으로 지식 쌓는 방법"},
    {"part_id": "1.3", "title": "정보 수집과 정제의 기술", 
     "description": "AI를 활용한 효과적인 정보 수집 및 정리 방법"},
    {"part_id": "1.4", "title": "낯선 주제 탐색하기", 
     "description": "완전히 새로운 주제에 대한 탐색 전략"},
    
    # Part 2: 복잡한 과제 분해하기
    {"part_id": "2", "title": "복잡한 과제 분해하기", 
     "description": "큰 프로젝트와 과제를 관리 가능한 단위로 분해하는 방법"},
    {"part_id": "2.1", "title": "과제 분석과 분해 전략", 
     "description": "복잡한 과제의 요구사항 파악 및 구조화 방법"},
    {"part_id": "2.2", "title": "정보 수집과 검증의 순환", 
     "description": "필요한 정보를 수집하고 검증하는 반복적 과정"},
    {"part_id": "2.3", "title": "통합적 관점 구축하기", 
     "description": "수집한 정보를 종합하여 전체 그림 그리기"},
    {"part_id": "2.4", "title": "복잡한 과제 분해 연습", 
     "description": "실제 과제를 단계별로 분해하는 실습"},
    
    # Part 3: 맥락 유지와 대화 관리
    {"part_id": "3", "title": "맥락 유지와 대화 관리", 
     "description": "긴 대화와 복잡한 맥락을 효과적으로 관리하는 방법"},
    {"part_id": "3.1", "title": "토큰 제한 극복하기", 
     "description": "AI 모델의 토큰 제한을 효과적으로 다루는 전략"},
    {"part_id": "3.2", "title": "대화 재설정 기술", 
     "description": "대화를 효과적으로 재시작하고 맥락 유지하기"},
    {"part_id": "3.3", "title": "프롬프트 관리 시스템", 
     "description": "프롬프트 버전 관리와 체계적 저장 방법"},
    {"part_id": "3.4", "title": "장기 프로젝트 관리하기", 
     "description": "장기간 진행되는 프로젝트의 일관성 유지 방법"},
    
    # Part 4: 학술 에세이 및 보고서 작성
    {"part_id": "4", "title": "학술 에세이 및 보고서 작성", 
     "description": "학술적 글쓰기 향상을 위한 AI 활용 방법"},
    {"part_id": "4.1", "title": "연구 주제 탐색 및 구체화", 
     "description": "광범위한 연구 분야에서 구체적 주제 도출"},
    {"part_id": "4.2", "title": "논리적 구조 개발", 
     "description": "설득력 있는 에세이 구조와 논증 흐름 설계"},
    {"part_id": "4.3", "title": "학술적 표현과 인용", 
     "description": "효과적인 학술 표현과 올바른 인용 방법"},
    {"part_id": "4.4", "title": "보고서 개선하기", 
     "description": "기존 보고서의 품질을 향상시키는 방법"},
    
    # Part 5: 프로그래밍 과제 해결
    {"part_id": "5", "title": "프로그래밍 과제 해결", 
     "description": "코딩 문제 해결과 소프트웨어 개발 지원"},
    {"part_id": "5.1", "title": "코딩 개념 이해하기", 
     "description": "복잡한 프로그래밍 개념의 학습과 적용"},
    {"part_id": "5.2", "title": "코드 생성과 최적화", 
     "description": "효율적인 코드 작성과 성능 최적화"},
    {"part_id": "5.3", "title": "프로젝트 구조화와 관리", 
     "description": "소프트웨어 프로젝트의 아키텍처 설계"},
    {"part_id": "5.4", "title": "프로그래밍 프로젝트 개발", 
     "description": "전체 프로그래밍 프로젝트 진행 전략"},
    
    # Part 6-9 요약 (간략화)
    {"part_id": "6", "title": "도메인별 프롬프트 최적화", 
     "description": "다양한 학문 및 전문 분야별 맞춤형 프롬프트 전략"},
    {"part_id": "7", "title": "고급 프롬프트 테크닉", 
     "description": "역할 기반 프롬프팅, 단계적 사고 유도 등 고급 기법"},
    {"part_id": "8", "title": "프롬프트 디버깅과 개선", 
     "description": "문제가 있는 프롬프트의 분석과 체계적 개선 방법"},
    {"part_id": "9", "title": "윤리적 활용과 한계 인식", 
     "description": "AI의 책임감 있는 활용과 학문적 진실성 유지"}
]

def parse_arguments():
    """
    명령줄 인자 파싱
    
    Returns:
        파싱된 인자
    """
    parser = argparse.ArgumentParser(description="프롬프트 엔지니어링 교안 실행 도구")

    parser.add_argument('--run', type=str, 
                        help='실행할 파트/섹션 ID (예: 1.2)')
    parser.add_argument('--list', action='store_true', 
                        help='사용 가능한 파트 및 섹션 목록 표시')
    parser.add_argument('--config', action='store_true', 
                        help='설정 파일 확인 및 수정')
    
    return parser.parse_args()

def list_parts():
    """
    사용 가능한 파트 및 섹션 목록 표시
    """
    print("\n===== 프롬프트 엔지니어링 교안 목차 =====\n")
    
    current_main_part = None
    
    for part in COURSE_PARTS:
        part_id = part["part_id"]
        title = part["title"]
        description = part.get("description", "")
        
        # 메인 파트 구분
        if len(part_id) == 1:
            current_main_part = part_id
            print(f"\n[Part {part_id}] {title}")
            print(f"  - {description}")
        
        # 섹션 표시
        elif "." in part_id:
            main_part = part_id.split(".")[0]
            # 들여쓰기로 계층 표현
            print(f"  ● {part_id}: {title}")
            if description:
                print(f"    - {description}")
    
    print("\n실행 방법: python main.py --run <파트ID 또는 섹션ID>")

def run_exercise(part_id: str):
    """
    특정 파트 또는 섹션의 실습 코드 실행
    
    Args:
        part_id: 실행할 파트 또는 섹션 ID (예: "1", "1.2")
    """
    # 파트/섹션 유효성 검사
    valid_parts = [p["part_id"] for p in COURSE_PARTS]
    if part_id not in valid_parts:
        print(f"오류: '{part_id}'를 찾을 수 없습니다.")
        print("사용 가능한 파트 및 섹션 목록을 확인하려면 --list 옵션을 사용하세요.")
        return
    
    # 파트/섹션 정보 찾기
    part_info = next((p for p in COURSE_PARTS if p["part_id"] == part_id), None)
    if not part_info:
        print(f"오류: '{part_id}' 정보를 찾을 수 없습니다.")
        return
    
    # 메인 파트인 경우 (예: "1", "2") - 해당 파트의 모든 섹션 실행
    if len(part_id) == 1:
        print(f"\n===== Part {part_id}: {part_info['title']} =====\n")
        
        # 해당 파트의 모든 섹션 찾기
        sections = [p for p in COURSE_PARTS if p["part_id"].startswith(f"{part_id}.")]
        
        if not sections:
            print(f"이 파트에 실행 가능한 섹션이 없습니다.")
            return
        
        # 첫 번째 섹션만 실행 (또는 사용자 선택 가능)
        first_section = sections[0]
        print(f"섹션 {first_section['part_id']}: {first_section['title']}을(를) 실행합니다.\n")
        run_section_exercise(first_section["part_id"])
    
    # 섹션인 경우 (예: "1.1", "2.3") - 해당 섹션 실행
    else:
        run_section_exercise(part_id)

def run_section_exercise(section_id: str):
    """
    특정 섹션의 실습 코드 실행
    
    Args:
        section_id: 실행할 섹션 ID (예: "1.2")
    """
    # 섹션 정보 찾기
    section_info = next((p for p in COURSE_PARTS if p["part_id"] == section_id), None)
    if not section_info:
        print(f"오류: 섹션 '{section_id}' 정보를 찾을 수 없습니다.")
        return
    
    main_part = section_id.split(".")[0]
    
    # 스크립트 파일 경로 구성
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "exercises",
        f"part{main_part}",
        section_id,
        f"{section_id}_{section_info['title'].lower().replace(' ', '_').replace('-', '_')}.py"
    )
    
    # 파일 존재 확인
    if not os.path.exists(script_path):
        # 섹션의 모든 파일 경로 체크
        section_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "exercises",
            f"part{main_part}",
            section_id
        )
        
        # 디렉토리는 있지만 파일이 없는 경우
        files = os.listdir(section_dir)
        if not files:
            print(f"오류: 실행할 파일이 없습니다. 섹션 {section_id} 디렉토리가 비어 있습니다.")
            return
        
        # 첫 번째 파일 선택 (또는 특정 패턴 매칭)
        for file in files:
            if file.startswith(f"{section_id}_") and file.endswith(".py"):
                script_path = os.path.join(section_dir, file)
                break
        else:
            print(f"오류: 섹션 {section_id}에 적합한 실행 파일을 찾을 수 없습니다.")
            return
    
    # 스크립트 실행
    print(f"\n===== 섹션 {section_id}: {section_info['title']} =====\n")
    
    try:
        # 상대 경로에서 모듈 import 문제 방지를 위해 해당 디렉토리로 이동
        original_dir = os.getcwd()
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        
        # 스크립트 파일 이름 추출 (.py 제거)
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
    try:
        from utils.config import load_config, get_setting, update_setting
        
        config = load_config()
        
        print("\n===== 현재 설정 =====\n")
        print(f"AI 제공자: {get_setting('ai.provider')}")
        print(f"AI 모델: {get_setting('ai.model')}")
        print(f"기본 온도: {get_setting('ai.temperature')}")
        print(f"최대 토큰: {get_setting('ai.max_tokens')}")
        print(f"결과 저장: {get_setting('output.save_results')}")
        print(f"결과 디렉토리: {get_setting('output.results_dir')}")
        
        while True:
            print("\n수정할 설정 선택 (종료하려면 q 입력):")
            print("1. AI 제공자 (openai/gemini/anthropic)")
            print("2. AI 모델")
            print("3. 응답 온도 (0.0-1.0)")
            print("4. 최대 토큰 수")
            print("5. 결과 저장 여부")
            print("6. 결과 디렉토리 경로")
            
            choice = input("\n선택 (1-6, q): ").strip().lower()
            
            if choice == 'q':
                break
                
            try:
                if choice == '1':
                    value = input("AI 제공자 (openai/gemini/anthropic): ").strip()
                    update_setting('ai.provider', value)
                    
                elif choice == '2':
                    value = input("AI 모델: ").strip()
                    update_setting('ai.model', value)
                    
                elif choice == '3':
                    value = float(input("응답 온도 (0.0-1.0): ").strip())
                    update_setting('ai.temperature', value)
                    
                elif choice == '4':
                    value = int(input("최대 토큰 수: ").strip())
                    update_setting('ai.max_tokens', value)
                    
                elif choice == '5':
                    value = input("결과 저장 여부 (true/false): ").strip().lower() == 'true'
                    update_setting('output.save_results', value)
                    
                elif choice == '6':
                    value = input("결과 디렉토리 경로: ").strip()
                    update_setting('output.results_dir', value)
                    
                else:
                    print("잘못된 선택입니다.")
                    continue
                    
                print("설정이 업데이트되었습니다.")
                
            except Exception as e:
                print(f"설정 업데이트 중 오류 발생: {e}")
    except ImportError:
        print("오류: utils.config 모듈을 불러올 수 없습니다.")
        print("설정 관련 기능을 사용하려면 필요한 모듈을 설치하세요.")

def main():
    """
    메인 함수
    """
    # 명령줄 인자 파싱
    args = parse_arguments()
    
    # 인자에 따른 동작 수행
    if args.setup:
        setup_project()
    elif args.list:
        list_parts()
    elif args.config:
        edit_config()
    elif args.run:
        run_exercise(args.run)
    else:
        # 기본: 사용법 표시
        print("\n프롬프트 엔지니어링 교안 실행 도구\n")
        print("사용법:")
        print("  python main.py --list        # 목차 및 가용 파트 표시")
        print("  python main.py --run 1.2     # 특정 파트/섹션 실행")
        print("  python main.py --config      # 설정 확인 및 수정")

if __name__ == "__main__":
    main()