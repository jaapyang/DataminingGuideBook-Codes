#! /usr/bin/env python3
# -*-coding:utf-8-*-

"""
计算曼哈顿距离
"""


def manhattan(rating1, rating2):
    """
    calculate the manhattan distance,
    Both rating1 and rating2 are dictionaries of the form
    {'the strokes':3.9,'Slightly Stoopid':4.5}
    """
    distance = 0
    common_ratings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            common_ratings = True
    if common_ratings:
        return distance
    else:
        return -1


def calculate_nearest_neighbor(username, users):
    """计算与指定用户距离最近的列表"""
    distances = []
    self_data = users[username]
    for user in users:
        if user != username:
            distance = manhattan(users[user], self_data)
            distances.append(distance)
    distances.sort()
    return distances
