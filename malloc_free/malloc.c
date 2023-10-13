#include "main.h"

/**
* *new_int_array - Allocates Memory for integer array and initializes it
* @size: Size of array
* @num: Number to initialize array with
* 
* Return: New array of ints
*/

int *new_int_array(int size, int num)
{
    // Allocate memory for an integer array and initialize it
    int *int_array; // What's the difference between *int_array and int_array[]?
    int i;

    int_array = malloc(sizeof(int) * size); // Trivia Question (size of int?)

    for (i = 0; i < size; i++)
    {
        int_array[i] = num;
    }

    for (i = 0; i < size; i++)
    {
        printf("new_array[%d]: %d\n", i, int_array[i]);
    }

    free(int_array);
}

/**
* *new_string_array - Allocates Memory for array of strings and initializes it
* @size: Size of array
* @word: Word to initialize each index of string array
* 
* Return: New array of strings
*/

char **new_string_array(int size, char *word) // Add double pointer explanation/illustration 
{
    // Allocate memory for an array of strings, as well as each index of
    // the array, then initialize each index
    char **str_array; // Quick review double pointers (pointer to pointer)
    int i;           // what does dereferencing do with double pointers?

    str_array = malloc(sizeof(char *) * (size + 1)); // Why the + 1?

    for (i = 0; i < size; i++)
    {
        str_array[i] = malloc(sizeof(char) * (strlen(word) + 1)); // Audience Collaboration
        strcpy(str_array[i], word); // Why strcpy() instead of str_array[i] = word?
    }
    str_array[i] = NULL; // What's this for?

    for (i = 0; i < size; i++)
    {
        printf("str_array[%d]: %s\n", i, str_array[i]);
    }

    for (i = 0; i < size; i++)
    {
        free(str_array[i]); // Why do we need to free indices when we didn't
    }                       // have to with the int_array?
    free(str_array);
}
