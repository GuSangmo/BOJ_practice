/*
2752. 세수정렬

내장함수 쓸게 아니었으니 minimum, maximum은 3개 수 입력받아서 하나하나 저장하고 
argmin, argmax가 아닌 걸 medium으로!

*/



#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int num1, num2, num3 ;
	cin >> num1 >> num2 >> num3; 
	int arr[3] = {num1, num2, num3};
	int minimum = 1000001 ; //여기가 문제일까?
	int maximum = -1;
	int medium, argmax, argmin;
	
	for (int i = 0; i<3; i++){
		if (arr[i]>=maximum){ 
			maximum = arr[i];
			argmax = i;
		}
		if (arr[i]<minimum){
			minimum = arr[i];
			argmin = i;
		}
	}
	
	for (int i = 0; i<3; i++){
		if (i==argmax || i ==argmin) {continue;} //하나만 쓰는 것은 bitwise!
		medium = arr[i];
	}	
	cout << minimum <<" "<<medium<<" "<<maximum;
} 
