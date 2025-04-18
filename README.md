<h1 align="center" style="background-color: white; color: orange; padding: 10px; border-radius: 5px; font-weight: bold; font-family: 'Arial', sans-serif;">
  <img src="versions/v2/web_flask/home/static/img/favicon.png" 
       alt="icon" 
       style="width: 40px; height: 40px; border-radius: 50%; border: 2px dashed orange; padding: 5px; vertical-align: middle;"> 
  <span style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">EduPathway</span> 
</h1>

## 🔭 *1. Project Description*
*Edupathway 🎓 is a platform dedicated to supporting SDG 4: Quality Education by providing 100% free, secure, and accessible solutions for students and educational institutions. Our mission is to break financial barriers and ensure that education is truly accessible to everyone. From tuition payments to managing student records and facilitating seamless transactions, Eduthpay eliminates all costs for users, creating a world where education is a right, not a privilege.*

- ### *What Does Edupathway Do?*
*Edupathway helps students take any program or course they wish by providing 100% free, secure, and accessible payment solutions. It tracks students' progress and evolution throughout their academic journey, ensuring they have all the resources needed to succeed. With a simple and user-friendly platform, Edupathway empowers students to manage their tuition payments, view their progress, and access their records—all at no cost. By eliminating financial barriers, Edupathway makes education accessible to everyone, turning learning into a right, not a privilege*
- ### *Technologies used*
<p align="center"> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>  </p>


*We used Linux as the operating system for its stability, Python (Flask) for its simplicity in building scalable web applications, and MySQL for efficient data management. Nginx serves as the web server, while Bootstrap, HTML5, CSS3, and JavaScript enable a responsive, dynamic, and interactive front-end experience. Git helps with version control throughout development.*
## 🛠️ *2. Installation Steps*
*⚠️ Ensure that the technologies listed above are installed before proceeding with the installation steps, as it won't work otherwise!*

*1. Clone the repository*

```bash
git clone https://github.com/antoineleno/EduPathway.git
```

*2. Change the working directory*

```bash
cd EduPathway
``` 

*3. Create a virtual environment*

```bash
python3 -m venv myenv
```
*4. Activate the virtual environment*

```bash
source myenv/bin/activate
```

*5. Install dependencies*

```bash
pip install -r requirements/requirements.txt
```
*6. Set up the database*
```bash
sudo mysql -u root -p < requirements/database_setup.sql
sudo mysql -u root -p < requirements/edupathway_db.sql
```
*7. Set up the trigger for room*
```bash
sudo mysql -u root -p < requirements/room_trigger.sql
```

*8. Change the working directory and Run the app*

### *For version 1*

```bash
cd; cd EduPathway/versions/v1/web_flask; python3 app.py
```
### *For version 2*

```bash
cd; cd EduPathway/versions/v2/web_flask; python3 app.py
```
🌟 You are all set!


## 📘  *How to use this project*
*After completing the installation steps, an admin, and two students users will be created with the following credentials :*
> - ***email***&nbsp;: *edupathwayadmin@gmail.com*
> - ***password*** : *edupathwaypassword*

> - ***email***&nbsp;: *nouhandoumbouya@gmail.com*
> - ***password*** : *nouhanpassword*

> - ***email***&nbsp;: *alisena@gmail.com*
> - ***password*** : *alisenapassword*

## 👯 *3. Project Contributors*

<p align="center">
  <a href="https://github.com/antoineleno/EduPathway/graphs/contributors">
    <img src="versions/v2/web_flask/home/static/img/antoineleno.png" alt="Profile Picture" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-right: 20px;">
    <img src="versions/v2/web_flask/home/static/img/nouhandoubouya.png" alt="Profile Picture" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-right: 20px;">
    <img src="versions/v2/web_flask/home/static/img/alisena_d.png" alt="Profile Picture" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-right: 20px;">
    <img src="versions/v2/web_flask/home/static/img/maria_iqbal.png" alt="Profile Picture" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-right: 20px;">
    <img src="versions/v2/web_flask/home/static/img/rashdul.png" alt="Profile Picture" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-right: 20px;">
  </a>
</p>


> ### 📫 *How to reach us*
<p align="center">
  <strong>Antoine</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Nouhan</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Alisena</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Maria</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Rashidul</strong>
  <br>
  <a href="mailto:lenoantoine2000@gmail.com">
      <img src="versions/v2/web_flask/home/static/img/email.png" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://github.com/antoineleno">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://instagram.com/antoineleno7" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="20" width="20"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="mailto:nouhandoumbouya655@gmail.com">
      <img src="versions/v2/web_flask/home/static/img/email.png" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://github.com/NouhanDoumbouya123">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://www.instagram.com/doumbouyanouhan1234?igsh=cmdqd3ltdDFnam9u" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="20" width="20"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="mailto:ali.danishwer@student.aiu.edu.my">
      <img src="versions/v2/web_flask/home/static/img/email.png" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://github.com/alisenadanishwer">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://www.instagram.com/alisena.danishwer?igsh=bmFkamR3ZzAzejk4" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="20" width="20"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="mailto:mariaiqbal112003@gmail.com">
      <img src="versions/v2/web_flask/home/static/img/email.png" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://github.com/Maria200311">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://www.instagram.com/mariaiqbal200311?igsh=dTkwMnVmZnRtc3hy" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="20" width="20"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="mailto:mdislam0996@gmail.com">
    <img src="versions/v2/web_flask/home/static/img/email.png" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://github.com/mrirashid">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Instagram" height="20" width="20" />
  </a>
  <a href="https://www.instagram.com/mri_rashid?igsh=MWdjbTM4dWk0ZGQ1OA==" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="20" width="20" />
  </a>
</p>

## 🎯 *Roles and Contributions*

| **Contributor**           | **Role**                  | **Contributions** |
|---------------------------|---------------------------|-------------------|
| **Antoine Leno**          | Backend Developer          | Backend development (Flask, MySQL), database handling, and logic implementation. |
| **Nouhan Doumbouya**      | Frontend Developer         | Front-end development (HTML, CSS, Bootstrap), template integration, UI customization, and JavaScript interactivity. <br> &nbsp;&nbsp;• Developed admin dashboard for managing programs, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;courses, resources, projects, and quizzes <br> &nbsp;&nbsp;• Built program synopsis page displaying all related courses, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resources, projects, and quizzes <br> &nbsp;&nbsp;• Developed course content pages with access to resources, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;projects, and quizzes |
| **Alisena Danishwer**      | Frontend Developer         | Front-end development focused on user profile and peer learning page.<br> &nbsp;&nbsp;•  Developed user profile page <br> &nbsp;&nbsp;• Developed peers learning page |
| **Maria Iqbal**           | Data & Dashboard Engineer  | Data modeling, Student progress tracking features, Admin dashboard logic |
| **Rashidul Islam**        | QA & Optimization          | Error handling, Bug fixing, Testing, Code optimization |




## ✅ *4. Tests*
*Run the following command from the root of the project directory to execute all tests and verify the software functionality :*

### *For version 1*
```bash
cd; cd EduPathway/versions/v1; python3 -m unittest discover -v tests
```
### *For version 2*
```bash
cd; cd EduPathway/versions/v2; python3 -m unittest discover -v tests
```

## 🏅 *5. Badge*
<p align="center">
  <a href="https://github.com/antoineleno/EduPathway/fork" target="blank">
    <img src="https://img.shields.io/github/forks/antoineleno/EduPathway?style=flat-square" alt="aEduPathway forks"/>
  </a>
  <a href="https://github.com/antoineleno/EduPathway/stargazers" target="blank">
    <img src="https://img.shields.io/github/stars/antoineleno/EduPathway?style=flat-square" alt="EduPathway stars"/>
  </a>
  <a href="https://github.com/antoineleno/EduPathway/issues" target="blank">
    <img src="https://img.shields.io/github/issues/antoineleno/EduPathway?style=flat-square" alt="EduPathway issues"/>
  </a>
  <a href="https://github.com/antoineleno/EduPathway/pulls" target="blank">
    <img src="https://img.shields.io/github/issues-pr/antoineleno/EduPathway?style=flat-square" alt="EduPathway pull-requests"/>
  </a>
  <!-- Example Contribution Badge -->
  <a href="https://github.com/antoineleno/EduPathway/graphs/contributors" target="blank">
    <img src="https://img.shields.io/github/contributors/antoineleno/EduPathway?style=flat-square" alt="EduPathway contributors"/>
  </a>
</p>
