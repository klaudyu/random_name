import numpy as np
def random_name():
    """Generate a random name = adjective + noun ."""
    with open('adjectives.txt') as f:
        adj = f.readlines()
    with open('nouns.txt') as f:
        nns = f.readlines()
    adj, nns = [[x.strip() for x in content] for content in (adj, nns)]
    return '_'.join([np.random.choice(c) for c in (adj, nns)])


