#include <iostream>
#include <list>

void cijeli_brojevi(float a, float b) {
    for (int i=a; i<b; i++;) {
        list<int> brojevi;
        brojevi.assign(i);
        std::cout << brojevi << std::endl;
    }
}

int main {
    cijeli_brojevi(2,7);
    return 0;
}