//9252. LCS 2

/*  
두 문자열의 길이 N ,M 에 대한 table을 구하자!

LCS[i][j] = 

i,j가 0이라면 0 (null이랑 비교할 순 없죠)
A[i]랑 B[j]가 같다면 LCS[i-1][j-1] +1
아니라면 max(LCS[i][j-1], LCS[i-1][j]) 그대로!


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
	string LCS_string;
	int i = seq1.length();
	int j = seq2.length();
	int idx = 0;
	while (LCS[i][j]>0){
		if (LCS[i][j] == LCS[i-1][j]) i-=1; 
		else if (LCS[i][j] == LCS[i][j-1]) j-=1;
		else {
			if (LCS[i][j] == LCS[i-1][j-1]+1){
			LCS_string.push_back(seq1[i-1]);
			// cout << seq1[i-1];
			}
			i--; j--;
		}
	}
	
	for (int i = LCS_string.size()-1; i>=0; i--){
		cout << LCS_string[i];
	}
}
	

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
    solution();
}