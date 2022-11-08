#include "matrix.h"
#include<stdio.h>
#include<stdlib.h>
#include <errno.h> /* for ENOSYS */

int matrix_allocate(matrix_t *m, int rows, int columns) {
    // int size = rows * columns;

    m->rows = rows;
    m->columns = columns;
    // allocate memory for its content
    m->content = (int**)malloc(rows * sizeof(int*));

    if(m->content == NULL){return -1;}

    for(int i = 0; i <m->rows; i++){
        m->content[i] = (int*)malloc(sizeof(int) * m->columns);
    }  

    return 0;
}

void matrix_free(matrix_t *m) {
    for(int i = 0; i < m->rows; i++){
        free(m->content[i]);
        m->content[i] = NULL;
    }

    free(m->content);
    m->content = NULL;
}

void matrix_init_rand(matrix_t *m) {
    for(int i=0; i<m->rows; i++){
        for(int j=0; j<m->columns; j++){
            // Take values between -100 and 100   m--n rand()%200-99
            int x = rand()%(100-(-100)+1)+(-100);

            m->content[i][j] = x;
        }
    }
}

void matrix_init_zeros(matrix_t *m) {
    for(int i=0; i<m->rows; i++){
        for(int j=0; j<m->columns; j++){
            m->content[i][j] = 0;
        }
    }
} 

int matrix_init_identity(matrix_t *m){
    if(m->columns == m->rows){
        int j=0;
        for(int i=0; i<m->rows; i++){
            m->content[i][j++] = 1;
        }

        return 0;
    }else{
        return -1;
    }
}

int matrix_equal(matrix_t *m1, matrix_t *m2) {
    if(m1->rows != m2->rows || m1->columns != m2->columns){
        return 0;
    }

    if(m1->rows == m2->rows && m1->columns == m2->columns){
        for(int i=0; i<m1->rows; i++){
            for(int j=0; j<m1->columns; j++){
                if (m1->content[i][j] != m2->content[i][j]){
                    return 0;
                    
                }
            }
        }
        
        return 1;;
    }
}

int matrix_sum(matrix_t *m1, matrix_t *m2, matrix_t *result) {
    if(m1->rows != m2->rows && m1->columns != m2->columns){
        return -1;
    }

    matrix_allocate(result,m1->rows, m1->columns);
    if(m1->rows == m2->rows && m1->columns == m2->columns){
        for(int i = 0; i < result->rows; i++){
            for(int j = 0; j < result->columns; j++){
                result->content[i][j] += m1->content[i][j] + m2->content[i][j]; 
            }
        }

        return 0;
    }
}

int matrix_scalar_product(matrix_t *m, int scalar, matrix_t *result) {
    matrix_allocate(result,m->rows, m->columns);

    for(int i = 0; i < result->rows; i++){
        for(int j = 0; j < result->columns; j++){    
            result->content[i][j] = m->content[i][j] *scalar ;
        }
    }
    return 0;
}

int matrix_transposition(matrix_t *m, matrix_t *result) {
    matrix_allocate(result,m->columns, m->rows);

    for(int i = 0; i < m->rows; i++){
        for(int j = 0; j < m->columns; j++){
            result->content[j][i] = m->content[i][j];
        }
    }
    return 0;
}

int matrix_product(matrix_t *m1, matrix_t *m2, matrix_t *result) {
    if(m1->columns != m2->rows){
        return -1;
    }

    matrix_allocate(result, m1->rows, m2->columns);

        for(int i = 0; i < result->rows; i++){
            for(int j = 0; j < result->columns; j++){
                for(int k = 0; k < m1->columns; k++){
                    result->content[i][j] += m1->content[i][k] * m2->content[k][j];
                }
            }
        }
        return 0;

}

int matrix_dump_file(matrix_t *m, char *output_file) {
    /* implement the function here ... */
    return -ENOSYS;
}

int matrix_allocate_and_init_file(matrix_t *m, char *input_file) {
    FILE *fp = NULL;
    fp = fopen(input_file,"r");    
    fgets("");

    return -ENOSYS;
}

// displaying a matrix on the standard output
void print_matrix(matrix_t m){
    for(int i=0; i<m.rows; i++){
        for(int j=0; j<m.columns; j++){
            printf("%d ",m.content[i][j]);
        }
        printf("\n");
    }
}

