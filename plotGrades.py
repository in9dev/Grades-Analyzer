import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("grades.csv")
print(df.head())


x = np.arange(len(df["Subject"]))  # position for each subject
width = 0.25

plt.bar(x - width, df["Summative (avg)"], width=width, label="Summative")
plt.bar(x, df["Formative (avg)"], width=width, label="Formative")
plt.bar(x + width, df["Weighted_Avg"], width=width, label="Weighted Avg")

plt.xticks(x, df["Subject"], rotation=45)
plt.xlabel("Subjects")
plt.ylabel("Grades (%)")
plt.title("Grades Comparison by Subject")
plt.legend()
plt.tight_layout()
plt.savefig("grade_chart.png")
plt.show()
