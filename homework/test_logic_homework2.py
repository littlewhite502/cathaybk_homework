def grade(students):
    for name, score in students.items():
        if score % 5 != 0 and (5 - score % 5) <= 3:
            new_score = score + (5 - score % 5)
            if new_score < 40:
                continue
            else:
                students[name] = new_score
    return students

def main():
    students = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}
    students_new_score = grade(students)
    
    for name, score in students_new_score.items():
        print("{}: {}".format(name, score))

if __name__ == "__main__":
    main()