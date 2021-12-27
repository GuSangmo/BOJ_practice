//11726. 2*n 타일링

/*  

문양이 달라야 한다. 

D[N] = D[N-1] + D[N-2];

*/


#include <bits/stdc++.h>
using namespace std;


int solution(){
	int D[1005];
	int num; 
	cin >>num;
	
	D[1] = 1;
	D[2] = 2;
	// Data 입력받기
	for (int i=3 ; i<=num;i++){
		D[i] = (D[i-1]+ D[i-2]) %10007;
		}
	
	return D[num];
	}
	
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout << solution();
}