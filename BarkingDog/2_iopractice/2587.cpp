/*
2587. 대표값2
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int avg, medium;
	
	vector <int>v(5);
	avg = 0; 
	for (int i=0; i<5; i++){
		cin >> v[i];
		avg += v[i];
	}
	sort(v.begin(),v.end());

	avg = avg / v.size();
	medium = v[2];
	
	cout << avg <<"\n"<<medium;
		
	return 0;
} 
