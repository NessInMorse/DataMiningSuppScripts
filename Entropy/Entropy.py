from math import log


def calWeightedAverage(counts: list, entropies: list):
        """
        Calculates the weighted average for elements,
        based on the occurences of the elements in the data.
        in: 
                a list of all the counts of variables in a split
                a list of all the entropies calculated
        out:
                the weighted average entropy in the data
        """
        total_instances = sum([sum(i) for i in counts])
        return sum([entropies[i]*(sum(counts[i]) / total_instances)
                                for i in range(len(entropies))])

def cal_Entropy(odds):
        """
        Returns the entropy of all the 'odds'-elements in a list
        in:
                a list of all the odds of every element in a list
        out:
                the entropy of the list
        """
        entropy = [-odds[i] * log(odds[i], 2) for i in range(len(odds))]
        return sum(entropy)


def returnGroupLen(group: list):
        """
        Returns the total instances in a list
        in:
                a list
        out:
                the sum of all the integers in the list
        """
        return sum(group)

if __name__ == "__main__":
        # A list of counts of variables in a list.
        # j,n,n,n,j would be represented as [[2, 3]]
        # since 2 j's and 3 n's are present in the data
        # j,n,n,n,o, would be represented as [[1, 3, 1]]
        # splits are represented as: [[x, y], [x, y]]
        counts = [[2, 1, 2], [2, 2]]
        entropies = []
        for group in counts:
                total = returnGroupLen(group)
                odds = [i/total for i in group]
                entropies.append(cal_Entropy(odds))

        if len(counts) > 1:
                print("The Weighted average of the entropies is: " +\
                        f"{calWeightedAverage(counts, entropies):.2f}")
        else:
                print(f"The entropy is: {entropies[0]:.2f}")
