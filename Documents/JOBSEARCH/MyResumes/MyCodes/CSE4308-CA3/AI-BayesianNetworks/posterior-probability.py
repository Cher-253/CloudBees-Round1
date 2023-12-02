from sys import argv

class bags:
    def __init__(self, prior, cherry, lime):
        self.prior = prior
        self.cherry = cherry
        self.lime = lime

def predicted_probability():
    pred_cherry = pred_lime = 0
    for bag in bag_list:
        pred_cherry += bag.prior*bag.cherry
        pred_lime += bag.prior*bag.lime
    return pred_cherry, pred_lime

def posterior_probability(candy, pred_cherry, pred_lime):
    filehandle.write('\n')
    bag_count = 1
    if candy == 'C':
        for bag in bag_list:
            bag.prior = (bag.cherry*bag.prior)/pred_cherry
            filehandle.write(f'P(h{bag_count} | Q) = {bag.prior}\n')
            bag_count += 1
    else:
        for bag in bag_list:
            bag.prior = (bag.lime*bag.prior)/pred_lime
            filehandle.write(f'P(h{bag_count} | Q) = {bag.prior}\n')
            bag_count += 1
    filehandle.write('\n')


if __name__ == '__main__':
    flag = False
    if(len(argv)==1):
        Q = ''
        flag = True
    else:
        Q = argv[1]

    filehandle = open('result.txt', 'w')

    filehandle.write(f'Observation sequence Q: {Q}\n')
    filehandle.write(f'Length of Q: {len(Q)}\n')
    b1 = bags(0.1, 1, 0)
    b2 = bags(0.2, 0.75, 0.25)
    b3 = bags(0.4, 0.5, 0.5)
    b4 = bags(0.2, 0.25, 0.75)
    b5 = bags(0.1, 0, 1)
    bag_list = [b1, b2, b3, b4, b5]
    pred_cherry, pred_lime = predicted_probability()
    if flag:
        filehandle.write(f'\nProbability that the next candy we pick will be C, given Q: {pred_cherry}\n')
        filehandle.write(f'Probability that the next candy we pick will be L, given Q: {pred_lime}\n')
    candy_count = 1
    for candy in Q:
        filehandle.write(f'\nAfter Observation {candy_count} = {candy}:\n')
        posterior_probability(candy, pred_cherry, pred_lime)
        pred_cherry, pred_lime = predicted_probability()
        filehandle.write(f'Probability that the next candy we pick will be C, given Q: {pred_cherry}\n')
        filehandle.write(f'Probability that the next candy we pick will be L, given Q: {pred_lime}\n')
        candy_count += 1