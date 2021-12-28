//1003. 피보나치 함수

/*  
fib(N) 을 구하기 위해 fib(N-1)과 fib(N-2)를 호출하지.

따라서 fib(N)에서 호출되는 fib(0), fib(1)의 개수도 
저 둘의 합으로 표현 가능하다.
*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int T;
	int zeros[45];
	int ones[45];
	
	zeros[0] = 1;
	zeros[1] = 0;
	ones[0] = 0; 
	ones[1] = 1;
	
	for (int i=2; i<=40;i++){
		zeros[i] = zeros[i-1]+ zeros[i-2];
		ones[i] = ones[i-1]+ ones[i-2];
	}
	
	
	
	cin >>T;	
	for (int i=0; i<T; i++){
		int num;
		cin >> num;
		cout <<zeros[num]<<" "<<ones[num]<<"\n";
	}	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}