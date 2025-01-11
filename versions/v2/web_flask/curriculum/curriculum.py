#!/usr/bin/python3
"""
Curriculum module
"""

from flask import Blueprint, render_template
from flask import redirect, url_for, flash, request, jsonify
from models import storage
import markdown
from flask_login import current_user
from models.models import Program, Course, Enrollment, UserQuiz
from curriculum import app_views_curriculum

curriculum = Blueprint('curriculum', __name__)

@app_views_curriculum.route("/", methods = ['POST', 'GET'])
def home():
    """SignIn"""
    if request.method == "POST":
        data = request.json
        program_id = data.get('program_id')

        if program_id:
            try:
                user_enrollment = Enrollment(user_id=current_user.id,
                                            program_id=program_id,
                                            progress=0)
                user_enrollment.save()
            except Exception as e:
                return jsonify({'error': 'An error occured'}), 400
            return jsonify({'message': 'Enrolled successfully'}), 200
        else:
            return jsonify({'error': 'Missing program_id'}), 400
    if current_user.is_authenticated:
        program_id = request.args.get('program_id')
        if program_id is None:
            program_id = request.args.get('program_id')
        
        current_program = storage.get_object(Program, id=program_id)
        order_by = (Course.created_at, 'asc')

        all_scores = []
        passing_socres = []
        tottal_quizzes = 0
        is_enrolled = storage.get_object(Enrollment,
                                        user_id=current_user.id,
                                        program_id=program_id)
        all_courses = storage.get_object(cls=Course, all=True,
                                         order_by=order_by,
                                         program_id=program_id)
        courses = []
        for course in all_courses:
            resources = sorted(course.resources, key=lambda r: r.created_at)
            resources_titles = [resource.title for resource in resources]
            resources_ids = [resource.id for resource in resources]
            all_resources = list(zip(resources_titles, resources_ids))

            projects = course.projects
            projects_title = [project.title for project in projects]
            projects_ids = [project.id for project in projects]
            all_projects = list(zip(projects_title, projects_ids))

            quizzes = sorted(course.quizzes, key=lambda q: q.created_at)
            if len(quizzes) != 0:
                tottal_quizzes +=1

            quizzes_title = []
            if len(quizzes) != 0:
                quizzes_title = [['Quiz', course.id]]

            status = 'done'
            score = 0
            i = 0
            quiz_test = storage.get_object(UserQuiz,
                                           course_id=course.id,
                                           user_id=current_user.id)
            if quiz_test is not None:
                score = quiz_test.score
                all_scores.append(score)
                if score >= 50:
                    passing_socres.append(score)
                i +=1
            quiz_result = [score]

            if i == 0:
                status = 'pending'
                quiz_result = [0]
            quizzes_title = []
            if len(quizzes) != 0:
                quizzes_title = [['Quiz', course.id]]
            else:
                quiz_result = []
                status = 'done'
            if score < 50:
                status = 'pending'
            courses.append({'name': course.name,
                            'course_id': course.id,
                            'description': course.description,
                            'resources': all_resources,
                            'projects': all_projects,
                            'resouces_id': resources_ids,
                            'quiz_result': quiz_result,
                            'quizzes': quizzes_title,
                            'status': status})
        average = 0
        formatted_average = 0
        if len(all_scores) != 0:
            evolution = 0
            average = sum(all_scores) / len(all_scores)
            formatted_average = f"{average:.2f}"
            user_enrollment = storage.get_object(Enrollment,
                                                 user_id=current_user.id,
                                                 program_id=program_id)
            if tottal_quizzes != 0:
                evolution = len(passing_socres) / tottal_quizzes
            else:
                evolution = sum(passing_socres) / passing_socres

            user_enrollment.progress = evolution * 100
            storage.save()
        return render_template('program_content.html',
                            current_program=current_program,
                            current_page="programs",
                            courses=courses,
                            is_enrolled=is_enrolled,
                            average=formatted_average)
    else:
        messae = """You need to sign in first before opening a program"""
        flash(messae, "success")
        return redirect(url_for('app_views_home.home'))


@app_views_curriculum.route("/courses", methods = ['POST', 'GET'])
def course_content():
    """SignIn"""
    if request.method == "POST":
        course_id = request.args.get('course_id')
        course = storage.get_object(Course, id=course_id)
        program = course.program
        program_id = program.id
        
        answers = []
        quiz_answers = []
        all_quizes = course.quizzes
        selected_answers = request.form
        for quiz in all_quizes:
            quiz_answers.append(quiz.answer)
        
        for question_id, answer in selected_answers.items():
            answers.append(answer)
        i = 0;
        for response in answers:
            if response in quiz_answers:
                i +=1
        grade = i * 100 / len(quiz_answers)
        user_quiz = storage.get_object(UserQuiz,
                                       user_id=current_user.id,
                                       course_id=course.id)
        if user_quiz:
            user_quiz.score = grade
            storage.save()
        else:
            new_user_quiz = UserQuiz(user_id=current_user.id,
                                     course_id=course.id, score=grade)
            new_user_quiz.save()
        if grade >= 50:
            message = f"Your quiz score is {grade:.2f}%. Well done!"
            error_type = "success"
        else:
            message = f"Your quiz score is {grade:.2f}%. Keep practicing to improve!"
            error_type = "error"
        flash(message, error_type)
        return redirect(url_for('app_views_curriculum.home',
                                program_id=program_id))
    if current_user.is_authenticated:
        course_id = request.args.get('course_id')
        program_id = request.args.get('program_id')
        if program_id and not course_id:
            course = storage.get_object(Course, program_id=program_id,
                                        order_by=(Course.created_at, 'asc'))
            if course is not None:
                course_id = course.id
            else:
                message = """This program currently has no content.
                Please explore other available programs."""
                flash(message, "error")
                return redirect(url_for('app_views_home.home'))

            
        if course_id is not None:
            course = storage.get_object(Course, id=course_id)
            program_id = course.program.id
            user_enrollment = storage.get_object(Enrollment,
                                                 user_id=current_user.id,
                                                 program_id=program_id)
            print(user_enrollment)
            if user_enrollment is None:
                message = """You need to enrolled first before seeing the content of this course"""
                flash(message, "error")
                return redirect(url_for('app_views_home.home'))
            course = storage.get_object(Course, id=course_id)
            program_id = course.program.id
            all_resources = course.resources
            sorted_resources = sorted(all_resources,
                                    key=lambda resource: resource.created_at)
            lessons = []
            for resource in sorted_resources:
                lessons.append({"id": resource.id, "title": resource.title,
                                "description": markdown.markdown(resource.description,
                                                                extensions=['fenced_code'])})
            
            all_projects = course.projects
            project_tasks = []
            for project in all_projects:
                project_tasks.append({'task_name': project.task_name,
                                    'description': markdown.markdown(project.description,
                                                                    extensions=['fenced_code'])})
            
            all_quizes = course.quizzes
            quiz_questions = []
            time_limit = 0
            if len(all_resources) == 0 and len(all_projects) == 0 and len(all_quizes) == 0:
                message = "This course is currently empty. Please check back later for updates."
                flash(message, "success")
                return redirect(url_for('app_views_curriculum.home', program_id=program_id))
            for quiz in all_quizes:
                all_options = quiz.options
                time_limit += quiz.duration
                quiz_questions.append({"id": quiz.id, "question": quiz.question,
                                    "options": [option.option for option in all_options]})

            return render_template('course_content.html',
            lessons=lessons, quiz_questions=quiz_questions,
            project_tasks=project_tasks,
            current_page="programs",
            course=course, time_lit = time_limit * 60)
        return render_template('course_content.html')
    else:
        return render_template('404.html')
