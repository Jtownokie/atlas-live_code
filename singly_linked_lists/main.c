#include <stdio.h>
#include <stdlib.h>

/**
 * struct node_s - singly linked list
 * @data: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct node_s {
    int data;
    struct node_s* next;
} Node;

/**
 * insert_at_front - Function that inserts a node at the beginning of a list
 * @head: Pointer to Head Pointer
 * @data: Integer Data for Node
 * 
 * Return: Always Void
*/
void insert_at_front(Node **head, int data) {
    Node *new_node = NULL;

    new_node = malloc(sizeof(Node));
    if (new_node == NULL) {
        return;
    }
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

/**
 * main - Main Function
 * 
 * Return: Always 0
*/
int main(void) {

    Node *head = NULL;
    Node *current = NULL;
    Node *node_freer = NULL;
    int i = 0;

    insert_at_front(&head, 42);
    insert_at_front(&head, 22);
    insert_at_front(&head, 51);

    current = head;
    while (current != NULL) {
        i++;
        printf("Data: [%d] | Node: [%d]\n", current->data, i);
        current = current->next;
    }

    while (head != NULL) {
        node_freer = head;
        head = head->next;
        free(node_freer);
    }

    return (0);
}
