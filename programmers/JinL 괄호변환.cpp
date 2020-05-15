#include <iostream>
#include <string>
#include <vector>
using namespace std;

string balance(string p) {
    if (p == "")
        return p;
    string u, v;
    int point = 0, left = 0, right = 0;
    bool trigger_bal = true;//올바른 균형 : true, 균형 : false

    do{
        if(point>=p.size())
            break;
        if (p.at(point) == '(')
            left++;
        else if (p.at(point) == ')')
            right++;
        
        if (left < right)           //올바른 균형 판별
            trigger_bal = false;
        point++;
    } while (left != right);
    if (point == p.size()) {
        u = p;
        v = "";
    }
    else{
        u = p.substr(0, point);
        v = p.substr(point);
    }
   
        v = balance(v);
        if (!trigger_bal) {
            string newstring = "";
           
            u.erase(0, 1);
            u.pop_back();
            newstring = u;
            for (int i = 0; i < newstring.size(); i++) {
                if (newstring[i] == '(')
                    newstring[i] = ')';
                else if (newstring[i] == ')')
                    newstring[i] = '(';
            }
            u = '(' + v + ')' + newstring;
        }
        else
            u += v;
    return u;
}

string solution(string p) {
    string answer = "";
    answer = balance(p);
    return answer;
}

int main() {
    string input;
    cin >> input;
    cout << solution(input) << endl;
}
