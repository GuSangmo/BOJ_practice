/*
10828. 스택

입출력 이슈 잘 지키자!~



*/



//N 초기화 잘 시키자!


#include <bits/stdc++.h>
using namespace std;


int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	stack <int> S;
	cin >> N ;
	for (int i=0;i<N;i++){
		string order;
		cin >>order;
		if (order == "push"){
			int num;
			cin >>num;
			S.push(num);
		}
		else if(order == "pop"){
			if(S.empty()){cout<<-1<<'\n';}
			else{cout <<S.top()<<"\n";
				S.pop();}
		}
		else if (order == "size"){
			cout <<S.size()<<"\n";
		}

		else if (order == "empty"){
			if(S.empty()){cout<<1<<"\n";}
			else {cout<<0<<"\n";}
		}
		else if(order=="top"){
			if(S.empty()){cout<<-1<<"\n";}
			else {cout<<S.top()<<"\n";}
			}

	}
	
	return 0;	
}