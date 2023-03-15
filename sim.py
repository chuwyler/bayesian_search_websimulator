import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

class SearchSimulator:
    """
    This class implements a search simulator.
    
    Parameters
    ----------
    n_x : int
        Number of horizontal elements in the search array
    n_y : int
        Number of vertical elements in the search array
    p : float
        Probability with which the object is found when searching the sector containing the object
    exp : float
        Exponent to use when introducing skewness to the probability distribution (see code for further explanation)

    Attributes
    ----------
    prior : np.array
        Contains the prior probability for each sector (shape n_x * n_y)
    found : boolean
        Indicates whether the object has already been found
    n_tries : int
        number of tries
    true_sector : int
        sector where object is hidden
    queries : list
        query history
    """
    def __init__( self, n_x=3, n_y=3, p=0.6, exp=2 ):
        # set instance variables
        self.n_x = n_x
        self.n_y = n_y
        self.n = n_x * n_y
        self.p = p
        self.n_tries = 0
        self.found = False
        self.queries = []
        
        # randomize a prior distribution
        self.prior = np.random.rand( self.n )
        self.prior = self.prior ** exp # introduce a bit of asymmetry with exponent
        self.prior = self.prior / np.sum( self.prior )
        
        # randomize sector where object is hidden according to prior
        self.true_sector = np.random.choice( np.arange(self.n), p=self.prior )
    
    def query( self, sector ):
        """Performs a search in sector <sector>"""
        
        # only query if the object has not yet been found
        if self.found:
            raise Exception("The object has already been found!")
        
        self.queries.append( sector )
        
        # increment number of tries
        self.n_tries += 1
        
        # return result
        if self.true_sector == sector:
            if np.random.rand() <= self.p:
                self.found = True
                return (True, self.n_tries)
            else:
                return (False, self.n_tries)
        else:
            return (False, self.n_tries)
    
def show( prob, n_x, n_y, sector=None, found=False, cmap="jet" ):
    """Shows discrete probability distribution on a map"""

    # plot probabilities
    a = prob.reshape( n_x, n_y )
    fig = plt.figure( figsize=(n_x*1.3, n_y*1.3) )
    im = plt.matshow( a, cmap=cmap, fignum=fig )

    # number sectors
    for i in range( n_x ):
        for j in range( n_y ):
            plt.text(j-0.1, i+0.1, n_y*i+j)
    
    # draw a cross where object was found
    if found and sector is not None:
        i, j = np.where( np.arange(n_x*n_y).reshape(n_x, n_y) == sector )
        plt.plot(j, i, marker="x", color="black", markersize=20, linewidth=20)

    plt.colorbar()
    plt.title("Initial prior distribution")
    return fig
