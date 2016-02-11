import baseball_database_util
import operator


def near_manhatten_batters(batter):
    players = baseball_database_util.similar_batter_pa(batter, 10)

    batter_distance = {}

    for player in players:
        batter_distance[player] = batter.no_condition_manhatten_distance(player)

    return sorted(batter_distance, key=batter_distance.get)


def near_euclidean_batters(batter):
    players = baseball_database_util.similar_batter_pa(batter, 10)

    batter_distance = {}

    for player in players:
        batter_distance[player] = batter.no_condition_euclidean_distance(player)

    return sorted(batter_distance, key=batter_distance.get)


if __name__ == '__main__':

    batter1 = baseball_database_util.batter(2015, 'bryce')

    print batter1.Name
    print batter1.wRC_Plus
    print batter1.Dol
    print batter1.Year
    print batter1.Age
    print "---------------\n"
    manhatten_player = near_euclidean_batters(batter1)[0]

    print manhatten_player.Name
    print manhatten_player.wRC_Plus
    print manhatten_player.Dol
    print "---------------\n"
    print reduce(lambda x, y: x + y,
                 map(lambda x: x.wRC_Plus, near_euclidean_batters(batter1)[:10])) / 10
    print "---------------\n"

