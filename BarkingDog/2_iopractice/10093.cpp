/*
10093. 숫자

서브태스크가 2개 있는데, 
하나는 범위가 괜찮고
다른 하나는 int overflow가 날 수 있다. 
long long 쓰기

고려할 점이 있다면, 첫 째로 두 숫자의 대소관계가 주어지지 않았다.
그래서 작은거 큰걸 먼저 바꿔준다.

또한 두 수가 같을 수도 있다.


tmp 변수조차 long long으로 지정했어야 한다.

*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);	
	long long n1, n2; // 1~ 10**(15)까지 가능.
	cin >> n1 >> n2 ; 
	int length;
	if (n1>=n2){
		long long tmp = n1;
		n1 = n2; 
		n2 = tmp;}
	
	if (n2-n1<=1){cout<<0;}
	else{ 
		length = n2-n1-1;
		cout << length <<"\n";
		for (long long i=n1+1; i<n2; i++){
			cout << i  <<" ";
		}
	}

	
	
	
	
	
	
	
	return 0;
} 
