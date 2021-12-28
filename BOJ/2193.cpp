//2193. 이친수

/*  
D[N][0] = N자리 이진수 중 끝자리 수가 0
D[N][1] = N자리 이진수 중 끝자리 수가 1

D[N][0] = D[N-1][0] + D[N-1][1] //앞자리가 뭐든 상관없음
D[N][1] = D[N-1][0] //앞자리 수가 0일수밖에 없지.


*/


#include <bits/stdc++.h>
using namespace std;


long long d[100][3];
void solution(){
	int num;

	cin >>num;	
	
	
	//입력

	d[1][0] = 0;
	d[1][1] = 1;
	for (int i=2; i<=91; i++){
		d[i][0] = d[i-1][0] + d[i-1][1];
		d[i][1] = d[i-1][0];
		}
	cout << d[num][0]+d[num][1]<<"\n";
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}