import baseball_database_util

if __name__ == '__main__':
    batter1 = baseball_database_util.batter(2015, name='Dexter Fowler')

    print batter1

    # similar_batters = baseball_database_util.similar_batter_pa(batter1, percentage=10)

    # batter2 = baseball_database_util.closet_player_inlist(similar_batters, batter1, baseball_database_util.manhattan_predict)
    #
    # batter_list = baseball_database_util.knn_players(batter1)
    #
    # print batter_list
    #
    # print batter2

    print baseball_database_util.knn_predict_wrc_plus(batter1)

    # all_qualified_batters = baseball_database_util.qualified_batters(2015)
    #
    # correct = 0
    #
    # for batter in all_qualified_batters:
    #
    #     if batter is not None:
    #
    #         actual_wrc = batter.wRC_Plus
    #
    #         norm_batter = baseball_database_util.normalized_batter(2015, batter.playerid)
    #         closest_norm_batter = baseball_database_util.closet_player_inlist(
    #             baseball_database_util.all_normalized_batter_except_id(2015, batter.playerid), norm_batter,
    #             baseball_database_util.manhattan_batted_ball)
    #
    #         closest_batter = baseball_database_util.batter(2015, id=closest_norm_batter.playerid)
    #
    #         if closest_batter is not None:
    #
    #             predicted_wrc = closest_batter.wRC_Plus
    #
    #             print batter.Name + ' predict wrc+ ' + str(predicted_wrc)
    #             print batter.Name + ' actual wrc+ ' + str(actual_wrc)
    #
    #             if baseball_database_util.wrc_plus_eval(actual_wrc) == baseball_database_util.wrc_plus_eval(
    #                     predicted_wrc):
    #                 correct += 1
    #                 print batter.Name + ' is Correct on being ' + str(baseball_database_util.wrc_plus_eval(actual_wrc))
    #
    # print correct
    # print len(all_qualified_batters)