# Name: David Ng
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("D", "C")
    practice_graph.add_edge("D", "F")
    practice_graph.add_edge("D", "E")
    practice_graph.add_edge("F", "C")

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()

    rj.add_edge('Nurse', 'Juliet')
    rj.add_edge('Juliet', 'Tybalt')
    rj.add_edge('Juliet', 'Capulet')
    rj.add_edge('Juliet', 'Friar Laurence')
    rj.add_edge('Juliet', 'Romeo')
    rj.add_edge('Tybalt', 'Capulet')
    rj.add_edge('Capulet', 'Escalus')
    rj.add_edge('Capulet', 'Paris')
    rj.add_edge('Romeo', 'Friar Laurence')
    rj.add_edge('Romeo', 'Benvolio')
    rj.add_edge('Romeo', 'Montague')
    rj.add_edge('Romeo', 'Mercutio')
    rj.add_edge('Montague', 'Benvolio')
    rj.add_edge('Montague', 'Escalus')
    rj.add_edge('Escalus', 'Mercutio')
    rj.add_edge('Escalus', 'Paris')
    rj.add_edge('Paris', 'Mercutio')

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    common = set()

    for people in graph.neighbors(user):
        for friend in graph.neighbors(people):
            if friend != user and friend not in graph.neighbors(user):
                common.add(friend)

    return common


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2 in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    return set(graph.neighbors(user1)) & set(graph.neighbors(user2))


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    mutual_dict = {}
    for people in graph.neighbors(user):
        for mutuals in graph.neighbors(people):
            if mutuals != user and mutuals not in graph.neighbors(user):
                if mutuals not in mutual_dict.keys():
                    mutual_dict[mutuals] = 1
                else:
                    mutual_dict[mutuals] = mutual_dict[mutuals] + 1
    return mutual_dict


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    map = []
    map_sort = sorted(map_with_number_vals.items())
    sorted_list = sorted(map_sort, key=itemgetter(1), reverse=True)
    for keys in sorted_list:
        map.append(keys[0])
    return map


def rec_number_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    friend_recommendation = number_of_common_friends_map(graph, user)
    sorted_friend_list = number_map_to_sorted_list(friend_recommendation)
    return sorted_friend_list


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    map_dict = {}
    common_friend = number_of_common_friends_map(graph, user).keys()
    for friend in common_friend:
        friends_list = common_friends(graph, user, friend)
        score = 0
        friend_count = 0
        for number in friends_list:
            friend_count = (len(list(graph.neighbors(number))))
            score += 1/friend_count
        map_dict[friend] = score
    return map_dict


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    friend_recommendation = influence_map(graph, user)
    sorted_recommendation = number_map_to_sorted_list(friend_recommendation)
    return sorted_recommendation


###
#  Problem 5
###

def get_facebook_graph():
    """Builds and returns the facebook graph
    """

    # (Your Problem 5 code goes here.)
    facebook = nx.Graph()
    facebook_file = open("facebook-links.txt")
    facebook_read = facebook_file.readlines()
    for numbers in facebook_read:
        nums = numbers.split()
        facebook.add_edge(int(nums[0]), int(nums[1]))

    facebook_file.close
    return facebook


def main():
    practice_graph = get_practice_graph()

    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.

    draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()
    different_recommendation = []
    same_recommendation = []
    for people in rj.nodes:
        common_friends_recommendation = rec_number_common_friends(rj, people)
        influence_recommendation = recommend_by_influence(rj, people)
        if common_friends_recommendation != influence_recommendation:
            different_recommendation.append(people)
        else:
            same_recommendation.append(people)

    print("Unchanged Recommendations: ", sorted(same_recommendation))
    print("Changed Recommendations: ", sorted(different_recommendation))
    # (Your Problem 4 code goes here.)

    ###
    #  Problem 5
    ###

    # (Your Problem 5 code goes here. Make sure to call get_facebook_graph.)
    fb = get_facebook_graph()
    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    nodes = fb.nodes()
    friend_dict = {}
    dict_sort = sorted(nodes, key=int)
    for i in dict_sort:
        if i % 1000 == 0:
            recommended_list = rec_number_common_friends(fb, i)
            friend_dict[i] = recommended_list[:10]
            print(str(i) + "(by num_common_friends): " + str
                  (recommended_list[:10]))
    # (Your Problem 6 code goes here.)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    influence_dict = {}
    for i in dict_sort:
        if i % 1000 == 0:
            influence_list = recommend_by_influence(fb, i)
            influence_dict[i] = influence_list[:10]
            print(str(i) + "(by influence): " + str(influence_list[:10]))
    # (Your Problem 7 code goes here.)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    same_rec = []
    different_rec = []
    for keys in friend_dict:
        if friend_dict[keys] != influence_dict[keys]:
            different_rec.append(keys)
        if friend_dict[keys] == influence_dict[keys]:
            same_rec.append(keys)
    print("Same: " + str(len(same_rec)))
    print("Different: " + str(len(different_rec)))


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
