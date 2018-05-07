from matplotlib import pyplot as plt
from scipy.special import comb
import numpy as np
# Program inspired by AB Pre-Calc warm-up problem below

# Mr. Cole has a 90% chance of making a free throw. What is the probability that he makes...

# All 10 FT's, At least 8, etc.

# Define our function. This will plot the probabilities, and therfore we should call it plot_prob
def plot_prob(n,prob,r):
    # Global Veriable that keeps track of the sum of probabilities that we want
    sum_prob = 0
    values = np.array([]) # Array that stores all of our probabilities. It's empty upon initialization.
    ax = plt.subplot(111) # Sub-plot for text (not important)
    # For loop that will run n+1 times, to account for 0
    for i in range(0,n+1):
        # Declare our co-efficient, which we can get using the binomial theorem
        # The comb function returns n choose i
        coef = comb(n,i)
        # Our inverse probability (since Mr. Cole has a 90% chance of making a shot, he has a 1-.9
        # chance of missing a shot
        invprob = 1-prob
        # The number that we plot on our y axis, defined as y_
        # This number is the chance that Mr. Cole will make i shots
        # i gets updated after each iteration (i=0, then i=1, and so on...)
        y_ = coef*(prob**(n-i))*(invprob**i)
        # Add our probabilities if they're in bounds
        if(n-r >= i):
            sum_prob = sum_prob + y_
        # Just adds a small annotation to each data point, signifying each probability on the graph
        plt.annotate(round(y_,3), xy=(n-i, y_), xytext=(n-i, y_ + .01))
        # Add our values to global array
        values = np.append(values, y_)
        # Plot data values at x=n-i, y=y_
        plt.scatter(n-i,y_)
    # All of our x values on the graph (from 0- size of values)
    x = np.arange(0, values.size)
    # We need to reverse the order of the array, in order for the plot and the points to line up
    plt.plot(x, values[::-1])
    # Plot text in upper left of graph, showing correlation
    text = "P of making at least {} shots: {}{}".format(r,round(sum_prob*100,4),"%")
    ax.text(0.3,.9,text, ha='center',va='center',transform=ax.transAxes)

    # Show the plot and label axis
    plt.xlabel("Shots Total")
    plt.ylabel("Probability")
    plt.axvline(x=r, c='r')
    plt.show()
# Call our function to return the probability that out of 10 shots, at 85% per shot, Mr. Cole will
# make 5 shots

# Function call works like this: plot_prob(n, %chance per event, r)
plot_prob(10,.9,8)