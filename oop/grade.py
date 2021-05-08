


class Grade:
    def __init__(self, name):
        self.name = name
        self.marks = [] # list 로 초기화

    def addMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def main():
        student = Grade(input("학생이름 입력"))
        for subject in ['국어','영어','수학']:
            student.addMarks(int(input(subject+"점수 입력")))
        avg = student.avg()
        print(f'{student.name}의 과목 평균은 {int(avg)}이다.')
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"




if __name__ == '__main__':
    Grade.main()