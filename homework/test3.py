def grade(students):
    for name, score in students.items():
        if score % 5 != 0 and (5 - score % 5) <= 3:
            new_score = score + (5 - score % 5)
            if new_score >= 40:
                students[name] = new_score
    print("Updated Grades:")
    for name, score in students.items():
        print(f"{name}: {score}")

def main():
    students = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}
    grade(students)

if __name__ == "__main__":
    main()