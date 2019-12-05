import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from pylab import rcParams


def print_round_plot(values: list, title: str, ticks: list):
    fig1, ax1 = plot.subplots()
    colors = ['#dbdbdb', '#ededed', 'white']

    ax1.pie(values, labels=ticks, autopct='%1.1f%%', colors=colors,
            shadow=True, startangle=90)

    ax1.axis('equal')
    plot.title(title)
    plot.tight_layout()
    plot.show()


def print_plot(values: list, label_x: str, label_y: str, title: str, ticks: list):
    column_width = 0.8
    border_width = 0.3
    height = np.arange(len(values))
    rcParams['figure.figsize'] = 10, 5

    plot.title(title)
    plot.xlabel(label_x)
    plot.ylabel(label_y)

    max = plot.bar(height,
                   values['max'],
                   align="edge",
                   width=column_width,
                   color='white',
                   edgecolor='black',
                   linewidth=border_width)

    mean = plot.bar(height,
                    values['mean'],
                    align="edge",
                    width=column_width,
                    color='#ededed',
                    edgecolor='black',
                    linewidth=border_width)

    min = plot.bar(height,
                   values['min'],
                   align="edge",
                   width=column_width,
                   color='#dbdbdb',
                   edgecolor='black',
                   linewidth=border_width)

    plot.legend((max[0], mean[0], min[0]), ('Max', 'Avg', 'Min'))

    plot.xticks([r + column_width / 2 for r in range(len(values))], ticks)

    plot.show()


dataset = pd.read_csv("dataset.csv")

student_grades = dataset.groupby("stid")['stmark'].agg(['count', 'max', 'mean', 'min']).reset_index()
subject_marks = dataset.groupby("discid")['stmark'].agg(['count', 'max', 'mean', 'min']).reset_index()
semester_marks = dataset.groupby("semnum")['stmark'].agg(['count', 'mean']).reset_index()

print_plot(student_grades, "Student ID", "Mark", "Student to grade ratio", student_grades['stid'])
print_plot(subject_marks, "Subject ID", "Mark", "Subject to grade ratio", subject_marks['discid'])
print_round_plot(semester_marks['count'], "Subject to semester ratio", semester_marks['semnum'])
