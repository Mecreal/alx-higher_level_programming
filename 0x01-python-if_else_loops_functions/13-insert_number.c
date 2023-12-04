#include "lists.h"



/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to pointer of the first node of listint_t list
 * @number: Integer to be included in the new node
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	new_node->next = current;
	prev->next = new_node;

	return (new_node);
}
