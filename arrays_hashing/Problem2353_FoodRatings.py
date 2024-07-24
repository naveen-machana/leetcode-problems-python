import collections
from typing import List

from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodCuisines = {}
        self.foodRatings = {}
        self.cuisinesFoods = collections.defaultdict(SortedSet)
        for i in range(len(cuisines)):
            self.cuisinesFoods[cuisines[i]].add((-ratings[i], foods[i]))
            self.foodCuisines[foods[i]] = cuisines[i]
            self.foodRatings[foods[i]] = ratings[i]
    def changeRating(self, food: str, newRating: int) -> None:
        c = self.foodCuisines[food]
        r = self.foodRatings[food]
        self.cuisinesFoods[c].remove(-r, food)
        self.cuisinesFoods[c].add(-newRating, food)
    def highestRated(self, cuisine: str) -> str:
        return self.cuisinesFoods[cuisine][0][1]