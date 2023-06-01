# Final_year_proj_Energy
Certainly! Let's break down the code and explain the functionality in more detail:

1. Resampling and Preprocessing:
   - The initial dataset is resampled to a daily frequency and the mean value is calculated for each day.
   - The dataset is sorted by datetime for sequential processing.
   - Missing values in the 'Month', 'Year', and 'Week' columns are filled using forward fill, ensuring the values carry forward from the previous valid entry.
   - Missing values in the 'Consumption' column are replaced with random values within one standard deviation of the mean, ensuring the distribution is preserved.
   - The dataset is split into a training set and a test set, with the last 100 days reserved for testing.

2. Data Preparation for LSTM Model:
   - The training set is scaled using the MinMaxScaler to normalize the values between 0 and 1, which helps the model learn from consistent and comparable data.
   - The training data is organized into input sequences of 60 consecutive days and their corresponding output value.
   - The input sequences are transformed into a 3-dimensional array with the shape (number of samples, number of timesteps, number of features), as expected by the LSTM model.

3. LSTM Model Architecture:
   - A sequential model is used, which allows for the sequential stacking of layers.
   - Four LSTM layers are added to the model, which helps capture the temporal dependencies in the data.
   - Dropout regularization is applied after each LSTM layer to prevent overfitting. Dropout randomly sets a fraction of input units to 0 during training, reducing the reliance on specific input features and improving generalization.
   - The output layer consists of a single neuron that predicts the next value.
   - The model is compiled with the Adam optimizer, which adapts the learning rate during training, and the mean squared error (MSE) loss function, which measures the difference between predicted and true values.

4. Model Training:
   - The model is trained on the prepared training data for 1000 epochs, which means it iterates over the entire dataset 1000 times.
   - The training data is processed in batches of size 64, which helps improve efficiency and generalization.
   - The model learns to minimize the difference between the predicted and true values by adjusting the weights and biases of its layers using backpropagation and gradient descent.

5. Prediction on Test Data:
   - The test data is preprocessed by concatenating the predicted values from the training data and the actual test data.
   - Missing values in the concatenated data are filled with zeros to ensure consistent shapes for prediction.
   - The input data for prediction is extracted from the last 160 days, following a similar approach as the training data.
   - The input data is transformed using the same MinMaxScaler used for the training data to ensure consistency in scaling.
   - The input data is reshaped to match the input shape expected by the model.

6. Prediction Visualization:
   - The model predicts the values for the test data.
   - The predicted and true values are extracted from the model's predictions and the test data.
   - A dataframe is created to store the dates, true values, and predicted values for visualization.
   - A line plot is generated to visualize the predicted and true values over time, providing a visual understanding of the model's performance.

7. Accuracy Calculation and Visualization:
   - The difference between the predicted and true values is calculated to evaluate the model's prediction accuracy.
   - The percentage accuracy is calculated based on the difference and true values, considering cases where true values are not zero.
   - Multiple subplots are created to visualize the true values, predicted values, difference, and percentage accuracy over time, providing insights into the accuracy and trend of the predictions.



By combining all these code snippets and following the explanations above, you can create a comprehensive program that resamples and preprocesses the data, builds an LSTM model, makes predictions, and visualizes the results, enabling you to understand and evaluate the performance of the model in predicting future values.
