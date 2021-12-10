/*
1000. A+B
*/

#include <iostream>
using namespace std;

int solution(int arr[],int N){
	for (int i = 0; i<N; i++){
		int element = arr[i];
		if (arr[100-element] ==1){
			return 1;
		}
	}
	return 0;
	
	
	
}

int main(){
	int N;
	cin >> N ; 
	int arr[1001];
	for (int i=0;i<N;i++){
		cin>>arr[i];
	}
	int result = solution(arr, N);
	cout << result <<'\n';
	return 0;
} 
