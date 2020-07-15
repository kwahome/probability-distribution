# Unit tests to check your solution
import unittest
from gaussian import Gaussian


class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.file_path = "../resources/numbers.txt"

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, "incorrect mean")
        self.assertEqual(self.gaussian.stdev, 2, "incorrect standard deviation")

    def test_pdf(self):
        self.assertEqual(
            round(self.gaussian.pdf(25), 5),
            0.19947,
            "pdf function does not give expected result",
        )

    def test_mean_calculation(self):
        self.gaussian.read_data_file(self.file_path, True)
        self.gaussian.plot_histogram()
        self.assertEqual(
            self.gaussian.calculate_mean(),
            sum(self.gaussian.data) / float(max(1, len(self.gaussian.data))),
            "calculated mean not as expected",
        )

    def test_stdev_calculation(self):
        self.gaussian.read_data_file(self.file_path, True)
        self.assertEqual(
            round(self.gaussian.stdev, 2), 92.87, "sample standard deviation incorrect"
        )
        self.gaussian.read_data_file(self.file_path, False)
        self.assertEqual(
            round(self.gaussian.stdev, 2),
            88.55,
            "population standard deviation incorrect",
        )

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

    def test_repr(self):
        gaussian_one = Gaussian(25, 3)

        self.assertEqual(str(gaussian_one), "mean 25, standard deviation 3")


tests = TestGaussianClass()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)
