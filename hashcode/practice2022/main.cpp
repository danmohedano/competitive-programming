#include <bits/stdc++.h>
using namespace std;

struct Client
{
    vector<string> likes;
    vector<string> dislikes;
};

int clientNum;
vector<struct Client> clients;

unordered_map<string, pair<int, int>> ingredients;
vector<string> finalIngredients;

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

            //añadir al map de ingredientes
            auto elem = ingredients.find(tempIng);
            if (elem == ingredients.end()){
                ingredients.insert({tempIng, make_pair(0, 0)});
                elem = ingredients.find(tempIng);
            }
            elem->second.first += 1;

            //añadir a los datos del cliente
            clients[i].likes[j] = tempIng;
        }
        cin >> temp;
        clients[i].dislikes.resize(temp);
        for (int j = 0; j < temp; ++j) {
            string tempIng;
            cin >> tempIng;

            //añadir al map de ingredientes
            auto elem = ingredients.find(tempIng);
            if (elem == ingredients.end()){
                ingredients.insert({tempIng, make_pair(0, 0)});
                elem = ingredients.find(tempIng);
            }
            elem->second.second += 1;

            //añadir a los datos del cliente
            clients[i].dislikes[j] = tempIng;
        }
    }
    

    

    string ingredientName, maxLikesIngredient, maxDislikesIngredient;
    int cuantLikes, cuantDislikes, maxLikes=0, maxDislikes=0;

    for (std::pair<std::string, tuple<int, int>> element : ingredients)
    {
        ingredientName = element.first;
        tie(cuantLikes, cuantDislikes) = element.second;

        if (cuantLikes > maxLikes){
            maxLikes = cuantLikes;
            maxLikesIngredient = ingredientName;
        }

        if (cuantDislikes > maxDislikes){
            maxDislikes = cuantDislikes;
            maxDislikesIngredient = ingredientName;
        }
    }
    

    return 0;
}

void simpleHeur(){
    unordered_map<string, int> scores;
    for (auto& ingr : ingredients){
        scores.insert({ingr.first, ingr.second.first - ingr.second.second});
    }

    for (auto& ingr : scores){
        if (ingr.second > 0){
            finalIngredients.push_back(ingr.first);
        }
    }
}

void ponderedHeur(){
    unordered_map<string, double> scores;
    void manageScores(string elem, int pond, bool likes){
        auto elem = scores.find(elem);
        if (elem == scores.end()){
            scores.insert({elem, 0});
            elem = scores.find(elem);
        }
        if (likes){
            elem->second += 1/pond;
        }
        else{
            elem->second -= 1/pond;
        }
    }
    for (auto& client : clients){
        for (string ingr: client.likes){
            manageScores(ingr, client.likes.size(), true);
        }
        for (string ingr: client.dislikes){
            manageScores(ingr, client.dislikes.size(), false);
        }
    }

    for (auto& ingr : scores){
        if (ingr.second > 0){
            finalIngredients.push_back(ingr.first);
        }
    }
}

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

