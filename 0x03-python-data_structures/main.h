#ifndef STR
#define STR
typedef struct node
{
	int a;
	struct node* ptr;
}node;

void add_at_end(node* ptr, int data);
node* add_at_beg(node** ptr, int data);
#endif
