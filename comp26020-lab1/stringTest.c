#include<string.h>
#include<stdio.h>

int main(void)
{
    FILE *fp = NULL;
    int ch;
    int emptyLine = 0;
    int numRow = 0; /*calculate number of rows exactly */
    int numCol = 0; /*calculate number of cols */
    int numColBuffer = 0;

    int statusSpace = 1; /*check if pointer changes betweeen number and whitespace*/   
    int lc = 1;
    int statusLine = 1; /*check if pointer meets line termination*/

    fp = fopen("test.txt","r");    

    if(fp == NULL){
        return -1;
    }

    while ((ch = fgetc(fp)) != EOF){
        int last;
        if (ch == '\n' && last == '\n'){
            emptyLine = 0;
        }
        
        // at the end of each line
        if ((ch == '\n')){
            numRow++;   // number of rows increases
            statusLine = 1;
        }else{
            statusLine = 0;
        }
        
        // check if pointer meets with space
        if(ch == ' '){
            statusSpace = 1;
        }else{
            statusSpace = 0;
        }

        // calculate rech row has how many elements
        if(statusLine == 0){ 
            if(statusSpace != lc){   
                if(statusSpace = 0){
                    numColBuffer++;
                }
            }
        }else{
            statusSpace = 1;

            if(emptyLine  == 1){    // if meets empty row, 
                numRow--;
            }

            if(numRow == 1){    //  trye value of columns
                numCol = numColBuffer;
            }

            if(numCol != numColBuffer){    // Illegal matrix
                return -1;
            }

            numColBuffer = 0;
        }

       lc = statusSpace;

    }
     
    printf(" rows %d", numRow);
    printf(" columns %d", numCol);
    fclose(fp);
}