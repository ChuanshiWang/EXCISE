import random
import time

# Define the cards with their attributes
card_deck = [
    {"Name": "Diablo", "Health": 100, "Attack": 90, "Defense": 60},
    {"Name": "Medusa", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Jester", "Health": 120, "Attack": 60, "Defense": 90},
    {"Name": "Troll", "Health": 150, "Attack": 40, "Defense": 94},
    {"Name": "Specter", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Mist", "Health": 100, "Attack": 75, "Defense": 65},
    {"Name": "Savage", "Health": 100, "Attack": 90, "Defense": 50},
    {"Name": "Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    {"Name": "Wimp", "Health": 110, "Attack": 40, "Defense": 85},
    {"Name": "Sorcerer", "Health": 100, "Attack": 70, "Defense": 55}
]


# Function to simulate an attack
def attack(player_card, opponent_card):
    print(f"\n{player_card['Name']} attacks {opponent_card['Name']}!")
    if player_card['Attack'] > opponent_card['Defense']:
        damage = player_card['Attack'] - opponent_card['Defense']
        opponent_card['Defense'] = 0
        opponent_card['Health'] -= damage
        print(
            f"{player_card['Name']} did {damage} damage! {opponent_card['Name']} now has {opponent_card['Health']} health.")
    else:
        opponent_card['Defense'] -= player_card['Attack']
        print(
            f"{player_card['Name']} weakened {opponent_card['Name']}'s defense! {opponent_card['Name']} now has {opponent_card['Defense']} defense.")
    if opponent_card['Health'] <= 0:
        print(f"{opponent_card['Name']} has been defeated!")
        return True
    return False


# Function to run a round of battle
def battle_round(player_deck, opponent_deck):
    # Opponent picks a random card
    opponent_card = random.choice(opponent_deck)
    print("\nOpponent's card:")
    print(
        f"Name: {opponent_card['Name']}, Health: {opponent_card['Health']}, Attack: {opponent_card['Attack']}, Defense: {opponent_card['Defense']}")

    # Display player's deck
    print("\nYour cards:")
    for idx, card in enumerate(player_deck):
        print(
            f"{idx + 1}. Name: {card['Name']}, Health: {card['Health']}, Attack: {card['Attack']}, Defense: {card['Defense']}")

    # Player selects a card
    choice = int(input("\nChoose a card to fight (1-5): ")) - 1
    player_card = player_deck[choice]

    # Player's turn to attack
    if attack(player_card, opponent_card):
        opponent_deck.remove(opponent_card)

    time.sleep(3)  # Pause for effect

    # If opponent still has cards, it's their turn
    if len(opponent_deck) > 0:
        print("\nOpponent's turn...")
        if attack(opponent_card, player_card):
            player_deck.remove(player_card)

    time.sleep(3)  # Pause before the next round


# Main game loop
def start_game():
    deck_size = 5
    player_deck = random.sample(card_deck, deck_size)
    opponent_deck = random.sample(card_deck, deck_size)

    print("\nNew game begins!")
    while len(player_deck) > 0 and len(opponent_deck) > 0:
        battle_round(player_deck, opponent_deck)

    if len(opponent_deck) == 0:
        print("\nYou win!")
    else:
        print("\nOpponent wins!")


# Start the game
start_game()