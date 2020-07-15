import math
import matplotlib.pyplot as plt
from standard_distributions import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        probability (float) representing the probability of an event occurring
        size (int) number of trials

    """

    def __init__(self, probability=0.5, size=20):
        self.size = size
        self.probability = probability

        super(Binomial, self).__init__(self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

            Args:
                None

            Returns:
                float: mean of the data set

        """

        self.mean = self.probability * self.size

        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

            Args:
                None

            Returns:
                float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.size * self.probability * (1 - self.probability))

        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        self.size = len(self.data)
        self.probability = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.probability, self.size

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(
            x=["0", "1"],
            height=[(1 - self.probability) * self.size, self.probability * self.size],
        )
        plt.title("Bar Chart of Data")
        plt.xlabel("outcome")
        plt.ylabel("count")

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        a = math.factorial(self.size) / (
            math.factorial(k) * (math.factorial(self.size - k))
        )
        b = (self.probability ** k) * (1 - self.probability) ** (self.size - k)

        return a * b

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.size + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title("Distribution of Outcomes")
        plt.ylabel("Probability")
        plt.xlabel("Outcome")

        plt.show()

        return x, y

    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert (
                self.probability == other.probability
            ), "probability values are not equal"
        except AssertionError as error:
            raise

        result = Binomial()
        result.data = self.data + other.data
        result.size = self.size + other.size
        result.probability = self.probability
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}, probability {}, size {}".format(
            self.mean, self.stdev, self.probability, self.size
        )
