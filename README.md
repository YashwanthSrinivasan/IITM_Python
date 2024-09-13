# IITM_Python
A Card Game
Game Setup
Deck Generation: Use a standard deck of 52 cards, consisting of cards in the order '2,3,...,10,J,Q,K,A' across four suits: spades ("S"), hearts ("H"), clubs ("C"), and diamonds ("D"). Cards are denoted using the format "SA", "H3", etc.

Card Values: Each card has a value associated with it, with "2" being the lowest and "A" being the highest.

Players: The game can be played with any number of players (n_players).

Distribution: Distribute the deck almost equally among players. Additional cards should be given to players at lower indices.

Game Play
Rounds
Starting Player:

First round - The player who has the "SA" card starts the first round and plays the smallest card they have.
Other rounds - The player who played the largest card in the previous round or one how collected the cards in the previous round
Direction - The direction of the round always will be going in the increasing order of indices from the starting player.

Playing a Card: Each player must play the smallest card of the same suit as the starting card if they have it.

If all players play cards of the same suit, the played cards are removed from the game, and the player who played the highest card starts the next round.
Playing Without Matching Suit: If a player does not have a card of the suit that started the round, they must play the highest card they have in any suit.

The cards played up to that player are collected by the player who played the highest card.
Ties on highest and lowest cards - Ties on selecting the cards should resolved based on the suit where "S" being the lowest suit and "D" being the highest suit.

Ending the Game
The game ends when there is only one player remaining. And the last player is declared as the loser.
Additional Notes
Highest Card: In each round, the highest card is determined based on the card value (Aces high) within the suit that was played.

Card Collection: When a player collects cards in a round, they add them to their hand.
