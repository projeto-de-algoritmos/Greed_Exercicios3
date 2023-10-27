#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int> > stops;

int vis[10006];

int caminhoneiro(int units, int tank, int t){
    int visitados = 0;
    priority_queue<pair<int, int> > pq;
    while(tank<units){
        for(int k=0; k<t; ++k){
            if(tank<(units-stops[k].second) || vis[k]==1) continue;
            pq.push(make_pair(stops[k].first, stops[k].second));
            vis[k]=1;
        }
        if(pq.empty()) return -1;
        if(units>pq.top().second){
            tank = tank + pq.top().first - (units-pq.top().second);
            units = pq.top().second;
        } else {
            tank = tank + pq.top().first;
        }
        visitados++;
        pq.pop();

    }
    return visitados;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int t, N, distance, fuel, units, tank;
    cin >> t;
    while(t--){
        cin >> N;
        for(int i=0; i<N; ++i){
            cin >> distance >> fuel;
            stops.push_back(make_pair(fuel, distance));
        }
        sort(stops.begin(), stops.end());
        cin >> units >> tank;
        for(int i=0; i<N; ++i) vis[i] = 0;
        cout << caminhoneiro(units, tank, N) << '\n';
        stops.clear();
    }
    return 0;
}

// Saída da entrada.txt = 2
//                        2
// Saída da entrada1.txt = 3
//                         3