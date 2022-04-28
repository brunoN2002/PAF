#include <Particle.h>
#include <math.h>
#include <iostream>

void Particle::evolve() {
while (y>=0) {
    vx+=0.;
    vy+=g*dt;
    x+=vx*dt;
    y+=vy*dt
    t+=dt;
    }
}

Particle::Particle(double v, double theta, double x0, double y0, double step) {
    kut=theta*pi/180;
    vx=v*cos(kut);
    vy=v*sin(kut);
}

float Particle::range() {
    evolve();
    std::cout << x0 << std::endl;
}

float Particle::time() {
    evolve();
    std::cout << t << std::endl;
}