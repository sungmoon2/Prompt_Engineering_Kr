import os

def create_gitkeep_files(root_dir):
    """
    주어진 루트 디렉토리 아래의 모든 최하위 디렉토리에 .gitkeep 파일 생성
    
    Args:
        root_dir (str): .gitkeep 파일을 생성할 루트 디렉토리 경로
    """
    # 디렉토리 순회
    for part_dir in os.listdir(root_dir):
        part_path = os.path.join(root_dir, part_dir)
        
        # part 디렉토리인지 확인 (디렉토리이고 part로 시작하는지)
        if os.path.isdir(part_path) and part_dir.startswith('part'):
            # part 디렉토리 내 각 챕터 디렉토리 순회
            for chapter_dir in os.listdir(part_path):
                chapter_path = os.path.join(part_path, chapter_dir)
                
                # 챕터 디렉토리인지 확인
                if os.path.isdir(chapter_path):
                    # 챕터 디렉토리 내 각 하위 디렉토리 순회
                    for subchapter_dir in os.listdir(chapter_path):
                        subchapter_path = os.path.join(chapter_path, subchapter_dir)
                        
                        # 최하위 디렉토리인지 확인
                        if os.path.isdir(subchapter_path):
                            # .gitkeep 파일 경로 설정
                            gitkeep_path = os.path.join(subchapter_path, '.gitkeep')
                            
                            # .gitkeep 파일이 없으면 생성
                            if not os.path.exists(gitkeep_path):
                                with open(gitkeep_path, 'w') as f:
                                    pass  # 빈 파일 생성
                                print(f"Created .gitkeep in {subchapter_path}")

def main():
    # 스크립트의 현재 위치 기준으로 results 디렉토리 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(current_dir, 'results')
    
    # results 디렉토리 존재 확인
    if not os.path.exists(results_dir):
        print(f"Error: {results_dir} 디렉토리가 존재하지 않습니다.")
        return
    
    # .gitkeep 파일 생성
    create_gitkeep_files(results_dir)
    print("모든 최하위 디렉토리에 .gitkeep 파일 생성 완료.")

if __name__ == "__main__":
    main()