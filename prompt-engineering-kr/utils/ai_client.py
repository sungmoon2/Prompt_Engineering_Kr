"""
AI 모델 연결 및 응답 처리 모듈
대학생들이 다양한 AI 서비스를 쉽게 활용할 수 있는 인터페이스 제공
"""

import os
import requests
import json
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# Gemini API 사용을 위한 라이브러리 추가
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("google-generativeai 라이브러리가 설치되어 있지 않습니다. Gemini 기능을 사용할 수 없습니다.")
    print("설치하려면: pip install google-generativeai")

class AIClient:
    """AI 서비스 연결 및 응답 처리를 위한 클래스"""
    
    def __init__(self, api_key: Optional[str] = None, service: str = "gemini"):
        """
        AI 서비스 연결 객체 초기화
        
        Args:
            api_key: API 키 (없을 경우 환경 변수에서 로드)
            service: 사용할 AI 서비스 (gemini, openai, anthropic 등)
        """
        self.service = service.lower()
        self.api_key = api_key or self._get_api_key_from_env()
        
        # Gemini API 설정
        if self.service == "gemini" and GEMINI_AVAILABLE:
            genai.configure(api_key=self.api_key)
            self.model = self._get_default_model()
        else:
            self.base_url = self._get_base_url()
        
    def _get_api_key_from_env(self) -> str:
        """환경 변수에서 API 키 로드"""
        env_var = f"{self.service.upper()}_API_KEY"
        api_key = os.environ.get(env_var)
        if not api_key:
            raise ValueError(f"{env_var} 환경변수가 설정되어 있지 않습니다.")
        return api_key
    
    def _get_default_model(self) -> str:
        """서비스별 기본 모델명 반환"""
        defaults = {
            "gemini": "gemini-1.5-flash",
            "openai": "gpt-3.5-turbo",
            "anthropic": "claude-instant-1"
        }
        return defaults.get(self.service, "gemini-1.5-pro")
    
    def _get_base_url(self) -> str:
        """서비스별 기본 URL 반환"""
        urls = {
            "openai": "https://api.openai.com/v1/chat/completions",
            "anthropic": "https://api.anthropic.com/v1/messages",
            # 다른 서비스 추가 가능
        }
        return urls.get(self.service, urls["openai"])
    
    def get_response(self, prompt: str, 
                    max_tokens: int = 8000, 
                    temperature: float = 0.7,
                    additional_params: Dict[str, Any] = None) -> str:
        """
        AI 모델에 프롬프트를 전송하고 응답 받기
        
        Args:
            prompt: 사용자 프롬프트
            max_tokens: 최대 토큰 수
            temperature: 응답 다양성 (0~1)
            additional_params: 추가 파라미터
            
        Returns:
            AI 모델의 응답 텍스트
        """
        if self.service == "gemini" and GEMINI_AVAILABLE:
            return self._get_gemini_response(prompt, max_tokens, temperature, additional_params)
        else:
            params = self._prepare_request_params(prompt, max_tokens, temperature, additional_params)
            response = self._send_request(params)
            return self._extract_response_text(response)
    
    def _get_gemini_response(self, prompt, max_tokens, temperature, additional_params):
        """Gemini API를 사용하여 응답 얻기"""
        try:
            # 모델 가져오기
            model = genai.GenerativeModel(self.model)
            
            # 추가 파라미터 설정
            generation_config = genai.GenerationConfig(
                max_output_tokens = max_tokens,
                temperature = temperature
            )
            
            if additional_params:
                generation_config.update(additional_params)
            
            # 응답 생성
            response = model.generate_content(prompt, generation_config=generation_config)
            
            # 응답 텍스트 반환
            if hasattr(response, 'text'):
                return response.text
            elif hasattr(response, 'parts'):
                return ''.join(part.text for part in response.parts)
            else:
                return str(response)
                
        except Exception as e:
            print(f"Gemini API 호출 오류: {e}")
            return f"오류가 발생했습니다: {str(e)}"
    
    def _prepare_request_params(self, prompt, max_tokens, temperature, additional_params):
        """서비스별 요청 파라미터 준비"""
        if self.service == "openai":
            params = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": temperature
            }
        elif self.service == "anthropic":
            params = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": temperature
            }
        else:
            params = {"prompt": prompt, "max_tokens": max_tokens, "temperature": temperature}
        
        # 추가 파라미터 적용
        if additional_params:
            params.update(additional_params)
            
        return params
        
    def _send_request(self, params):
        """실제 API 요청 보내기"""
        try:
            response = requests.post(
                self.base_url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                },
                json=params,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"API 요청 오류: {e}")
            return {"error": str(e)}
    
    def _extract_response_text(self, response):
        """응답에서 텍스트 추출"""
        if self.service == "openai":
            return response.get("choices", [{}])[0].get("message", {}).get("content", "")
        elif self.service == "anthropic":
            return response.get("content", [{}])[0].get("text", "")
        return "응답을 처리할 수 없습니다."


def get_completion(prompt: str, 
                  provider: str = "gemini", 
                  temperature: float = 0.7, 
                  max_tokens: int = None,
                  system_prompt: Optional[str] = None,
                  **kwargs) -> str:

    """
    간편하게 AI 응답을 받는 유틸리티 함수
    
    Args:
        prompt: 사용자 프롬프트
        provider: 사용할 AI 서비스
        temperature: 응답 다양성 (0~1)
        max_tokens: 최대 토큰 수
        system_prompt: 시스템 프롬프트
        **kwargs: 추가 파라미터
        
    Returns:
        AI 모델의 응답 텍스트
    """
    # system_prompt가 있으면 프롬프트에 추가
    if system_prompt and provider != "gemini":
        full_prompt = f"{system_prompt}\n\n{prompt}"
    else:
        full_prompt = prompt
        
    # Gemini는 추가 파라미터에 system_prompt 추가
    additional_params = kwargs.copy()
    if system_prompt and provider == "gemini":
        additional_params["system_prompt"] = system_prompt
    
    # service 매개변수로 변경 (provider에서 service로)
    client = AIClient(service=provider)
    return client.get_response(
        prompt=full_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        additional_params=additional_params
    )