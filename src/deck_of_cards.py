from requests import Session

class DeckOfCards:
    def __init__(self) -> None:
        self.api = "http://deckofcardsapi.com/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def shuffle_cards(self, deck_count: int = 1) -> dict:
        return self._get(f"/deck/new/shuffle/?deck_count={deck_count}")

    def draw_card(
            self, deck_id: str = "new", count: int = 1) -> dict:
        return self._get(f"/deck/{deck_id}/draw/?count={count}")

    def reshuffle_cards(
            self, deck_id: str, remaining: bool = False) -> dict:
        params = {"remaining": remaining} if remaining else {}
        return self._get(f"/deck/{deck_id}/shuffle", params)

    def brand_new_deck(self, jokers_enabled: bool = False) -> dict:
        return self._get(f"/deck/new?jokers_enabled={jokers_enabled}")

    def partial_deck(
            self,
            cards: str = "AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH") -> dict:
        return self._get(f"/deck/new/shuffle/?cards={cards}")

    def add_to_piles(
            self,
            deck_id: str,
            pile_name: str,
            cards: str = "AS,2S") -> dict:
        return self._get(
            f"/deck/{deck_id}/pile/{pile_name}/add?cards={cards}")

    def shuffle_piles(self, deck_id: str, pile_name: str) -> dict:
        return self._get(f"/deck/{deck_id}/pile/{pile_name}/shuffle")

    def listing_cards_in_piles(
            self, deck_id: str, pile_name: str) -> dict:
        return self._get(f"/deck/{deck_id}/pile/{pile_name}/list")

    def draw_from_cards(
            self,
            deck_id: str,
            pile_name: str,
            cards: str = "AS,2S") -> dict:
        return self._get(
            f"/deck/{deck_id}/pile/{pile_name}/draw?cards={cards}")

    def draw_from_count(
            self,
            deck_id: str,
            pile_name: str,
            count: int) -> dict:
        return self._get(
            f"/deck/{deck_id}/pile/{pile_name}/draw?count={count}")

    def draw_bottom(self, deck_id: str) -> dict:
        return self._get(f"/deck/{deck_id}/draw/bottom")

    def draw_random(self, deck_id: str) -> dict:
        return self._get(f"/deck/{deck_id}/draw/random")

    def return_cards(self, deck_id: str) -> dict:
        return self._get(f"/deck/{deck_id}/return")
