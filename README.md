# Create User
*  create User name="Antoine LENO" email="lenoantoine@gmail.com" password="lenoantoine" role="Admin" profile_image="user/static/img/antoineleno"
# Create Program
* create Program name="Data Science" description="This program will give me understanding of computer"
# Create Enrollment
* create Enrollment user_id="" program_id=""
# Create Course
* create Course name="Machine Learning" description="This is machine learning program" user_id="" program_id=""
# Create Resource
* create Resource title="Introduction" link="program/resources/intro.pdg" course_id=""
# Create Project
* create Project title="AirBnB" course_id=""
# Create Task
create Task title="Prime Game" instruction="This is task one" project_id=""
# Create TaskAnswer
create TaskAnswer task_id="" link="task/resources/one"
# Create UserTask
* create UserTask user_id="" task_id="" score=100
# Create Quiz
* create Quiz title="First quiz" question="First question" duration=1 course_id=""
# create Answer
* create Answer answer="ABCD3" quiz_id=""
# create UserQuiz
* create UserQuiz user_id="35159ca3-aac5-40da-9f6e-cdfa9a4e0725" quiz_id="8842c22e-0852-49dd-81d6-5f86b4fd9992" score=50

# Update version
* Open Nginx config file : sudo nano /etc/nginx/sites-available/default
* Update line : set $backend blue
* text nginx : sudo nginx -t
* restart nginx : sudo systemctl restart nginx
* visit localhost : http://localhost

# Run all test cases
* ECOURSE_ENV=test python3 -m unittest discover tests
ENV="EDUPATHWAY_ENV" python3 -m unittest discover -v tests

# Couse name Max : 40 words program 26 words
# For program details : <!-- Program title with link href="{{ url_for('program_detail', program_id=course.id) }}"-->
