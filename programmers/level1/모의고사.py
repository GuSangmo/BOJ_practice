"""
Programmers lv1 - 모의고사
"""

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    length = len(answers)
    student1 = pattern1 * (length//5) + pattern1[:length%5]
    student2 = pattern2 * (length//8) + pattern2[:length%8]
    student3 = pattern3 * (length//10) + pattern3[:length%10]

    result = []
    for s in [student1,student2,student3]:
        result.append(sum(i==j for i,j in zip(s, answers)))
    answer = [i for i,j in enumerate(result,1) if j == max(result)]
    answer.sort()
    return answer