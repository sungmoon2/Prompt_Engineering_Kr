"""
results 폴더 아래에 part1부터 part9까지의 챕터 구조를 생성하는 스크립트

실행 방법: 프로젝트 루트에서 `python create_folder_structure.py` 명령 실행
"""

import os
import shutil

def find_project_root():
    """프로젝트 루트 디렉토리 찾기"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 현재 디렉토리가 이미 prompt-engineering-kr인 경우
    if os.path.basename(current_dir).lower() == 'prompt-engineering-kr':
        return current_dir
    
    # 상위 디렉토리 탐색
    root = current_dir
    while root:
        if os.path.basename(root).lower() == 'prompt-engineering-kr':
            return root
        parent = os.path.dirname(root)
        if parent == root:  # 루트에 도달
            break
        root = parent
    
    # 프로젝트 루트를 찾지 못한 경우 현재 디렉토리 반환
    print("경고: 'prompt-engineering-kr' 디렉토리를 찾지 못했습니다.")
    return current_dir

def clear_results_folder(results_dir):
    """
    results 폴더의 내용을 모두 삭제
    """
    if os.path.exists(results_dir):
        print(f"기존 results 폴더 삭제 중: {results_dir}")
        # 디렉토리 내 모든 항목 삭제
        for item in os.listdir(results_dir):
            item_path = os.path.join(results_dir, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        print("기존 results 폴더 내용이 모두 삭제되었습니다.")
    else:
        os.makedirs(results_dir)
        print(f"results 폴더 생성: {results_dir}")

def create_folder_structure(results_dir):
    """
    폴더 구조 생성 함수
    
    Args:
        results_dir: results 폴더 경로
    """
    # 폴더 구조 정의
    structure = {
        "part1": {
            "1.1": ["1.1.1", "1.1.2", "1.1.3"],
            "1.2": ["1.2.1", "1.2.2", "1.2.3"],
            "1.3": ["1.3.1", "1.3.2", "1.3.3"],
            "1.4": ["1.4.1", "1.4.2", "1.4.3"],
            "1.5": ["1.5.1", "1.5.2", "1.5.3"]
        },
        "part2": {
            "2.1": ["2.1.1", "2.1.2", "2.1.3"],
            "2.2": ["2.2.1", "2.2.2", "2.2.3"],
            "2.3": ["2.3.1", "2.3.2", "2.3.3"],
            "2.4": ["2.4.1", "2.4.2", "2.4.3"],
            "2.5": ["2.5.1", "2.5.2", "2.5.3"]
        },
        "part3": {
            "3.1": ["3.1.1", "3.1.2", "3.1.3"],
            "3.2": ["3.2.1", "3.2.2", "3.2.3"],
            "3.3": ["3.3.1", "3.3.2", "3.3.3"],
            "3.4": ["3.4.1", "3.4.2", "3.4.3"],
            "3.5": ["3.5.1", "3.5.2", "3.5.3"]
        },
        "part4": {
            "4.1": ["4.1.1", "4.1.2", "4.1.3"],
            "4.2": ["4.2.1", "4.2.2", "4.2.3"],
            "4.3": ["4.3.1", "4.3.2", "4.3.3"],
            "4.4": ["4.4.1", "4.4.2", "4.4.3"]
        },
        "part5": {
            "5.1": ["5.1.1", "5.1.2", "5.1.3"],
            "5.2": ["5.2.1", "5.2.2", "5.2.3"],
            "5.3": ["5.3.1", "5.3.2", "5.3.3"],
            "5.4": ["5.4.1", "5.4.2", "5.4.3"]
        },
        "part6": {
            "6.1": ["6.1.1", "6.1.2", "6.1.3"],
            "6.2": ["6.2.1", "6.2.2", "6.2.3"],
            "6.3": ["6.3.1", "6.3.2", "6.3.3"]
        },
        "part7": {
            "7.1": ["7.1.1", "7.1.2", "7.1.3"],
            "7.2": ["7.2.1", "7.2.2", "7.2.3"],
            "7.3": ["7.3.1", "7.3.2", "7.3.3"]
        },
        "part8": {
            "8.1": ["8.1.1", "8.1.2", "8.1.3"],
            "8.2": ["8.2.1", "8.2.2", "8.2.3"],
            "8.3": ["8.3.1", "8.3.2", "8.3.3"]
        },
        "part9": {
            "9.1": ["9.1.1", "9.1.2", "9.1.3"],
            "9.2": ["9.2.1", "9.2.2", "9.2.3"]
        }
    }
    
    # 폴더 생성
    created_folders = []
    
    for part, chapters in structure.items():
        part_dir = os.path.join(results_dir, part)
        os.makedirs(part_dir, exist_ok=True)
        created_folders.append(part_dir)
        
        for chapter, subchapters in chapters.items():
            chapter_dir = os.path.join(part_dir, chapter)
            os.makedirs(chapter_dir, exist_ok=True)
            created_folders.append(chapter_dir)
            
            for subchapter in subchapters:
                subchapter_dir = os.path.join(chapter_dir, subchapter)
                os.makedirs(subchapter_dir, exist_ok=True)
                created_folders.append(subchapter_dir)
    
    return created_folders

def main():
    """
    메인 함수
    """
    print("Results 폴더 구조 생성 도구")
    print("============================")
    
    # 프로젝트 루트 찾기
    project_root = find_project_root()
    results_dir = os.path.join(project_root, "results")
    
    print(f"프로젝트 루트: {project_root}")
    print(f"결과 폴더: {results_dir}")
    
    # 사용자 확인
    confirm = input(f"이 작업은 {results_dir} 폴더의 모든 내용을 삭제하고 part1~part9 구조를 생성합니다. 계속하시겠습니까? (y/n) [기본값: y]: ")
    if confirm.lower() not in ['', 'y', 'yes']:
        print("작업이 취소되었습니다.")
        return
    
    # results 폴더 초기화
    clear_results_folder(results_dir)
    
    # 폴더 구조 생성
    print("\n폴더 구조 생성 중...")
    folders = create_folder_structure(results_dir)
    
    # 결과 출력
    print(f"\n총 {len(folders)}개의 폴더가 생성되었습니다.")
    
    # 예시로 몇 개 경로 출력
    print("\n주요 폴더 경로 예시:")
    examples = [
        os.path.join(results_dir, "part1", "1.1", "1.1.1"),
        os.path.join(results_dir, "part2", "2.3", "2.3.2"),
        os.path.join(results_dir, "part5", "5.2"),
        os.path.join(results_dir, "part9", "9.1")
    ]
    
    for path in examples:
        if os.path.exists(path):
            print(f"  - {path}")
    
    print("\n폴더 구조 생성이 완료되었습니다.")

if __name__ == "__main__":
    main()