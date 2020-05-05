#include "lists.h"
/**
 * palindromenaitor - Recursive check for a singly linked list to see if it's
 * palindrome or nah
 * @initial: Holds the first value
 * @last: Initially holds also the  first value, later, will hold the last
 * Return: 0 if not, 1 if so
 */
int palindromenaitor(listint_t **initial, listint_t *last)
{
	if (!last)
		return (1);
	else if (palindromenaitor(initial, last->next) && (*initial)->n == last->n)
	{
		*initial = (*initial)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: Holds the head
 * Return: o if not, 1 if so
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (palindromenaitor(head, *head));
}
