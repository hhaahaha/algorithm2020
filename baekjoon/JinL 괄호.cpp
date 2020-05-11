#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	int T;
	string input;
	stack<char> check;
	cin >> T;
	
	int i = 0;
	while (i++ < T) {
		cin >> input;
		for (int j = 0; j < input.length(); j++)
			if (input.at(j) == '(')
				check.push(input.at(j));
			else if (input.at(j) == ')')
				if (check.empty()) {
					check.push(input.at(j));
					break;
				}
				else
					check.pop();
		if (check.empty())
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
		while (!check.empty())
			check.pop();
	}
}
