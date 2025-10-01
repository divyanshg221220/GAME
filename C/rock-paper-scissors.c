// ROCK PAPER SCISSORS
#include <stdio.h>
#include <stdlib.h>
int player_score=0,computer_score=0;
void welcome_message()
{
    printf("Welcome to Rock, Paper, Scissors!\n");
}

int player_turn()
{
    int player_move=0;
    scanf("%d", &player_move);
    return player_move;
}

int computer_turn()
{
    int computer_move=rand()%3+1;
    printf("Computer chose: %d\n", computer_move);
    return computer_move;
}

void choice()
{
    printf("Choose your move:\n");
    printf("1. Rock\n");
    printf("2. Paper\n");
    printf("3. Scissors\n");
    printf("Enter the number of your choice: ");
}

int will_play_again()
{
    char play_again;
    printf("Do you want to play again? (y/n): ");
    scanf(" %c", &play_again);
    if (play_again=='y'||play_again=='Y')
        return 1;
    else
        return 0;
}

int scores(int status)
{
    if (status==1)
        player_score++;
    else if (status==0)
        computer_score++;
    return player_score,computer_score;
}

int main(int argc, char const *argv[])
{
    welcome_message();
    do
    {
        choice();
        int player_move=player_turn();
        if (player_move<1||player_move>3)
        {
            printf("Invalid move! Please choose 1, 2, or 3.\n");
            continue;
        }
        int computer_move=computer_turn();
        if (player_move==computer_move)
        {
            printf("It's a tie!\n");
        }
        else if ((player_move==1&&computer_move==3)||(player_move==2&&computer_move==1)||(player_move==3&&computer_move==2))
        {
            printf("Player wins!\n");
            scores(1);
        }
        else if ((player_move==1&&computer_move==2)||(player_move==2&&computer_move==3)||(player_move==3&&computer_move==1))
        {
            printf("Computer wins!\n");
            scores(0);
        }
    } while (will_play_again()==1);
    printf("Final Scores - Player: %d, Computer: %d\n", player_score, computer_score);
    if (player_score>computer_score)
        printf("Overall Winner: Player!\n");
    else if (computer_score>player_score)
        printf("Overall Winner: Computer!\n");
    else
        printf("Overall Result: It's a tie!\n");
    return 0;
}