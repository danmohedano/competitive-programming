#include <bits/stdc++.h>
using namespace std;

vector<string> todosLosIngredientes;

vector<string> finalIngredients;

struct Client
{
    vector<string> likes;
    vector<string> dislikes;
};

int clientNum;
vector<struct Client> clients;



int score(){
    int points = 0;
    bool clientCounts;
    for (auto & client: clients){
        
        clientCounts = true;

        //CHECK LIKES
        for (auto & ingredient: client.likes){
            bool isContained = find(finalIngredients.begin(), finalIngredients.end(), ingredient) != finalIngredients.end();
            if(!isContained){
                clientCounts = false;
                break;
            }
        }
        if(clientCounts == false) continue;


        //CHECK DISLIKES
        for (auto & ingredient: client.dislikes){
            bool isContained = find(finalIngredients.begin(), finalIngredients.end(), ingredient) != finalIngredients.end(); 
            if(!isContained){
                clientCounts = false;
                break;
            }
        }
        if(clientCounts == false) continue;

        points++;
    }
    
    return points;
}



int main(){

    cin >> clientNum;
    clients.resize(clientNum);

    int temp;
    for (int i = 0; i < clientNum; ++i){
        cin >> temp;
        clients[i].likes.resize(temp);
        for (int j = 0; j < temp; ++j) {
            string tempIng;
            cin >> tempIng;
            clients[i].likes[j] = tempIng;
        }
        cin >> temp;
        clients[i].dislikes.resize(temp);
        for (int j = 0; j < temp; ++j) {
            string tempIng;
            cin >> tempIng;
            clients[i].dislikes[j] = tempIng;
        }
    }
    




    //EMPEZAR A PROBAR COMBINACIONES
    string tempIngredient;
    int lenCombination;

    ifstream input;
    input.open("data/combinations-c.txt");
    string line;


    //PROBAR COMBINACIONES
    while (getline(input, line)) {
        istringstream iss(line);
        iss >> lenCombination;
        
        finalIngredients.clear();
        for (int i=0; i < lenCombination; i++){
            iss >> tempIngredient;
            finalIngredients.push_back(tempIngredient);
        }
        cout << score() << "\n";
    }
}




