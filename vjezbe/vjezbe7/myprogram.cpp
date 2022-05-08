#include <iostream>
#include <Particle.h>

using namespace std;

int main()
{
Particle p1(10,45,0,0);
Particle p2(20,78,10,0);
p1.range(0.01);
p1.time(0.01);
p2.range(0.01);
p2.time(0.01);
return(0);
}