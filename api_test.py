#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
api_test.py - Google Gemini API 연결 테스트 스크립트

이 스크립트는 Google Gemini API와의 연결 및 API 키가 올바르게 설정되었는지 
테스트하기 위한 간단한 도구입니다. .env 파일에서 API 키를 읽어 간단한
프롬프트를 전송하고 응답을 받아 표시합니다.

사용법:
    python api_test.py  # Windows
    python3 api_test.py  # macOS/Linux
"""

import os
import sys
from dotenv import load_dotenv
import time

# 프로그램 시작 메시지 출력 함수
def print_start_message():
    print("=" * 60)
    print("Google Gemini API 연결 테스트 스크립트")
    print("=" * 60)
    print("이 스크립트는 API 키가 올바르게 설정되었는지 확인합니다.")
    print("테스트 중입니다. 잠시만 기다려주세요...\n")

# 프로그램 완료 메시지 출력 함수
def print_completion_message(success=True):
    print("\n" + "=" * 60)
    if success:
        print("✅ API 테스트가 성공적으로 완료되었습니다!")
        print("이제 실습 파일을 실행하여 프롬프트 엔지니어링을 시작하세요.")
    else:
        print("❌ API 테스트가 실패했습니다.")
        print("오류를 확인하고 API 키 설정을 다시 확인해주세요.")
    print("=" * 60)

# .env 파일의 API 키 확인 함수
def check_api_key():
    """
    .env 파일에서 GEMINI_API_KEY를 로드하고 유효성을 확인합니다.
    """
    print("1. .env 파일을 확인하는 중...")
    
    # .env 파일 로드
    load_dotenv()
    
    # API 키 가져오기
    api_key = os.getenv("GEMINI_API_KEY")
    
    # API 키 존재 확인
    if not api_key:
        print("❌ .env 파일에서 GEMINI_API_KEY를 찾을 수 없습니다.")
        print("다음 단계를 수행해주세요:")
        print("  1. 프로젝트 루트 디렉토리에 .env 파일이 있는지 확인하세요.")
        print("  2. .env 파일에 다음 줄이 있는지 확인하세요:")
        print("     GEMINI_API_KEY=your_actual_api_key_here")
        print("  3. your_actual_api_key_here 부분을 Google AI Studio에서 발급받은 실제 API 키로 교체하세요.")
        return False
    
    # API 키 형식 기본 확인 (길이나 형식이 올바른지)
    if len(api_key) < 10 or "'" in api_key or '"' in api_key:
        print("❌ API 키 형식이 잘못되었습니다.")
        print("API 키에 따옴표나 공백이 포함되어 있지 않은지 확인하세요.")
        return False
    
    print("✅ .env 파일에서 API 키를 찾았습니다.")
    return api_key

# Google Gemini API 테스트 함수
def test_gemini_api(api_key):
    """
    Google Gemini API에 간단한 요청을 보내 API 연결을 테스트합니다.
    """
    print("\n2. Google Gemini API 연결 테스트 중...")
    
    try:
        # google.generativeai 라이브러리 가져오기 시도
        try:
            import google.generativeai as genai
        except ImportError:
            print("❌ 'google-generativeai' 패키지를 찾을 수 없습니다.")
            print("다음 명령어로 설치해주세요:")
            print("  pip install google-generativeai  # Windows")
            print("  pip3 install google-generativeai  # macOS/Linux")
            return False
        
        # API 설정
        genai.configure(api_key=api_key)
        
        # 간단한 모델 생성 및 쿼리 전송
        print("   API에 테스트 메시지를 전송하는 중...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 간단한 테스트 프롬프트
        response = model.generate_content("안녕하세요, 테스트 메시지입니다.")
        
        # 응답이 있는지 확인
        if not response or not hasattr(response, 'text'):
            print("❌ API에서 응답을 받았지만, 형식이 예상과 다릅니다.")
            return False
        
        # 응답 출력
        print("✅ API 응답 받음: ", response.text)
        return True
        
    except Exception as e:
        print(f"❌ API 연결 중 오류 발생: {str(e)}")
        if "invalid api key" in str(e).lower():
            print("   API 키가 유효하지 않습니다. Google AI Studio에서 새 키를 발급받아 시도하세요.")
        elif "permission denied" in str(e).lower():
            print("   API 사용 권한이 없습니다. Google AI Studio에서 권한을 확인하세요.")
        elif "quota" in str(e).lower():
            print("   API 할당량이 초과되었습니다. 나중에 다시 시도하거나 새 API 키를 발급받으세요.")
        return False

def main():
    """
    메인 함수 - API 연결 테스트 실행
    """
    print_start_message()
    
    # API 키 확인
    api_key = check_api_key()
    if not api_key:
        print_completion_message(success=False)
        return
    
    # API 연결 테스트 및 약간의 지연 효과
    time.sleep(1)  # 사용자 경험을 위한 짧은 대기 시간
    success = test_gemini_api(api_key)
    
    # 결과 출력
    print_completion_message(success)

if __name__ == "__main__":
    main()