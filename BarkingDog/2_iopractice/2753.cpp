/*
2753. 윤년
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N ;
	bool isYoon = false;
	cin >> N;
	if (N%4 == 0){
		if (N%100 ==0){
			if (N%400 ==0) {isYoon = true; }
			else {isYoon = false;}
		}
		else{isYoon = true;}
	}
	cout << (int) isYoon;
	return 0;
} 
