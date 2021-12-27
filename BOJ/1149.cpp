//1149. RGB 거리

/*  

colors[i][j] = i번째 집을 j번째 색으로 칠하는 경우의 최소 비용 
colors[i][j] = min(colors[i-1][!=j]) + cost[i][j]
배열 크기 넉넉하게 선언하자.

*/


#include <bits/stdc++.h>
using namespace std;


int solution(){
	int cost[1005][3];
	int colors[1005][3];
	int num; 
	cin >>num;
	
	// Data 입력받기
	for (int i=1 ; i<=num;i++){
		for (int j = 0 ; j<3; j++){
			cin >> cost[i][j];
		}
	}
	
	// 처음은 그대로
	colors[1][0] = cost[1][0];
	colors[1][1] = cost[1][1];
	colors[1][2] = cost[1][2];
	
	
	for (int i = 1 ; i<=num; i++){
		for (int j = 0; j<3; j++){
			colors[i][j] = min(colors[i-1][(j+1)%3], colors[i-1][(j+2)%3]) + cost[i][j];
		}
			
	
	}
	
	int result = min(min(colors[num][0],colors[num][1]),colors[num][2]);
	return result;

	}
	
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout << solution();
}