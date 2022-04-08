#include <iostream>
#include <cmath>

void kruznica(float r, float p, float q, float x, float y) {
    float r2;
    r2=sqrt(pow((x-p),2)+pow((y-q),2));

    if (r2>r) {
        std::cout << "tocka se nalazi izvan kruznice" << std::endl;
    }
    if (r2<r) {
        std::cout << "tocka se nalazi unutar kruznice" << std::endl;
    }
    if (r2==r) {
        std::cout << "tocka se nalazi na kruznici" << std::endl;
    }
}

int main() {
    kruznica(5,0,0,1,1);
    return 0;
}