import sys

totalScore = 0.0
totalCredit = 0.0

for _ in range(20):
    subject, score, grade = sys.stdin.readline().split()
    if grade != "P":
        if grade == "A+":
            totalScore += float(score) * 4.5
            totalCredit += float(score)
        elif grade == "A0":
            totalScore += float(score) * 4.0
            totalCredit += float(score)
        elif grade == "B+":
            totalScore += float(score) * 3.5
            totalCredit += float(score)
        elif grade == "B0":
            totalScore += float(score) * 3.0
            totalCredit += float(score)
        elif grade == "C+":
            totalScore += float(score) * 2.5
            totalCredit += float(score)
        elif grade == "C0":
            totalScore += float(score) * 2.0
            totalCredit += float(score)
        elif grade == "D+":
            totalScore += float(score) * 1.5
            totalCredit += float(score)
        elif grade == "D0":
            totalScore += float(score) * 1.0
            totalCredit += float(score)
        elif grade == "F":
            totalScore += float(score) * 0.0
            totalCredit += float(score)

if totalCredit != 0.0:
    totalScore = totalScore / totalCredit
else:
    totalScore = 0.0

print("%0.6f" % totalScore)

# 제미나이 제안 소스

import sys

# 등급별 과목 평점을 딕셔너리로 미리 정의
grade_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_score = 0.0
total_credit = 0.0

for _ in range(20):
    subject, credit, grade = sys.stdin.readline().split()

    # P 등급은 계산에서 제외
    if grade == "P":
        continue

    credit = float(credit)

    # 딕셔너리에서 평점을 찾아 계산
    total_score += credit * grade_map[grade]
    total_credit += credit

# 총 학점이 0인 경우 0.0 출력, 아니면 GPA 계산
if total_credit == 0:
    print("0.000000")
else:
    gpa = total_score / total_credit
    print(f"{gpa:.6f}")
