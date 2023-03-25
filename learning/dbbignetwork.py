from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from pandas import DataFrame, Series
from datetime import datetime
from numpy import ndarray


# def get_readings():
#     reader = Reader()
#
#     times = [t_id for date, time, t_id in reader.get_commons(OBS, READ)]
#
#     powers = reader.powers()
#
#     out = []
#
#     for t in times:
#         wind = reader.even(t, OBS)
#         power = powers[t]
#
#         out.append([wind, power])
#
#     return out


# def get_predictions(start: datetime, end: datetime):
#     reader = Reader()
#
#     times = []
#     winds = []
#
#     for date, time, t_id in reader.get_commons(PRD):
#         time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
#
#         if start < time < end:
#             times.append(time)
#             winds.append(reader.even(t_id, PRD))
#
#     return times, winds


def create_dataframe(wind_data: list) -> tuple:
    frame = DataFrame(wind_data)
    mean = frame.mean().dropna()
    headers = dict(mean)

    wf = frame[headers].fillna(mean)

    scale = StandardScaler()
    scale.fit(wf)

    return scale.transform(wf), mean, scale


def filled_dataframe(wind_data: list, mean: Series, scale: StandardScaler) -> ndarray:
    headers = dict(mean)

    wf = DataFrame(wind_data)
    wf = wf[headers]
    wf = wf.fillna(mean)
    wf = wf.dropna(axis=1)

    return scale.transform(wf)


def train(data, nodes, activation, solver="lbfgs", alpha=0.0001):
    wind, power = zip(*data)

    wf, mean, s = create_dataframe(wind)

    mod = MLPRegressor(nodes, activation, solver=solver, alpha=alpha, max_iter=20000, random_state=0)
    mod.fit(wf, power)

    return mod, mean, s


def test(data,  model: MLPRegressor, mean, s):
    wind, power = zip(*data)

    wa = filled_dataframe(wind, mean, s)
    score = model.score(wa, power)

    return score


def predict(wind_values,  model: MLPRegressor, mean: Series, s):
    if len(wind_values):
        wf = filled_dataframe(wind_values, mean, s)
        predictions = model.predict(wf)

        return predictions
