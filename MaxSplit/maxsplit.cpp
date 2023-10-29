class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        if(finalSum%2==1)
            return {};
        vector<long long> resposta;
        long long reps = 0;
        long long sum = 0;
        while(finalSum>=(reps+1)*2){
            resposta.push_back(2*(reps+1));
            sum+=2*(reps+1);
            reps++;
            if(sum>=finalSum) break;
        }
        if(sum>finalSum){
            sum = sum - (reps)*2;
            resposta.pop_back();
            while(sum!=finalSum){
                for(long long k=reps-2; sum<finalSum; --k){
                    sum+=2;
                    resposta[k]+=2;
                }
            }
        }
        return resposta;
    }
};