from src.core.matrix import Matrix
from src.loss.losses import mse


class LinearRegression:
    """
    A Linear Regression model implemented using batch gradient descent.

    Attributes:
        weights (Matrix): The feature weights, initialized to zero.
        bias (float): The intercept term, initialized to zero.
    """
    def __init__(self, n_features: int) -> None:
        """
        Initializes the model with the expected number of features.

        Args:
            n_features: The number of input features (columns in X).
        """
        self.weights = Matrix.zeros(n_features, 1)
        self.bias = 0.0

    def predict(self, x: Matrix) -> Matrix:
        """
        Generates predictions using the linear equation: y = Xw + b.

        Args:
            x: Input matrix of shape (n_samples, n_features).

        Returns:
            A Matrix of shape (n_samples, 1) containing predicted values.
        """
        return x * self.weights + self.bias

    def fit(self, x: Matrix, y_true: Matrix, learning_rate: float, epochs: int) -> None:
        """
        Fits the model parameters (weights and bias) to the data using
        batch gradient descent.

        Args:
            x: Training input matrix of shape (n_samples, n_features).
            y_true: Target values matrix of shape (n_samples, 1).
            learning_rate: The step size for weight updates.
            epochs: Number of iterations over the entire dataset.
        """
        n_samples = x.shape[0]

        for epoch in range(epochs):
            preds = self.predict(x)
            errors = preds - y_true

            gradient_weights = (x.transpose() * errors) * (2.0 / n_samples)
            gradient_bias = errors.sum() * (2.0 / n_samples)

            self.weights = self.weights - (gradient_weights * learning_rate)
            self.bias = self.bias - (gradient_bias * learning_rate)

            if epoch % 100 == 0:
                loss = mse(y_true, preds)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
