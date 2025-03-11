"""
API 연결 및 모델 관련 유틸리티

이 모듈은 다양한 AI API 서비스에 연결하고 텍스트를 생성하는 공통 기능을 제공합니다.
"""
import os
import time
import logging
from dotenv import load_dotenv

# 환경 변수 로드 시도
load_dotenv()

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def generate_text(prompt, model="openai", temperature=0.7, max_tokens=1000):
    """여러 AI 모델 API에 프롬프트를 전송하고 결과를 반환하는 함수
    
    Args:
        prompt (str): 전송할 프롬프트
        model (str, optional): 사용할 모델 유형. Defaults to "openai".
            "openai": OpenAI GPT 모델
            "gemini": Google Gemini 모델
            "claude": Anthropic Claude 모델
            "mock": 테스트용 가짜 응답
        temperature (float, optional): 생성 다양성 설정 (0.0-1.0). Defaults to 0.7.
        max_tokens (int, optional): 최대 생성 토큰 수. Defaults to 1000.
        
    Returns:
        str: 생성된 텍스트
    """
    # 모의 응답 모드 (개발 및 테스트용)
    if model == "mock":
        logger.info("Mock 모드로 실행 중")
        time.sleep(1)  # API 호출 시뮬레이션
        
        if "보고서" in prompt.lower() or "리포트" in prompt.lower():
            if len(prompt) < 100:  # 짧은 프롬프트
                return """# 인공지능 활용 보고서

인공지능은 다양한 분야에서 활용되고 있습니다. 이 보고서에서는 인공지능의 주요 활용 사례를 살펴보겠습니다.

## 주요 활용 분야
- 의료
- 교육
- 금융
- 제조

인공지능은 앞으로 더 많은 분야에서 활용될 것으로 예상됩니다."""
            else:  # 긴 프롬프트
                return """# 인공지능 기술의 교육적 활용과 그 영향

## 1. 서론

### 배경
인공지능(AI) 기술은 21세기 들어 급속도로 발전하며 다양한 산업 분야에 혁신을 가져오고 있습니다. 교육 분야 역시 이러한 기술적 변화의 영향을 피할 수 없으며, 오히려 적극적으로 AI 기술을 교수학습 과정에 도입하여 교육의 효율성과 효과성을 높이려는 시도가 전 세계적으로 확산되고 있습니다.

### 중요성
교육에서의 AI 활용은 단순한 기술 도입 이상의 의미를 갖습니다. 학습자 중심 교육, 개인화된 학습 경험, 교육 형평성 제고 등 현대 교육이 추구하는 핵심 가치를 실현하는 데 AI가 중요한 역할을 할 수 있기 때문입니다. 또한, 4차 산업혁명 시대에 필요한 역량을 갖춘 인재 양성을 위해서도 교육 환경에서의 AI 통합은 필수적입니다.

### 연구 질문
본 보고서는 다음과 같은 핵심 질문에 답하고자 합니다:
1. 현재 교육 분야에서 AI 기술은 어떻게 활용되고 있는가?
2. AI 기반 교육 도구와 시스템은 학습 성과에 어떤 영향을 미치는가?
3. AI 교육 도구 활용에 있어 주요 도전과제와 한계점은 무엇인가?
4. 교육에서의 AI 활용이 가져올 미래 전망과 정책적 제언은 무엇인가?

## 2. 이론적 배경

### AI 교육 도구의 발전
인공지능 기술의 교육적 적용은 1970년대 초기 컴퓨터 기반 교육(Computer-Based Education)에서 시작되었으나, 최근 딥러닝과 자연어 처리 기술의 발전으로 획기적인 변화를 맞이했습니다. 초기의 단순한 분기형 튜토리얼 시스템에서 개인화된 적응형 학습 시스템으로 발전해왔습니다.

Hwang 외(2020)에 따르면, 현대 교육 AI 시스템은 크게 다음과 같이 분류됩니다:
1. 지능형 튜터링 시스템 (Intelligent Tutoring Systems)
2. 적응형 학습 플랫폼 (Adaptive Learning Platforms)
3. 자동화된 평가 시스템 (Automated Assessment Systems)
4. 교육 데이터 분석 도구 (Educational Data Mining Tools)
5. 가상 학습 도우미 (Virtual Learning Assistants)

### 현황
최근 연구(Kim & Lee, 2022)에 따르면, 전 세계적으로 교육 분야의 AI 시장은 연평균 36%의 성장률을 보이며, 2025년까지 약 200억 달러 규모로 성장할 것으로 예측됩니다. 특히 COVID-19 팬데믹 이후 원격 교육의 확산과 함께 AI 기반 교육 도구의 활용이 급증했습니다.

## 3. 적용 사례 분석

### 사례 1: Carnegie Learning의 MATHia
MATHia는 중등 수학 교육을 위한 AI 기반 적응형 학습 플랫폼으로, 학생의 문제 해결 과정을 실시간으로 분석하여 개인화된 학습 경로를 제공합니다. Long & Aleven(2021)의 연구에 따르면, MATHia를 사용한 학생들은 표준화된 수학 시험에서 평균 27% 향상된 성과를 보였습니다.

### 사례 2: Duolingo의 언어 학습 AI
언어 학습 애플리케이션 Duolingo는 AI 알고리즘을 활용해 사용자의 언어 능력을 평가하고, 최적의 복습 시점을 예측하는 '간격 반복(spaced repetition)' 시스템을 구현합니다. Settles & Meeder(2020)의 연구는 이 시스템이 전통적인 언어 학습 방법보다 학습 효율성을 최대 45% 향상시킬 수 있음을 보여주었습니다."""
        
        elif "코드" in prompt.lower() or "프로그래밍" in prompt.lower():
            return """```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 사용 예시
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

버블 정렬(Bubble Sort)은 인접한 두 원소를 비교하여 필요시 위치를 교환하는 방식으로 작동하는 간단한 정렬 알고리즘입니다. 시간 복잡도는 O(n²)로 대규모 데이터에는 비효율적이지만, 구현이 간단하고 이해하기 쉬운 장점이 있습니다."""
        
        else:
            return "이것은 테스트 응답입니다. 실제 API가 연결되지 않았습니다."
    
    # OpenAI 모델 사용
    elif model == "openai":
        try:
            if not OPENAI_API_KEY:
                logger.warning("OpenAI API 키가 설정되지 않았습니다. 환경 변수를 확인하세요.")
                return "OpenAI API 키가 설정되지 않았습니다. .env 파일에 OPENAI_API_KEY를 설정하세요."
            
            logger.info("OpenAI API 호출 중...")
            
            # OpenAI 패키지 동적 임포트 (필요 시에만 임포트)
            import openai
            openai.api_key = OPENAI_API_KEY
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
        
        except ImportError:
            logger.error("openai 패키지가 설치되지 않았습니다. 'pip install openai' 명령어로 설치하세요.")
            return "openai 패키지가 설치되지 않았습니다. 'pip install openai' 명령어로 설치하세요."
        
        except Exception as e:
            logger.error(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return f"OpenAI API 호출 중 오류 발생: {str(e)}"
    
    # Google Gemini 모델 사용
    elif model == "gemini":
        try:
            if not GOOGLE_API_KEY:
                logger.warning("Google API 키가 설정되지 않았습니다. 환경 변수를 확인하세요.")
                return "Google API 키가 설정되지 않았습니다. .env 파일에 GOOGLE_API_KEY를 설정하세요."
            
            logger.info("Google Gemini API 호출 중...")
            
            # Gemini 패키지 동적 임포트
            import google.generativeai as genai
            
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens,
                }
            )
            
            return response.text
        
        except ImportError:
            logger.error("google-generativeai 패키지가 설치되지 않았습니다. 'pip install google-generativeai' 명령어로 설치하세요.")
            return "google-generativeai 패키지가 설치되지 않았습니다. 'pip install google-generativeai' 명령어로 설치하세요."
        
        except Exception as e:
            logger.error(f"Google Gemini API 호출 중 오류 발생: {str(e)}")
            return f"Google Gemini API 호출 중 오류 발생: {str(e)}"
    
    # Anthropic Claude 모델 사용
    elif model == "claude":
        try:
            if not ANTHROPIC_API_KEY:
                logger.warning("Anthropic API 키가 설정되지 않았습니다. 환경 변수를 확인하세요.")
                return "Anthropic API 키가 설정되지 않았습니다. .env 파일에 ANTHROPIC_API_KEY를 설정하세요."
            
            logger.info("Anthropic Claude API 호출 중...")
            
            # 요청 보내기
            import requests
            
            headers = {
                "x-api-key": ANTHROPIC_API_KEY,
                "content-type": "application/json"
            }
            
            data = {
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "model": "claude-2",
                "temperature": temperature,
                "max_tokens_to_sample": max_tokens
            }
            
            response = requests.post(
                "https://api.anthropic.com/v1/complete",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json().get("completion", "").strip()
            else:
                error_message = f"API 오류: {response.status_code} - {response.text}"
                logger.error(error_message)
                return error_message
        
        except ImportError:
            logger.error("requests 패키지가 설치되지 않았습니다. 'pip install requests' 명령어로 설치하세요.")
            return "requests 패키지가 설치되지 않았습니다. 'pip install requests' 명령어로 설치하세요."
        
        except Exception as e:
            logger.error(f"Anthropic Claude API 호출 중 오류 발생: {str(e)}")
            return f"Anthropic Claude API 호출 중 오류 발생: {str(e)}"
    
    else:
        logger.error(f"지원하지 않는 모델: {model}")
        return f"지원하지 않는 모델입니다: {model}. 'openai', 'gemini', 'claude' 또는 'mock' 중 하나를 사용하세요."

def compare_responses(prompt, models=None, temperature=0.7):
    """여러 모델의 응답을 비교하는 함수
    
    Args:
        prompt (str): 전송할 프롬프트
        models (list, optional): 비교할 모델 목록. Defaults to ["openai", "gemini", "mock"].
        temperature (float, optional): 생성 다양성 설정. Defaults to 0.7.
        
    Returns:
        dict: 각 모델별 응답 및 메타데이터
    """
    if models is None:
        models = ["openai", "gemini", "mock"]
    
    results = {}
    
    for model in models:
        logger.info(f"{model} 모델 응답 생성 중...")
        
        start_time = time.time()
        response = generate_text(prompt, model=model, temperature=temperature)
        elapsed_time = time.time() - start_time
        
        # 응답 길이 및 단어 수 계산
        char_count = len(response)
        word_count = len(response.split())
        
        results[model] = {
            "response": response,
            "elapsed_time": f"{elapsed_time:.2f}초",
            "char_count": char_count,
            "word_count": word_count
        }
    
    return results