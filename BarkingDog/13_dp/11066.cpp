#include <bits/stdc++.h>
using namespace std;


//11066. 파일 합치기

/*  
구간 DP의 예시

D[L][R] = L에서 R까지 파일을 합치는 최소 비용

테이블을 채워나가는 순서는, L과 R이 1차이날떄부터, 마지막(L이 처음,R이 끝)일 떄까지.

그런데 K가 500이니까, O(N^3)을 세워볼법 하다.

D[L][R] = min(D[L][K]+D[K+1][R], for k = l ~ r-1.)
이렇게 하면 모든 갱신 로직을 다 검증할 수 있다!


*/





void solution(){
	int T;
	cin >> T;
	int D[505][505];
	int psum[505][505];
	for (int i=1;i<=T; i++){
		int K;
		cin >> K;
		fill(D[0],D[505],0);
		fill(psum[0],psum[505],0);
		int pages[505];
		for (int i=1;i<=K;i++){ //250000게 = 100만개 = 1MB 
			cin >> pages[i];
			D[i][i] = pages[i];
			psum[i][i] = pages[i];
		}
		
		//테이블 로직 : pages에는 1~K개까지의 데이터가 있음
		
		for (int interval=1; interval<=K-1;interval++){
			for (int start = 1; start<=K; start++){
				int end = start+interval;
				if (end >K) continue;
				psum[start][end]= 100000000; //초기화;
				if (interval ==1){
					D[start][start+1] = pages[start]+pages[start+1];
					psum[start][start+1] = pages[start]+ pages[start+1];
					continue;
				}
				
				for (int term=start; term<=end-1;term++){
					D[start][end] = D[start][term]+ D[term+1][end]; // 늘 sum(start:end와 동일할수밖에 없음)
					int candidate = psum[start][term] + psum[term+1][end] + D[start][end];			
					if (term== start){candidate = psum[term+1][end]+D[start][end];}
					else if (term== end-1){candidate = psum[start][term]+D[start][end];}
					psum[start][end] = min(psum[start][end], candidate);
		
					
					
					
				} 
			}
		}	
		cout << psum[1][K] << "\n";
	

	}
}





	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}