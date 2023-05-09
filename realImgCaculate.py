import numpy as np

def realImgCaculate(dif_virus1, dif_virus2=None):
    """
    Calculate internal or external covariance of virus data

    Parameters:
        dif_virus1 (ndarray): Difference array of virus data 1
        dif_virus2 (ndarray): The difference array of virus data 2, optional, the default is None, at this time, the internal covariance of dif_virus1 is calculated

    Returns:
        tuple: Contains two arrays, which are the real part covariance and imaginary part covariance of the virus data
    """
    if dif_virus2 is None:
        virus1_M_virus2 = dif_virus1 * dif_virus1
    else:
        virus1_M_virus2 = dif_virus1 * dif_virus2

    real_virus1_virus2 = np.copy(virus1_M_virus2)
    real_virus1_virus2[real_virus1_virus2 < 0] = 0

    img_virus1_virus2 = np.copy(virus1_M_virus2)
    img_virus1_virus2[img_virus1_virus2 > 0] = 0
    img_virus1_virus2 = -img_virus1_virus2

    return (real_virus1_virus2, img_virus1_virus2)
