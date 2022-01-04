//12852. 1로 만들기 2

/*  
이젠 역추적을 하면 된다.
*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int n; 
	int dist[1000005];
	int prev[1000005];
	
	prev[2] = 1; prev[3] = 1; 
	dist[1] = 0;
	dist[2] = 1;
	dist[3] = 1;
	cin >>n ;
	for (int i= 4; i<=1000005; i++){
		dist[i] = dist[i-1] + 1; 
		prev[i] = i-1;
		if (i%2==0) { 
			if (dist[i]>= dist[i/2]+1) {
				dist[i] = dist[i/2]+1;
				prev[i] = i/2;
			}
		}
			
		if (i%3==0) { 
			if (dist[i]>= dist[i/3]+1) {
				dist[i] = dist[i/3]+1;
				prev[i] = i/3;
			}
		}
	}
	cout << dist[n]<<"\n";	
	int temp = n;
	while(temp!=prev[temp]){
		cout <<temp<<" ";
		temp = prev[temp];	
	}
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}