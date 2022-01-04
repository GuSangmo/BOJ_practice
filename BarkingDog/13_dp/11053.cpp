//11053. 가장 긴 증가 부분 수열1 (LIS)

/*  
D[i] = i번째에서 끝나는 LIS의 길이 

D[i]를 일단 1로 세팅한 후, 
1부터 i-1까지의 j에 대해 

numbers[j]<numbers[i]면 D[i] = max(D[i],D[j]+1)로 세팅! 
그 후 max_element!

*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int D[1010];
	int numbers[1010];
	int N;
	cin >> N;
	for (int i=0;i<N;++i){
		cin >> numbers[i];
		D[i] = 1;
	}
	
	for (int i=0;i<N;++i){
		for (int j=0;j<i;++j){
			if (numbers[j]<numbers[i]){			
				D[i] = max(D[i], D[j]+1);
			}
		}
		
	}
	cout << *max_element(D,D+N) <<"\n";
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}