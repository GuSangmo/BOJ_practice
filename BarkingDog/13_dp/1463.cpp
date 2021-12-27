//1463. 1로 만들기

// 1<= N<= 1000000


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int dist[1000005];
	
	dist[1] = 0; // 초기화
	
	for (int i= 2; i<1000001; i++){
		if (i%2==0 && i%3==0) {
			dist[i] = min(min(dist[i/2], dist[i/3]),dist[i-1])+1;
			}
		else if (i%2==0){
			dist[i] = min(dist[i/2], dist[i-1])+1;
		}
		
		else if (i%3==0) {
			dist[i] = min(dist[i/3], dist[i-1])+1;
		}
		else {	dist[i] = dist[i-1] +1 ;}
	}
	int N;
	cin >> N; 
	cout<< dist[N];
}





int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	solution();
}