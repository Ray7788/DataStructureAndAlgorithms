#include <stdio.h>
#include <stdlib.h> // exit malloc free atoi abs
#include <math.h>   // lround

float c2f(float c);
float f2c(float f);


int main(int argc, char* argv[]) {
    //The wrong number of parameters have been supplied
    if (argc != 3) {
        return 1;
    }

    //Failed to supply either - f or -c as the first option
    if (strcmp(argv[1], "-f") != 0 && strcmp(argv[1], "-c") != 0)
    {
        return 2;
    }

    //Malformed number in second parameter
    float tem, tem_out;
    int temp = 0;

    if (strspn(argv[2], ".-0123456789") != strlen(argv[2]))
    {
        return 3;
    }
    if (sscanf(argv[2], "%f", &tem) <= 0)
    {
        return 3;
    }

    //Temperatures below absolute zero
    if (strcmp(argv[1], "-f") == 0){

        if (tem > -459.67){
            //convert f to c
            tem_out = f2c(tem);
            printf("%.2f°C = %.2f°F\n", tem_out, tem);
        }
        else{
            return 4;
        }
    } else if (strcmp(argv[1], "-c") == 0) {
        if (tem > -273.15)
        {
            //convert c to f
            tem_out = c2f(tem);
            printf("%.2f°C = %.2f°F\n", tem, tem_out);
        } else{
            return 4;
        }
    }


    return 0;
}

   
//convert function: f=9*c/5+32
float c2f(float c){
    return 9 * c / 5 + 32;
}

float f2c(float f){
    return (f - 32) * 5 / 9;
}
