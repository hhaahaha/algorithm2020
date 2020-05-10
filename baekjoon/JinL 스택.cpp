#include <iostream>
#include <string>
#include<sstream>
#include<stack>
using namespace std;
int main() {
	stack <int>stk;
	int N, count = 0;
	string input;
	stringstream in;

	cin >> N;
	cin.ignore();
	int i = 0;
	while (i++<N) {
		getline(cin,input,'\n');

		string check;
		in.clear();
		in.str(input);
		in >> check;
		if (check == "push") {
			int num;
			in >> num;
			stk.push(num);
		}
		else if (check == "pop") {
			if (stk.empty())
				cout << -1 << endl;
			else {
				cout << stk.top() << endl;
				stk.pop();
			}
		}
		else if (check == "size") {
			cout << stk.size() << endl;
		}
		else if (check == "empty") {

			if (stk.empty())
				cout << 1 << endl;
			else
				cout << 0 << endl;
		}
		else if (check == "top") {
			if (stk.empty())
				cout << -1 << endl;
			else
				cout << stk.top() << endl;
		}
	}
	while (!stk.empty()) {
		stk.pop();
	}
	
}
