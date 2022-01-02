//9251. LCS

/*  
두 문자열의 길이 N ,M 에 대한 table을 구하자!

LCS[i][j] =

A[i]랑 B[j]가 같다면 LCS[i-1][j-1]


*/


#include <bits/stdc++.h>
using namespace std;


int LCS[1010][1010]; // 100만개쯤. 4MB

int result = 0;
void solution(){
	string seq1,seq2;
	cin >> seq1 ;
	cin >> seq2 ;
	for (int i=0; i<=seq1.length(); i++){
		for (int j=0; j<=seq2.length();j++){
			if (i==0 or j==0){
				LCS[i][j] = 0;				
			}
			else if (seq1[i-1]== seq2[j-1]){
				LCS[i][j] = LCS[i-1][j-1]+1;
				result = max(LCS[i][j], result);				
			}
			else{
				LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j]);
			}
		}
	}
	cout << result << "\n";
	
	}
	
	
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}