#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if there is a cyclic linked list
 * @list: the address of the first node in the linked list
 *
 * Return: 1 if it's Cyclic or 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;

	do {
		ptr = ptr->next;
		if (ptr == NULL)
		{
			return (0);
			/*break;*/
		}
		else
		{
			continue;
		}
	} while (ptr != list);
	return (1);
}
