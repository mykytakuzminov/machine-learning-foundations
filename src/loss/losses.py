from src.core.matrix import Matrix


def mse(y_true: Matrix, y_pred: Matrix) -> float:
    """
    Calculates the Mean Squared Error (MSE) between the ground truth and predictions.

    The MSE is calculated as the average of the squares of the errors (the difference
    between true and predicted values).

    Args:
        y_true: The ground truth Matrix.
        y_pred: The predicted values Matrix.

    Returns:
        The calculated MSE as a float.
    """
    loss = ((y_true - y_pred) ** 2).mean()
    return loss

