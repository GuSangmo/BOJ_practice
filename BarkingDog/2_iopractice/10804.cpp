/*
10804. 카드 역배치

하나하나 다시 수정하는 작업을 하자!
*/

#include <bits/stdc++.h>
using namespace std;


void change_arr(int arr[], int a,int b){	
	//arr[a-1]부터 arr[b-1]을 서로 바꿔야함.
	reverse(arr+a-1,arr+b);
	}



int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	int arr[20];
	
	for (int i=0; i<20; i++){
		arr[i] = (i+1);
	}
	
	for (int i = 0; i<10;i++){
		int a,b;
		cin >>a>>b;
		change_arr(arr,a,b);
	}
	
	for (int i= 0; i<20;i++){
		cout << arr[i] <<" ";
	}
	
		
	return 0;
	}

	
