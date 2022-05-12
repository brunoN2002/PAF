class Particle {

    private:
    void evolve(double dt);

    public:
    double v, x, y, vx, vy, theta;
    double t=0;
    double g=-9.81;
    Particle(double v0, double theta0, double x0, double y0);
    double range(double dt);
    double time(double dt);
};