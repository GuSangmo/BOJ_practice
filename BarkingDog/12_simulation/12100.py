#12100. 2048(Easy)
"""
이 문제에서 따져봐야 할 것은 


LRUD의 이동을 구현하는 것이다.

N개의 mtx에 대해 각각의 줄을 다 봐야 하므로 O(N^2)이 기본으로 들 것.

그런데 총 5번 이동할 수 있으므로, case는 4**5 = 2**10


maximum size = 20 * 20 * 1024 = 400000 언저리라 가능할 것 같다!

memory 또한 1024 * 400 * 4byte = 1.6kb * 1024 = 1MB 언저리? 
"""

import sys
input = sys.stdin.readline
from itertools import product

"""
이 문제에서 tilt 함수를 구현하고자 한다.
tilt에서 중요한 기능은

- 이전 원소가 무엇인지 기억한 후 합친다. 
단 같은 원소가 3연속이면 안 합쳐지기에 그걸 감안한다 

- 0이면 그냥 무시한다


이제 하나하나 해보자


LRUD 어찌할지 고민해보자!

"""

array = [0,2,0,2,2,4,4,0,8,0,0,4,8]
#[4,2,8,8,4,8]



max_element = 0

def tilt(array):
    previous = None;   
    normal = True
    cnt = 0;           
    new_array = []
    for idx, ele in enumerate(array):    
        if ele == 0 : continue #0은 취급하지 않는다. 0은 어차피 padding용.
    
        if previous is None:  #첫번째 nonzero인 원소
            previous = ele
            new_array.append(ele)
            cnt+=1
            continue
        else:
            if ele == previous: #합쳐질때만 신경쓰면 되니깐
                if normal: 
                    new_array[cnt-1] *= 2
                else: 
                    new_array.append(ele)
                    cnt+=1
                normal = not normal
            else: 
                new_array.append(ele)
                cnt+=1
                normal = True
            previous = ele #다시 갱신!
    result = new_array + [0 for _ in  range(len(array)-cnt)]
    maximum = max(result)
    return result, maximum



def overwrite(original_matrix, option):
    #덮어씌워질수 있으니 계속해서 새로운걸 호출
    matrix = [[original_matrix[row][col] for col in range(N)] for row in range(N)]
    real_maximum = -1
    if option == "L":
        for row in range(N):
            matrix[row], maximum = tilt(matrix[row])
            real_maximum = max(maximum, real_maximum)
    elif option == "R":
        for row in range(N):
            need_process, maximum = tilt(matrix[row][::-1])
            
            matrix[row] = need_process[::-1]
            real_maximum = max(maximum, real_maximum)
    elif option == "U":
        for col in range(N):
            original_col = [matrix[i][col] for i in range(N)]
            need_process, maximum = tilt(original_col)
            real_maximum = max(maximum, real_maximum)
            for i in range(N):
                matrix[i][col] = need_process[i]
        
    elif option == "D":
        for col in range(N):        
            original_col = [matrix[N-1-i][col] for i in range(N)]
            need_process, maximum = tilt(original_col)
            real_maximum = max(maximum, real_maximum)
            
            new_column = need_process[::-1]
            for i in range(N):
                matrix[i][col] = new_column[i]
            
    return matrix, real_maximum


N = int(input())
mtx = [list(map(int,input().rstrip().split())) for _ in range(N)]


#Execution

for ordering in product("LRUD", repeat = 5):
    new_mtx = mtx
    
    for each_order in ordering:
        new_mtx, maximum = overwrite(new_mtx, each_order)
        max_element = max(maximum, max_element)
       
print(max_element)




#Right으로 기울이는 함수는 당연히 뒤집은걸 다시 기울이면 되지 

    
    
    
    
    








