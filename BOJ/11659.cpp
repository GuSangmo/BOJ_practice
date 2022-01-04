//11659. 구간 합 구하기 4

/*  
Prefix sum을 이용하는 문제!
1000 * 10만이면 10^9 네. 
혹시 모르니 long long 쓰자

*/


#include <bits/stdc++.h>
using namespace std;


void solution(){
	int n,m; 
	int arr[100005];
	long long psum = 0;
	int psum_arr[100005];
	psum_arr[0] = 0;
	
	cin >> n>> m;
	
	for (int i= 1; i<=n; i++){
		cin >> arr[i];
		psum += arr[i];
		psum_arr[i] = psum;
	}
	
	// prefix sum 구하기
	for (int i=0 ; i<m;i++){
		int start, end;
		cin >>start>>end;
		long long result =  psum_arr[end] - psum_arr[start-1];
		cout << result <<"\n";
	}
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}