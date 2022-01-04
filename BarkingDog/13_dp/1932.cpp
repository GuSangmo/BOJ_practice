//1932. 정수 삼각형

/*  
psum[i][j] = i번째 열의 j번쨰 원소를 택할떄의 최댓값

*/


#include <bits/stdc++.h>
using namespace std;


int tri[505][505];
int psum[505][505];
void solution(){
	int num;

	cin >>num;	
	
	//입력
	for (int i=1; i<=num; i++){
		for (int j = 1;j<=i;j++){
			cin >> tri[i][j];
		}
	}
	
	psum[1][1] = tri[1][1];
	for (int i=2; i<=num;i++){
		for (int j=1; j<=i ; j++){			
			psum[i][j] = tri[i][j] + max(psum[i-1][j],psum[i-1][j-1]) ;
		}
	}

	int max = 0; 
	
	for (int i=1; i<=num;i++){
		if (psum[num][i]>=max){
			max = psum[num][i];
		}
	}
	
	cout << max;
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}