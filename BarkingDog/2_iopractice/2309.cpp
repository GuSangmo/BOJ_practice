/*
2309. 일곱난쟁이

9개중 루프를 2개 돌려서 뺐을 때 0이 나오는걸 확인해보면 된다.

*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);	
	int summation, medium;
	int liar1, liar2;   // 거짓말치는 2명의 idx
	vector <int>v(9);
	summation = 0;
	for (int i=0; i<9; i++){
		cin >> v[i];
		summation += v[i];
	}

	for (int idx1=0; idx1<9;idx1++){
		for (int idx2=idx1+1; idx2<9; idx2++){
			if (summation - v[idx1]-v[idx2] == 100){
				liar1 = idx1; liar2 = idx2;
				break;
			}			
		}	
	}
	
	vector <int> new_vector;  //empty vector 생성. new_vector(10,n)은 10개의 원소를 n으로 초기화
	for (int j=0;j<9;j++){
		if (j!=liar1 && j!=liar2){
			new_vector.push_back(v[j]);
		}
	}
	
	sort(new_vector.begin(),new_vector.end());

	for (int j=0;j<7;j++){
		cout << new_vector[j] <<"\n";
	}
		
	return 0;
} 
