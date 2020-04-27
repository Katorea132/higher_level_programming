#include "lists.h"
/**
 * check_cycle - finds the loop
 * @list: Holds the head
 * Return: 1 if loop 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *past, *future;

	for (past = future = list; past && future;)
	{
		past = past->next;
		future = future->next->next;
		if (past == future)
			return (1);
	}
	return (0);
}
