import pandas
import json

student = pandas.read_csv("students.csv")
student_dict = student.to_dict()
stu_num = len(student)

courses = pandas.read_csv("courses.csv")
course_dict = courses.to_dict()
cour_num = len(courses)

tests = pandas.read_csv("tests.csv")
test_dict = tests.to_dict()
tes_num = len(tests)

marks = pandas.read_csv("marks.csv")
marks_dict = marks.to_dict()
mark_num = len(marks)

i = 0
final_list_student = []
output_dict = {}


def weight_check():
    for j in range(cour_num):
        weight = 0
        for test in range(tes_num):
            if course_dict["id"][j] == test_dict["course_id"][test]:
                weight += test_dict["weight"][test]
        if weight == 100:
            return True
        else:
            return False


# adding students in main dictionary
while i < stu_num:
    j = 0
    final_dict_student = {}
    final_list_course = []
    total_percent = 0
    final_dict_student["id"] = student_dict["id"][i]
    final_dict_student["name"] = student_dict["name"][i]
    # adding courses for each student
    while j < cour_num:
        final_dict_course = {}
        final_percent = 0
        percent_per_test = 0
        try:
            final_dict_course["id"] = course_dict["id"][j]
            final_dict_course["name"] = course_dict["name"][j]
            final_dict_course["teacher"] = course_dict["teacher"][j]
            # checking per course percentage for each student and each
            for mark in range(mark_num):
                # matching each student id with student id in marks so student gets own marks
                if student_dict["id"][i] == marks_dict["student_id"][mark]:
                    # going through all tests so weight can be taken for each test
                    for tes in range(tes_num):
                        # matching each course id with course id in tests so weight can be managed
                        if course_dict["id"][j] == test_dict["course_id"][tes]:
                            if test_dict["id"][tes] == marks_dict["test_id"][mark]:
                                test_percent = (marks_dict["mark"][mark] * test_dict["weight"][tes]) / 100
                                final_percent += test_percent
            final_dict_course["courseAverage"] = round(final_percent, 2)
            total_percent += final_percent
            round(total_percent, 2)
        except KeyError:
            final_percent = 0
        if not weight_check():
            final_dict_course = {"error": "Invalid course weights"}
        final_list_course.append(final_dict_course)
        j += 1

    totalAvg = (total_percent / cour_num)
    final_dict_student["totalAverage"] = round(totalAvg, 2)
    final_dict_student["courses"] = final_list_course
    final_list_student.append(final_dict_student)
    i += 1

output_dict["students"] = final_list_student

with open("output.json", "w") as file:
    json.dump(output_dict, file, indent=4)
