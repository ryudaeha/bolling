import unittest
from unittest import skip

from game import Game


class TestBowlingGame(unittest.TestCase):
    def test_모두0점획득(self):
        game = Game()
        for i in range(20):
            game.roll(0)

        self.assertEqual(0, game.score())

    @skip
    def test_각1점씩획득(self):
        game = Game()
        for i in range(20):
            game.roll(1)

        self.assertEqual(20, game.score())

    @skip
    def test_스페어(self):
        game = Game()
        game.roll(5)
        game.roll(5)  # spare
        game.roll(3)
        for i in range(3, 20):
            game.roll(0)

        self.assertEqual(16, game.score())
    @skip
    def test_스트라이크(self):
        game = Game()
        for i in range(12):
            game.roll(10)

        self.assertEqual(300, game.score())
    @skip
    def test_샘플게임(self):
        game = Game()
        game.roll(1)
        game.roll(4)
        game.roll(4)
        game.roll(5)
        game.roll(6)
        game.roll(4)
        game.roll(5)
        game.roll(5)
        game.roll(10)
        game.roll(0)
        game.roll(1)
        game.roll(7)
        game.roll(3)
        game.roll(6)
        game.roll(4)
        game.roll(10)
        game.roll(2)
        game.roll(8)
        game.roll(6)

        self.assertEqual(133, game.score())