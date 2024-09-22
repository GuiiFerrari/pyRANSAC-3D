#ifndef VECTOR_MATH_H
#define VECTOR_MATH_H

#define M_PI 3.14159265358979323846

double norm(double *vector);

void cross_prod(double *left_vector, double *right_vector, double *target_vector);

void substract_vectors(double *left_vector, double *right_vector, double *target_vector);

void normalize_vector(double *vector);

#endif