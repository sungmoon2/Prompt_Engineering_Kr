"""
설정 관리 모듈

프로젝트 설정 및 환경 변수 관리 기능을 제공합니다.
"""

import os
import json
from typing import Dict, Any, Optional

# 기본 설정값
DEFAULT_CONFIG = {
    # AI 설정
    "ai": {
        "provider": "openai",
        "model": "gpt-4",
        "api_key_env": "OPENAI_API_KEY",
        "temperature": 0.7
        # "max_tokens": 
    },
    
    # 출력 설정
    "output": {
        "default_format": "markdown",
        "save_results": True,
        "results_dir": "results",
        "use_chapter_folders": True  # 챕터별 폴더 사용 여부 설정 추가
    },
    
    # 학습 예제 설정
    "examples": {
        "use_examples": True,
        "examples_dir": "examples"
    },
    
    # 로깅 설정
    "logging": {
        "enabled": True,
        "log_level": "INFO",
        "log_file": "prompt_engineering.log"
    }
}

# 설정 파일 경로
CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config.json"
)

# 전역 설정 객체
_config = None


def load_config() -> Dict[str, Any]:
    """
    설정 파일 로드
    
    Returns:
        설정 딕셔너리
    """
    global _config
    
    # 이미 로드된 설정이 있으면 반환
    if _config is not None:
        return _config
    
    # 설정 파일이 있으면 로드
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                
            # 기본 설정과 병합
            merged_config = DEFAULT_CONFIG.copy()
            _merge_dicts(merged_config, loaded_config)
            _config = merged_config
            
        except Exception as e:
            print(f"설정 파일 로드 오류: {e}")
            _config = DEFAULT_CONFIG.copy()
    else:
        # 설정 파일이 없으면 기본값 사용
        _config = DEFAULT_CONFIG.copy()
        
        # 기본 설정 파일 생성
        save_config(_config)
    
    return _config


def save_config(config: Dict[str, Any]) -> None:
    """
    설정 파일 저장
    
    Args:
        config: 저장할 설정 딕셔너리
    """
    global _config
    
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        # 전역 설정 업데이트
        _config = config
        
    except Exception as e:
        print(f"설정 파일 저장 오류: {e}")


def get_setting(key: str, default: Any = None) -> Any:
    """
    특정 설정값 가져오기
    
    Args:
        key: 설정 키 (점으로 구분된 경로, 예: 'ai.model')
        default: 설정이 없을 경우 기본값
        
    Returns:
        설정값 또는 기본값
    """
    config = load_config()
    keys = key.split('.')
    
    # 설정값 찾기
    value = config
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return default
    
    return value


def update_setting(key: str, value: Any) -> None:
    """
    특정 설정값 업데이트
    
    Args:
        key: 설정 키 (점으로 구분된 경로, 예: 'ai.model')
        value: 새 설정값
    """
    config = load_config()
    keys = key.split('.')
    
    # 마지막 키를 제외한 경로 따라가기
    target = config
    for k in keys[:-1]:
        if k not in target:
            target[k] = {}
        target = target[k]
    
    # 마지막 키에 값 설정
    target[keys[-1]] = value
    
    # 설정 저장
    save_config(config)


def get_api_key(provider: Optional[str] = None) -> Optional[str]:
    """
    AI 제공자의 API 키 가져오기
    
    Args:
        provider: AI 제공자 (없으면 설정에서 가져옴)
        
    Returns:
        API 키 또는 None
    """
    if provider is None:
        provider = get_setting('ai.provider')
    
    env_var = f"{provider.upper()}_API_KEY"
    
    # 설정에 지정된 환경변수 이름이 있으면 사용
    config_env_var = get_setting(f'ai.api_key_env')
    if config_env_var:
        env_var = config_env_var
    
    return os.environ.get(env_var)


def get_results_dir() -> str:
    """
    결과 저장 디렉토리 경로 가져오기
    
    Returns:
        결과 디렉토리 절대 경로
    """
    results_dir = get_setting('output.results_dir', 'results')
    
    # 상대 경로인 경우 프로젝트 루트 기준으로 절대 경로 변환
    if not os.path.isabs(results_dir):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        results_dir = os.path.join(base_dir, results_dir)
    
    # 디렉토리가 없으면 생성
    os.makedirs(results_dir, exist_ok=True)
    
    return results_dir


def _merge_dicts(target: Dict[str, Any], source: Dict[str, Any]) -> None:
    """
    딕셔너리 재귀적 병합 (target을 업데이트)
    
    Args:
        target: 대상 딕셔너리
        source: 소스 딕셔너리
    """
    for key, value in source.items():
        if key in target and isinstance(target[key], dict) and isinstance(value, dict):
            _merge_dicts(target[key], value)
        else:
            target[key] = value