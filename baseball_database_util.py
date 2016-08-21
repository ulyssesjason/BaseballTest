from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import baseball_player_model
import baseball_util_constant

import scipy.spatial

engine = create_engine('postgresql://localhost:5432/test')
operation_session = Session(engine)


def wrc_plus_eval(wrc_plus):
    assert isinstance(wrc_plus, int)

    if wrc_plus >= 160:
        return 'Excellent'
    elif wrc_plus >= 140:
        return 'Great'
    elif wrc_plus >= 115:
        return 'Above Average'
    elif wrc_plus > 100:
        return 'Average'
    elif wrc_plus > 80:
        return 'Below Average'
    elif wrc_plus > 75:
        return 'Poor'
    elif wrc_plus > 60:
        return 'Awful'
    else:
        return 'Dead end'


def all_batters(year):
    assert isinstance(year, int)

    return operation_session.query(baseball_player_model.Batter).filter(
        baseball_player_model.Batter.Year == year).all()


def qualified_batters(year):
    assert isinstance(year, int)

    return operation_session.query(baseball_player_model.Batter) \
        .filter(baseball_player_model.Batter.Year == year,
                baseball_player_model.Batter.PA > baseball_util_constant.QUALIFIED_AT_BATT_COUNT) \
        .all()


def all_batters_except_id(year, id):
    assert isinstance(year, int)
    assert isinstance(id, int)

    return operation_session.query(baseball_player_model.Batter).filter(
        baseball_player_model.Batter.Year == year, baseball_player_model.Batter.playerid != id).all()


def batter(year, **player):
    assert isinstance(year, int)

    if player.has_key('name'):
        name = player['name']
        ret = operation_session.query(baseball_player_model.Batter).filter(
            baseball_player_model.Batter.Year == year, baseball_player_model.Batter.Name == name).first()

        if ret is None:
            ret = operation_session.query(baseball_player_model.Batter).filter(
                baseball_player_model.Batter.Year == year,
                baseball_player_model.Batter.Name.ilike('%' + name + '%')).first()
    elif player.has_key('id'):
        id = player['id']
        ret = operation_session.query(baseball_player_model.Batter).filter(
            baseball_player_model.Batter.Year == year, baseball_player_model.Batter.playerid == id).first()
    else:
        ret = None

    return ret


def next_year_batter(target):
    assert isinstance(target, baseball_player_model.Batter)

    next_batter = batter(target.Year + 1, id=target.playerid)

    if next_batter is not None and next_batter.PA >= baseball_util_constant.QUALIFIED_AT_BATT_COUNT:
        return next_batter
    else:
        return None


def normalized_batter(year, playerid):
    assert isinstance(year, int)
    assert isinstance(playerid, int)

    return operation_session.query(baseball_player_model.Normalized_Batter).filter(
        baseball_player_model.Normalized_Batter.playerid == playerid,
        baseball_player_model.Normalized_Batter.Year == year).first()


def all_normalized_batter_except_id(year, id):
    return operation_session.query(baseball_player_model.Normalized_Batter).filter(
        baseball_player_model.Normalized_Batter.Year == year,
        baseball_player_model.Normalized_Batter.playerid != id).all()


def similar_batter_pa(batter, percentage=baseball_util_constant.COMPARE_PERCENTAGE):
    """

    :rtype: list of batter object
    """
    assert isinstance(batter, baseball_player_model.Batter)
    assert isinstance(percentage, int)

    return operation_session.query(baseball_player_model.Batter) \
        .filter(
        baseball_player_model.Batter.PA <= int(batter.PA * (1.0 + float(percentage) / 100)),
        baseball_player_model.Batter.PA >= int(batter.PA * (1.0 - float(percentage) / 100))).all()


def manhattan_dict(target_dict, comp_dict):
    assert isinstance(target_dict, dict)
    assert isinstance(comp_dict, dict)

    assert len(target_dict) == len(comp_dict)

    return scipy.spatial.distance.cityblock(target_dict.values(), comp_dict.values())


def manhattan_batted_ball(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return manhattan_dict(batter.batted_ball(), comp_batter.batted_ball())


def manhattan_plate_discipline(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return manhattan_dict(batter.plate_discipline(), comp_batter.plate_discipline())


def manhattan_predict(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return manhattan_dict(batter.predictable(), comp_batter.predictable())


def manhattan_performance(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return manhattan_dict(batter.performance(), comp_batter.performance())


def euclidean_dict(target_dict, comp_dict):
    assert isinstance(target_dict, dict)
    assert isinstance(comp_dict, dict)

    assert len(target_dict) == len(comp_dict)

    return scipy.spatial.distance.euclidean(target_dict.values(), comp_dict.values())


def euclidean_batted_ball(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return euclidean_dict(batter.batted_ball(), comp_batter.batted_ball())


def euclidean_plate_discipline(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return euclidean_dict(batter.plate_discipline(), comp_batter.plate_discipline())


def euclidean_predict(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return euclidean_dict(batter.predictable(), comp_batter.predictable())


def euclidean_performance(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return euclidean_dict(batter.performance(), comp_batter.performance())


def cosine_dict(target_dict, comp_dict):
    assert isinstance(target_dict, dict)
    assert isinstance(comp_dict, dict)

    assert len(target_dict) == len(comp_dict)

    return scipy.spatial.distance.cosine(target_dict.values(), comp_dict.values())


def cosine_performance(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return cosine_dict(batter.performance(), comp_batter.performance())


def cosine_predict(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return cosine_dict(batter.predictable(), comp_batter.predictable())


def cosine_standard(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return cosine_dict(batter.standard(), comp_batter.standard())


def cosine_woba(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return cosine_dict(batter.woba_related(), comp_batter.woba_related())


def euclidean_woba(batter, comp_batter):
    assert isinstance(comp_batter, baseball_player_model.AbstractBatter)
    return euclidean_dict(batter.woba_related(), comp_batter.woba_related())


def closet_player_inlist(players, player, function):
    assert hasattr(function, '__call__')

    # sorted[0] is this batter himself
    return sorted(players, key=lambda x: function(x, player))[1]


def sort_player_inlist(players, player, function):
    assert hasattr(function, '__call__')

    return sorted(players, key=lambda x: function(x, player))[1:]


# KNN Algorithm: find K Nearest batter, weighted and calculate the WRC+

def knn_players(batter, function=manhattan_predict, k=baseball_util_constant.NEAREST_NEIGHBOUR_COUNT):
    assert isinstance(batter, baseball_player_model.Batter)
    assert hasattr(function, '__call__')

    similar_batters = similar_batter_pa(batter)
    return sort_player_inlist(similar_batters, batter, function)[:k]


def knn_wrc_plus(batter, function=manhattan_predict, k=baseball_util_constant.NEAREST_NEIGHBOUR_COUNT):
    assert isinstance(batter, baseball_player_model.Batter)
    assert hasattr(function, '__call__')

    similar_batters = similar_batter_pa(batter)
    sorted_player = sort_player_inlist(similar_batters, batter, function)[:k]

    bucket = {}
    distance_sum = 0

    for player in sorted_player:
        distance_reciprocal = 1 / function(batter, player)
        bucket[player] = distance_reciprocal
        distance_sum += distance_reciprocal

    k_bucket_normalize = {k: (v / distance_sum) for k, v in bucket.items()}
    print sorted_player
    print bucket
    print k_bucket_normalize
    return reduce(lambda x, key: x + key.wRC_Plus * k_bucket_normalize[key], k_bucket_normalize, 0)


def knn_predict_wrc_plus(batter, function=manhattan_predict, k=baseball_util_constant.NEAREST_NEIGHBOUR_COUNT):
    assert isinstance(batter, baseball_player_model.Batter)
    assert hasattr(function, '__call__')

    similar_batters = similar_batter_pa(batter)
    sorted_player = sort_player_inlist(similar_batters, batter, function)[:k]

    valid_player_list = []
    bucket = {}
    distance_sum = 0

    for player in sorted_player:
        next_year_player = next_year_batter(player)
        if next_year_player is not None:
            # put next year's batter and its distance' reciprocal into bucket and normalize
            valid_player_list.append(next_year_player)
            distance_reciprocal = 1 / function(batter, next_year_player)
            bucket[next_year_player] = distance_reciprocal
            distance_sum += distance_reciprocal

    # TODO: handle while bucket's size is smaller than k

    # get first k valid next-year-player
    k_bucket = {key: bucket[key] for key in valid_player_list[:k]}

    print sorted_player

    print valid_player_list

    print k_bucket

    k_bucket_normalize = {k: (v / distance_sum) for k, v in k_bucket.items()}

    print k_bucket_normalize

    return reduce(lambda x, key: x + key.wRC_Plus * k_bucket_normalize[key], k_bucket_normalize, 0)
