from time import sleep
from random import randint

def animation_nums(pod: list) -> list:
    """
    Input: A list of random integers with len of n,
    Output: A list of FORMATTED random integers.
    """
    pod = pod.split()
    new_string = []
    max_num = len(max(pod, key=len))
    for iterations in range(max_num):
        string = ''
        for i in range(len(pod)):
            try:
                string += pod[i][iterations].ljust(2)
            except IndexError:
                string += ' '.ljust(2)
        new_string.append(string.rstrip())
    return new_string

def animation(nums: list, sleept: int=2) -> None:
    """
    Input: List of animation_nums
    Output: None, just prints out the nice numbers.
    """
    for animate in nums:
        print(animate)
        sleep(sleept/10)

def random_integers(length: int, min: int=3, max: int=25) -> str:
    """
    Input: An int of the length the list want to be.
    Output: A list of UNFORMATTED random integers.
    """
    pod = ''
    for i in range(length):
        scope_length = randint(min, max)
        for p in range(scope_length):
            pod += str(randint(0, 9))
        pod += ' '
    return pod

def animate(num: int) -> None:
    """
    The function to actually animate....
    Input: An int of the length the range want to be.
    Output: The animation.
    """
    for i in range(num):
        sum_num = randint(7, 31)
        animation(animation_nums(random_integers(sum_num)))
        print()
