#include "Particle.h"
#include <math.h>
#include <iostream>

Particle::Particle(double v0, double theta0, double x0, double y0) {
    theta=theta0;
    double theta_radijani;
    theta_radijani=theta0*3.141592/180;
    v=v0;
    x=x0;
    y=y0;
    vx=v0*cos(theta_radijani);
    vy=v0*sin(theta_radijani);
}

void Particle::evolve(double dt) {
while (y>=0) {
    vx+=0.;
    vy+=g*dt;
    x+=vx*dt;
    y+=vy*dt;
    t+=dt;
    }
}

double Particle::range(double dt) {
    evolve(dt);
    std::cout << x << std::endl;
    return (x);
}

double Particle::time(double dt) {
    evolve(dt);
    std::cout << t << std::endl;
    return (t);
}