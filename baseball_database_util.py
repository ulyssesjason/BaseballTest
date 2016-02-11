from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import baseball_player_model

engine = create_engine('')
operation_session = Session(engine)


def all_batters(year):
    assert isinstance(year, int)

    return operation_session.query(baseball_player_model.Batter).filter(
        baseball_player_model.Batter.Year == year).all()


def batter(year, name):
    assert isinstance(year, int)
    assert isinstance(name, basestring)

    ret = operation_session.query(baseball_player_model.Batter).filter(
        baseball_player_model.Batter.Year == year, baseball_player_model.Batter.Name == name).first()

    if ret is None:
        ret = operation_session.query(baseball_player_model.Batter).filter(
            baseball_player_model.Batter.Year == year,
            baseball_player_model.Batter.Name.ilike('%' + name + '%')).first()

    return ret


def similar_batter_pa(batter, percentage=10):
    """

    :rtype: list of batter object
    """
    assert isinstance(batter, baseball_player_model.Batter)
    assert isinstance(percentage, int)

    return operation_session.query(baseball_player_model.Batter) \
        .filter(baseball_player_model.Batter.Year == batter.Year,
                baseball_player_model.Batter.Name != batter.Name,
                baseball_player_model.Batter.PA <= int(batter.PA * (1.0 + float(percentage) / 100)),
                baseball_player_model.Batter.PA >= int(batter.PA * (1.0 - float(percentage) / 100))).all()
