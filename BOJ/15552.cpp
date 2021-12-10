/*
15552. 빠른 A+B

그때 봤던 내용.
빠른 입출력을 위해 sync_wth_stdio, cin.tie를 지정해주는 부분.
*/

#include <bits/stdc++.h>
using namespace std;




int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;  //100만이라 long long일 필요는 없음
	cin >>T;
	for (int i=0;i<T; i++){
		int a,b;
		cin >> a>>b;
		cout <<a+b <<"\n";
	}
	
	return 0;
	}

	
