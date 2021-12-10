/*
2490. 윷놀이

cnt로 도, 개, 걸, 윷 판단
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[4];
	
	for (int i=0; i<3;i++){
		int cnt = 0;
		for (int i=0; i<4;i++){
			cin >> arr[i];
			if (arr[i] ==0) {cnt= cnt+1;}
		}
		if ( cnt == 4) {cout << "D\n";}
		else if (cnt == 3){cout <<"C\n";}
		else if (cnt == 2){cout <<"B\n";}
		else if (cnt == 1){cout <<"A\n";}
		else {cout <<"E\n";}
	}
	return 0;
} 
