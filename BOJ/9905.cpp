//9095. 1,2,3, 더하기

/*
[1] 먼저, +1, +2, +3을 더하는 경우는 서로 독립적임. (순서를 고려하므로)

[2] 또한 저 3가지 경우로 모든 경우를 표현할 수 있음.(그 외엔 없음.)

따라서 dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]이 가능하다.

*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int dist[20];
	int T; 
	
	cin >> T;
	
	dist[1] = 1 ; // 1
	dist[2] = 2 ; // 1+1, 2
	dist[3] = 4 ; // 1+1+1, 1+2, 2+1, 3
	
	//테이블 채우기 
	
	for (int i = 4; i<12; i++){
		dist[i] = dist[i-1] + dist[i-2] + dist[i-3] ;
	}
	

	for (int i=0;i<T;i++){
		int n;
		cin >> n;
		cout << dist[n]<<"\n";
	}
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	solution();
}