//11055. 가장 큰 증가 부분 수열

/*  
tables :  값이 담긴 수열
psum[i] : i번째 원소를 반드시 포함하는 가장 큰 증가 수열

psum[i]를 update하기 위해,
i+1 ~ N번째 원소까지를 스캔해가며 
tables[i]<=tables[j]라면 psum[j] 중 가장 큰 걸 더한다. 
그리고 그걸로 psum[i]를 update한다!

그리고 psum[1] ~ psum[N]까지 중 최댓값을 출력하면 충분하다.
*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int tables[1005];
	int psum[1005];
	int num;
	cin >>num;		
	for (int i= 1; i<=num; i++){
		cin >> tables[i];
	}
	for (int i= num; i>=1; i--){
		int add_part = 0;
		psum[i] = tables[i];
		for (int j= i+1; j<=num; j++){
			if (tables[i]<tables[j]){				
				if (psum[j]>=add_part){
					add_part = psum[j];
				}
			}
		psum[i] = tables[i] + add_part;	// psum[i] += add_part ; 는 이상했는데...
		}
	}
	
	int result = 0;
	for (int i= 1; i<=num;i++){
		if (psum[i]>=result) {result = psum[i];}
	}
	
	cout << result <<"\n";

}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}