import datetime


def calc_avg_hr(hr, times, cutoff_time):
    hr_since = []
    if cutoff_time == 1:
        avg = sum(hr)/len(hr)
    else:
        for x in times:
            if datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') \
                    > cutoff_time:
                i = times.index(x)
                hr_since.append(hr[i])
        avg = sum(hr_since)/len(hr_since)
    return avg
