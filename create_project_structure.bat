@echo off
REM 프로젝트 루트 디렉토리 생성
mkdir prompt-engineering-kr
cd prompt-engineering-kr

REM 기본 파일 생성
type nul > README.md
type nul > requirements.txt
type nul > .env.example
type nul > .gitignore

REM 폴더 구조 생성
mkdir samples\documents\reports
mkdir samples\documents\presentations
mkdir samples\documents\academic
mkdir samples\data\text_samples
mkdir samples\data\structured_data
mkdir samples\templates\academic
mkdir samples\templates\creative
mkdir samples\templates\professional

REM 챕터 폴더 생성
mkdir exercises
mkdir solutions

REM 챕터별 실습 폴더 및 파일 생성
for /l %%i in (1, 1, 7) do (
  mkdir exercises\chapter%%i
  type nul > exercises\chapter%%i\README.md
  mkdir solutions\chapter%%i
)

REM 챕터 1: 학업 기본: 보고서 및 과제 작성 최적화
type nul > exercises\chapter1\1.1_report_quality.py
type nul > exercises\chapter1\1.2_major_specific_reports.py
type nul > exercises\chapter1\1.3_academic_writing.py
type nul > exercises\chapter1\1.4_term_reports.py
type nul > exercises\chapter1\1.5_presentations.py

REM 챕터 2: 프로그래밍 학습 및 과제 지원
type nul > exercises\chapter2\2.1_coding_concepts.py
type nul > exercises\chapter2\2.2_coding_assignments.py
type nul > exercises\chapter2\2.3_debugging.py
type nul > exercises\chapter2\2.4_project_planning.py
type nul > exercises\chapter2\2.5_documentation.py

REM 챕터 3: 연구 및 데이터 분석 지원
type nul > exercises\chapter3\3.1_research_planning.py
type nul > exercises\chapter3\3.2_data_analysis.py
type nul > exercises\chapter3\3.3_paper_writing.py
type nul > exercises\chapter3\3.4_experiment_design.py
type nul > exercises\chapter3\3.5_academic_presentations.py

REM 챕터 4: 취업 준비 및 경력 개발
type nul > exercises\chapter4\4.1_resume_cover_letter.py
type nul > exercises\chapter4\4.2_portfolio.py
type nul > exercises\chapter4\4.3_interview_prep.py
type nul > exercises\chapter4\4.4_competition_proposals.py
type nul > exercises\chapter4\4.5_career_planning.py

REM 챕터 5: 실용적 프롬프트 패턴 마스터하기
type nul > exercises\chapter5\5.1_role_prompting.py
type nul > exercises\chapter5\5.2_chain_of_thought.py
type nul > exercises\chapter5\5.3_few_shot_learning.py
type nul > exercises\chapter5\5.4_format_control.py
type nul > exercises\chapter5\5.5_complex_prompts.py

REM 챕터 6: 실전 프로젝트 및 활용 사례
type nul > exercises\chapter6\6.1_term_project_system.py
type nul > exercises\chapter6\6.2_job_prep_system.py
type nul > exercises\chapter6\6.3_creative_project.py
type nul > exercises\chapter6\6.4_study_optimization.py
type nul > exercises\chapter6\6.5_success_templates.py

REM 챕터 7: 윤리적 활용과 학문적 진실성
type nul > exercises\chapter7\7.1_ethical_boundaries.py
type nul > exercises\chapter7\7.2_academic_integrity.py
type nul > exercises\chapter7\7.3_critical_thinking.py
type nul > exercises\chapter7\7.4_data_privacy.py
type nul > exercises\chapter7\7.5_sustainable_use.py

REM 부록: 대학생활 필수 프롬프트 템플릿
mkdir exercises\appendix
type nul > exercises\appendix\README.md
type nul > exercises\appendix\a1_academic_templates.py
type nul > exercises\appendix\a2_research_templates.py
type nul > exercises\appendix\a3_career_templates.py
type nul > exercises\appendix\a4_creative_templates.py
type nul > exercises\appendix\a5_productivity_templates.py

REM 유틸리티 폴더 및 파일
mkdir utils
type nul > utils\__init__.py
type nul > utils\api_utils.py
type nul > utils\prompt_utils.py
type nul > utils\file_utils.py
type nul > utils\evaluation_utils.py

echo 프롬프트 엔지니어링 교안 프로젝트 구조가 성공적으로 생성되었습니다!