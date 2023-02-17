//zadanie 1: krizovatky
//autor: Roman Hudec
//datum: 10.3.2022

#include <iostream>
#include <tuple>
#include <unordered_map>
#include <queue>
#define triple tuple<long long, long long, long long>

using namespace std;

struct compare{

    bool operator()(const triple &a, const triple &b){
        return a > b;
    }
};



class City{
    unordered_map<long long,  unordered_map<long long, pair<long long, bool> > > graph;

public:
    void addHouse(long long house){
        //ak tam este nie je, pridaj ho aj s jeho hash mapou
        if(graph.find(house) == graph.end()){
            graph[house] = unordered_map<long long, pair<long long, bool> >();
        }
    }

    void addRoute(long long house1, long long house2, long long distance, bool isSafe){
        addHouse(house1);
        addHouse(house2);

        //ak este nikdy medzi nimi hrana nebola
        if(graph[house1].find(house2) == graph[house1].end()){
            graph[house1][house2] = pair<long long, bool> (distance, isSafe);
            graph[house2][house1] = pair<long long, bool> (distance, isSafe);

        }else{
            pair<long long, bool> edge = graph[house1][house2];

            //nahradzam hranu, ak mame rovnaku boolean hodnotu alebo nova je okay, ale stara nebola
            if((isSafe == edge.second && edge.first > distance) || (isSafe && !edge.second)){
                graph[house1][house2] = pair<long long, bool> (distance, isSafe);
                graph[house2][house1] = pair<long long, bool> (distance, isSafe);
            }

        }
    }

    unordered_map<long long, pair<long long, long long>> dijkstra(long long start){

        //long long N = graph.size(); //pocet vrcholov
        unordered_map<long long, pair<long long, long long>> D; //pole vzdialenosti


        //long long visited[N];
        unordered_map<long long, bool> visited;

        for (auto vertex : graph){
            visited[vertex.first] = false;
        }

        /*for(long long i=0; i < N; i++){
            visited[i] = -1;
        }*/

        priority_queue<triple, vector<triple>, compare> pq;

        pq.push(triple(0, 0, start)); //pridavame trojicu (nebezpecie, bezpecie, vrchol)

        while(!pq.empty()){
            triple first = pq.top();
            pq.pop();

            long long dangerousDistance = get<0>(first);
            long long distance = get<1>(first);
            long long v = get<2>(first);

            if(visited[v] == false){
                D[v] = pair<long long, long long> (dangerousDistance, distance);
                visited[v] = true;

                for(auto n : graph[v]){ //prvky z hash mapy
                    long long w = n.first; //sused v-cka
                    if(visited[w] == false){
                        if(n.second.second){ // safe/not safe
                            long long weight = n.second.first;
                            pq.push(triple(dangerousDistance, distance+weight, w));
                        }else{
                            long long weight = n.second.first;
                            pq.push(triple(dangerousDistance+weight, distance+weight, w));
                        }


                    }
                }
            }
        }
        return D;
    }

    pair<long long, long long> getPath(long long start,long long end){

        if(graph.find(start) == graph.end()) return pair<long long, long long> (-1, -1);

        unordered_map<long long, pair<long long, long long>> D = dijkstra(start);


        if(D.find(end) == D.end()){
            return pair<long long, long long> (-1, -1);
        }

        //pair<long long, long long> output = D[end];

        return D[end];
    }
};

int main() {


    long long vrcholy, hrany, otazky;
    cin >> vrcholy >> hrany >> otazky;
    City city;

    for(long long m = 0; m < hrany; m++){
        long long zac, kon, vaha;
        bool ok;
        char pis;

        cin >> zac >> kon >> vaha >> pis;
        ok = (pis == 'B');

        city.addRoute(zac, kon, vaha, ok);
    }

    for(long long q = 0; q < otazky; q++){
        long long zac, kon;
        cin >> zac >> kon;
        pair<long long, long long> odpoved = city.getPath(zac, kon);
        cout << odpoved.first << " " <<odpoved.second << endl;

    }
    return 0;
}
