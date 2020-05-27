#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int num;
	vector<int> row;
	vector<char> sol;
	stack<int> st;
	cin >> num;
	for (int i = 0; i < num; i++) {
		int in;
		cin >> in;
		row.push_back(in);
	}
	int count = 1;
	int index = 0;
	while (index<num) {
		if (st.empty()) {
			st.push(count);
			sol.push_back('+');
			count++;
		}
		else {
			if (st.top() == row[index]) {
				sol.push_back('-');
				st.pop();
				index++;
			}
			else if (st.top() < row[index]) {
				st.push(count);
				sol.push_back('+');
				count++;
			}
			else if (st.top() > row[index]) {
				cout << "NO" << endl;
				break;
			}
		}
	}
	if (index == num) {
		for (int i = 0; i < sol.size(); i++)
			cout << sol[i] << '\n';
	}
}
