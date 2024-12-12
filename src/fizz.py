"""
This is a FizzBuzzWhizz problem.
"""

import dataclasses
class Fizz:
    """
    FizzBuzzWhizz
    1. 3 -> Fizz
    2. 5 -> Buzz
    3. 7 -> Whizz
    4. 3, 5, 7 -> FizzBuzzWhizz
    5. 3, 5 -> FizzBuzz
    6. 3, 7 -> FizzWhizz
    7. 5, 7 -> BuzzWhizz

    1. 1
    2. 1 2
    3. 1 2 Fizz
    5. 1 2 Fizz 4 Buzz
    15. 1 2 Fizz 4 Buzz Fizz Whizz 8 Fizz Buzz 11 Fizz 13 Whizz FizzBuzz
    """
    def __init__(self):
        self.mapping = Mapping().mapping

    def convert(self, idx: int)->str:
        """
        Convert the number to FizzBuzzWhizz

        Args:
            idx: int

        Returns:
            str
        """
        ans = []
        for i in range(1, idx + 1):
            current = ""
            for key, value in self.mapping.items():
                if i % key == 0:
                    current += value

            if current:
                ans.append(current)
            else:
                ans.append(str(i))
        return self.make_return_value(ans)

    def make_return_value(self, ans_list: list)->str:
        """
        Make the return value

        Args:
            ans_list: list of str

        Returns:
            str
        """
        return " ".join(ans_list)

@dataclasses.dataclass
class Mapping:
    """
    Mapping of FizzBuzzWhizz
    """
    def __init__(self):
        self.mapping = {
            3: "Fizz",
            5: "Buzz",
            7: "Whizz"}


if __name__ == "__main__":
    fizz = Fizz()
    print(fizz.convert(15))
