//1912. 연속합

/*  
연속합은 결국 1번쨰 원소에서 끝나는 연속합 ~ 마지막 원소에서 끝내는 연속합으로 
분해될 수 있다. 

K번째 원소에서 끝나는 연속합이 최대이려면 
K-1번째 원소에서 끝나는 연속합 +  K번째 원소(상수)
이므로 K-1이 최대여야한다.

D[1] = max(0, scores[1])

D[i] = max(D[i-1],0) + scores[i]
- i번째에서 끝나는 연속합 중 가장 큰 연속합.
단 반드시 i번째 원소를 포함한다. 


여기서 고려해볼 것은 state를 어떻게 분기하느냐인데, 

0이 선택되면 D[i]부터 새롭게 연속을 시작한단 의미이고
D[i-1]이 선택되면 D[i]가 이전 연속을 계속 물려받는단 의미이다.
즉 어느 형태로든 연속성은 보장되므로, 연속합이다!

*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int D[100005];
	int tables[100005];
	int num;
	cin >>num;	
	D[0] = 0;
	
	for (int i= 1; i<=num; i++){
		cin >> tables[i];
		D[i] = max(D[i-1],0) + tables[i];
	}
	
	long long result = -1000000000000;
	
	for (int i=1; i<=num;i++){
		if (D[i]>=result){result = D[i];}
	}
	
	cout << result<<"\n";
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}