from math import log


def cal_Entropy(odds):
        entropy = [0 for i in range(len(odds))]
        for i in range(len(odds)):
                entropy[i] = -odds[i] * log(odds[i], 2)

        print(sum(entropy))


def make_data_list(counts: dict):
        total = 0
        for item in range(len(counts)):
                total += len([item for i in range(counts[item])])
        return total

if __name__ == "__main__":
        counts = [4, 3, 2]
        total = make_data_list(counts)
        odds = [i/total for i in counts]
        cal_Entropy(odds)
