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

	lili = malloc(sizeof(listint_t));
	if (lili == 0)
		return (0);
	lili->n = number;
	if (*head == 0 || tmp->n >= number)
	{
		lili->next = tmp;
		*head = lili;
		return (lili);
	}
	for (; tmp->next&& tmp->next-> n <= number; tmp = tmp->next)
		;
	lili->next = tmp->next;
	tmp->next = lili;
	return (lili);
}
