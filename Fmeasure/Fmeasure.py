def calcFmeasure(precision: float, recall: float):
        """
        Calculates the F-measure based on the formula:
                (2 * recall * precision) / (recall + precision)
        """
        return (2 * recall * precision) / (recall + precision)

def calcRecall(data: list):
        truePos = data[0][0]
        falseNeg = data[1][0]
        return truePos / (truePos + falseNeg)


def calcPrecision(data: list):
        truePos = data[0][0]
        falsePos = data[0][1]
        return truePos / (truePos + falsePos)

def openFile():
        """
        Opens a prediction matrix in the format:
                TP, FP
                FN, TN
        """
        infile = open("positives_and_negatives.csv", "r")
        raw = infile.read().split()
        data = [[int(j) for j in i.split(",")] for i in raw]
        return data


if __name__ == "__main__":
        data = openFile()
        precision = calcPrecision(data)
        recall = calcRecall(data)
        f = calcFmeasure(precision, recall)
        print(f"Precision is: {precision}\nRecall is: {recall}\nF-measure is: {f}")
