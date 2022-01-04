/*
10807. 개수 세기

그냥 입력받으면서 더해주면 된다.

*/


#include <bits/stdc++.h>
using namespace std;


int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, v;
	cin >>N;
	
	vector <int> cnt(201);  // -100 ~100 배열을 담을 201개
	vector <int> arr(105); // 최대 105개
	for (int i=0; i<N; i++){
		cin >>arr[i];
		cnt[arr[i]+100] +=1;
	}
	cin >>v;
	cout << cnt[v+100];
	
	return 0;
}