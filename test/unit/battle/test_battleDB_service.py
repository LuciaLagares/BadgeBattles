from app.services.battleDB_service import get_all_battles_details
from unittest.mock import patch


def test_get_all_battles_details():
    with patch("app.repositories.battle_repo.get_all_battles_id") as mocked_function:
        mocked_function.return_value = {
            "id" : 1,
            "attacker_pokemon" : 6,
            "defender_pokemon" : 3,
            "result" : 1,
            "date" : "13/01/2026",
            "attacker_id" : 1,
            "defender_id" : 2
        }
        resultado=get_all_battles_details()
    
     
