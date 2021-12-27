//2579. 계단 오르기

/*  Table을 다음과 같의 정의한다고 하자.

** 2번쨰 점화식

dist[i] = i번쨰 계단을 오를 때 밟지 않을 계단의 최솟값
(이때 i번째 계단은 반드시 합에 포함시켜야 함.)

# i-1 번째 는 반드시 밟으니깐, i-2번째나 i-3번째중 하나를 안 밟음.
dist[i] = min(dist[i-2], dist[i-3]) + floors[i]

*/


#include <bits/stdc++.h>
using namespace std;


int solution(){
	int dist[305];
	int floors[305];
	int num; 
	int summation = 0;
	cin >>num;
	
	for (int i=1 ; i<=num;i++){
		cin >> floors[i];  // 배열 입력받기
		summation += floors[i];
	}
	
	
	
	if (num==1) {return floors[1];}
	if (num==2) {return floors[1]+floors[2];}
	dist[0] = 0;
	dist[1] = floors[1] ;
	dist[2] = floors[2];
	dist[3] = floors[3];
	

	for (int i=4; i<=num;i++){
		dist[i] = min(dist[i-2], dist[i-3]) + floors[i];
	}
	int result = summation -min(dist[num-2],dist[num-1]);
	return result;
	
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout << solution();
}