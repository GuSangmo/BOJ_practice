//10844. 쉬운 계단 수

/*  
맨 마지막자리수가 0인지 9인지만 따로 분류해주면 된다.

D[N][i] = n자리 계단 수 중 맨 끝자리수가 i인 것
(D[N][0] = D[N-1][1], D[N][9] = D[N-1][8]
나머진 D[n][i] = D[n-1][i+1] + D[n-1][i-1])


* BIG_NUM 은 그냥 복사해서 끌고 오자.
* modular 연산은 늘 섬세하게.

*/


#include <bits/stdc++.h>
using namespace std;


int N;
long long D[105][12];
int big_num = 1000000000;
	
	
void solution(){	
	cin >> N ;
	fill(D[1],D[1]+10,1);
	D[1][0] = 0;
	for (int i=2; i<=100; i++){
		for (int j= 0; j<=9; j++){
			if (j==0){
				D[i][j] = (D[i-1][j+1])%big_num;
			}
			else if (j==9){
				D[i][j] = D[i-1][j-1]%big_num;
			}
			else {
				D[i][j] = (D[i-1][j-1] + D[i-1][j+1])%big_num;
			}
		}
	}
	long long result = 0;	
	for (int j= 0;j<=9;j++){
		result = (result+D[N][j]);
		cout << D[N][j] <<"\n";
	}
	result = result%big_num;
	cout << result <<"\n";
	
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}