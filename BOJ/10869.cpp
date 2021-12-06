/*
10869. 사칙연산
*/

// cin으로 받지 않고 변수선언만 하면 0으로 초기화되어서 core_dumped error 가 뜬 것.

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a,b;	
	cin >> a>> b;
	//이 코드가 a,b를 입력받지 않은 상황에서 초기화되어서 core_dumped가 뜬 것. 
	cout << a+b <<"\n"<<a-b<<"\n"<<a*b<<"\n"<< a/b<< "\n"<<a%b<<"\n"; 
	return 0;
} 
