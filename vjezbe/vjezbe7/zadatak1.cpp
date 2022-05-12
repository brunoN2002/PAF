#include <iostream>
#include <math.h>

class Particle {

    public:
    double v, x, y, vx, vy, theta;
    double t=0;
    double g=-9.81;

    Particle(double v0, double theta0, double x0, double y0){
        theta=theta0;
        double theta_radijani;
        theta_radijani=theta0*3.141592/180;
        v=v0;
        x=x0;
        y=y0;
        vx=v0*cos(theta_radijani);
        vy=v0*sin(theta_radijani);
    }

    double range(double dt) {
        evolve(dt);
        std::cout << x << std::endl;
        return (x);
    }

    double time(double dt) {
        evolve(dt);
        std::cout << t << std::endl;
        return (t);
    }


    private:
    void evolve(double dt){
        while (y>=0) {
            vx+=0.;
            vy+=g*dt;
            x+=vx*dt;
            y+=vy*dt;
            t+=dt;
    }
    }
};

int main() {
    Particle p1(10, 45, 0, 0);
    p1.range(0.1);
    p1.time(0.1);
    return(0);
}