"""
파일 처리 유틸리티

이 모듈은 파일 읽기/쓰기, 결과 저장 등의 공통 기능을 제공합니다.
"""
import os
import json
import csv
import pandas as pd
from datetime import datetime
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 기본 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
DATA_DIR = os.path.join(BASE_DIR, "data")

# 필요한 디렉토리 생성
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

def save_result(content, filename, format="txt"):
    """결과 저장 함수

    Args:
        content (str): 저장할 내용
        filename (str): 파일명 (확장자 제외)
        format (str, optional): 파일 형식 ("txt", "md", "json"). Defaults to "txt".

    Returns:
        str: 저장된 파일 경로
    """
    # 확장자 설정
    if format in ["txt", "md"]:
        ext = format
    elif format == "json" and isinstance(content, (dict, list)):
        ext = "json"
    else:
        ext = "txt"
    
    # 파일 경로 구성
    if not filename.endswith(f'.{ext}'):
        filename = f"{filename}.{ext}"
    
    filepath = os.path.join(RESULTS_DIR, filename)
    
    try:
        # 내용 저장
        if ext == "json":
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(content, f, ensure_ascii=False, indent=2)
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
        
        logger.info(f"결과가 저장되었습니다: {filepath}")
        return filepath
    
    except Exception as e:
        logger.error(f"파일 저장 중 오류 발생: {str(e)}")
        raise

def load_text_file(filename, folder="data"):
    """텍스트 파일 로드 함수

    Args:
        filename (str): 파일명
        folder (str, optional): 폴더명. Defaults to "data".

    Returns:
        str: 파일 내용
    """
    if folder == "data":
        filepath = os.path.join(DATA_DIR, filename)
    else:
        filepath = os.path.join(BASE_DIR, folder, filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"파일을 찾을 수 없습니다: {filepath}")
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filepath}")
    except Exception as e:
        logger.error(f"파일 로드 중 오류 발생: {str(e)}")
        raise

def save_to_markdown(content, filename):
    """마크다운 파일로 저장

    Args:
        content (str): 저장할 내용
        filename (str): 파일명 (확장자 없이 제공 가능)

    Returns:
        str: 저장된 파일 경로
    """
    return save_result(content, filename, format="md")

def save_to_json(data, filename):
    """JSON 파일로 저장

    Args:
        data (dict or list): 저장할 데이터
        filename (str): 파일명 (확장자 없이 제공 가능)

    Returns:
        str: 저장된 파일 경로
    """
    return save_result(data, filename, format="json")

def load_csv_data(filename):
    """CSV 파일 로드

    Args:
        filename (str): CSV 파일명 (확장자 포함)

    Returns:
        pandas.DataFrame: 로드된 CSV 데이터
    """
    filepath = os.path.join(DATA_DIR, filename)
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        logger.error(f"CSV 파일을 찾을 수 없습니다: {filepath}")
        raise FileNotFoundError(f"CSV 파일을 찾을 수 없습니다: {filepath}")
    except Exception as e:
        logger.error(f"CSV 로드 중 오류 발생: {str(e)}")
        raise

def save_csv_data(df, filename):
    """DataFrame을 CSV로 저장

    Args:
        df (pandas.DataFrame): 저장할 DataFrame
        filename (str): 파일명 (확장자 없이 제공 가능)

    Returns:
        str: 저장된 파일 경로
    """
    # 확장자가 없으면 .csv 추가
    if not filename.endswith('.csv'):
        filename = f"{filename}.csv"
    
    filepath = os.path.join(RESULTS_DIR, filename)
    try:
        df.to_csv(filepath, index=False, encoding='utf-8')
        logger.info(f"CSV 파일이 저장되었습니다: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"CSV 저장 중 오류 발생: {str(e)}")
        raise

def create_comparison_report(original_prompt, enhanced_prompt, original_result, enhanced_result, analysis=None):
    """프롬프트 비교 보고서 생성

    Args:
        original_prompt (str): 원본 프롬프트
        enhanced_prompt (str): 향상된 프롬프트
        original_result (str): 원본 결과
        enhanced_result (str): 향상된 결과
        analysis (str, optional): 결과 분석. Defaults to None.

    Returns:
        str: 보고서 파일 경로
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"prompt_comparison_{timestamp}.md"
    
    content = f"""# 프롬프트 비교 실험 결과
실행 시간: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 원본 프롬프트
```
{original_prompt}
```

## 향상된 프롬프트
```
{enhanced_prompt}
```

## 원본 프롬프트 결과
{original_result[:1000]}
{'' if len(original_result) <= 1000 else '... (생략됨)'}

## 향상된 프롬프트 결과
{enhanced_result[:1000]}
{'' if len(enhanced_result) <= 1000 else '... (생략됨)'}
"""

    if analysis:
        content += f"""
## 결과 분석
{analysis}
"""
    
    # 간단한 통계 추가
    content += f"""
## 통계
- 원본 프롬프트 길이: {len(original_prompt)} 자
- 향상된 프롬프트 길이: {len(enhanced_prompt)} 자
- 원본 결과 길이: {len(original_result)} 자
- 향상된 결과 길이: {len(enhanced_result)} 자
- 길이 변화율: {((len(enhanced_result) / len(original_result)) * 100) - 100:.1f}%
"""
    
    return save_to_markdown(content, filename)

def load_json_file(filename, folder="data"):
    """JSON 파일 로드 함수

    Args:
        filename (str): 파일명
        folder (str, optional): 폴더명. Defaults to "data".

    Returns:
        dict or list: 로드된 JSON 데이터
    """
    if folder == "data":
        filepath = os.path.join(DATA_DIR, filename)
    else:
        filepath = os.path.join(BASE_DIR, folder, filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"JSON 파일을 찾을 수 없습니다: {filepath}")
        raise FileNotFoundError(f"JSON 파일을 찾을 수 없습니다: {filepath}")
    except json.JSONDecodeError:
        logger.error(f"JSON 형식이 잘못되었습니다: {filepath}")
        raise ValueError(f"JSON 형식이 잘못되었습니다: {filepath}")
    except Exception as e:
        logger.error(f"JSON 파일 로드 중 오류 발생: {str(e)}")
        raise