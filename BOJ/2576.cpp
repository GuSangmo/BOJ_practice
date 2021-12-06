/*
2576. 홀수
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[8];
	int summation = 0;
	int minimum = 101;
	bool isoddin = false;
	
	for (int i=0; i<7;i++){
		cin >> arr[i];
		if (arr[i]%2 == 0) {continue;}
		isoddin = true;
		summation += arr[i];
		if (arr[i]<=minimum){minimum = arr[i];}
	}
	if (isoddin){cout <<summation<<"\n"<<minimum ;}
	else {cout <<-1;}
	return 0;
} 
