import os
import numpy as np

def random_name():
    """Generate a random name = adjective + noun."""
    package_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(package_dir, 'adjectives.txt')) as f:
        adj = f.readlines()
    with open(os.path.join(package_dir, 'nouns.txt')) as f:
        nns = f.readlines()
    adj, nns = [[x.strip() for x in content] for content in (adj, nns)]
    return '_'.join([np.random.choice(c) for c in (adj, nns)])
