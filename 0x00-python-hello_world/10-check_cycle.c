#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a singly linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{

	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = list->next;
	slow = list;


	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
			return (0);
	}
	return (0);
}
