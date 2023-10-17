from project import display_king_status
from project import check_game
from project import feed_status

def main():
    test_display_king_status()
    test_check_game()
    test_feed_status()


def test_display_king_status():
    assert display_king_status(2) == "The King is very hungry!"
    assert display_king_status(8) == "The King is nearly satisfied!"
    assert display_king_status(15) == "Done"
    assert display_king_status(0) == "Over"
def test_check_game():
    assert check_game("Done") == "Win"
    assert check_game("Over") == "Loss"
    assert check_game("none") is None
def test_feed_status():
    assert feed_status(2) == "My royal taste buds require a Juicy Meal!"
    assert feed_status(5) == "Right now I desire to taste something with strong flavor."
    assert feed_status(8) == "Prepare for me something sugary I need energy!"
