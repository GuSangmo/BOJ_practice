/*
9498. 시험 성정
*/

// switch 문을 쓰면 이건 run-time constant이기 때문에 안돼

/*
switch(expression)
{
case (test1) : operation ; break ;
case (test2) : operation ; break ;
.
.
default : operation; break ;
}


*/


#include <bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int score;	
	cin >> score;
	//이 코드가 a,b를 입력받지 않은 상황에서 초기화되어서 core_dumped가 뜬 것. 
	
	if	 	(score>=90){cout <<"A";}
	else if (score>=80){cout<<"B";}
	else if (score>=70){cout<<"C";}
	else if (score>=60){cout<<"D";}
	else{cout<<"F";}
	return 0;
} 
