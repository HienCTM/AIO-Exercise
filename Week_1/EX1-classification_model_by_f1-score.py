def f1_score(tp, fp, fn):
    if type(tp) is not int:
        return ("tp must be int")
    elif type(fp) is not int:
        return ("fp must be int")
    elif type(fn) is not int:
        return ("fn must be int")
    else:
        if not (tp > 0 and fp > 0 and fn > 0):
            print("tp and fp and fn must be greater than zero")
        else:
            precision = tp / (tp + fp)
            recall = (tp / (tp + fn))
            f1_score = 2 * (precision * recall) / (precision + recall)

            print(f"Precision is {precision}")
            print(f"Recall is {recall}")
            print(f"F1-score is {f1_score}")

# test
f1_score(tp = 2, fp = 3, fn =4 )
f1_score(tp ='a', fp = 3, fn = 4)
