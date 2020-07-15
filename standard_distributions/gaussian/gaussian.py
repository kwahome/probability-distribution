import math
import matplotlib.pyplot as plt
from standard_distributions import Distribution


class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats extracted from the data file
            
    """

    def __init__(self, mu=0, sigma=1):
        super(Gaussian, self).__init__(mu, sigma)

    def calculate_mean(self):

        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        # to avoid ZeroDivisionError exceptions,
        # we always make sure the divisor is greater than 0
        self.mean = 1.0 * sum(self.data) / max(len(self.data), 1)
        return self.mean

    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """
        count = len(self.data)
        if sample:
            count -= 1

        sigma = sum([(d - self.mean) ** 2 for d in self.data])

        self.stdev = math.sqrt(sigma / count)

        return self.stdev

    def read_data_file(self, file_name, sample=True):

        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
            sample (bool): whether the data represents a sample or population
        
        Returns:
            None
        
        """
        super(Gaussian, self).read_data_file(file_name=file_name)

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        plt.hist(self.data)
        plt.title("Histogram of Data")
        plt.xlabel("data")
        plt.ylabel("count")

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """

        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(
            -0.5 * ((x - self.mean) / self.stdev) ** 2
        )

    def plot_histogram_pdf(self, n_spaces=50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=0.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title("Normed Histogram of Data")
        axes[0].set_ylabel("Density")

        axes[1].plot(x, y)
        axes[1].set_title(
            "Normal Distribution for \n Sample Mean and Sample Standard Deviation"
        )
        axes[0].set_ylabel("Density")
        plt.show()

        return x, y

    def __add__(self, other):

        """Magic method to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """

        result = Gaussian()

        result.data = self.data + other.data
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt((self.stdev ** 2) + (other.stdev ** 2))

        return result

    def __repr__(self):

        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """

        return "mean {0}, standard deviation {1}".format(self.mean, self.stdev)