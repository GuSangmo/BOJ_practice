//14501. 퇴사

/*  

D[i] - i일차 상담을 했을때의 최대 수익 

D[i] = P[i] + D[i+T[i]]
i+T[i]가 N보다 크면 0으로 놓아야함

조금 기다린 후에 상담을 받을 수 있는데, 그 경우를 고려하지 못했음.
*/


#include <bits/stdc++.h>
using namespace std;


int price[1010]; // 가격 저장
int times[1010]; //시간 저장
int D[1010];  //우리가 원하는 테이블
int N;
void solution(){	
	cin >> N ;
	for (int i=1; i<=N; i++){
		cin >> times[i] >> price[i];
		D[i] = 0;
	}
	D[N+1] = 0;
	for (int i=N; i>=1; i--){
		if (i+ times[i] > N+1){D[i] = D[i+1];}
		else{
			if (i+times[i] == N+1){ D[i] = max(price[i],D[i+1]);}
			D[i] = max(price[i] + D[i+times[i]], D[i+1]);
		}
	}
	
	for (int i=1; i<=N;i++){
		cout << D[i] <<"\n";
	}
	
	cout << *max_element(D+1, D+N+1);
	
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}