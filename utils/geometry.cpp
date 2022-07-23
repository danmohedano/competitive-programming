#include <bits/stdc++.h>

using namespace std;

pair<double, double> equidistant_point(vector<pair<double, double>> p); // Equidistant point from 3 points
double angle_of_vectors(pair<double, double> a, pair<double, double> b); // Angle defined by two vectors
double area_polygon(int n_sides, double radius); // Area of polygon 

pair<double, double> equidistant_point(vector<pair<double, double>> p){
    pair<double, double> solution;
    double D;

    D = 2 * (p[0].first * (p[1].second - p[2].second) + 
             p[1].first * (p[2].second - p[0].second) +
             p[2].first * (p[0].second - p[1].second));

    solution.first = ((pow(p[0].first, 2) + pow(p[0].second, 2)) * (p[1].second - p[2].second) +
                      (pow(p[1].first, 2) + pow(p[1].second, 2)) * (p[2].second - p[0].second) +
                      (pow(p[2].first, 2) + pow(p[2].second, 2)) * (p[0].second - p[1].second)) / D;
    solution.second = ((pow(p[0].first, 2) + pow(p[0].second, 2)) * (p[2].first - p[1].first) +
                       (pow(p[1].first, 2) + pow(p[1].second, 2)) * (p[0].first - p[2].first) +
                       (pow(p[2].first, 2) + pow(p[2].second, 2)) * (p[1].first - p[0].first)) / D;

    return solution;
}

double angle_of_vectors(pair<double, double> a, pair<double, double> b){
    double dot = a.first * b.first + a.second * b.second;
    double dem = sqrt(pow(a.first, 2) + pow(a.second, 2)) * sqrt(pow(b.first, 2) + pow(b.second, 2));
    if (dot < 0) dot *= -1.;
    return acos(dot / dem);
}

double area_polygon(int n_sides, double radius){
    return pow(radius, 2) * n_sides  * 0.5 * sin(2 * M_PI / n_sides);
}

