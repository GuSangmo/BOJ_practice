//11727. 2xn 타일링 2

/*  
D[N][Good]= N개의 타일을 가로 직사각형으로 채우는 경우의 수
D[N][Bad] = N개의 타일의 마지막을 세로 직사각형으로 채우는 경우의 수 


D[N][Good] = D[N-2] * 2
D[N][Bad]  = D[N-1]

Good과 Bad는 겹치지 않을 것이므로

D[N] = 2 * D[N-2] + D[N-1]이 성립할 것이라는 가설을 세우자.



*/


#include <bits/stdc++.h>
using namespace std;


int d[1005];
void solution(){
	int num;

	cin >>num;	
	
	
	//입력

	d[1] = 1;
	d[2] = 3;
	for (int i=3; i<=1005; i++){
		d[i] = (d[i-1] + 2 * d[i-2]) % 10007;
		}
	cout << d[num]<<"\n";
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}