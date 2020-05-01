import numpy as np
from scipy.optimize import minimize

class BradleyTerry:
    def __init__(self, comparisons, parsefunc = None):
        """
        Constructor
        :param comparisons: list of comparisons
        :param parsefunc: optionally pass a custom parsign function to cope with different data formats
        """
        parsefunc = parsefunc if parsefunc is not None else self.__parsefunc__
        self.items, self.comparisons, self.merits = parsefunc(comparisons)

    @staticmethod
    def __parsefunc__(comparisons) -> tuple:
        """
        Function to parse supplied comparison data to the format needed by the model
        :param comparisons: comparison data
        :return
        """
        items = list(set([x[0] for x in comparisons]+[x[1] for x in comparisons]))
        
        # Mapping
        items_parsed = {x: i for i, x in enumerate(items)}

        # Mapped comparisons
        comparisons_parsed = []
        for arg1_id, arg2_id, tie in comparisons:
            comparisons_parsed.append([
                items_parsed[arg1_id],
                items_parsed[arg2_id],
                tie
            ])

        # Initialize zero-vector for merits
        merits = np.zeros(len(items))

        return (items_parsed, comparisons_parsed, merits)

    @staticmethod
    def __pfunc__(i: float, j: float, t: float) -> float:
        """
        Function to compute pairwise comparison probabilities of non-ties
        :param i: merit of the winning item
        :param j: merit of the loosing item
        :param s: annotation quality score
        :param t: difference threshold
        :return: propability of item i beating item j
        """
        p = np.exp(i) / (np.exp(i) + np.exp(j) * np.exp(t))
        return np.log10(p)

    @staticmethod
    def __tfunc__(i: float, j: float, t: float) -> float:
        """
        Function to compute pairwise comparison probabilities of ties
        :param i: merit of the winning item
        :param j: merit of the loosing item
        :param t: difference threshold
        :return: propability of item i beating item j
        """
        f1 = np.exp(i) * np.exp(j) * (np.square(np.exp(t)) - 1)
        f2 = (np.exp(i) + np.exp(j) * np.exp(t)) * (np.exp(i) * np.exp(t) + np.exp(j))
        p = f1 / f2
        return np.log10(p)

    def __rfunc__(self, i: float, l: float) -> float:
        """
        Function to compute regularized probability
        :param i: item merit
        :param l: regularization factor
        :return: value of __pfunc__ for matches with dummy item weighted by l
        """
        return l * (self.__pfunc__(i, 1, 0) + self.__pfunc__(1, i, 0))

    def __log_likelihood__(self, merits: np.ndarray) -> float:
        """
        Log-Likelihood Function
        :param merits: merit vector
        :return: log-likelihood value
        """
        k: float = 0  # Maximization sum

        # Summing Edge Probabilities
        for arg1, arg2, tie in self.comparisons: 
            if tie:
                k += self.__tfunc__(merits[arg1], merits[arg2], self.threshold)
            else:
                k += self.__pfunc__(merits[arg1], merits[arg2], self.threshold)

        # Regularization
        for x in range(len(self.items)):  
            k += self.__rfunc__(merits[x], self.regularization)

        return -1 * k

    def fit(self, regularization: float = 0, threshold: float = 0) -> None:
        """
        Optimize the model for merits
        :param regularization: regularization parameter
        :param threshold: difference threshold
        """
        self.merits = np.ones(len(self.items))
        self.threshold = threshold
        self.regularization = regularization
        
        res = minimize(self.__log_likelihood__, self.merits, method='BFGS', options={"maxiter": 100})
        self.merits = res.x

    def get_merits(self, normalize=False) -> list:
        """
        Returns the merits mapped to items
        :param normalize: if true, returns normalized merit vector to 0-1 range instead of original scores
        :return: dict in the form of {argument_id: merit} sorted by merits
        :exception: Exception if model was not fitted
        """
        if not self.merits.any():
            raise Exception('Model has to be fitted first!')
        else:
            d = {argument_id: self.merits[index] for argument_id, index in self.items.items()}
            if normalize:
                mi = min(d.values())
                ma = max(d.values())
                normalize = lambda mi, ma, v: (v-mi)/(ma-mi)
                d.update({k: normalize(mi,ma,v) for k, v in d.items()})
            return sorted(d.items(), key=lambda kv: kv[1])
