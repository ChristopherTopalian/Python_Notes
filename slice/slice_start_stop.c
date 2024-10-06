// slice_start_stop.c

#include <stdio.h>

int main()
{
    // declare an array of modifiable strings
    char people[][20] = { "Melissa", "Jennifer", "Tabitha", "Jane" };

    // start and stop indices
    int start = 0;
    int stop = 2;

    // loop from start to stop, printing each element
    for (int i = start; i < stop; i++)
    {
        printf("%s\n", people[i]);
    }

    return 0;
}

//--//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian
// https://sites.google.com/view/CollegeOfScripting

