from requests import Session

class DeckOfCards:
    def __init__(self) -> None:
        self.api = "http://deckofcardsapi.com/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
    
    def shuffle_cards(self, deck_count: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/deck/new/shuffle/?deck_count={deck_count}").json()
    
    def draw_card(
            self,
            deck_id: str = "new",
            count: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/draw/?count={count}").json()
    
    def reshuffle_cards(
            self,
            deck_id: str,
            remaining: bool = False) -> dict:
        params = {"remaining": remaining} if remaining else {}
        return self.session.get(
            f"{self.api}/deck/{deck_id}/shuffle", params=params).json()
    
    def brand_new_deck(
            self,
            jokers_enabled: bool = False) -> dict:
        return self.session.get(
            f"{self.api}/deck/new?jokers_enabled={jokers_enabled}").json()
    
    def partial_deck(
            self,
            cards: str = "AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH") -> dict:
        return self.session.get(
            f"{self.api}/deck/new/shuffle/?cards={cards}").json()
    
    def add_to_piles(
            self,
            deck_id: str,
            pile_name: str,
            cards: str = "AS,2S") -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/pile/{pile_name}/add?cards={cards}").json()
    
    def shuffle_piles(
            self,
            deck_id: str,
            pile_name: str) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/pile/{pile_name}/shuffle").json()
    
    def listing_cards_in_piles(
            self,
            deck_id: str,
            pile_name: str) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/pile/{pile_name}/list").json()
    
    def draw_from_cards(
            self,
            deck_id: str,
            pile_name: str,
            cards: str = "AS,2S") -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/pile/{pile_name}/draw?cards={cards}").json()
    
    def draw_from_count(
            self,
            deck_id: str,
            pile_name: str,
            count: int) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/pile/{pile_name}/draw?count={count}").json()
            
    def draw_bottom(self, deck_id: str) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/draw/bottom").json()
    
    def draw_random(self, deck_id: str) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/draw/random").json()
    
    def return_cards(self, deck_id: str) -> dict:
        return self.session.get(
            f"{self.api}/deck/{deck_id}/return").json()
