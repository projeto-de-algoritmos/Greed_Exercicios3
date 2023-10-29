class Solution {
public:
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
};
