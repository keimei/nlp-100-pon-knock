v = "I am an NLPer"

def trail(v, n):
    gram = []
    for i in range(len(v)-1):
        gram.append(v[i:i+n])
    return gram

def n_gram(v, n):
    return trail(v.replace(' ', ''), n)

def nw_gram(v, n):
    return trail(v.split(" "), n)


if __name__ == '__main__':
    print "bi-word-gram", nw_gram(v, 2)
    print "bi-gram: ",n_gram(v, 2)

