import datetime


def calc_avg_hr(hr, times, cutoff_time):
    hr_since = []
    if cutoff_time == 1:
        avg = sum(hr)/len(hr)
    else:
        cutoff_time1 = datetime.datetime.strptime(
            cutoff_time, '%Y-%m-%d %H:%M:%S.%f')
        for x in times:
            if datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') \
                    > cutoff_time1:
                i = times.index(x)
                hr_since.append(hr[i])

        if len(hr_since) == 0:
            raise UnboundLocalError
        else:
            avg = sum(hr_since)/len(hr_since)
    return avg
