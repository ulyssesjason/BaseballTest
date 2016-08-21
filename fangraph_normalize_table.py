from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import baseball_player_model
from ConfigParser import SafeConfigParser

import numpy


def calculate_normalized_batter(year, operation_session):
    # create median and deviate player

    median_batter = baseball_player_model.Normalized_Batter()

    deviate_batter = baseball_player_model.Normalized_Batter()

    all_batters = operation_session.query(baseball_player_model.Batter).filter(
        baseball_player_model.Batter.Year == year,
        baseball_player_model.Batter.PA > 500).all()

    for attribute in dir(median_batter):
        if not attribute.startswith(
                '_') and attribute != 'playerid' and attribute != 'Year' and attribute != 'metadata' and attribute != 'type':
            origin = operation_session.query(baseball_player_model.Batter.__dict__[attribute]).filter(
                baseball_player_model.Batter.Year == year,
                baseball_player_model.Batter.PA > 500).all()
            list = []
            for o in origin:
                list.extend(o)

            try:
                median = numpy.median(list)

                size = len(list)
                sum = 0
                for number in list:
                    sum += abs(number - median)

                deviate = (sum / size)
                print deviate
                median_batter.__dict__[attribute] = median
                deviate_batter.__dict__[attribute] = deviate
            except Exception:
                pass

    median_batter.playerid = -1
    median_batter.Year = year
    deviate_batter.playerid = -2
    deviate_batter.Year = year

    operation_session.add(median_batter)
    operation_session.add(deviate_batter)

    for batter in all_batters:
        norm_batter = baseball_player_model.Normalized_Batter(playerid=batter.playerid, Year=batter.Year)

        for attribute in dir(norm_batter):
            if not attribute.startswith(
                    '_') and attribute != 'playerid' and attribute != 'Year' and attribute != 'metadata' and attribute != 'type':
                # adjusted z-score: (original value - median) / (absolute standard deviation)
                try:
                    norm_batter.__dict__[attribute] = (batter.__dict__[attribute] - median_batter.__dict__[attribute]) / \
                                                      deviate_batter.__dict__[attribute]
                except:
                    pass

        operation_session.add(norm_batter)


if __name__ == '__main__':
    parser = SafeConfigParser()
    parser.read('config')

    url = parser.get('database', 'url')

    engine = create_engine(url)

    session = sessionmaker()
    session.configure(bind=engine)

    operation_session = Session(engine)

    operation_session.query(baseball_player_model.Normalized_Batter).delete()

    for year in range(1871, 2016):
        calculate_normalized_batter(year, operation_session)

    operation_session.commit()
    operation_session.close()
