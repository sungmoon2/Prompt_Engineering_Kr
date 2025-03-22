"""
챕터 관련 유틸리티 모듈

실습 코드 결과를 챕터별로 적절한 폴더에 저장하는 기능을 제공합니다.
"""

import os
import re
import inspect

def get_chapter_save_path(file_path=None):
    """
    파일 경로에서 챕터 정보를 추출하고, 저장할 경로를 반환합니다.
    
    Args:
        file_path: 파일 경로 (없으면 호출한 파일의 경로를 사용)
        
    Returns:
        저장할 경로 (results/part{}/챕터/...)
    """
    # 파일 경로가 제공되지 않으면 호출한 파일의 경로를 사용
    if file_path is None:
        frame = inspect.stack()[1]
        file_path = frame.filename
    
    # 경로를 정규화 (슬래시 방향 통일)
    file_path = os.path.normpath(file_path).replace('\\', '/')
    file_name = os.path.basename(file_path)
    
    # 프로젝트 루트 찾기
    project_root = os.path.dirname(file_path)
    while project_root and os.path.basename(project_root).lower() != 'prompt-engineering-kr':
        parent = os.path.dirname(project_root)
        if parent == project_root:  # 루트에 도달
            break
        project_root = parent
    
    # 1. 파일 이름에서 챕터 번호 추출 시도
    # 1.1_clear_instructions.py 또는 1.1.1_specific_requests.py 패턴
    chapter_match = re.match(r'^(\d+)\.(\d+)(?:\.(\d+))?_', file_name)
    
    if chapter_match:
        # 파트 번호 (예: 1)
        part_num = chapter_match.group(1)
        # 챕터 번호 (예: 1.1)
        chapter_num = f"{part_num}.{chapter_match.group(2)}"
        # 서브챕터 번호 (예: 1.1.1, 없으면 None)
        subchapter_num = chapter_match.group(3)
        
        # 결과 저장 경로 생성
        if subchapter_num:
            # 예: 1.1.1_specific_requests.py -> results/part1/1.1/1.1.1
            full_chapter = f"{chapter_num}.{subchapter_num}"
            save_path = os.path.join(project_root, "results", f"part{part_num}", chapter_num, full_chapter)
        else:
            # 예: 1.1_clear_instructions.py -> results/part1/1.1
            save_path = os.path.join(project_root, "results", f"part{part_num}", chapter_num)
    else:
        # 2. 디렉토리 경로에서 챕터 정보 추출 시도
        # exercises/part1/1.1/ 또는 exercises/part1/1.1/1.1.1 패턴
        path_pattern = r'exercises/part(\d+)/(\d+\.\d+)(?:/(\d+\.\d+\.\d+))?'
        path_match = re.search(path_pattern, file_path)
        
        if path_match:
            part_num = path_match.group(1)
            chapter_num = path_match.group(2)
            subchapter_path = path_match.group(3)
            
            if subchapter_path:
                # 서브챕터 경로가 있는 경우
                save_path = os.path.join(project_root, "results", f"part{part_num}", chapter_num, subchapter_path)
            else:
                # 서브챕터 경로가 없는 경우
                save_path = os.path.join(project_root, "results", f"part{part_num}", chapter_num)
        else:
            # 3. 파일이 있는 디렉토리 이름이 챕터 번호 형식인지 확인
            dir_name = os.path.basename(os.path.dirname(file_path))
            parent_dir_name = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
            
            if re.match(r'^\d+\.\d+\.\d+$', dir_name) and re.match(r'^\d+\.\d+$', parent_dir_name):
                # 디렉토리가 1.1.1 형식이고 부모 디렉토리가 1.1 형식인 경우
                part_num = dir_name.split('.')[0]
                chapter_num = f"{part_num}.{dir_name.split('.')[1]}"
                save_path = os.path.join(project_root, "results", f"part{part_num}", chapter_num, dir_name)
            elif re.match(r'^\d+\.\d+$', dir_name):
                # 디렉토리가 1.1 형식인 경우
                part_num = dir_name.split('.')[0]
                save_path = os.path.join(project_root, "results", f"part{part_num}", dir_name)
            else:
                # 챕터 정보를 찾지 못한 경우 임시 디렉토리
                save_path = os.path.join(project_root, "results", "unknown")
    
    # 디버그 출력
    print(f"파일 경로: {file_path}")
    print(f"저장 경로: {save_path}")
    
    # 디렉토리가 없으면 생성
    os.makedirs(save_path, exist_ok=True)
    
    return save_path

def save_result(content, filename, title=None, calling_file=None):
    """
    실습 결과를 챕터에 맞는 경로에 저장합니다.
    
    Args:
        content: 저장할 내용
        filename: 파일 이름 (확장자 포함)
        title: 제목 (마크다운 파일인 경우 추가)
        calling_file: 호출 파일 경로 (없으면 호출 스택에서 추출)
        
    Returns:
        저장된 파일의 절대 경로
    """
    # 호출 파일이 제공되지 않으면 호출 스택에서 추출
    if calling_file is None:
        frame = inspect.stack()[1]
        calling_file = frame.filename
        
    # 호출한 파일에 맞는 저장 경로 가져오기
    save_path = get_chapter_save_path(calling_file)
    
    # 파일 확장자 확인
    if not filename.endswith(('.md', '.txt', '.json', '.csv')):
        filename += '.md'  # 기본값으로 마크다운 확장자 추가
    
    # 전체 파일 경로
    file_path = os.path.join(save_path, filename)
    
    # 마크다운 파일이고 제목이 있는 경우
    if filename.endswith('.md') and title:
        content = f"# {title}\n\n{content}"
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"결과가 저장되었습니다: {file_path}")
    return file_path