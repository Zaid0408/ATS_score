from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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

resume1_processed=preprocess(resume1)
resume2_processed=preprocess(resume2)
resume3_processed=preprocess(resume3)
resume4_processed=preprocess(resume4)
resumes=[resume1_processed,resume2_processed,resume3_processed,resume4_processed]

documents = resumes + [job_desc_processed]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert the TF-IDF matrix to an array
tfidf_array = tfidf_matrix.toarray()

# Separate the resume vectors and the job description vector
resume_vectors = tfidf_array[:-1]  # All except the last
job_desc_vector = tfidf_array[-1].reshape(1, -1)  # The last vector, reshaped

# Calculate cosine similarities
similarities = cosine_similarity(resume_vectors, job_desc_vector)

# Calculate percentage matches
percentage_matches = [round(similarity[0] * 100, 2) for similarity in similarities]

# Print the results
for i, percentage_match in enumerate(percentage_matches):
    print(f"Resume {i + 1}: {percentage_match}% match with job description")