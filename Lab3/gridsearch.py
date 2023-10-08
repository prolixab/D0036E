import matplotlib.pyplot as plt


class GridSearch:

    def __init__(self, a, b, step, func):
        self.a = a
        self.b = b
        self.step = step
        self.func = func
        self.hyperparameter_list = []
        self.result_list = []

    def perform_search(self):
        self.hyperparameter_list = []
        self.result_list = []
        for x in range(self.a, self.b, self.step):
            self.hyperparameter_list.append(x)

            result = self.func(x)
            self.result_list.append(result)

    def plot_results(self):
        plt.plot(self.hyperparameter_list, self.result_list)
        plt.xlabel('Hyperparameter')
        plt.ylabel('Silhouette Coefficient')
        plt.title('Silhouette Coefficient based on Hyperparameter')
        plt.show()
