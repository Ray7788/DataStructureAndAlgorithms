#include<string.h>
#include<stdio.h>

int main(void)
{
    FILE *fp = NULL;
    int ch;
    int emptyLine = 0;
    int numRow = 0; /*calculate number of rows */
    int numCol = 0; /*calculate number of cols */
    int statusSpace = 2;    
    int statusLine = 2;

    fp = fopen("test.txt","r");    

    if(fp == NULL){
        return -1;
    }

    while ((ch = fgetc(fp)) != EOF){
        int last;
        if (ch == '\n' && last == '\n'){
            emptyLine++;
        }
        
        // at the end of each line
        if ((ch == '\n')){
            numRow++;
            statusLine = 1;
            statusSpace = 1;
        }else{
            statusLine = 0;
        }
        
        // test if the char ends with space
        if(ch == ' '){
            statusSpace = 1;
        }else{
            statusSpace = 0;
        }

        // calculate rech row has how many elements
        if(statusSpace == 1){    
            if(statusLine = 0){
                numCol++;
            }else{

            }

        }

       last = ch;

    }
     
    numRow -= emptyLine;
}