import numpy as np

def avgCaculate(virus, inputGap=15):
    """
    Computing window averages for virus data

    Parameters:
        virus (ndarray): virus data array
        inputGap (int): window size, default is 15

    Returns:
        ndarray: Array of windowed mean values for virus data
    """
    length_virus = len(virus)
    avg_virus = np.zeros(length_virus)

    for i in range(length_virus):
        if i <= length_virus - inputGap - 1:
            avg_virus[i] = np.mean(virus[i:i+inputGap])
        else:
            avg_virus[i] = np.mean(virus[i:length_virus])

    return avg_virus
