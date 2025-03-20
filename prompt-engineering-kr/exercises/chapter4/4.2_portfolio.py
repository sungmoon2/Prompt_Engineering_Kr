"""
누락된 챕터 파일 생성 스크립트
챕터 2-7의 x.2, x.3, x.4, x.5 세부 챕터 파일 생성
"""

import os

def create_empty_file(path):
    """빈 파일 생성"""
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w', encoding='utf-8') as f:
        pass
    print(f"파일 생성: {path}")

def main():
    # 현재 작업 디렉토리 확인 (prompt-engineering-kr 안에 있다고 가정)
    cwd = os.getcwd()
    if not os.path.basename(cwd) == "prompt-engineering-kr":
        print("경고: 이 스크립트는 prompt-engineering-kr 디렉토리 내에서 실행되어야 합니다.")
        choice = input("계속 진행하시겠습니까? (y/n): ")
        if choice.lower() != 'y':
            return
    
    # 누락된 챕터 2의 파일들
    chapter2_missing = [
        "2.2.1_task_analysis.py",
        "2.2.2_algorithm_design.py",
        "2.2.3_implementation_guide.py",
        "2.2.4_code_request_strategy.py",
        "2.3.1_error_diagnosis.py",
        "2.3.2_code_improvement.py",
        "2.3.3_code_explanation.py",
        "2.3.4_style_enhancement.py",
        "2.4.1_software_design.py",
        "2.4.2_project_structure.py",
        "2.4.3_requirements_definition.py",
        "2.4.4_oop_design.py",
        "2.5.1_code_documentation.py",
        "2.5.2_readme_guide.py",
        "2.5.3_api_documentation.py",
        "2.5.4_tech_stack_description.py"
    ]
    
    # 누락된 챕터 3의 파일들
    chapter3_missing = [
        "3.2.1_data_interpretation.py",
        "3.2.2_statistical_analysis.py",
        "3.2.3_data_visualization.py",
        "3.2.4_analysis_method_selection.py",
        "3.3.1_paper_structure.py",
        "3.3.2_literature_review.py",
        "3.3.3_result_discussion.py",
        "3.3.4_abstract_conclusion.py",
        "3.4.1_experiment_consultation.py",
        "3.4.2_variable_control.py",
        "3.4.3_result_analysis_framework.py",
        "3.4.4_experiment_limitations.py",
        "3.5.1_research_presentation.py",
        "3.5.2_poster_design.py",
        "3.5.3_qa_preparation.py",
        "3.5.4_feedback_utilization.py"
    ]
    
    # 누락된 챕터 4의 파일들
    chapter4_missing = [
        "4.2.1_portfolio_content_planning.py",
        "4.2.2_project_description.py",
        "4.2.3_design_direction.py",
        "4.2.4_target_audience_design.py",
        "4.3.1_job_specific_questions.py",
        "4.3.2_experience_structured_response.py",
        "4.3.3_pressure_question_strategy.py",
        "4.3.4_interview_simulation.py",
        "4.4.1_competition_proposal_writing.py",
        "4.4.2_idea_differentiation.py",
        "4.4.3_criteria_optimized_proposal.py",
        "4.4.4_presentation_optimization.py",
        "4.5.1_capability_assessment.py",
        "4.5.2_job_specific_analysis.py",
        "4.5.3_personal_branding.py",
        "4.5.4_networking_preparation.py"
    ]
    
    # 누락된 챕터 5의 파일들
    chapter5_missing = [
        "5.2.1_complex_problem_decomposition.py",
        "5.2.2_logical_reasoning_guide.py",
        "5.2.3_error_detection.py",
        "5.2.4_subject_specific_thinking.py",
        "5.3.1_example_selection.py",
        "5.3.2_pattern_recognition.py",
        "5.3.3_zero_shot_learning.py",
        "5.3.4_example_frameworks.py",
        "5.4.1_document_format_control.py",
        "5.4.2_structured_output.py",
        "5.4.3_template_consistency.py",
        "5.4.4_korean_document_guidelines.py",
        "5.5.1_combined_pattern_prompts.py",
        "5.5.2_prompt_chaining.py",
        "5.5.3_feedback_improvement.py",
        "5.5.4_complex_task_prompting.py"
    ]
    
    # 누락된 챕터 6의 파일들 
    chapter6_missing = [
        "6.1.1_assignment_planner.py",
        "6.1.2_research_collector.py",
        "6.1.3_report_workflow.py",
        "6.1.4_review_process.py",
        "6.2.1_job_document_workflow.py",
        "6.2.2_company_research.py",
        "6.2.3_interview_feedback_system.py",
        "6.2.4_career_branding_strategy.py",
        "6.3.1_idea_generation.py",
        "6.3.2_team_project_planning.py",
        "6.3.3_content_creation_workflow.py",
        "6.3.4_creative_project_evaluation.py",
        "6.4.1_study_material_summary.py",
        "6.4.2_personalized_learning_plan.py",
        "6.4.3_review_reinforcement.py",
        "6.4.4_exam_preparation_workflow.py",
        "6.5.1_major_specific_cases.py",
        "6.5.2_academic_year_templates.py",
        "6.5.3_student_success_analysis.py",
        "6.5.4_prompt_library_guide.py"
    ]
    
    # 누락된 챕터 7의 파일들
    chapter7_missing = [
        "7.2.1_ai_content_citation.py",
        "7.2.2_plagiarism_prevention.py",
        "7.2.3_transparency_maintenance.py",
        "7.2.4_academic_writing_position.py",
        "7.3.1_response_evaluation.py",
        "7.3.2_creativity_balance.py",
        "7.3.3_dependency_prevention.py",
        "7.3.4_learning_enhancement.py",
        "7.4.1_sensitive_info_prompts.py",
        "7.4.2_anonymization_strategy.py",
        "7.4.3_data_sharing_precautions.py",
        "7.4.4_security_awareness.py",
        "7.5.1_cost_effective_usage.py",
        "7.5.2_token_optimization.py",
        "7.5.3_learning_capability_balance.py",
        "7.5.4_technology_adaptation.py"
    ]
    
    # 모든 누락된 파일 리스트
    missing_files = {
        "chapter2": chapter2_missing,
        "chapter3": chapter3_missing,
        "chapter4": chapter4_missing,
        "chapter5": chapter5_missing,
        "chapter6": chapter6_missing,
        "chapter7": chapter7_missing
    }
    
    # 누락된 파일 생성
    for chapter, files in missing_files.items():
        for file in files:
            file_path = os.path.join("exercises", chapter, file)
            create_empty_file(file_path)
    
    print("\n모든 누락된 파일이 성공적으로 생성되었습니다!")

if __name__ == "__main__":
    main()