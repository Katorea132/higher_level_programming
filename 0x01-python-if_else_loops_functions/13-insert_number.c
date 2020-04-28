#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a linked list in a sorted position
 * @head: HOlds the head
 * @number: Holds the value to add
 * Return: pointer to the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *lili;
	listint_t *tmp = *head;

	if (head == 0)
		return (0);
	lili = malloc(sizeof(listint_t *));
	if (lili == 0)
		return (0);
	lili->n = number;
	lili->next = 0;
	if (tmp->n >= number)
	{
		lili->next = tmp;
		*head = lili;
		return (lili);
	}
	for (; tmp; tmp = tmp->next)
	{
		if (tmp->n < number && tmp->next && tmp->next->n >= number)
		{
			lili->next = tmp->next;
			tmp->next = lili;
			return (lili);
		}
		else if (!tmp->next)
		{
			tmp->next = lili;
			return (lili);
		}
	}
	return (0);
}
