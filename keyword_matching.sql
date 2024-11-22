create database master;
--CREATE DATABASE

\c master;
--connected to database "master"

create table dataOfResumes( sl_no serial primary key, resume_text varchar);
-- CREATE TABLE dataOfResumes

insert into dataOfResumes (resume_text) values ('Experienced in developing web applications using Django and FastAPI. Proficient in building RESTful APIs, and handling middleware and ORM with Pydantic for data validation.'),('Skilled in mobile app development using Flutter, with expertise in microservices architecture. Experienced in integrating Kafka and Redis for efficient data processing and messaging.'),('Hands-on experience with Django and FastAPI for web development, implementing microservices and leveraging Kafka and Redis for real-time data streaming and caching.'),('Skilled in designing and deploying microservices, with expertise in middleware integration, building RESTful APIs, and utilizing Kafka and Redis for efficient data handling.'),('Proficient in web application development using Django and FastAPI, with strong experience in implementing ORM and data validation using Pydantic');
-- INSERT  5 values into the table dataOfResumes

-- Insert the same values over 50 times in the table
do $$
 begin
   for i in 1..49 loop
      insert into dataOfResumes (resume_text) values ('Experienced in developing web applications using Django and FastAPI. Proficient in building RESTful APIs, and handling middleware and ORM with Pydantic for data validation.'),('Skilled in mobile app development using Flutter, with expertise in microservices architecture. Experienced in integrating Kafka and Redis for efficient data processing and messaging.'),('Hands-on experience with Django and FastAPI for web development, implementing microservices and leveraging Kafka and Redis for real-time data streaming and caching.'),('Skilled in designing and deploying microservices, with expertise in middleware integration, building RESTful APIs, and utilizing Kafka and Redis for efficient data handling.'),('Proficient in web application development using Django and FastAPI, with strong experience in implementing ORM and data validation using Pydantic');
  end loop;
 end $$;


-- Main Query to do keyword matching with skills and resume data, will work with all columns of database
SELECT sl_no, resume_text
FROM dataOfResumes
WHERE resume_text ILIKE '%Django%'
  AND resume_text ILIKE '%FastAPI%'
  AND (resume_text ILIKE '%Flutter%' OR resume_text ILIKE '%ORM%' OR resume_text ILIKE '%Microservices%' OR resume_text ILIKE '%RESTful APIs')
  AND (resume_text ILIKE '%Kafka%' OR resume_text ILIKE '%Redis%');
-- AND is to include all of the 4 words, OR is to include iny one of the words mentioned in single quotes


-- To check for the presence of all the keywords in data
SELECT sl_no, resume_text FROM dataOfResumes
WHERE resume_text LIKE '%Django%'
   AND resume_text LIKE '%FastAPI%'
   AND resume_text LIKE '%Flutter%'
   AND resume_text LIKE '%ORM%'
   AND resume_text LIKE '%Pydantic%'
   AND resume_text LIKE '%Microservices%'
   AND resume_text LIKE '%Middleware%'
   AND resume_text LIKE '%RESTful APIs%'
   AND resume_text LIKE '%Kafka%'
   AND resume_text LIKE '%Redis%';

