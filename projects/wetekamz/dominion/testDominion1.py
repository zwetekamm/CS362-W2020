# -*- coding: utf-8 -*-
"""
Created on 1/19/20

@author: Zachary Wetekamm
"""

import Dominion
import testUtility

def main():
    #Get player names
    player_names = ["Annie","*Ben","*Carla"]

    # Number of curses and victory cards
    if len(player_names)>2:
        nV=12
    else:
        nV=8
    nC = -10 + 10 * len(player_names)

    # Costruct the Player objects
    players = testUtility.createPlayers(player_names)

    # Create the box
    box = testUtility.getBoxes(nV)

    # Establish supply with 10 cards
    supply = testUtility.establishSupply(box, nC, nV, player_names)

    # Play Dominion
    testUtility.play(supply, players)
    
    # Show final score
    testUtility.finalScore(players)

main()