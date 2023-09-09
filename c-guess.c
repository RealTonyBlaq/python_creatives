#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int main(void)
{
	int attempts = 0;
	int guess, min = 1, max = 100;
	int randomm;

	srand(time(NULL));
	randomm = ((rand() % (max - min + 1)) + 1);
	while (1)
	{
		printf("Enter your guess: ");
		scanf("%d", &guess);
		attempts++;
		if (guess > randomm)
			printf("Too high. Try again!\n");
		else if (guess < randomm)
			printf("Too low. Try again!\n");
		else if (guess == randomm)
		{
			printf("Congratulations! You won the game after %d trials\n", attempts);
			break;
		}
		else if (isalpha(guess))
			printf("Please enter a valid number\n");
	}
	return (0);
}