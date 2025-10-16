# Grades-Analyzer
A smart Python tool to analyze and visualize my school grades with real-time weighted averages.

### Features

* ✅ Enter multiple summative and formative grades per subject
* ✅ Automatically calculate weighted averages (70% Summative, 30% Formative)
* ✅ Supports partial subjects (only formatives or only summatives)
* ✅ Automatically saves and appends grades to grades.csv
* ✅ Generates bar chart visualizations using Matplotlib
* ✅ Clean, modular, beginner-friendly Python code

### File structure

```
grade-analyzer/
│
├── main.py             # main program to enter and calculate grades
├── plotGrades.py       # plotting script for visualization
├── grades.csv          # stores all subjects and grades
├── requirements.txt    # pip project requirements
└── README.md           # project documentation
```

### What I learned

* Handling data persistence with CSV files
* Using Pandas for data manipulation
* Using Matplotlib and NumPy for data visualization
* Writing modular and readable Python scripts1
* Building tools that help real students track progress

### Grading system
- Summatives (70%) → Major assignments, exams, or projects
- Formatives (30%) → Quizzes, homework, classwork
- Final Grade = (Summative Avg × 0.7) + (Formative Avg × 0.3)

##### Example
| Subject | Summative Avg | Formative Avg | Final |
|---------|---------------|---------------|-------|
| Physics | 97.5          | 98.75         | 97.9  |
| English | 0             | 81            | 81    |


### Output

##### grades.csv
```csv
Subject,Summative (avg),Formative (avg),Weighted_Avg
Islamic,100.0,100.0,100.0
English,0.0,81.0,81.0
Psychology,96.67,90.0,94.67
Arabic,93.34,100.0,95.33
Stats & Prob,100.0,76.67,93.0
Physics,97.5,98.75,97.9
Environmental Studies,93.33,97.92,94.71
```

##### Plot
![Plot][grade_chart.png]
