
## Linear Methods of Dimension Reduction

- Allowed to rotate and stretch data
- Relationships are preserved

## Non Linear Methods of Dimension Reduction

- Rotate stretch and bend the data
- Will make dramatic changes such as turning data _inside out_

## PCA Principal Component Analysis

- Reduce number of variable of data set while keeping as much info as possible
- Several correlated features and project them onto a coordinate axis system
- These new components are called principal components
- Identify patterns and latent structures
- Create new columns

With a data matrix being of size _n_ × _d_


where _n_ is number of observations


_d_ is the original number of features


then PCA projects the matrix onto a matrix of size _n_ × _k_ (where _k_ < d)

- Creates new columns that maximize the variance in out data
- Principal components are ordered by variance (higher variance means more informative)
- Indicates direction in which the data varies the most

Steps involved for the PCA are as follows


(why do i need each step explain)

1. Standardize/Normalize
	1. PCA is is sensitive regarding the variance i.e. spread of data
	2. Goal is to standardize the range of the continuous initial variable
	3. Variables with larger ranges will dominate over those with smaller ones
2. Calculating covariance matrix
	1. z= value-mean/standard deviation
	2. Goal is to see if there is relationship between features that are similar to one another
	3. Sometimes, variables are highly correlated and contain redundant information
	4. PCA uses this correlation to reduce dimensionality while retaining as much variance as possible

		$$
		cov(X,Y) = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{n}
		$$

3. Calculate Eigenvalues, Eigenvectors and identify principal components
	1. Principle components are new variables that are constructed as linear combinations or mixtures of the initial variables
	2. Allows u to reduce dimensionality without losing much information.
	3. Principle components are less interpretable and don't have real meaning
	4. These components can be thought of as new axes that provide the best angle and to see and evaluate the data
	5. A v = lambda v
4. Recasting the data along PC Axes
	1. Final data set = standardized original data set
