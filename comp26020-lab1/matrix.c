#include "matrix.h"

#include <errno.h> /* for ENOSYS */

int matrix_allocate(matrix_t *m, int rows, int columns) {
    int size = rows * columns;

    m->rows = rows;
    m->columns = columns;
    m->matrix_t = (float **)malloc(sizeof(float *)*m->rows);

    for(int i = 0; i <m->rows; i++){
        m->matrix_t[i] = (float *)malloc(sizeof(float)*m->columns);
    }  

    return m;
}

void matrix_free(matrix_t *m) {
    for(int i = 0; i < m->row; i++){
        free(m->matrix_t[i]);
        m->matrix_t[i] = NULL;
    }

    free(m->matrix_t);
    m->matrix_t = NULL;
}

void matrix_init_zeros(matrix_t *m) {
    for(int i=0; i<m->rows; i++){
        for(int j=0; j<m->columns; j++){
            m->matrix_t[i][j] = 0;
        }
    }
} 

int matrix_init_identity(matrix_t *m){
    if(m->columns != m->rows){
        exit
    }

    int j=0;
    for(int i=0; i<m->rows; i++){
        m->matrix_t[i][j++] = 1;
    }

    return m;
}

void matrix_init_rand(matrix_t *m) {
    for(int i=0; i<m->rows; i++){
        for(int j=0; j<m->columns; j++){
            // Take values between -100 and 100
            int x = rand()%200-99

            m->matrix_t[i][j] = x;
        }
    }
}

int matrix_equal(matrix_t *m1, matrix_t *m2) {
    if(m1.rows != m2.rows || m1.columns != m2.columns){
        return 0;
    }else{
        return 1;
    }
}

int matrix_sum(matrix_t *m1, matrix_t *m2, matrix_t *result) {
    if(matrix_equal == 0){}

    for(int i = 0; i < result.rows; i++){
        for(int j = 0; j < result.columns; j++){
            result.matrix_t[i][j] += m1.matrix[i][j] + m2.matrix[i][j]; 
        }
    }
  
    return result;
}

int matrix_scalar_product(matrix_t *m, int scalar, matrix_t *result) {
    for(int i = 0; i < result.rows; i++){
        for(int j = 0; j < result.columns; j++){    
            result.matrix_t[i][j] = m1.matrix[i*scalar][j*scalar];
        }
    }
    return result;
}

int matrix_transposition(matrix_t *m, matrix_t *result) {
    for(int i = 0; i < m->rows; i++){
        for(int j = 0; j < m->columns; j++){
            m->matrix_t[i][j] = result.matrix_t[j][i];
        }
    }
}

int matrix_product(matrix_t *m1, matrix_t *m2, matrix_t *result) {
    if(m1->columns != m2->rows){
        exit
    }

     for(int i = 0; i < result.rows; i++){
        for(int j = 0; j < result.columns; j++){
            for(int k = 0; k < m1.columns; k++){
                result.matrix_t[i][j] += m1.matrix_t[i][k] * m2.matrix_t[k][j];
            }
        }
    }

    return result;
}

int matrix_dump_file(matrix_t *m, char *output_file) {
    /* implement the function here ... */
    return -ENOSYS;
}

int matrix_allocate_and_init_file(matrix_t *m, char *input_file) {
    /* implement the function here ... */
    return -ENOSYS;
}

void print_matrix(matrix_t m){
    for(int i=0; i<m.rows; i++){
        for(int j=0; j<m.columns; j++){
            printf("%d ",m.matrix_t[i][j]);
        }
        printf("\n");
    }
}
