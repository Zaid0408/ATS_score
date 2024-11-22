from pyresparser import ResumeParser
import os
# from docx import Document


filed='/Users/sherazhasan/Desktop/test3/scripts-archive/ZaidResume.pdf'
reume_text="""
Zaid Hasan
zaidhasan04081999@gmail.com |9004496896 | Bengaluru,Karnataka | Linkdeln | Github

Education
BMS College Of Engineering, Bangalore	Expected May 2025 Bachelor of Information Scienec Engineering	Cgpa:8.0 out of 10
Relevant Coursework: Data Structures | Algorithms | Object Oriented Programming | Operating System | Database management Systems | Computer networks | Artificial Intelligence | Web Development | App Development

Skills
Proficient in programming languages like C++, Java 
Proficient in Data Structures and Algorithms
Knowledge of HTML, CSS, MySQL and MongoDB
Native Proficiency in English and  Hindi

Projects
Image Classifier using Binary Classification	
To classify whether image is happy or sad using Machine learning and nueral networks. Implementing the project using python libraries such as OpenCv,Tensorflow and Matplotlib.
To import data and then using deep Nueral Network to classify if an image is happy or sad. Link
Property Managemnt System   
Web-based application designed to streamline property management, transactions, and user interactions. Serving as a database management system, this project empowers users to effortlessly perform CRUD (Create, Read, Update, Delete) operations on property details.
Key Features of thewebsite using: User Authentication, transaction records, Search and filter options, Responsive user interface. 
Used HTML,CSS, JavaScript and frameworks like node.js and react.js along with MongoDB to store property and user details. Link
Restaurant Website	
Implemented a responsive website using HTML and CSS to provide an interactive inetrface. Link

Certifications
Adavnced machine Learning Algorithms
Learning about Nueral networks, ReLu activation Function, Softmax function and Multi-class Classification
Supervised Machine Learning Algorithms such as Regression and Classification
Learning algorithms and having a basic understanding of linear and logistic regression and Binary Classification.

Hackathons
SecureHack 												     July 2023
A cybersecurity Hackathon conducted by BMSCE IEEE society. Developed a Discord Bot to check if a file sent on the platform is harmful or not.
Codeathon											        December 2023
A 24-hour DSA focused Hackathon conducted to challenge coding and problem-solving skills.


"""

data = ResumeParser(reume_text).get_extracted_data()
print(data)


    