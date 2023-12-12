CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(255) NOT NULL,
	birth_date DATE NOT NULL,
	contact_info VARCHAR(255)
);


CREATE TABLE teachers (
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(255) NOT NULL,
	birth_date DATE NOT NULL,
	contact_info VARCHAR(255)
);


CREATE TABLE subjects (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	description TEXT
);


CREATE TABLE courses (
	id SERIAL PRIMARY KEY,
	subject_id INT NOT NULL,
	teacher_id INT NOT NULL,
	semester INT NOT NULL,
	FOREIGN KEY (subject_id) REFERENCES subjects (id),
	FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);


CREATE TABLE grades (
	id SERIAL PRIMARY KEY,
	student_id INT NOT NULL,
	course_id INT NOT NULL,
	grade INT CHECK (grade >= 1 AND grade <= 5),
	FOREIGN KEY (student_id) REFERENCES students (id),
	FOREIGN KEY (course_id) REFERENCES courses (id)
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

ALTER TABLE students
ADD COLUMN group_id INT,
ADD FOREIGN KEY (group_id) REFERENCES groups (id);
