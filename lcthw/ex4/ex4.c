#include <stdio.h>

void crash() {
    char *test = NULL;
    int i = 0;

    for(i = 0; i < 10000000000000; i++) {
        printf("%c", test[i]);
    }
            
}

int main(int argc, char *argv[])
{
    int age = 10;
    int height = 72;

    printf("I am %d years old.\n", age);
    printf("I am %d inches tall.\n", height);
    crash();
    crash();
    crash();
    crash();

    return 0;
}
