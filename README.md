### We used https://colab.google/ to train and forecast data
## Model Evaluation Metrics

- **Mean Absolute Error (MAE):** 1.6989571427738888

The Mean Absolute Error (MAE) is a metric used to evaluate the accuracy of a regression model. It measures the average magnitude of errors between predicted and actual values. MAE calculates the absolute difference between each predicted and actual value, then averages these differences. A lower MAE indicates better accuracy, as it signifies that the model's predictions are closer to the actual values on average. MAE is particularly useful when the dataset contains outliers, as it treats all errors equally regardless of their direction (overestimation or underestimation).

- **Mean Squared Error (MSE):** 10.70514753852184

Mean Squared Error (MSE) is another metric used to evaluate the performance of a regression model. It calculates the average of the squares of the differences between predicted and actual values. MSE penalizes larger errors more heavily than smaller ones, making it sensitive to outliers. Lower MSE values indicate better accuracy, as they signify that the model's predictions are closer to the actual values on average.

- **Root Mean Squared Error (RMSE):** 3.271872176372702

Root Mean Squared Error (RMSE) is the square root of the Mean Squared Error. RMSE provides a measure of the spread of errors in the predicted values. Like MSE, RMSE penalizes larger errors more heavily than smaller ones. It is interpreted in the same units as the dependent variable and provides an easily interpretable measure of prediction error. Lower RMSE values indicate better accuracy, as they signify that the model's predictions are closer to the actual values on average.

- **R-squared (R²):** 0.18092148919383466

R-squared (R²) is a statistical measure that represents the proportion of the variance in the dependent variable that is explained by the independent variables in the model. It ranges from 0 to 1, where 0 indicates that the model does not explain any of the variance and 1 indicates that the model explains all the variance. Higher R-squared values indicate a better fit of the model to the data. However, R-squared does not indicate whether the model's predictions are biased, and it can be misleading when applied to models with many predictors.

These metrics provide insights into the performance of the model. Lower values of MAE, MSE, and RMSE indicate better accuracy, while a higher R-squared value closer to 1 indicates a better fit of the model to the data.

These metrics provide insights into the performance of the model. Lower values of MAE, MSE, and RMSE indicate better accuracy, while a higher R-squared value closer to 1 indicates a better fit of the model to the data.

<!-- We used https://colab.google/ to train and forecast data -->

