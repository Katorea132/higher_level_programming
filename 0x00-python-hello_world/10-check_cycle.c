#include "lists.h"
/**
 * check_cycle - finds if there's a loop on a singly linked list
 * @list: Holds the head
 * Return: 1 if loop 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *past, *future;

	if (list == 0)
		return (0);

	for (past = future = list; past && future;)
	{
		past = past->next;
		future = future->next->next;
		if (past == future)
			return (1);
	}
	return (0);
}
