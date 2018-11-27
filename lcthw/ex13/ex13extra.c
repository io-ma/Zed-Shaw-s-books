#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;

    // let's make our own array of strings
    char *states[] = {
        "California", "Oregon",
        "Washington", "Texas\0"
    };

    argv[1] = states[1];
    states[1] = argv[2];

    for (i = 1; i < argc; i++) {
        printf("arg %d: %s\n", i, argv[i]);
    }

    int num_states = 4;

    for (i = 0; i < num_states; i++) {
        printf("state %d: %s\n", i, states[i]);
    }

    return 0;
}
