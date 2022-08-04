import matplotlib.pyplot as plt

def plot_line_chart(algo_type, num_rows, times):
    """
    Plotting points for each function on a different charts.
    """
    plt.title(f'Complaints by State Using {algo_type}')
    plt.ylabel('runtime')
    plt.xlabel('data size')
    plt.plot(num_rows, times)
    plt.savefig(f'/home/ra-terminal/Desktop/projects/medium_projects/time_complexity/{algo_type}.png')
    plt.show(block=False)

def plot_line_chart2(dict1, dict2, dict3):
    """
    Plotting points for each function on a single chart.
    """
    plt.title(f'Measuring Speed for Calculating Complaints by State')
    plt.ylabel('runtime (seconds)')
    plt.xlabel('data size')
    plt.plot(list(dict1.keys()), list(dict1.values()), color='r', label='For Loop')
    plt.plot(list(dict2.keys()), list(dict2.values()), color='g', label='Pandas')
    plt.plot(list(dict3.keys()), list(dict3.values()), color='b', label='Counter', alpha=0.4)
    # plt.plot(list(dict2.keys()), list(dict2.values()), color='g', label='Pandas')
    plt.legend()
    plt.savefig(f'/home/ra-terminal/Desktop/projects/medium_projects/time_complexity/time_complexity_calculating_complaints_by_state.png')
    plt.show(block=False)