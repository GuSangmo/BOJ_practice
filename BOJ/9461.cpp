//9461. 파도반 수열

/*  

P[N] = P[N-1] + P[N-5]

범위 조심. %가 없으면 어지간해선 long long이라고 여기자.

*/


#include <bits/stdc++.h>
using namespace std;


long long P[105];
int T;
void solution(){	
	cin >> T;
	P[1] = 1; 
	P[2] = 1;
	P[3] = 1;
	P[4] = 2;
	P[5] = 2;
	for (int i=6;i<=101;i++){
		P[i] = P[i-1] + P[i-5];
	}
	for (int i=1; i<=T; i++){
		int N;
		cin >> N;
		cout << P[N]<<"\n";
		
	}	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}