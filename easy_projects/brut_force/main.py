import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open("google-10000-english.txt", "r") as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f"Common match: {match} (#{i}"

def brut_force(
        word: str,
        length: int,
        digits:bool = False,
        symbols:bool = False
) -> str | None:
    chars: str = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    attemps: int = 0
    for guess in itertools.product(chars, repeat=length):
        attemps += 1
        guess: str = "".join(guess)
        if guess == word:
            return f"{word} was hacked in {attemps:,} attempts"

def main():
    print("searching")
    password: str = "exi"
    start_time: float = time.perf_counter()
    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3,6):
            if cracked := brut_force(password, length=i, digits=True, symbols=True):
                print(cracked)
                break
            else:
                print("there was no match...")
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), "seconds")


if __name__ == "__main__":
    main()