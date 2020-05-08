#include<iostream>
#include<string>
#include<sstream>
#include<stack>
using namespace std;

struct oper {
	int pri; // 연산자 우선순위
	string opt; // 연산자
};
stack<int> num; // 숫자 스택
stack<oper>ops; // 연산자 스택

void calc() {

}

int main()
{
	string cal;
	stringstream check;
	bool minimize = false;

	cin.ignore(50, '\n');
	getline(cin, cal);
	check.clear();
	check.str(cal);

	string opt;
	while (check >> opt) {
		if (opt=="(" || opt==")") {
			//do not thing
		}
		else if (opt == "+"||opt == "-") {
			int prior;
			if (opt == "+")
				prior = 2;
			else
				prior = 1;
			if (minimize) {
				minimize = false;

			}
			else {
				minimize = true;
				ops.push({ 0,"(" });
			}

			ops.push({prior,opt});
		}
		else {
			//입력값이 숫자인 경우 저장
			num.push(stoi(opt));
		}
	}
}
