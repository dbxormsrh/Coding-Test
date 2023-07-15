#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion){
    string answer  ="";
    vector<string>::iterator iter_com;
    vector<string>::iterator iter_par;
    for(iter_com = completion.begin(); iter_com != completion.end(); iter_com++){
        if (participant.size() == 1){
            break;
        }
            for(iter_par = participant.begin(); iter_par != participant.end(); iter_par++){
                if (*iter_par == *iter_com){
                    participant.erase(iter_par);
                    break;
                }
            }
    }
    answer = participant[0];
    return answer;
}

int main(){
    vector<string> participant_1{"leo", "kiki", "eden"};
    vector<string> participant_2{"marina", "josipa", "nikola", "vinko", "filipa"};
    vector<string> participant_3{"mislav", "stanko", "mislav", "ana"};

    vector<string> completion_1{"eden", "kiki"};
    vector<string> completion_3{"josipa", "filipa", "marina", "nikola"};
    vector<string> completion_4{"stanko", "ana", "mislav"};

    cout << solution(participant_1, completion_1) << endl;
}