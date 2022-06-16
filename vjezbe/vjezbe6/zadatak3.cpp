#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
void print(vector <int> lista)
{
    for(int i=0; i < lista.size(); i++)
    {
        std::cout << lista[i] << ' ';
    }
    std::cout<<std::endl;
}

void interval(vector <int> lista, int a, int b)
{
    for (int i=0; i < lista.size(); i++)
    {
        if (a <= lista[i] and lista[i] <= b)
    {
            std::cout << lista[i] << ' ';
    }
    }
    std::cout<<std::endl;
}

vector<int> obrnuti(vector<int> lista)
{
    vector<int> rlista={};
    for (int i=1; i <= lista.size(); i++)
    {
        rlista.push_back(lista[lista.size()-i]);
    }
    return rlista;
}

vector<int> zamijeniti(vector<int> lista,int a, int b)
{
    vector<int> z_lista=lista;
    z_lista[b]=lista[a];
    z_lista[a]=lista[b];
    return z_lista;
}

int max(vector <int> lista)
{   int max=lista[0];
    for (int i=0; i < lista.size(); i++)
    {
        if (max < lista[i])
        {
            max=lista[i];
        }
    }
    return max;
}

int main()
{
    vector<int> lista={1,2,3,4,5,6,7,8,10,9};
    interval(lista,5,9);
    print(obrnuti(lista));
    print(zamijeniti(lista,2,5));
    std::cout<<max(lista)<<std::endl;
    return 0;
}