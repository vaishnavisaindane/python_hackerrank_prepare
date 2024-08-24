def marks_avg(student_marks,query_name):
    for key,values in student_marks.items():
        if key == query_name:
            averagemarks=sum(values)/len(values)
    print(f"{averagemarks:.2f}")
    return
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks_avg(student_marks,query_name)
