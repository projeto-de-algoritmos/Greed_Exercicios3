#include <bits/stdc++.h>
using namespace std;

int maxSatisfaction(vector<int>& satisfaction) {
    sort(satisfaction.begin(), satisfaction.end(), greater<int>());
    int size = satisfaction.size();
    int soma = 0;
    int sentinela = 0;
    for(int k=0; k<size; ++k){
        soma = soma + satisfaction[k];
        if(soma<0) break;
        sentinela++;
    }
    int resposta = 0;
    int t = sentinela;
    if(soma){
        for(int j=0; j<sentinela; ++j){
            resposta = resposta + satisfaction[j]*t;
            t--;
        }
    }
    return resposta;
}

int main(){
    vector<int> vetor1 = {-1,-8,0,5,-7};
    vector<int> vetor2 = {4,3,2};
    vector<int> vetor3 = {-1,-4,-5};
    int resp = maxSatisfaction(vetor1);
    cout << "Result: " << resp << '\n';
    resp = maxSatisfaction(vetor2);
    cout << "Result: " << resp << '\n';
    resp = maxSatisfaction(vetor3);
    cout << "Result: " << resp << '\n';
    return 0;
}
