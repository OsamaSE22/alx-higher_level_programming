#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t* half_linkedlist(listint_t* head)
{
	listint_t* current;
	listint_t* head2;
	int count;
	int mid_list;
	int i;

	if (head == NULL || head->next == NULL) 
	{
		return NULL; /* can't split if 0 or 1 elementsi*/
	}

	count = 0;
	current = head;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	
	mid_list = count / 2;
	/* Move to the node just before the second half*/
	current = head;
	for (i = 1; i < mid_list; i++)
	{
		current = current->next;
	}

	/* Split the list*/
	head2 = current->next; /*start of the second half */
	current->next = NULL;
	return head2; /* start of the second half*/
}
listint_t* reverse(listint_t* head)
{
	listint_t* prev;
	listint_t* current;
	listint_t* next;

	prev = NULL;
	current = head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	head = prev;
	return head;

}

int is_palindrome(listint_t **head)
{
	listint_t* second_half;
	listint_t* reversed;
	listint_t* p1;
	listint_t* p2;
	second_half = half_linkedlist(*head);
	reversed = reverse(second_half);
	p1 = *head;
	p2 = reversed;
	while(p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);


}
