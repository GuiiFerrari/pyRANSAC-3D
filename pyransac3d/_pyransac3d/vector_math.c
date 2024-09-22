
#include "vector_math.h"
double norm(double *vector)
{
    return (double)sqrt((double)pow(vector[0], 2.) + (double)pow(vector[1], 2.) + (double)pow(vector[2], 2.));
}

void cross_prod(double *left_vector, double *right_vector, double *target_vector)
{
    target_vector[0] = (double)left_vector[1] * right_vector[2] - left_vector[2] * right_vector[1];
    target_vector[1] = (double)-(left_vector[0] * right_vector[2] - left_vector[2] * right_vector[0]);
    target_vector[2] = (double)left_vector[0] * right_vector[1] - left_vector[1] * right_vector[0];
}

void substract_vectors(double *left_vector, double *right_vector, double *target_vector)
{
    for (int i = 0; i < 3; i++)
    {
        target_vector[i] = left_vector[i] - right_vector[i];
    }
}

void normalize_vector(double *vector)
{
    double vector_norm = norm(vector);
    for (int i = 0; i < 3; i++)
    {
        vector[i] = (double)vector[i] / vector_norm;
    }
}