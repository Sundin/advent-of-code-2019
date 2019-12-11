from asteroid_detector import *

def test_number_of_asteroids():
    assert number_of_asteroids("""
    .#..#
    .....
    #####
    ....#
    ...##
    """) == 10
    assert number_of_asteroids("""
    .#..#
    .....
    #####
    """) == 7

def test_get_all_asteroids():
    assert get_all_asteroids("""
    .#..#
    .....
    ##...
    """) == [(1,0),(4,0),(0,2),(1,2)]

def test_count_asteroids_in_sight():
    assert count_asteroids_in_sight("""
    #..
    #..
    #..
    """, (0,0)) == 1
    # assert count_asteroids_in_sight("""
    # .#..#
    # .....
    # #####
    # ....#
    # ...##
    # """, (3,4)) == 8

def test_has_line_of_sight():
    map = """
    ###
    ##.
    #.#
    """
    assert has_line_of_sight(map, (0,0), (0,2)) == False
    assert has_line_of_sight(map, (0,0), (0,1)) == True
    assert has_line_of_sight(map, (0,0), (1,0)) == True
    assert has_line_of_sight(map, (0,0), (2,0)) == False

    assert has_line_of_sight(map, (2,0), (0,0)) == False
    assert has_line_of_sight(map, (0,1), (0,0)) == True
    assert has_line_of_sight(map, (1,0), (0,0)) == True
    assert has_line_of_sight(map, (2,0), (0,0)) == False

    assert has_line_of_sight(map, (0,0), (1, 1)) == True
    assert has_line_of_sight(map, (0,0), (2, 2)) == False
    assert has_line_of_sight(map, (1,1), (0,0)) == True
    assert has_line_of_sight(map, (2,2), (0,0)) == False
