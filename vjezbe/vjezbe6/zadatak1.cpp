#include <iostream>
void pravac(float x1, float y1, float x2, float y2) {
    float k;
    k=(y2-y1)/(x2-x1);

    if (k*x1-y1<0) {
        std::cout << "y = " << k << "x + " << abs(k*x1-y1) << std::endl;
        
    }
    if (k*x1-y1>0) {
        std::cout << "y = " << k << "x - " << abs(k*x1-y1) << std::endl;    
    }
}
int main() {
    pravac(0,2,5,7);
return 0;
}