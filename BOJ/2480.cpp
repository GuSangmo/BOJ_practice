/*
2480. 주사위 세 개

max, min 쓰면 되겠지만 일단은 BF로 짜보자
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n1, n2, n3 ;
	bool isYoon = false;
	int result;
	cin >> n1 >> n2 >> n3;
	int arr[3] = {n1,n2,n3};
	int maximum = 0;
	for (int i=0; i<3;i++){
		if (arr[i]>=maximum){maximum = arr[i];}
	}
	
	
	if ( n1==n2 && n2==n3) {result = 10000+ n1 * 1000;}
	else if (n1==n2){result = 1000 + n1 * 100;}
	else if (n2==n3){result = 1000 + n2 * 100;}
	else if (n1==n3){result = 1000 + n3 * 100;}
	else {result = maximum * 100;}
	
	cout << result;
	
} 
