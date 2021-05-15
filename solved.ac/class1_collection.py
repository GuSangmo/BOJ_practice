"""
Solved.ac Project:: Class 1 Code
"""
###### Posted some bookmarks and comments on velog



#1001. A+B
a,b=map(int,input().split())
print(a+b)

#1002. A-B
a,b=map(int,input().split())
print(a-b)

#1008. A/B
a,b=map(int,input().split())
print(a/b)


#1152. 단어의 개수
"""

string을 input으로 받아서 list로 쪼갠 후 list의 원소 개수를 세면 충분.
"""
import sys
string=list(sys.stdin.readline().split())
print(len(string))


#1157.단어 공부

"""
제일 많이 등장하는 최빈 단어를 세는 문제. 
나는 Counter를 썼는데,
인상깊은 풀이로는 statistics의 mode를 쓰는 방법도 있었다.
"""

from collections import Counter
string=input().lower()
my_dict=Counter(string)
maximum=max(my_dict.values())
max_indices=[i for i in my_dict.keys() if my_dict[i]==maximum]
if len(max_indices)>1:
    print("?")
else:
    print(my_dict.most_common(1)[0][0].upper())
    
#1330.두 수 비교하기

A,B=map(int,input().split())
result="=="
if A>B:
    result=">"
if A<B:
    result="<"
print(result)

#1546. 평균
import sys
N=int(sys.stdin.readline())
score=list(map(int,sys.stdin.readline().split() ) )
new_score=[]
M=max(score)
for ele in score:
    new_ele=ele/M * 100
    new_score.append(new_ele)
print(sum(new_score)/len(new_score))

#2438. 별 찍기-1
N=int(input())
for itr in range(1,N+1):
    print("*"* itr)
    
#2439. 별 찍기-2
N=int(input())
for itr in range(1,N+1):
    print(" "*(N-itr)+"*"* itr)

#2475. 검증수
num_list=list(map(int,input().split()))
new_list=[i**2 for i in num_list]
check_num=sum(new_list)%10
print(check_num)

#2557. Hello World
print("Hello World!")

#2562. 최댓값
import sys
num_list=[]
for _ in range(9):
    ele=int(sys.stdin.readline())
    num_list.append(ele)
print(max(num_list))
print((num_list.index(max(num_list)) +1))
    
#2577. 숫자의 개수
import sys
mul=1
for _ in range(3):
    multiply=int(sys.stdin.readline())
    mul*=multiply
num=[int(j) for j in list(str(mul))]
cnt_list=[num.count(j) for j in range(10)]
for cnt in cnt_list:
    print(cnt)
    
#2675. 문자열 반복  
T=int(input())
for _ in range(T):
    num, string=input().split()
    new_string=''
    num=int(num)
    for letter in string:
        new_string+=letter*num
    print(new_string)
    
    
#2739. 구구단
N=int(input())
for j in range(1,10):
    print("{} * {} = {}".format(N,j,N*j))
    
    
#2741. N 찍기
N=int(input())
for s in range(1,N+1): 
    print(s)
    
#2742. 기찍 N
"""
슬라이싱에서 step을 잘 이용하면 편하다.
"""

N=int(input())
for s in list(range(1,N+1))[::-1]: 
    print(s)

#2753. 윤년
import sys
year=int(sys.stdin.readline().rstrip())
yoon=False
if (year%4==0 and year%100!=0) or (year%400==0):
    yoon=True
print(int(yoon))
```

#2884. 알람 시계
import sys
H,M=map(int,sys.stdin.readline().split())

if M<45:
    M=M+15
    if H==0:
        H=23
    else:
        H-=1
else:
    M=M-45
print(H,M) 


#2908. 상수

"""
Number as string
"""
num1, num2= input().split()
num1=int(num1[::-1])
num2=int(num2[::-1])
print(max(num1,num2))


#2920. 음계
num_list=list(map(int,input().split()))

if num_list == sorted(num_list):
    print("ascending")
elif num_list==sorted(num_list)[::-1]:
    print('descending')
else:
    print("mixed")
    
    
#3052. 나머지
"""
Set은 중복된 원소들을 제거해준다.
"""
import sys
mod_list=[]
for _ in range(10):
    ele=int(sys.stdin.readline())
    mod_list.append(ele%42)
print(len(set(mod_list)))



#8958. OX퀴즈
import sys
N=int(sys.stdin.readline().rstrip())
for _ in range(N):
    string=sys.stdin.readline().rstrip()
    score, circle_count=0,0
    for letter in string:
        if letter=="O":
            circle_count+=1    
        else:
            circle_count=0
        score+=circle_count    
    print(score)        

#9498. 시험 성적
import sys
score=int(sys.stdin.readline().rstrip())
if score>=90:
    rank="A"
elif score>=80:
    rank="B"
elif score>=70:
    rank="C"
elif score>=60:
    rank="D"
else:
    rank="F"
print(rank)

#10171. 고양이
str1="\    /\\"
str2=" )  ( ')"
str3="(  /  ) "
str4=" \(__)| "
print(str1)
print(str2)
print(str3)
print(str4)

#10172. 개
str1="|\_/|"
str2="|q p|   /}"
str3='( 0 )"""\\'
str4='|"^"`    |'
str5="||_/=\\\\__|"

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

#10809. 알파벳 찾기
## 아스키 코드를 쓰거나 re를 써도 되겠으나 편의상 이렇게 하였다.

string=input()
for letter in "abcdefghijklmnopqrstuvwxyz":
    print(string.find(letter), end=' ')

#10818. 최소, 최대
import sys
N=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().rstrip().split()))
print( min(num_list), max(num_list))

#10869. 사칙연산
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10871. X보다 작은 수
import sys
N,X= map(int,sys.stdin.readline().split())
candidate=list(map(int,sys.stdin.readline().split()))
for ele in candidate:
    if ele<X:
        print(ele,end=' ')
        
#10950. A+B -3
T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    print(A+B)

# 10951. A+B-4
"""
Input이 끝날때에 대한 조건을 걸어주기.
"""
import sys
while True:
    use=sys.stdin.readline().rstrip()
    if use:
        A,B=map(int,use.split())
        print(A+B)
    else:
        break
    
    
#10952. A+B -5
import sys
nonzero=True
while nonzero:
    A,B=map(int,sys.stdin.readline().rstrip().split())
    if A==0 and B==0:
        nonzero=False
        break
    else:
        print(A+B)
        
#10998. A X B
a,b=map(int,input().split())
print(a*b)

#11654. 아스키 코드
s=input()
print(ord(s))


#11720 .숫자의 합
import sys
N=int(sys.stdin.readline())
string=sys.stdin.readline().rstrip()
num_list=[int(i) for i in string]
print(sum(num_list))
