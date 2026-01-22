📌 Project Overview

The Student Result Management System (SRMS) is a simple software application developed to help manage and display students’ academic results.
The system allows a user (lecturer) to add student names and their scores, store them, and display the results.

This project was developed following the Software Development Life Cycle (SDLC) methodology.

⸻

🧩 Problem Statement

Manual recording and processing of student results can lead to:
	•	Errors in calculation
	•	Data loss
	•	Time consumption

The SRMS provides a simple automated solution to store and display student results accurately.

⸻

🎯 Project Objectives
	•	To automate student result recording
	•	To reduce errors associated with manual result processing
	•	To demonstrate practical application of SDLC concepts
	•	To implement a simple Python-based system

⸻

🔁 Software Development Life Cycle (SDLC)

1️⃣ Requirement Analysis

At this stage, the system requirements were identified.

Functional Requirements:
	•	The system shall accept student names
	•	The system shall accept student scores
	•	The system shall store student results
	•	The system shall display stored results

Non-Functional Requirements:
	•	The system shall be easy to use
	•	The system shall run on any system with Python installed

⸻

2️⃣ System Design

The system was designed using a simple structure.

Design Components:
	•	Input: Student name and score
	•	Processing: Store data using a dictionary
	•	Output: Display student name and score

Data Structure Used:
	•	Python Dictionary
	•	Key: Student Name
	•	Value: Student Score

⸻

3️⃣ Implementation

The system was implemented using Python.

Main Functions Implemented:
	•	add_student_result(name, score)
	•	display_results()

Source Code File:
	•	srms.py

⸻

4️⃣ Testing

The system was tested using sample data to ensure correctness.

Test Cases:
	•	Adding a student result → Successful
	•	Displaying stored results → Successful

No errors were detected during testing.

⸻

5️⃣ Deployment

The system was deployed by:
	•	Uploading the source code to a GitHub repository
	•	Making the repository public for access and submission

⸻

6️⃣ Maintenance

Future improvements may include:
	•	Adding grade calculation (A, B, C, etc.)
	•	Saving results to a file or database
	•	Adding a user authentication system
	•	Creating a graphical user interface (GUI)

⸻

🛠️ How to Run the Project
	1.	Ensure Python is installed
	2.	Download or clone the repository
	3.	Run the program using:

python srms.py


⸻

📂 Project Structure

student-result-management-system/
│
├── srms.py
└── README.md

Conclusion

The Student Result Management System demonstrates the practical application of the Software Development Life Cycle (SDLC) from requirement analysis to maintenance.
This project fulfills the requirements of the SEN 201 assignment and serves as a foundation for more advanced systems.
