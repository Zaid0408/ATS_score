from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = """
zaid.has07@gmail.com | +91 9004496896 | LinkedIn | Github | Bengaluru,Karnataka | www.github.com/zaidhasan | https://www.linkedin.com/in/zaid-hasan/ mbn.com/zaidhasan | http://zaidhasan.github.io/ linkedin.com/zaidhasan
https://www.linkedin.com/



Education
Bachelor of Engineering: Information Science 	              	 2021-2025          XYZ College of Engineering	     

Skills
Programming Languages:  Java | Python | C++ | Kotlin | JavaScript 
Web development: HTML |  CSS |  JavaScript |  React.js |  Node.js |  Flask 
Databases: MongoDB | Google Firebase Database 
Machine Learning and AI: Tensorflow |  Pytorch | OpenCV 
Mobile development: Android Studio 

You can also reach me at 12345-67890 or +1234567890123. my altremail is zaidhasan@yahoo.com  zaid@@info.com zaid@

"""

text2="""FIRST LAST

Bay Area, California • +1-234-456-789 • professionalemail@resumeworded.com • linkedin.com/in/username

PROFESSIONAL EXPERIENCE
Resume Worded, New York, NY Jun 2018 – Present
QA Manual Tester
● Enabled critical test case complexity metrics with support for Rapid adoption of functional automation using
a scriptless test case adaptor by standardizing a Test Case construction method that was built
Automation-ready & supported a test automation framework leading to a  increase in reusability with
reductions in TCO approaching 25%.
● Optimized scripting, modularity, & maintenance which resulted in an 1 decrease in workflow friction.
● Increased the company's ability to take and complete projects without increasing manpower  by
reducing QA testing turnaround time by 30%.
Growthsi, New York, NY Jan 2015 - May 2018
QA Manual Tester
● Restructured utilities & improved the process documentation leading to a  reduction in client support
tickets & an  increase in uptime.
● Achieved department-wide improvement metrics based on QA scorecard through the 46% & 22% workload
reduction of the customer support & IT departments respectively.
● Standardized Test Plan, Test Scripts/Test Cases, Daily Status Reports, etc., documents leading to a 20%
increase in productivity.
● Established monthly sprint backlog items as well as performed agile meetings while updating the activities in
Microsoft TFS in an optimized manner which resulted in saving 10 hours of monthly lost time.
RW Capital, San Diego, CA May 2008 - Dec 2014
QA Manual Tester (Nov 2011 - Dec 2014)
● Optimized the build process by increasing the system's quality level and reducing 45 of defects found.
● Established proper team communication that identified, triaged, reproduced, & fixed found issues using JIRA
increasing the overall workflow by 25%.
Junior QA Manual Tester (May 2010 - Oct 2011)
● Wrote & optimized test scripts in towels which led to a  reduction in the overall testing hours.
● Created traceability matrix to fill in the gap between requirements and tests covered contributing to the 10%
increase in test case count.
EDUCATION
Resume Worded University, San Francisco, CA May 2010
BSc. Computer Science
SKILLS
● Test Automation
Frameworks
● Java
● Javascript

● Microsoft TFS
● CharlesProxy
● SQL/NoSQL
● Selenium/Webdriver

● TestNG
● JIRA
● Jenkins
● Agile

● Source Versioning
● JUnit
● Scrum"""

job_desc="""AI/ML Engineer

Location: San Francisco, CA, USA

Company: Innovative Tech Solutions

About Us:
Innovative Tech Solutions is a leading technology company specializing in cutting-edge AI and machine learning solutions. Our mission is to transform industries and improve lives through innovative AI applications. We are looking for a talented and passionate AI/ML Engineer to join our dynamic team.

Job Description:

Responsibilities:

Design, develop, and deploy machine learning models and algorithms to solve complex problems.
Collaborate with cross-functional teams to identify and implement AI solutions in various projects.
Conduct research to stay current with the latest AI/ML advancements and integrate relevant findings into projects.
Optimize machine learning models for performance, scalability, and accuracy.
Develop and maintain scalable data pipelines for training and deploying models.
Analyze large datasets to extract meaningful insights and drive decision-making.
Monitor and evaluate the performance of deployed models, making improvements as necessary.
Participate in code reviews, ensuring code quality and best practices.
Requirements:

Bachelor’s or Master’s degree in Computer Science, Electrical Engineering, or a related field. A PhD is a plus.
Proven experience as an AI/ML Engineer or in a similar role.
Strong programming skills in Python and experience with ML frameworks such as TensorFlow, PyTorch, or scikit-learn.
Solid understanding of machine learning algorithms, including supervised and unsupervised learning techniques.
Experience with data preprocessing, feature engineering, and model evaluation.
Familiarity with cloud platforms such as AWS, Google Cloud, or Azure.
Strong analytical and problem-solving skills.
Excellent communication and teamwork abilities.
Experience with natural language processing (NLP) or computer vision is a plus.
Preferred Qualifications:

Experience in deploying machine learning models in production environments.
Knowledge of big data technologies such as Hadoop, Spark, or Kafka.
Understanding of software development best practices, including version control and CI/CD pipelines.
Published research papers or contributions to open-source projects.
What We Offer:

Competitive salary and benefits package.
Opportunity to work on cutting-edge AI projects with a talented and passionate team.
Professional development opportunities and support for continuous learning.
Flexible work hours and remote work options.
A collaborative and inclusive work environment.
How to Apply:
Interested candidates are invited to submit their resume and a cover letter detailing their relevant experience and motivation for applying to careers@innovativetechsolutions.com.

Innovative Tech Solutions is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.

"""

def extract_email_phone(text):
    email_regex = r'[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}'
    phone_regex = r'\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3}\s\d{3}\s\d{4}|\d{10}|\d{5}\s\d{5}|\+\d{2}\s\d{10}|\+\d{2}\s\d{5}\s\d{5}'

    emails = re.findall(email_regex, text)
    phones = re.findall(phone_regex, text)
    urls= re.findall(r'\b((?:https?:\/\/|www\.)(?:[-a-zA-Z0-9@:%._\+~#=]{1,256}\.)+[a-zA-Z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*))', text)
    
    processed_phones = []
    for phone in phones:
        if len(phone) > 10:
            phone = phone[-10:]  # Keep the last 10 digits
        processed_phones.append(phone)

    linkedin_regex = r'^https?://(?:www\.)?linkedin\.com/[^\s]+'
    linkedin_urls = []

    for url in urls:
        if re.match(linkedin_regex, url):
            linkedin_urls.append(url)

    return emails, processed_phones, urls, linkedin_urls

def extract_skills_from_resume(text, skills_list):
    skills = []

    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills

def extract_education_from_resume(text):
    education = []

    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education

def extract_college_name(text):
    lines = text.split('\n')
    college_pattern = r"(?i).*college.*"
    for line in lines:
        if re.match(college_pattern, line):
            return line.strip()
    
    return None

# emails, phones,urls,linkedIn_url = extract_email_phone(text)
# print(emails)  
# print(phones)
# print(urls)
# print(linkedIn_url)

# edu_details=extract_education_from_resume(text)
# print(edu_details) # get education details

# college_name=extract_college_name(text)
# print(college_name) # get college name

# skills_list=['Java', 'Python', 'C++', 'Kotlin', 'JavaScript','machine learning', 'Tensorflow', 'Pytorch', 'OpenCV','Artificial Intelligence (AI)'
# 'Communication','Computer Science','Data Science','Deep Learning''Web Development','Code Review','Natural Language Processing''Problem Solving',
# 'MySQL','Git','AWS','Docker','Scrum','Jira','Github','Jenkins','Agile','Content Management System (CMS)','Content Management System (CMS)']


# skills_list = [
#     "Machine Learning",  
#     "TensorFlow",
#     "PyTorch",
#     "scikit-learn",
#     "Aritificial Intelligence",
#     "Feature Engineering",
#     "Model Evaluation",
#     "Data Analysis",
#     "Cloud Platforms (AWS, Google Cloud, Azure)", 
#     "Natural Language Processing (NLP)",
#     "Computer Vision",
#     "Deep Learning",
#     "Data Science",
#     "Big Data Technologies (Hadoop, Spark, Kafka)",
#     "Version Control (Git)"
# ]

# skills=extract_skills_from_resume(text,skills_list)
# print(skills)


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def preprocess(text):
    text = text.lower()
    word_tokens = word_tokenize(text)

    # Remove punctuations
    word_tokens = [word for word in word_tokens if word.isalnum()]

    # Remove stopwords and common words
    stop_words = set(stopwords.words('english'))
    # Add more common words to remove if needed
    common_words = set(['from', 'what', 'and'])
    word_tokens = [word for word in word_tokens if not word in stop_words and not word in common_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in word_tokens]
    return ' '.join(lemmatized_tokens)

job_desc_processed = preprocess(job_desc)
job_desc_skills = set(job_desc_processed.split())
print(job_desc_skills)
