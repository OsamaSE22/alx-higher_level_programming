#include <stdio.h>
#include <stdlib.h>
#include "main.h"
node* half_linkedlist(node* head)
{
    if (head == NULL || head->ptr == NULL) {
        return NULL; // can't split if 0 or 1 elements
    }

    int count = 0;
    node* current = head;
    while (current != NULL) {
        count++;
        current = current->ptr;
    }

    int mid_list = count / 2;

    // Move to the node just before the second half
    current = head;
    for (int i = 1; i < mid_list; i++) {
        current = current->ptr;
    }

    // Split the list
    node* head2 = current->ptr; /*start of the second half */
    current->ptr = NULL;

    return head2; // start of the second half
}

node* reverse(node* head)
{
	node* prev;
	node* current;
	node* next;

	prev = NULL;
	current = head;

	while (current != NULL)
	{
		next = current->ptr;
		current->ptr = prev;
		prev = current;
		current = next;
	}
	head = prev;
	return head;

}
int main(void)
{
	node* head;
	node* headrep;
	node* headrep2;
	node* h;
	node* h2;
	node* h3;
	head = malloc(sizeof(node));
	head->a = 1;
	head->ptr = NULL;
	
	add_at_end(head, 2);
	add_at_end(head, 3);
	add_at_end(head, 4);
	add_at_end(head, 5);
	add_at_end(head, 6);
	add_at_end(head, 7);
	add_at_end(head, 8);
	add_at_end(head, 9);
	add_at_end(head, 10);
	
	/*headrep = head;
	h = half_linkedlist(headrep);

	while(h != NULL)
	{
		printf("%d\n", h->a);
		h = h->ptr;
	}*/

	printf("Now, it's the reversed linked list:\n");
	headrep2 = head;
	h2 = half_linkedlist(headrep2);
	h3 = reverse(h2);

	while(h3 != NULL)
        {
                printf("%d\n", h3->a);
                h3 = h3->ptr;
        }
	

	return 0;
}

