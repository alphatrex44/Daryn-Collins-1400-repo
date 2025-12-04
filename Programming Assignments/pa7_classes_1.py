from collections import Counter

# ---------------- Parent Class ----------------
class Standard52CardGames:
    def __init__(self, playerCount, jokers_included):
        self.playerCount = playerCount
        self.jokers_included = jokers_included

    def __repr__(self):
        return f"Standard52CardGames(playerCount={self.playerCount}, jokers_included={self.jokers_included})"

    def __str__(self):
        jokers_text = "with jokers included" if self.jokers_included else "without jokers"
        return f"This card game supports {self.playerCount} players, {jokers_text}."

    def playerCountThingy(self):
        if self.playerCount <= 2:
            return "Too few players to form teams."
        for i in range(2, int(self.playerCount ** 0.5) + 1):
            if self.playerCount % i == 0:
                return "Teams can be evenly divided."
        return "Teams cannot be evenly divided."

    def cardsPerPlayer(self):
        deck_size = 54 if self.jokers_included else 52
        if self.playerCount > deck_size:
            return "There are not enough cards to evenly divide among players."
        cards_each = deck_size // self.playerCount
        return f"With {self.playerCount} players, each person would receive {cards_each} cards."


# ---------------- Child Classes ----------------
class ScumGame(Standard52CardGames):
    def __init__(self, playerCount, jokers_included, min_cards_per_player, scumCount):
        super().__init__(playerCount, jokers_included)
        self.min_cards_per_player = min_cards_per_player
        self.scumCount = scumCount

    def __repr__(self):
        return (f"ScumGame(playerCount={self.playerCount}, jokers_included={self.jokers_included}, "
                f"min_cards_per_player={self.min_cards_per_player}, scumCount={self.scumCount})")

    def __str__(self):
        jokers_text = "with jokers included" if self.jokers_included else "without jokers"
        return (f"Scum is played by {self.playerCount} players, {jokers_text}. "
                f"Each player must have at least {self.min_cards_per_player} cards, "
                f"and there are {self.scumCount} scum titles in play.")

    def deck_count(self):
        deck_size = 54 if self.jokers_included else 52
        decks_needed = 1
        while deck_size // self.playerCount < self.min_cards_per_player:
            decks_needed += 1
            deck_size += 54 if self.jokers_included else 52
        return f"You need {decks_needed} decks to meet the minimum cards per player."

    def scum_check(self):
        required_players = self.scumCount * 2
        if required_players > self.playerCount:
            return "Not enough players for the amount of scums."
        return "Valid number of scums."


class Blackjack(Standard52CardGames):
    def __init__(self, playerCount, jokers_included, deck_amount, current_cards):
        super().__init__(playerCount, jokers_included)
        self.deck_amount = deck_amount
        self.current_cards = current_cards

    def __repr__(self):
        return (f"Blackjack(playerCount={self.playerCount}, jokers_included={self.jokers_included}, "
                f"deck_amount={self.deck_amount}, current_cards='{self.current_cards}')")

    def __str__(self):
        jokers_text = "with jokers included" if self.jokers_included else "without jokers"
        return (f"Blackjack is played by {self.playerCount} players, {jokers_text}. "
                f"The shoe contains {self.deck_amount} decks, and the current hand is {self.current_cards}.")

    def hit_odds(self):
        normalize = {
            "jack": "J", "queen": "Q", "king": "K", "ace": "A",
            "j": "J", "q": "Q", "k": "K", "a": "A",
            "joker": "JOKER"
        }
        values = {"J": 10, "Q": 10, "K": 10, "A": 11, "JOKER": 0}
        total, aces = 0, 0
        for card in self.current_cards.lower().split():
            card = normalize.get(card, card)
            if card.isdigit():
                total += int(card)
            elif card in values:
                total += values[card]
                if card == "A":
                    aces += 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        deck_counts = {str(i): 4 for i in range(2, 11)}
        deck_counts.update({"J": 4, "Q": 4, "K": 4, "A": 4})
        if self.jokers_included:
            deck_counts["JOKER"] = 2
        for k in deck_counts:
            deck_counts[k] *= self.deck_amount
        total_cards = sum(deck_counts.values())
        safe_cards = 0
        for card, count in deck_counts.items():
            if card.isdigit():
                new_total = total + int(card)
            elif card in ["J", "Q", "K"]:
                new_total = total + 10
            elif card == "A":
                new_total = total + 11 if total + 11 <= 21 else total + 1
            elif card == "JOKER":
                new_total = total
            else:
                new_total = total
            if new_total <= 21:
                safe_cards += count
        probability = safe_cards / total_cards if total_cards > 0 else 0.0
        return f"Chance of not busting if you hit: {probability:.2%}"

    def cards_left(self):
        deck_size = 54 if self.jokers_included else 52
        total_cards = self.deck_amount * deck_size
        used_cards = self.playerCount * 2
        remaining = total_cards - used_cards
        return f"There are {remaining} cards left in the shoe after dealing."


class PokerGame(Standard52CardGames):
    def __init__(self, playerCount, jokers_included, hand, community):
        super().__init__(playerCount, jokers_included)
        self.hand = self.parse_cards(hand)
        self.community = self.parse_cards(community)

    def __repr__(self):
        return (f"PokerGame(playerCount={self.playerCount}, jokers_included={self.jokers_included}, "
                f"hand={self.hand}, community={self.community})")

    def __str__(self):
        jokers_text = "with jokers included" if self.jokers_included else "without jokers"
        return (f"Poker is played by {self.playerCount} players, {jokers_text}. "
                f"Your hand is {self.hand}, and the community cards are {self.community}.")

    def parse_cards(self, card_string):
        rank_map = {
            "ace": "A", "king": "K", "queen": "Q", "jack": "J", "joker": "JOKER",
            "a": "A", "k": "K", "q": "Q", "j": "J"
        }
        suit_map = {"spades": "♠", "hearts": "♥", "diamonds": "♦", "clubs": "♣",
                    "s": "♠", "h": "♥", "d": "♦", "c": "♣"}
        cards, tokens, i = [], card_string.lower().split(), 0
        while i < len(tokens):
            word = tokens[i]
            if word in rank_map:
                rank = rank_map[word]
                if rank == "JOKER":
                    cards.append(("JOKER", None))
                    i += 1
                    continue
                if i+2 < len(tokens) and tokens[i+1] == "of":
                    suit = suit_map.get(tokens[i+2], "?")
                    cards.append((rank, suit))
                    i += 3
                else:
                    cards.append((rank, None))
                    i += 1
            elif word.isdigit():
                rank = word
                if i+2 < len(tokens) and tokens[i+1] == "of":
                    suit = suit_map.get(tokens[i+2], "?")
                    cards.append((rank, suit))
                    i += 3
                else:
                    cards.append((rank, None))
                    i += 1
            else:
                i += 1
        return cards

    def determine_hand(self):
        all_cards = self.hand + self.community
        ranks = [c[0] for c in all_cards if c[0] != "JOKER"]
        suits = [c[1] for c in all_cards if c[0] != "JOKER"]
        joker_count = sum(1 for c in all_cards if c[0] == "JOKER")

        rank_counts = Counter(ranks)
        suit_counts = Counter([s for s in suits if s is not None])

        # Simplified evaluator with Joker support
        flush_suit, flush_count = (None, 0)
        if suit_counts:
            flush_suit, flush_count = max(suit_counts.items(), key=lambda kv: kv[1])
        can_flush = (flush_count + joker_count) >= 5

        order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        rank_set = set(ranks)

        def can_straight():
            for i in range(len(order) - 4):
                window = order[i:i + 5]
                missing = sum(1 for r in window if r not in rank_set)
                if missing <= joker_count:
                    return True
            return False

        straight_possible = can_straight()

        has_four = any(count + joker_count >= 4 for count in rank_counts.values())
        has_three = any(count + joker_count >= 3 for count in rank_counts.values())
        pairs_possible = sum(1 for count in rank_counts.values() if count >= 2)
        pairs_possible += max(0, min(joker_count, 2))

        if can_flush and straight_possible:
            return "Straight Flush"
        if has_four:
            return "Four of a Kind"
        if has_three and pairs_possible >= 1:
            return "Full House"
        if can_flush:
            return "Flush"
        if straight_possible:
            return "Straight"
        if has_three:
            return "Three of a Kind"
        if pairs_possible >= 2:
            return "Two Pair"
        if pairs_possible >= 1:
            return "Pair"
        return "High Card"

    def chance_higher(self):
        all_cards = self.hand + self.community
        ranks = [c[0] for c in all_cards if c[0] != "JOKER"]
        rank_counts = Counter(ranks)

        jokers_in_hand = sum(1 for c in self.hand if c[0] == "JOKER")
        jokers_in_community = sum(1 for c in self.community if c[0] == "JOKER")
        total_jokers = 2 if self.jokers_included else 0
        jokers_seen = jokers_in_hand + jokers_in_community
        jokers_unseen = max(0, total_jokers - jokers_seen)

        possible_stronger = []
        for rank, count in rank_counts.items():
            remaining = 4 - count
            you_have_rank = any(c[0] == rank for c in self.hand)
            if remaining >= 2 and not you_have_rank:
                possible_stronger.append(f"Opponent could have trips/quads of {rank}")
            elif remaining == 1 and not you_have_rank:
                possible_stronger.append(f"Opponent could have trips of {rank}")

        opponents = max(0, self.playerCount - 1)
        base_factor = 0.12
        if jokers_unseen > 0 and jokers_in_hand == 0:
            base_factor += 0.08 * jokers_unseen

        risk_terms = len(possible_stronger)
        chance = min(1.0, base_factor * risk_terms * opponents)

        return (f"With {self.playerCount} players and community {self.community}, "
                f"possible stronger hands: {possible_stronger}. "
                f"Estimated chance someone beats you: {chance:.2%}.")

# ---------- Helper functions (outside main) ----------
def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            v = int(input(prompt))
            if min_val is not None and v < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and v > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y","yes"): return True
        if ans in ("n","no"): return False
        print("Please enter y/n.")

def create_standard_from_input():
    pc = get_int("Enter player count: ", 1)
    ji = get_yes_no("Include jokers? (y/n): ")
    return Standard52CardGames(pc, ji)

def create_scum_from_input():
    pc = get_int("Enter player count: ", 1)
    ji = get_yes_no("Include jokers? (y/n): ")
    mcpp = get_int("Enter minimum cards per player: ", 1)
    sc = get_int("Enter number of scum titles: ", 0)
    return ScumGame(pc, ji, mcpp, sc)

def create_blackjack_from_input():
    pc = get_int("Enter player count: ", 1)
    ji = get_yes_no("Include jokers? (y/n): ")
    decks = get_int("Enter deck amount: ", 1)
    hand = input("Enter current hand (e.g., 'A of spades 9 of hearts' or '10 J'): ").strip()
    return Blackjack(pc, ji, decks, hand)

def create_poker_from_input():
    pc = get_int("Enter player count: ", 2)
    ji = get_yes_no("Include jokers? (y/n): ")
    hand = input("Enter your hand (e.g., 'A of spades K of hearts'): ").strip()
    community = input("Enter community cards (e.g., '2 of diamonds 7 of clubs 9 of hearts'): ").strip()
    return PokerGame(pc, ji, hand, community)


# Optional samples you can use (edit as you like)
samples = {
    "Standard52CardGames": [
        {"playerCount": 4, "jokers_included": False},
        {"playerCount": 5, "jokers_included": True},
    ],
    "ScumGame": [
        {"playerCount": 6, "jokers_included": False, "min_cards_per_player": 5, "scumCount": 2},
        {"playerCount": 8, "jokers_included": True, "min_cards_per_player": 7, "scumCount": 3},
    ],
    "Blackjack": [
        {"playerCount": 3, "jokers_included": False, "deck_amount": 2, "current_cards": "A 9"},
        {"playerCount": 4, "jokers_included": True, "deck_amount": 4, "current_cards": "10 J"},
    ],
    "PokerGame": [
        {"playerCount": 5, "jokers_included": True, "hand": "2 of hearts 2 of clubs", "community": "3 of diamonds 4 of spades 5 of hearts joker"},
        {"playerCount": 6, "jokers_included": False, "hand": "ace of spades king of hearts", "community": "2 of diamonds 7 of clubs 9 of hearts"},
    ],
}


def main():
    print("Welcome! You have 2 lists of amazing objects.")
    print("Type '1' to build the Standard52CardGames family (File 1).")
    print("Type '2' to build the other parent family (File 2, coming soon).")

    choice = input("Enter your choice (1 or 2): ").strip()
    all_objects = []

    if choice == "1":
        # Create 2 parent instances
        print("\nCreate 2 Standard52CardGames parent instances.")
        for i in range(2):
            use_sample = get_yes_no(f"Use sample for Standard52CardGames instance {i+1}? (y/n): ")
            if use_sample:
                sample = samples["Standard52CardGames"][i]
                parent_obj = Standard52CardGames(sample["playerCount"], sample["jokers_included"])
            else:
                parent_obj = create_standard_from_input()
            all_objects.append(parent_obj)
            show_object_functions(parent_obj)  # print functions immediately

        # Create child instances (each up to 2)
        usage_caps = {"ScumGame": 2, "Blackjack": 2, "PokerGame": 2}
        auto_sample_all = get_yes_no("\nUse samples for ALL child instances? (y/n): ")

        while sum(usage_caps.values()) > 0:
            # Build numbered menu from remaining options
            available = [c for c in usage_caps if usage_caps[c] > 0]
            print("\nRemaining child classes:")
            for idx, name in enumerate(available, start=1):
                print(f"{idx}. {name} ({usage_caps[name]} left)")

            # User chooses by number
            try:
                choice_num = int(input("Choose a child class by number: ").strip())
                if choice_num < 1 or choice_num > len(available):
                    print("Invalid number. Try again.")
                    continue
                chosen = available[choice_num - 1]
            except ValueError:
                print("Please enter a number.")
                continue

            # Sample or manual input
            use_sample = auto_sample_all or get_yes_no(f"Use sample for {chosen}? (y/n): ")
            if use_sample:
                idx = 2 - usage_caps[chosen]
                sample = samples[chosen][idx]
                if chosen == "ScumGame":
                    obj = ScumGame(sample["playerCount"], sample["jokers_included"],
                                   sample["min_cards_per_player"], sample["scumCount"])
                elif chosen == "Blackjack":
                    obj = Blackjack(sample["playerCount"], sample["jokers_included"],
                                    sample["deck_amount"], sample["current_cards"])
                elif chosen == "PokerGame":
                    obj = PokerGame(sample["playerCount"], sample["jokers_included"],
                                    sample["hand"], sample["community"])
            else:
                if chosen == "ScumGame":
                    obj = create_scum_from_input()
                elif chosen == "Blackjack":
                    obj = create_blackjack_from_input()
                elif chosen == "PokerGame":
                    obj = create_poker_from_input()

            all_objects.append(obj)
            usage_caps[chosen] -= 1
            show_object_functions(obj)  # print functions immediately

        # Ask to also build the second parent family
        also_build_second = get_yes_no("\nDo you also want to build the second parent family (2 parent instances + children)? (y/n): ")
        if also_build_second:
            print("Second parent family will be available once pa7_classes_2.py is implemented.")

    elif choice == "2":
        print("\nSecond parent family will be available once pa7_classes_2.py is implemented.")
    else:
        print("Invalid choice. Please run the program again and enter 1 or 2.")
        return

    print("\nFinal list of created objects (parent + children):")
    for obj in all_objects:
        print(obj)

    print("\nProgram complete. Goodbye!")


if __name__ == "__main__":
    main()
