/*
1267. 핸드폰 요금

어느 것이 효과적인지를 알기 위해 영식, 민식요금제를
모두 계산하는 함수를 짜자.
*/

#include <bits/stdc++.h>
using namespace std;


int yeongsik(int N){
	int tmp1 = N / 30 ;
	return (tmp1+1) * 10;
}

int minsik(int N){
	int tmp2 = N/60;
	return (tmp2+1) * 15;
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	int arr[21];
	int cmp1 = 0;
	int cmp2 = 0;
	cin >> N ;
	
	for (int i = 0; i<N;i++){
		cin >> arr[i];
		cmp1+= yeongsik(arr[i]);
		cmp2+= minsik(arr[i]);
	}
	
	if (cmp1>cmp2){cout << "M "<<cmp2;}
	else if (cmp1<cmp2){cout <<"Y "<<cmp1;}
	else {cout <<"Y M "<<cmp1;}
	
	return 0;
	}

	
