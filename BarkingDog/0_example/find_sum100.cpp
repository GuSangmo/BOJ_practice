/*
Example 2. 두 수의 합이 100인 두 원소 찾기 
*/

#include <iostream>
using namespace std;

int solution(int arr[],int visit[], int N){
	for (int i = 0; i<N; i++){
		int element = arr[i];
		visit[element] = 1;
		if (visit[100-element] ==1 && element!= 50){
			return 1;
		}
	}
	return 0;
	
	
	
}

int main(){
	int N;
	cin >> N ; 
	int arr[1001];
	int visit[1001];
	for (int i=0;i<N;i++){
		cin>>arr[i];
	}
	
	
	for (int i=0;i<N;i++){
		cout<<"이번 변수는"<<arr[i]<<'\n';
	}
	
	
	int result = solution(arr, visit, N);
	cout << result <<'\n';
	return 0;
} 
