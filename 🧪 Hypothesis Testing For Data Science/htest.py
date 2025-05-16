import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

def _compute_p_value(t_dist, t, test_type):
    if test_type == 'lower':
        p_value = t_dist.cdf(t)
    elif test_type == 'upper':
        p_value = 1 - t_dist.sf(t)
    elif test_type == 'two-tailed':
        p_value = 2 * t_dist.sf(abs(t))
    else:
        raise Exception('Unknown test type: {}'.format(test_type))
    return p_value

def t_test_one_sample(mu, data, test_type):
    """Computes a one-sample t-test against our data.

    Args:
        mu (float): Null hypothesis mu assumption.
        data (ndarray): Raw sample data.
        test_type ({'lower', 'upper', 'two-sided'}): Type

    Raises:
        Exception: test_type must be a valid test.

    Returns:
        (t, p-value): Returns t-score and corresponding p-value
    """
    # compute mean, standard deviation, and degrees of freedom
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    n = len(data)
    dof = n - 1

    # generate the corresponding t-distribution
    t_dist = stats.t(dof)

    # compute t-score
    t = (sample_mean - mu) / (sample_std / np.sqrt(n))

    # compute p-value
    p_value = _compute_p_value(t_dist, t, test_type)
    return t, p_value

def t_test_two_sample(sample1, sample2, test_type):
    """Computes a two-sample t-test against our data.

    Args:
        sample1 (ndarray): first sample
        sample2 (ndarray): second sample
        test_type ({'lower', 'upper', 'two-sided'}): Type of test

    Raises:
        Exception: test_type must be a valid test.

    Returns:
        (t, p-value): Returns t-score and corresponding p-value
    """
    # compute mean, standard deviation, and degrees of freedom
    sample_mean1 = np.mean(sample1)
    sample_mean2 = np.mean(sample2)
    sample_std1 = np.std(sample1, ddof=1)
    sample_std2 = np.std(sample2, ddof=1)
    n1 = len(sample1)
    n2 = len(sample2)
    dof = n1 + n2 - 2

    # generate corresponding t-distribution
    t_dist = stats

    # compute pooled standard deviation
    s_p = np.sqrt(((n1 - 1) * sample_std1 ** 2 + (n2 - 1) * sample_std2 ** 2) / dof)

    # compute t-score
    t = (sample_mean1 - sample_mean2) / (s_p * math.sqrt(1. / n1 + 1 / n2))

    # compute p-value
    p_value = _compute_p_value(t_dist, t, test_type)
    return t, p_value

def plot_graph(t, dof, test_type, critical_value):
    """Plots a t-distribution with dof defrees of freedom and

    Args:
        t (float): t-score
        dof (int): degrees of freedom for t-distribution
        test_type ({'lower', 'upper', 'two-sided'}): type of test
        critical_value (float): alpha level

    Raises:
        Exception: test_type must be a valid test.
    """
    MIN_PPF = 0.001
    MAX_PPF = 0.999

    # construct the t-dist
    t_dist = stats.t(dof)