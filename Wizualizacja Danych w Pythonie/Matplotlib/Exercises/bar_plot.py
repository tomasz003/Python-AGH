import matplotlib.pyplot as plt


def bars(values):
    categories=['A', 'B', 'C', 'D', 'E']
    plt.bar(categories, values)
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.title("Bar Plot")