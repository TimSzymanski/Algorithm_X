from AlgorithmX import AlgorithmXSolver

class MySolver(AlgorithmXSolver):

    def __init__(self):
        requirements = [('requirement 1', ), ('requirement 2', )]
        actions = {
            ('Cover Req 1', ):[('requirement 1', )],
            ('Cover Req 2', ):[('requirement 2', )]
        }

        super().__init__(requirements, actions)

def count_all_stars(galaxies):
    total_stars = 0
    for stars in galaxies:
        total_stars = stars  # fix me!
    return total_stars
