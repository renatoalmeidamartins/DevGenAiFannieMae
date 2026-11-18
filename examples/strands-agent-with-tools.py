from strands import Agent, tool
from strands.vended_tools import write, web_fetch

@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


agent = Agent(tools=[letter_counter, write, web_fetch])
agent('How many letter R\'s are in the word "strawberry"? Write the answer to c:\\tmp\\answer.txt.')
agent('Fetch the names and prices for the top 3 stocks being traded in NASDAQ')