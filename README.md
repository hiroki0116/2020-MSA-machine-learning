This is MSA 2020 - AI & Advanced Analytics program.
Coding Approach


1.	Detailed description of the idea and project

      Build a machine learning model to classify the species of an iris flower based on its size of petal and sepal.

      Using the iris data set that comes standard with scikit-learn,
      I implemented Random Forest model to predict which iris varieties belong from the measured values ​​of flowers.
      Random forests make many different decision trees. The correct answer is the label with the highest probability
      from the results predicted by all decision trees. Individual trees may be overfitting,
      but aggregating many results has the effect of suppressing overfitting.



2.	Environment setup & dependencies

    ・Jupyter notebook in the local environment
    ・Python 3.6
    
3.	Step-by-step instruction on how to train and/or test your model (IMPORTANT)  

    3.1 Install required libraries to enhance a machine learning model

    3.2 Get data set

      The iris dataset dealt with this time is a famous dataset that has been used for a long time in the field of machine learning and statistics.
      It is composed of the length of the petal and sepal.
      This dataset is included in the datasets module of scikit-learn, and you can retrieve the dataset with the load_iris function.
      Classify by 4 features of each specie [‘sepal width’, ‘petal width’, ‘sepal length’, ‘sepal width’]

    3.3 Data visualization by using pair plot

      Before constructing the machine learning model, we will plot the scatter plot with a combination of features and visualize the data.
      Based on the 4 features of the iris data set (sepal length, sepal width, petal length, petal width),
      visually checking whether varieties can be classified.

    3.4 Split into training data and test data

      Split the iris dataset into training and test data.
      Build a machine learning model from the training data and evaluate how accurate the built model works using the test data.
      Use a 75/25 split for train/test respectively.

    3.5 Fit the datasets

      Train a model in Random Forest. In the fit function the parameter of "n_estimators" is the number of trees. "n_jobs" is the number of jobs to execute in parallel.

    3.6 Compute the accuracy of the prediction
      Use score function to know the accuracy of this machine learning model.
