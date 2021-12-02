#17478. 재귀함수가 뭔가요?
"""
반복되는 부분을 출력하는 함수를 recursive하게 짜자!
"""


A = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
B = '"재귀함수가 뭔가요?"'
C = ['"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']

E = '"재귀함수는 자기 자신을 호출하는 함수라네"'
D = '라고 답변하였지.'




def repeat(N):
    if N == 1 :
        result = []
        result.append("____" + B)
        result.append("____" + E)
        result.append("____" + D)
        return result
    else:
        prev = repeat(N-1)
        new = ["____"+B] +["____"+sen for sen in C] + ["____"+ prev_sen for prev_sen in prev] + ["____"+D]
        return new

def solution(N):
    print(A)
    print(B)
    for sen in C:
        print(sen)
    for sen in repeat(N):
        print(sen)
    print(D)
    
N = int(input().rstrip())
solution(N)
    