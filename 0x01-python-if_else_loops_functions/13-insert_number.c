#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
 *

listint_t *insert_node(listint_t **head, int number)
{
	while (head != NULL)
	{
		printf("%d ", head -> number);
		head = head->next;
	}
}
