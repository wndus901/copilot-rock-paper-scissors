import main as game

def test_main():
    # Test case 1: User chooses rock, computer chooses scissors
    # Expected output: You win!
    assert game.main('rock', 'scissors') == 'You win!'

    # Test case 2: User chooses paper, computer chooses rock
    # Expected output: You win!
    assert game.main('paper', 'rock') == 'You win!'

    # Test case 3: User chooses scissors, computer chooses paper
    # Expected output: You win!
    assert game.main('scissors', 'paper') == 'You win!'

    # Test case 4: User chooses spock, computer chooses lizard
    # Expected output: Computer wins!
    assert game.main('spock', 'lizard') == 'Computer wins!'

    # Test case 5: User chooses lizard, computer chooses spock
    # Expected output: You win!
    assert game.main('lizard', 'spock') == 'You win!'

    # Test case 6: User chooses rock, computer chooses rock
    # Expected output: It's a tie!
    assert game.main('rock', 'rock') == "It's a tie!"

    # Test case 7: User chooses paper, computer chooses paper
    # Expected output: It's a tie!
    assert game.main('paper', 'paper') == "It's a tie!"

    # Test case 8: User chooses scissors, computer chooses scissors
    # Expected output: It's a tie!
    assert game.main('scissors', 'scissors') == "It's a tie!"

    # Test case 9: User chooses spock, computer chooses spock
    # Expected output: It's a tie!
    assert game.main('spock', 'spock') == "It's a tie!"

    # Test case 10: User chooses lizard, computer chooses lizard
    # Expected output: It's a tie!
    assert game.main('lizard', 'lizard') == "It's a tie!"

    print("All test cases passed!")

# Run the test cases
test_main()