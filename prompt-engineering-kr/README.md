# 프롬프트 엔지니어링 실습 자료

프롬프트 엔지니어링의 핵심 개념과 기법을 체계적으로 학습하고 실습할 수 있는 교육 자료입니다.
AI가 생성하는 결과를 어떻게 개선하고 최적화할 수 있는지 실습을 통해 배울 수 있습니다.

## 📚 개요

본 교안은 프롬프트 엔지니어링의 다양한 측면을 다룹니다:
- 학업 보고서 및 과제 작성 최적화
- 프로그래밍 학습 및 과제 지원
- 연구 및 데이터 분석 지원
- 취업 준비 및 경력 개발
- 실용적 프롬프트 패턴 마스터하기
- 윤리적 활용과 학문적 진실성

각 주제별로 실습 코드와 예시가 제공됩니다.

## 🔧 설치 및 설정

### 기본 요구사항

- Python 3.8 이상
- 인터넷 연결

### 설치 방법

1. 저장소 복제:
   ```bash
   git clone https://github.com/yourusername/prompt-engineering-practice.git
   cd prompt-engineering-practice
   ```

2. 필요한 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

3. 환경 설정 파일 생성:
   ```bash
   cp .env.example .env
   # .env 파일을 편집하여 실제 API 키 입력
   ```

## 🚀 실습 시작하기

각 챕터별 실습 예시:

```bash
# 챕터 1: 학업 기본 - 보고서 및 과제 작성 최적화
python chapters/chapter1/1.1_report_writing.py

# 챕터 2: 프로그래밍 학습 및 과제 지원
python chapters/chapter2/2.1_code_explanation.py

# 기타 챕터도 동일한 방식으로 실행
```

## 🧪 API 키 없이 테스트하기

API 키가 없거나 API 호출을 절약하고 싶은 경우, 'mock' 모드를 사용할 수 있습니다:

```python
from utils import generate_text

# 모의 응답 모드 사용
result = generate_text("인공지능에 대해 설명해주세요.", model="mock")
print(result)
```

## 📁 프로젝트 구조

```
prompt-engineering-practice/
├── chapters/                   # 챕터별 실습 코드
│   ├── chapter1/               # 학업 기본: 보고서 및 과제 작성 최적화
│   ├── chapter2/               # 프로그래밍 학습 및 과제 지원
│   └── ...
├── utils/                      # 공통 유틸리티 함수
│   ├── api_utils.py            # API 연결 및 LLM 모델 유틸리티
│   ├── prompt_utils.py         # 프롬프트 관리 유틸리티
│   └── file_utils.py           # 파일 처리 유틸리티
├── data/                       # 샘플 데이터 (필요시)
├── results/                    # 생성된 결과 저장 폴더
├── .env.example                # 환경 변수 예시 파일
├── .gitignore                  # Git 제외 파일 목록
├── requirements.txt            # 필요한 Python 패키지
└── README.md                   # 프로젝트 설명
```

## 💡 자원 및 참고 자료

- [OpenAI API 문서](https://platform.openai.com/docs/)
- [Google Gemini API 문서](https://ai.google.dev/docs)
- [Anthropic Claude API 문서](https://docs.anthropic.com/claude/docs)
- [프롬프트 엔지니어링 가이드](https://www.promptingguide.ai/)

## 🤝 기여하기

버그 리포트, 기능 요청, 풀 리퀘스트는 모두 환영합니다.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.