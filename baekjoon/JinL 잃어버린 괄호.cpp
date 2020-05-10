#include <iostream>
#include <string>
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
	int a, b, result;
	b = num.top();
	num.pop();
	a = num.top();
	num.pop();
	string oper = ops.top().opt;
	ops.pop();
	if (oper == "+")
		result = a + b;
	else if (oper == "-")
		result = a - b;
	num.push(result);
}

int main()
{
	string cal;
	stringstream check;
	bool minimize = false;

	getline(cin, cal);
	check.clear();
	check.str(cal);

	string opt;
	while (check >> opt) {
		if (opt=="(" || opt==")") {
			//최소값을 구하기 위해 괄호를 무시
		}
		else if (opt == "+"||opt == "-") {
			int prior;
			//더하기의 연산 우선순위를 높여줌
			if (opt == "+")
				prior = 2;
			else if(opt == "-")
				prior = 1;
			//연산자 우선순위가 낮은게 top으로 올때 까지 계산
			while (!ops.empty() && prior <= ops.top().pri)
				calc();
			//연산자 스택에 push
			ops.push({prior,opt});
		}
		else {
			//입력값이 숫자인 경우 저장
			try {
				num.push(stoi(opt));
			}
			catch (exception e) {
				cout << "잘못된 입력" << endl;
				break;
			}
		}
	}
	//나머지 계산
	while (!ops.empty())
		calc();
	//결과값 출력
	cout << num.top();
}
