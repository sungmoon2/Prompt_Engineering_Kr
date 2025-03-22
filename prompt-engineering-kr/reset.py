"""
프롬프트 엔지니어링 교안 프로젝트 구조 완전 재구성 스크립트

모든 섹션에 .1, .2, .3까지의 세부파일을 포함하는 구조:
/exercises
  /part1
    /1.1
      1.1_clear_instructions.py
      1.1.1_specific_requests.py
      1.1.2_key_questions.py
      1.1.3_concrete_terms.py
    /1.2
      1.2_asking_without_knowledge.py
      1.2.1_knowledge_level.py
      1.2.2_basic_concepts.py
      1.2.3_stepping_stones.py
    ...
"""

import os
import shutil
import re
from pathlib import Path

# 기본 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent
EXERCISES_DIR = BASE_DIR / "exercises"

# 제거할 폴더 (chapter 폴더)
CHAPTER_DIRS_TO_REMOVE = [
    "chapter1", "chapter2", "chapter3", "chapter4", 
    "chapter5", "chapter6", "chapter7"
]

# 각 파트별 폴더 및 파일 구조 정의
EXERCISE_STRUCTURE = {
    "part0": {
        "0.1": [
            "0.1_intro_to_prompting.py",
            "0.1.1_basic_prompts.py",
            "0.1.2_prompt_components.py",
            "0.1.3_prompt_examples.py"
        ],
        "0.2": [
            "0.2_conversation_model.py",
            "0.2.1_conversation_principles.py",
            "0.2.2_dialog_examples.py",
            "0.2.3_interaction_patterns.py"
        ],
        "0.3": [
            "0.3_setup_environment.py",
            "0.3.1_api_setup.py",
            "0.3.2_usage_tips.py",
            "0.3.3_troubleshooting.py"
        ]
    },
    "part1": {
        "1.1": [
            "1.1_clear_instructions.py",
            "1.1.1_specific_requests.py",
            "1.1.2_key_questions.py",
            "1.1.3_concrete_terms.py"
        ],
        "1.2": [
            "1.2_asking_without_knowledge.py",
            "1.2.1_knowledge_level.py",
            "1.2.2_basic_concepts.py",
            "1.2.3_stepping_stones.py"
        ],
        "1.3": [
            "1.3_information_gathering.py",
            "1.3.1_exploration_techniques.py",
            "1.3.2_follow_up_questions.py",
            "1.3.3_information_refinement.py"
        ],
        "1.4": [
            "1.4_exploring_new_topics.py",
            "1.4.1_unfamiliar_subjects.py",
            "1.4.2_incremental_learning.py",
            "1.4.3_concept_connections.py"
        ]
    },
    "part2": {
        "2.1": [
            "2.1_task_analysis.py",
            "2.1.1_requirement_identification.py",
            "2.1.2_scope_definition.py",
            "2.1.3_success_criteria.py"
        ],
        "2.2": [
            "2.2_info_gathering.py",
            "2.2.1_research_strategies.py",
            "2.2.2_data_validation.py",
            "2.2.3_information_organization.py"
        ],
        "2.3": [
            "2.3_integrative_thinking.py",
            "2.3.1_pattern_recognition.py",
            "2.3.2_synthesis_methods.py",
            "2.3.3_insight_development.py"
        ],
        "2.4": [
            "2.4_complex_task_decomposition.py",
            "2.4.1_subtask_definition.py",
            "2.4.2_dependency_mapping.py",
            "2.4.3_resource_allocation.py"
        ]
    },
    "part3": {
        "3.1": [
            "3.1_overcome_token_limits.py",
            "3.1.1_compression_techniques.py",
            "3.1.2_chunking_methods.py",
            "3.1.3_information_prioritization.py"
        ],
        "3.2": [
            "3.2_conversation_reset.py",
            "3.2.1_context_preservation.py",
            "3.2.2_summary_techniques.py",
            "3.2.3_continuity_strategies.py"
        ],
        "3.3": [
            "3.3_prompt_management.py",
            "3.3.1_organization_methods.py",
            "3.3.2_versioning_system.py",
            "3.3.3_template_creation.py"
        ],
        "3.4": [
            "3.4_longterm_project.py",
            "3.4.1_persistent_context.py",
            "3.4.2_progressive_refinement.py",
            "3.4.3_milestone_tracking.py"
        ]
    },
    "part4": {
        "4.1": [
            "4.1_research_topic_exploration.py",
            "4.1.1_topic_refinement.py",
            "4.1.2_research_questions.py",
            "4.1.3_literature_mapping.py"
        ],
        "4.2": [
            "4.2_logical_structure.py",
            "4.2.1_outline_development.py",
            "4.2.2_argument_flow.py",
            "4.2.3_coherence_techniques.py"
        ],
        "4.3": [
            "4.3_academic_writing.py",
            "4.3.1_scholarly_language.py",
            "4.3.2_citation_methods.py",
            "4.3.3_evidence_integration.py"
        ],
        "4.4": [
            "4.4_report_improvement.py",
            "4.4.1_revision_strategies.py",
            "4.4.2_feedback_incorporation.py",
            "4.4.3_quality_enhancement.py"
        ]
    },
    "part5": {
        "5.1": [
            "5.1_code_concept_understanding.py",
            "5.1.1_algorithm_explanation.py",
            "5.1.2_code_visualization.py",
            "5.1.3_concept_implementation.py"
        ],
        "5.2": [
            "5.2_code_generation.py",
            "5.2.1_requirement_translation.py",
            "5.2.2_optimization_strategies.py",
            "5.2.3_code_quality.py"
        ],
        "5.3": [
            "5.3_project_structure.py",
            "5.3.1_architecture_design.py",
            "5.3.2_modular_organization.py",
            "5.3.3_scalability_planning.py"
        ],
        "5.4": [
            "5.4_programming_project.py",
            "5.4.1_development_process.py",
            "5.4.2_testing_strategies.py",
            "5.4.3_documentation_practices.py"
        ]
    },
    "part6": {
        "6.1": [
            "6.1_domain_introduction.py",
            "6.1.1_field_terminology.py",
            "6.1.2_domain_concepts.py",
            "6.1.3_knowledge_structure.py"
        ],
        "6.2": [
            "6.2_field_specific_prompts.py",
            "6.2.1_specialized_language.py",
            "6.2.2_expert_knowledge.py",
            "6.2.3_field_practices.py"
        ],
        "6.3": [
            "6.3_expert_perspective.py",
            "6.3.1_role_simulation.py",
            "6.3.2_professional_insights.py",
            "6.3.3_expertise_levels.py"
        ],
        "6.4": [
            "6.4_multidisciplinary_exploration.py",
            "6.4.1_cross_domain_approaches.py",
            "6.4.2_interdisciplinary_analysis.py",
            "6.4.3_knowledge_integration.py"
        ]
    },
    "part7": {
        "7.1": [
            "7.1_role_prompting.py",
            "7.1.1_persona_definition.py",
            "7.1.2_expert_emulation.py",
            "7.1.3_perspective_diversity.py"
        ],
        "7.2": [
            "7.2_chain_of_thought.py",
            "7.2.1_reasoning_steps.py",
            "7.2.2_logical_progression.py",
            "7.2.3_conclusion_derivation.py"
        ],
        "7.3": [
            "7.3_format_control.py",
            "7.3.1_output_structuring.py",
            "7.3.2_template_design.py",
            "7.3.3_format_specifications.py"
        ],
        "7.4": [
            "7.4_advanced_patterns.py",
            "7.4.1_pattern_combination.py",
            "7.4.2_custom_techniques.py",
            "7.4.3_pattern_adaptation.py"
        ]
    },
    "part8": {
        "8.1": [
            "8.1_prompt_analysis.py",
            "8.1.1_component_identification.py",
            "8.1.2_effectiveness_evaluation.py",
            "8.1.3_structural_analysis.py"
        ],
        "8.2": [
            "8.2_iterative_improvement.py",
            "8.2.1_testing_methodology.py",
            "8.2.2_incremental_refinement.py",
            "8.2.3_comparative_analysis.py"
        ],
        "8.3": [
            "8.3_prompt_optimization.py",
            "8.3.1_performance_metrics.py",
            "8.3.2_optimization_techniques.py",
            "8.3.3_benchmarking_methods.py"
        ],
        "8.4": [
            "8.4_debugging_workshop.py",
            "8.4.1_common_issues.py",
            "8.4.2_resolution_strategies.py",
            "8.4.3_preventive_practices.py"
        ]
    },
    "part9": {
        "9.1": [
            "9.1_academic_integrity.py",
            "9.1.1_ethical_guidelines.py",
            "9.1.2_proper_attribution.py",
            "9.1.3_plagiarism_prevention.py"
        ],
        "9.2": [
            "9.2_critical_evaluation.py",
            "9.2.1_fact_checking.py",
            "9.2.2_bias_identification.py",
            "9.2.3_source_verification.py"
        ],
        "9.3": [
            "9.3_sustainable_learning.py",
            "9.3.1_skill_development.py",
            "9.3.2_knowledge_retention.py",
            "9.3.3_independent_thinking.py"
        ]
    }
}

def create_exercise_file(filepath, filename):
    """실습 파일 기본 구조 생성"""
    # 파일 이름에서 부분 정보 추출
    parts = filename.split('_')
    section_id = parts[0]  # 예: 1.1.1
    
    # 파트 번호와 섹션 번호 추출
    if '.' in section_id:
        part_num = section_id.split('.')[0]
        section_desc = section_id
    else:
        part_num = section_id[0]
        section_desc = section_id
    
    file_title = ' '.join(word.capitalize() for word in '_'.join(parts[1:]).split('.')[0].split('-'))
    
    content = f'''"""
{file_title} 실습 모듈

Part {part_num} - 섹션 {section_desc} 실습 코드: 기본 프롬프트와 향상된 프롬프트의 차이 비교
"""

import os
import sys
from typing import Dict, List, Any, Optional

# 상위 디렉토리를 경로에 추가하여 utils 모듈을 import할 수 있게 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.ai_client import get_completion
from utils.prompt_builder import PromptBuilder
from utils.file_handler import save_markdown
from utils.ui_helpers import (
    print_header, print_step, get_user_input, 
    display_results_comparison, print_prompt_summary,
    print_learning_points
)
from utils.example_data import get_examples_by_category
# from utils.prompt_templates import get_basic_{file_title.lower().replace(' ', '_')}_prompt, get_enhanced_{file_title.lower().replace(' ', '_')}_prompt

def main():
    """메인 함수"""
    print_header(f"{file_title}")
    
    # 1. 주제/과제 선택 또는 입력
    print_step(1, "주제 선택")
    # TODO: 예제 데이터 및 사용자 입력 구현
    
    # 2. 기본 프롬프트 생성 및 실행
    print_step(2, "기본 프롬프트로 질문하기")
    # TODO: 기본 프롬프트 생성 및 실행
    
    # 3. 향상된 프롬프트 생성 및 실행
    print_step(3, "향상된 프롬프트로 질문하기")
    # TODO: 향상된 프롬프트 생성 및 실행
    
    # 4. 결과 비교 및 저장
    print_step(4, "결과 비교 및 저장")
    # TODO: 결과 비교 및 저장
    
    # 5. 학습 내용 정리
    print_step(5, "학습 내용 정리")
    # TODO: 학습 내용 정리

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\n\\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as err:
        print(f"\\n오류 발생: {{err}}")
        print("API 키나 네트워크 연결을 확인하세요.")
'''
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def check_existing_files():
    """exercises 폴더 내의 기존 파일 정리"""
    if not os.path.exists(EXERCISES_DIR):
        return
    
    # 기존 실습 파일 검사 및 정리
    for part_dir in os.listdir(EXERCISES_DIR):
        part_path = os.path.join(EXERCISES_DIR, part_dir)
        if os.path.isdir(part_path):
            # 현재 part 폴더 내의 모든 파일 및 폴더 삭제
            for item in os.listdir(part_path):
                item_path = os.path.join(part_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"파일 삭제: {part_dir}/{item}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"폴더 삭제: {part_dir}/{item}")

def main():
    """메인 함수"""
    print("프롬프트 엔지니어링 교안 프로젝트 구조 재구성을 시작합니다...")
    
    # 1. chapter 폴더 삭제
    for dir_name in CHAPTER_DIRS_TO_REMOVE:
        dir_path = os.path.join(BASE_DIR, dir_name)
        if os.path.exists(dir_path):
            print(f"chapter 폴더 삭제: {dir_name}")
            shutil.rmtree(dir_path)
    
    # 2. exercises 폴더 내의 기존 파일 정리
    check_existing_files()
    
    # 3. 새로운 폴더 구조 및 파일 생성
    print("\n새로운 폴더 구조 및 파일 생성 중...")
    total_files = 0
    
    for part, sections in EXERCISE_STRUCTURE.items():
        part_dir = os.path.join(EXERCISES_DIR, part)
        os.makedirs(part_dir, exist_ok=True)
        
        for section, files in sections.items():
            section_dir = os.path.join(part_dir, section)
            os.makedirs(section_dir, exist_ok=True)
            print(f"폴더 생성: {part}/{section}")
            
            # 모든 관련 파일 생성
            for file in files:
                file_path = os.path.join(section_dir, file)
                create_exercise_file(file_path, file)
                print(f"  파일 생성: {part}/{section}/{file}")
                total_files += 1
    
    print("\n프로젝트 구조 재구성이 완료되었습니다!")
    print(f"총 {total_files} 개의 실습 파일이 생성되었습니다.")

if __name__ == "__main__":
    main()