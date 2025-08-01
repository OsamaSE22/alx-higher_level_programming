#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *dptr;
    listint_t *nptr = malloc(sizeof(listint_t));
    if (nptr == NULL)
        return NULL;

    nptr->n = number;
    nptr->next = NULL;

    if (*head == NULL || number < (*head)->n)
    {
        nptr->next = *head;
        *head = nptr;
        return nptr;
    }

    dptr = *head;
    while (dptr->next != NULL && dptr->next->n < number)
    {
        dptr = dptr->next;
    }

    nptr->next = dptr->next;
    dptr->next = nptr;
    return nptr;
}

