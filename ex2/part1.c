
#include<stdio.h>   // scanf, getchar
#include <iostream>
#include <ctype.h>// toupper  tolower
#include <cstring>
#include <string.h>
#include <string>


//Step 1A
int main()
{
    printf("Please Type in");

    char str[100];
    scanf("%s",str);

    int n, i;
    int to_up = 0, to_low = 0;
   
    //计算长度
    n = strlen(str);

    for (i = 0; i < n; i++)
    {
        if (c >= 'a' && c <= 'z')
        {
            //to upper case
            c = toupper(c);
            fprintf(fp_out, "%c", c);
            to_up++;
        }
        else if (c >= 'A' && c <= 'Z')
        {
            //to lower case
            c = tolower(c);
            fprintf(fp_out, "   %c", c);
            to_low++;
        }else

        str[i] = getchar();
        str[i] = toupper(str[i]); // 小写转大写
    }

    // 大写转小写字母（只能是对字母有效）
   
    printf("%s", str);
    printf("Read d% characters in total, %d converted to upper-case, d to lower-case", n, to_up, to_low);

    return 0;
}