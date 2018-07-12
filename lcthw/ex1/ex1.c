#include <stdio.h>
#include <string.h>

/* This is a comment. */
int main(int argc, char *argv[])
{
    int distance = 100;
    char azeroth[8];
    strcpy(azeroth, "Azeroth");

    // this is also a comment
    printf("You are %d miles away.\n", distance);
    printf("I go to %s right now.\n", azeroth);

    return 0;
}
