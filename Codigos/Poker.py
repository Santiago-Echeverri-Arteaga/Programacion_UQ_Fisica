class Wordplay:
    def __init__(self, word_list):
        self.word_list = word_list

    def words_with_length(self, length):
        result = []
        for word in self.word_list:
            if len(word) == length:
                result.append(word)
        return result

    def starts_with(self, s):
        result = []
        for word in self.word_list:
            if word.startswith(s):
                result.append(word)
        return result

    def ends_with(self, s):
        result = []
        for word in self.word_list:
            if word.endswith(s):
                result.append(word)
        return result

    def palindromes(self):
        result = []
        for word in self.word_list:
            if word == word[::-1]:
                result.append(word)
        return result

    def only(self, L):
        result = []
        for word in self.word_list:
            if all(letter in L for letter in word):
                result.append(word)
        return result

    def avoids(self, L):
        result = []
        for word in self.word_list:
            if all(letter not in L for letter in word):
                result.append(word)
        return result

word_list = ["hello", "world", "level", "python", "racecar", "programming"]
wordplay = Wordplay(word_list)

print(wordplay.words_with_length(5))  # Words with length 5
print(wordplay.starts_with("p"))  # Words that start with "p"
print(wordplay.ends_with("g"))  # Words that end with "g"
print(wordplay.palindromes())  # Palindromes in the list
print(wordplay.only("lorw"))  # Words that contain only letters in "lorw"
print(wordplay.avoids("xyz"))  # Words that contain none of the letters in "xyz"


############################
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def _get_rank_counts(self):
        rank_counts = {}
        for card in self.cards:
            rank = card.rank
            if rank in rank_counts:
                rank_counts[rank] += 1
            else:
                rank_counts[rank] = 1
        return rank_counts

    def _get_suit_counts(self):
        suit_counts = {}
        for card in self.cards:
            suit = card.suit
            if suit in suit_counts:
                suit_counts[suit] += 1
            else:
                suit_counts[suit] = 1
        return suit_counts

    def has_royal_flush(self):
        rank_counts = self._get_rank_counts()
        if self.has_straight_flush() and '10' in rank_counts:
            return True
        return False

    def has_straight_flush(self):
        suit_counts = self._get_suit_counts()
        if self.has_flush() and self.has_straight():
            return True
        return False

    def has_four_of_a_kind(self):
        rank_counts = self._get_rank_counts()
        for count in rank_counts.values():
            if count == 4:
                return True
        return False

    def has_full_house(self):
        rank_counts = self._get_rank_counts()
        has_two = False
        has_three = False
        for count in rank_counts.values():
            if count == 2:
                has_two = True
            if count == 3:
                has_three = True
        return has_two and has_three

    def has_flush(self):
        suit_counts = self._get_suit_counts()
        for count in suit_counts.values():
            if count >= 5:
                return True
        return False

    def has_straight(self):
        rank_counts = self._get_rank_counts()
        sorted_ranks = sorted(rank_counts.keys())
        if len(sorted_ranks) < 5:
            return False
        for i in range(len(sorted_ranks) - 4):
            if sorted_ranks[i:i+5] == list(range(int(sorted_ranks[i]), int(sorted_ranks[i])+5)):
                return True
        return False

    def has_three_of_a_kind(self):
        rank_counts = self._get_rank_counts()
        for count in rank_counts.values():
            if count == 3:
                return True
        return False

    def has_two_pair(self):
        rank_counts = self._get_rank_counts()
        pair_count = 0
        for count in rank_counts.values():
            if count == 2:
                pair_count += 1
        return pair_count == 2

    def has_pair(self):
        rank_counts = self._get_rank_counts()
        for count in rank_counts.values():
            if count == 2:
                return True
        return False

    def best(self):
        if self.has_royal_flush():
            return "Royal Flush"
        elif self.has_straight_flush():
            return "Straight Flush"
        elif self.has_four_of_a_kind():
            return "Four of a Kind"
        elif self.has_full_house():
            return "Full House"
        elif self.has_flush():
            return "Flush"
        elif self.has_straight():
            return "Straight"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_two_pair():
            return "Two Pair"
        elif self.has_pair():
            return "Pair"
        else:
            return "High Card"
