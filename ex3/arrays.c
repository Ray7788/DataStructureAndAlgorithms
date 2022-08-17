#include <stdio.h>
#include "arrays.h"

/* declare your struct for a person here */
typedef struct person {
  char* name;
  int age;
} person;


static void insert(/* array parameter */person *people[], char *name, int age, int *nextinsert) 
{
    /* put name and age into the next free place in the array parameter here */
    people[*nextinsert]->name = malloc(sizeof(struct person));

    if(!people[*nextinsert])
    {
        printf("Faild: Not enough memory\n");
        exit(-1);
    }

    // strcpy(people[*nextinsert]->name, name);
    people[*nextinsert]->age = age;
    people[*nextinsert]->age = age;

    /* modify nextfreeplace here */
    (*nextinsert)++;
}

int main(int argc, char **argv) 
{
    int nextinsert = 0;
    /* declare the people array here */
    person *people[HOW_MANY];

    for (int i = 0; i < HOW_MANY ;i++) 
    {
        insert(people, names[i], ages[i], nextinsert[i]);
    }

    /* print the people array here*/
        for(int j = 0; j < HOW_MANY; j++)
    {
        printf("%d: %s is %d\n", j, people[j]->name, people[j]->age);
    }


  return 0;
}