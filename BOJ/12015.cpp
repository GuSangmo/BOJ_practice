//12015. 가장 긴 증가 부분 수열2 (LIS)

/*  

N이 100만이므로 N log N 솔루션을 써야 한다.
그건 바로 binary_search!

key idea는 LIS의 마지막 원소가 작으면 더 많이 들어갈 여지가 있기에, 
배열의 처음부터 LIS를 조금씩 갱신해주는 것! 

새 원소가 들어올때 그 원소가 들어갈 위치가 마지막이라면 
LIS의 길이를 늘려준다. 
아니라면 중요하지 않음.

__

index_arr을 
전역 변수로 잡으면 잘 뜨는데,
지역 변수로 잡으면 계속 core dumped가 뜸. 

[1] 초기화를 안해서 그런가? -> 0으로 떠도 오류가 난다.

==> 확인결과 컴파일러 별 stackframe의 size를 넘어서 그런듯! 


*/


#include <bits/stdc++.h>
using namespace std;

//int index_arr[1000010];

int K[1000010];
int numbers[1000010];
void solution(){
		
	int N;
	cin >> N;
		
	int idx = 0; // LIS의 길이
	for (int i=1;i<=N;i++){
		cin >> numbers[i];
		
		if (idx == 0){ 
			K[idx] = numbers[i] ;
			index_arr[i] = 0;
			idx+=1;
		}
		
		else {
			if (K[idx-1]<numbers[i]) // 마지막이면 갱신 가능
			{
			index_arr[i] = idx;
			K[idx] = numbers[i];
			idx+=1;
		}
			else {
				index_arr[i] = lower_bound(K,K+idx, numbers[i])-K;
				K[lower_bound(K,K+idx, numbers[i])-K] = numbers[i];
			}
		}	
	}
	
	cout << idx <<"\n";
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}