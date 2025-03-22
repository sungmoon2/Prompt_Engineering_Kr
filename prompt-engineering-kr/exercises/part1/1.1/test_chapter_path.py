"""
향상된 챕터 경로 추출 및 결과 폴더 생성 테스트 스크립트

실행 방법: 프로젝트 루트에서 `python test_chapter_path_improved.py` 명령 실행
"""

import os
import sys
import re
import inspect
from typing import Optional, Tuple

# 현재 파일의 절대 경로
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)

print(f"현재 파일: {current_file}")
print(f"현재 디렉토리: {current_dir}")

# 프로젝트 루트 찾기
project_root = current_dir
while project_root and os.path.basename(project_root).lower() != 'prompt-engineering-kr':
    parent = os.path.dirname(project_root)
    if parent == project_root:  # 루트에 도달
        break
    project_root = parent

print(f"프로젝트 루트: {project_root}")

# 시스템 경로 출력
print("\n시스템 경로:")
for i, path in enumerate(sys.path):
    print(f"  {i}: {path}")

# 직접 get_chapter_info 함수 구현
def get_chapter_info_direct(file_path: str) -> Tuple[Optional[str], str, str]:
    """
    파일 경로에서 챕터 정보를 직접 추출
    
    Args:
        file_path: 파일 경로
        
    Returns:
        챕터 ID, 챕터 이름, 프로젝트 루트 경로
    """
    print(f"\n직접 구현한 get_chapter_info 함수 호출:")
    print(f"분석 중인 파일: {file_path}")
    
    # 파일 경로 정규화
    file_path = os.path.abspath(file_path)
    file_basename = os.path.basename(file_path)
    print(f"파일 이름: {file_basename}")
    
    # 기본값 설정
    chapter_id = None
    chapter_name = "unknown"
    
    # 1. 파일 이름에서 챕터 정보 추출 (예: 1.1_clear_instructions.py)
    # 패턴 1: 1.1_clear_instructions.py
    match = re.match(r'^(\d+\.\d+)_(.+?)\.py$', file_basename)
    if match:
        chapter_id = match.group(1)
        chapter_name = match.group(2)
        print(f"기본 패턴 매치: chapter_id={chapter_id}, chapter_name={chapter_name}")
    
    # 패턴 2: 1.1.1_specific_requests.py
    if not match:
        match = re.match(r'^(\d+\.\d+\.\d+)_(.+?)\.py$', file_basename)
        if match:
            chapter_id = match.group(1)
            chapter_name = match.group(2)
            print(f"하위 챕터 패턴 매치: chapter_id={chapter_id}, chapter_name={chapter_name}")
    
    # 2. 경로에서 챕터 정보 추출 (예: .../exercises/part1/1.1/...)
    if chapter_id is None:
        normalized_path = file_path.replace('\\', '/')
        match = re.search(r'/exercises/part\d+/(\d+\.\d+)/', normalized_path)
        if match:
            chapter_id = match.group(1)
            print(f"경로에서 챕터 ID 추출: chapter_id={chapter_id}")
            
            # 챕터 이름은 파일명에서 가져옴
            if '_' in file_basename:
                chapter_name = file_basename.split('_', 1)[1].split('.', 1)[0]
            else:
                chapter_name = os.path.splitext(file_basename)[0]
            print(f"파일 이름에서 챕터 이름 추출: chapter_name={chapter_name}")
    
    # 3. 디렉토리 이름에서 챕터 정보 추출
    if chapter_id is None:
        dir_name = os.path.basename(os.path.dirname(file_path))
        if re.match(r'^\d+\.\d+$', dir_name):
            chapter_id = dir_name
            print(f"디렉토리 이름에서 챕터 ID 추출: chapter_id={chapter_id}")
            
            # 챕터 이름은 파일명에서 가져옴
            if '_' in file_basename:
                file_parts = os.path.splitext(file_basename)[0].split('_', 1)
                if len(file_parts) > 1:
                    chapter_name = file_parts[1]
            else:
                chapter_name = os.path.splitext(file_basename)[0]
            print(f"파일 이름에서 챕터 이름 추출: chapter_name={chapter_name}")
    
    print(f"최종 결과: chapter_id={chapter_id}, chapter_name={chapter_name}")
    return (chapter_id, chapter_name, project_root)

# 직접 구현한 results 디렉토리 경로 생성 함수
def get_results_path_direct(file_path: str) -> str:
    """
    파일 경로에서 결과 저장 경로를 직접 생성
    
    Args:
        file_path: 파일 경로
        
    Returns:
        결과 저장 경로
    """
    print(f"\n직접 구현한 get_results_path 함수 호출:")
    
    # 챕터 정보 추출
    chapter_id, chapter_name, project_root = get_chapter_info_direct(file_path)
    
    # 결과 폴더 경로 생성
    if chapter_id:
        # 파트 번호 추출 (예: 1.1 -> 1)
        if '.' in chapter_id:
            part_num = chapter_id.split('.')[0]
            part_path = f"part{part_num}"
            
            # 챕터 경로 생성
            chapter_parts = chapter_id.split('.')
            if len(chapter_parts) == 2:  # 예: 1.1
                results_dir = os.path.join(project_root, "results", part_path, chapter_id)
            elif len(chapter_parts) == 3:  # 예: 1.1.1
                parent_chapter = f"{chapter_parts[0]}.{chapter_parts[1]}"
                results_dir = os.path.join(project_root, "results", part_path, parent_chapter, chapter_id)
            else:
                results_dir = os.path.join(project_root, "results", f"{chapter_id}_{chapter_name}")
        else:
            results_dir = os.path.join(project_root, "results", f"{chapter_id}_{chapter_name}")
    else:
        results_dir = os.path.join(project_root, "results")
    
    print(f"생성된 결과 경로: {results_dir}")
    return results_dir

def test_file_path(file_path):
    """
    주어진 파일 경로에 대한 챕터 정보 및 결과 디렉토리 테스트
    """
    print("\n" + "=" * 70)
    print(f"테스트 파일: {file_path}")
    print("=" * 70)
    
    # 직접 구현한 함수로 테스트
    chapter_id, chapter_name, root = get_chapter_info_direct(file_path)
    results_dir = get_results_path_direct(file_path)
    
    print(f"\n생성된 결과 경로가 존재하는지 확인:")
    if os.path.exists(os.path.dirname(results_dir)):
        parent_dir = os.path.dirname(results_dir)
        print(f"  상위 디렉토리 존재: {parent_dir}")
        
        # 필요한 디렉토리 생성
        os.makedirs(results_dir, exist_ok=True)
        print(f"  결과 디렉토리 생성 완료: {results_dir}")
    else:
        print(f"  상위 디렉토리가 존재하지 않습니다: {os.path.dirname(results_dir)}")

def main():
    """
    메인 함수
    """
    print("\n챕터 경로 추출 및 결과 폴더 생성 테스트 (향상된 버전)")
    print("================================================")
    
    # 테스트할 파일 경로 목록
    test_files = []
    
    # 실제 exercises 디렉토리에서 파일 찾기
    if os.path.exists(os.path.join(project_root, "exercises")):
        for part_dir in os.listdir(os.path.join(project_root, "exercises")):
            if part_dir.startswith("part"):
                part_path = os.path.join(project_root, "exercises", part_dir)
                if os.path.isdir(part_path):
                    for chapter_dir in os.listdir(part_path):
                        chapter_path = os.path.join(part_path, chapter_dir)
                        if os.path.isdir(chapter_path) and re.match(r'^\d+\.\d+$', chapter_dir):
                            # 폴더에서 Python 파일 찾기
                            for file in os.listdir(chapter_path):
                                if file.endswith(".py"):
                                    test_files.append(os.path.join(chapter_path, file))
                                    break  # 각 챕터당 한 파일만 테스트
    
    # 테스트 파일이 없으면 현재 파일 추가
    if not test_files:
        test_files.append(__file__)
    
    # 각 파일에 대해 테스트 실행
    for file_path in test_files:
        if os.path.exists(file_path):
            test_file_path(file_path)
        else:
            print(f"\n파일이 존재하지 않습니다: {file_path}")
    
    print("\n테스트 완료")

if __name__ == "__main__":
    main()