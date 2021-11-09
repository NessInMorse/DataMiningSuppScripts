def printGraph(graph: list):
        """
        Prints a graph in a more visually pleasing style.
        """
        columns = [sum([j[i] for j in graph]) 
                   for i in range(len(graph[0]))]
        print("_"*len(graph)*12)
        for row in graph:
                for column in row:
                        print(f"| {column:^8.1f} |", end="")
                print(f"|{sum(row):>7.1f}")
        print("="*len(graph)*15)
        for column in columns:
                print(f"| {column:^8.1f} |", end="")
        print(f"| {sum(columns):^8.1f}")


def checkCorrect(data: list, kap_graph: list, perfect:list) -> float:
        """
        Calculates the Kappa-statistic based on the formula:
        (Dobserved - Dexpected) / (Dperfect - Dexpected).
        in:
                the original graph
                the kappa graph
                the total amount of instances
        out:
                The Kappa-statistic
        """
        observed = 0
        expected = 0
        for i in range(len(data)):
                observed += data[i][i]
                expected += kap_graph[i][i]
        kappa_statistic = (observed - expected) / (perfect - expected)
        return kappa_statistic


def makeKappaGraph(rows: list, columns: list) -> list:
        """
        Creates the kappa graph with predictions purely based on chance.
        """
        kap_graph = [[(columns[j]/sum(columns))*rows[i] 
                                for j in range(len(columns))]
                                for i in range(len(rows))]
        return kap_graph


def openFile(filename):
        """
        Opens a csv file and creates a graph from it.
        also calculates the sum of each row and column.
        in:
                nothing
        out:
                data: a graph containing all information from the file
                rows: all the sums of rows in a list
                columns: all the sums of columns in a list
        """
        infile = open(filename, "r")
        raw = infile.read().split("\n")

        data = [[int(j) for j in i.split(",")]
                        for i in raw]
        rows = [sum(i) for i in data]

        columns = [sum([j[i] for j in data]) 
                        for i in range(len(data))]
        return data, rows, columns


if __name__ == "__main__":
        data, rows, columns = openFile("confusion_matrix.csv")
        kap_graph = makeKappaGraph(rows, columns)
        perfect = sum(rows)
        kappa_statistic = checkCorrect(data, kap_graph, perfect)
        printGraph(data)
        print(f"K-statistic: {kappa_statistic}")
        printGraph(kap_graph)
