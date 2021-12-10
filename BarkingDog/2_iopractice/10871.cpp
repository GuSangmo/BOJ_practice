/*
10871. X보다 작은 수 
그냥 입력받으면서 실시간으로 출력하면 되니깐
*/

#include <bits/stdc++.h>
using namespace std;

	
int arr[10001];

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, X;
	cin >> N >> X ; 
	for (int i = 0; i<N; i++){
		cin >>arr[i];
		if (arr[i]<X) cout<<arr[i]<<" ";
	}
	return 0;
} 
