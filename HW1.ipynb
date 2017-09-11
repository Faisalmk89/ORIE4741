# test:
# We'll use the PyPlot (matplotlib) plotting library:
# It works exactly as it would in Python.
using PyPlot

# don't change this: it sets the random number generator, 
# so everyone in the class will have consistent results
srand(17)

# set dimensions
n = 50
d = 2
# generate input: the rows of X are the data points
# notice the last column encodes the offset
X = [randn(n, d) ones(n)]

# Generate the target function w♮
# Store the correct decision for each datapoint in y
w♮ = randn(d+1)
y = sign(X*w♮);

# plot data points X and color according to y
clf()
hold(true)
axis("off")
for i=1:n
    plot(X[i,1], X[i,2], y[i]==1 ? "ro" : "bd")
end

# set figure limits
ylim([-2,2])
xlim([-2,2])
savefig("perceptron_data_hw1.eps")

"""
This function takes data points X, plots them, and colors them correctly according to y.
This function also plots the line w'*x = 0.
We are plotting just the first two dimensions of x; 
the last (offset) coordinate of w sets the offset of the line from the origin.
"""
function plot_perceptron(X,y,w)
    # plot data points X and color according to y
    clf()
    hold(true)
    axis("off")
    for i=1:n
        plot(X[i,1], X[i,2], y[i]==1 ? "ro" : "bd")
    end
    
    # plot vector w
    x1samples = [minimum(X[:,1]), maximum(X[:,1])]
    if w[2]!=0
        plot(x1samples, [-(w[1]*x1 + w[3])/w[2] for x1 in x1samples], color="black")
    end
    
    # set figure limits
    ylim([-2,2])
    xlim([-2,2])
end
# Double check our function by plotting the points with the truth vector 
plot_perceptron(X,y,w♮)

"""
the following function gets a vector point of X_i and a point y (y_i) and checks if X_i is classified correctly
or it is misclassified.
"""
"""
the following function gets a vector point of X_i and a point y (y_i) and checks if X_i is classified correctly
or it is misclassified.
"""
function checkClassification02(wOld,vector,point)
    dummyResult = wOld*vector*point;
    # println(dummyResult)
    if dummyResult <= 0
        return false
    else 
        return true
    end
end



function perceptron(X,y;
                    maxsteps=100, # 
                    w = rand(size(X,2))) # initial guess for w
    
    ## YOUR CODE HERE p
    IterCounter = 0
    println(w)
    wOld = w'
    for iter = 1:maxsteps
        rows_X,cols_X = size(X)
        # wOld = w
        println("the iter is ",iter)
        counter = 0 # count the number of misclassified points
        for i = 1:rows_X
            if checkClassification02(wOld,X[i,:],y[i])
                # correctly classified point
            else
                wOld = wOld + (X[i,:]*y[i])'
                counter = counter + 1
            end
        end
        IterCounter = IterCounter + 1;
        w = wOld
        if counter == 0
            break
        end
    end
    println(w)
    return w
end



plot_perceptron(X,y,w_final)

function dataGenerator(n,d)
    # generate input: the rows of X are the data points
    # notice the last column encodes the offset
    X = [randn(n, d) ones(n)]

    # Generate the target function w♮
    # Store the correct decision for each datapoint in y
    w♮ = randn(d+1)
    y = sign.(X*w♮);
    return X, w♮, y
end


# solve part b: by varying n
n = 100
X, y, w♮  = dataGen(n);
wPerc, iterations = perceptron(X,y)


function perceptronRandomPick(X,y;
                    maxsteps=500, # 
                    w = rand(size(X,2))) # initial guess for w
    
    ## YOUR CODE HERE p
    # generate random integers with no repitition
    #using StatsBase
    rows_X,cols_X = size(X)
    a = sample(1:rows_X, rows_X, replace = false) 
    IterCounter = 0
    println(w)
    wOld = w'
    for iter = 1:maxsteps
        # wOld = w
        # println("the iter is ",iter)
        counter = 0 # count the number of misclassified points
        for i = 1:rows_X
            index = a[i];
            if checkClassification02(wOld,X[index,:],y[index])
                # correctly classified point
            else
                wOld = wOld + (X[index,:]*y[index])'
                counter = counter + 1
            end
        end
        IterCounter = IterCounter + 1;
        w = wOld
        if counter == 0
            break
        end
    end
    println(w)
    return w, IterCounter
end

numberOfIters = zeros(100)
for i = 1:length(numberOfIters)
    w,dummyVal =  perceptronRandomPick(X,y);
    numberOfIters[i] = dummyVal;
end
