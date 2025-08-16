#include <stdio.h>
#include <stdlib.h>
#include "main.h"

node* add_at_beg(node** ptr, int data)
{
	node* temp;
	temp = malloc(sizeof(node));
	temp->a = data;
	temp->ptr = *ptr;

	*ptr = temp;

}
