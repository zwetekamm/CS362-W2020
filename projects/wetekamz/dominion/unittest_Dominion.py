##
##  Zachary Wetekamm
##  2/2/20
##  CS362 - Assignment 3a
##

from unittest import TestCase
import unittest
import testUtility
import Dominion


class TestAction_card(TestCase):
    def test_init(self):
        # test case that each variable is initialized
        ac = Dominion.Action_card('TESTCARD',0,1,2,3,4)
        self.assertEqual('TESTCARD', ac.name)
        self.assertEqual(0, ac.cost)
        self.assertEqual(1, ac.actions)
        self.assertEqual(2, ac.cards)
        self.assertEqual(3, ac.buys)
        self.assertEqual(4, ac.coins)


    def test_use(self):
        ac = Dominion.Action_card('TESTCARD',0,0,0,0,0)
        player = Dominion.Player('Annie')
        trash = []

        # test case that after use method, action card is moved from hand to played
        player.hand.append(ac)
        ac.use(player,trash)
        self.assertIn(ac, player.played)
        self.assertNotIn(ac, player.hand)


    def test_augment(self):
        ac = Dominion.Action_card('TESTCARD',1,1,1,1,1)
        player = Dominion.Player('Annie')
        player.actions = player.buys = player.purse = 1
        pActions = player.actions
        pBuys = player.buys
        pPurse = player.purse

        # test case to show player values have changed and have player has drawn cards
        ac.augment(player)
        self.assertNotEqual(pActions-1, player.actions)
        self.assertNotEqual(pBuys-1, player.buys)
        self.assertNotEqual(pPurse-1, player.purse)
    


class TestPlayer(TestCase):
    def test_stack(self):
        player = Dominion.Player('Annie')
        self.assertEqual(10, len(player.stack()))

        player.deck = [Dominion.Copper()] * 10 + [Dominion.Estate()] * 3
        self.assertEqual(18, len(player.stack()))


    def test_action_balance(self):
        player = Dominion.Player('Annie')
        # base deck has nothing to balance, expect 0
        self.assertEqual(0, player.action_balance())

        # add one action card to change the balance variable, which will change return value to non-zero
        player.deck = [Dominion.Copper()] * 7 + [Dominion.Estate()] * 3 + [Dominion.Thief()] * 1
        self.assertIsNot(0, player.action_balance())


    


    def test_draw(self):
        player = Dominion.Player('Annie')
        self.assertEqual(5, len(player.deck)) # starting deck size
        self.assertEqual(5, len(player.hand)) # starting hand size

        # test case for draw() method; increase hand and decrease deck
        player.draw()
        self.assertEqual(4, len(player.deck)) # deck size decreases 1
        self.assertEqual(6, len(player.hand)) # hand size increases 1

        # test case if deck is length 0, will replenish it with discard pile
        player.discard = [Dominion.Copper()] * 7 + [Dominion.Estate()] * 3
        player.deck = []
        player.draw()
        self.assertEqual(9, len(player.deck))

  
    def test_cardsummary(self):
        player = Dominion.Player('Annie')
        
        # test integer values for each element in summary dictionary
        summary = player.cardsummary()
        for item in summary:
            self.assertLessEqual(0, summary[item]) # no negative values here


class testGameOver(TestCase):
    def test_gameover(self):
        supply = testUtility.establishSupply(testUtility.getBoxes(1),1,1,['Annie','Bob'])
        
        # test case that end of function reached; returns False
        self.assertFalse(Dominion.gameover(supply))

        # test case to remove Province card, so first if branch returns True
        supply["Province"].pop()
        self.assertTrue(Dominion.gameover(supply))

        # test case to force the out variable to increase above 3, which returns True
        supply = testUtility.establishSupply(testUtility.getBoxes(1),1,1,['Annie','Bob'])
        for stack in supply:
            supply[stack] = []
        self.assertTrue(Dominion.gameover(supply))
        

if __name__ == '__main__':
    unittest.main()