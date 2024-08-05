from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

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
def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

resume1=read_txt_file('resume1.txt')
resume2=read_txt_file('resume2.txt')
resume3=read_txt_file('resume3.txt')
resume4=read_txt_file('resume4.txt')
resumes=[resume1,resume2,resume3,resume4]

# Combine the skill list into a single string for TF-IDF vectorization
# skill_string = " ".join(skills_list)

#  Assume documents include multiple resumes and one job description
documents = resumes+ [job_desc]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert the TF-IDF matrix to an array
tfidf_array = tfidf_matrix.toarray()

# Separate the resume vectors and the job description vector
resume_vectors = tfidf_array[:-1]  # All except the last
job_desc_vector = tfidf_array[-1]  # The last vector

# Create and train the KNN model on resume vectors
knn_model = NearestNeighbors(n_neighbors=4, metric='cosine')
knn_model.fit(resume_vectors)

# Find the k most similar resumes to the job description vector
distances, indices = knn_model.kneighbors(job_desc_vector.reshape(1, -1))
ats_scores = (1 - distances) * 100

# Print the results
print("Distances to the nearest resumes:", distances)
print("Indices of the nearest resumes:", indices)
print("ATS Scores:", ats_scores)