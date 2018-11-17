import datetime


def calc_avg_hr(hr, times=1, cutoff_time=1):
    """ Calculates average heart rate based on inputs

    If only heart rate data is input into the function,
    the function will calculate the total average of
    the heart rate list.

    If a list of times and a cutoff time are entered, the
    function will calculate the average heart rate since that
    cutoff time.

    Args:
        hr (list): List of heart rates for patient
        times (list): List of times corresponding to the heart rates
        cutoff_time (str): Cutoff time for calculation

    Returns:
        avg (float): Average heart rate
    """
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
