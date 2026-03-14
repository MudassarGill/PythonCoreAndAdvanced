import logging
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# ---------------- Logger Setup ---------------- #
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("project.log")
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Preparing started")

# ---------------- Custom Exception ---------------- #
class NegativeValueError(Exception):
    """Raise this if dataset contains negative values"""
    pass

# ---------------- Dataset Generation ---------------- #
try:
    logger.info('Generating random data')
    X = np.random.rand(100, 2) * 10  # values 0-10
    y = 3 * X[:, 0] + 5 * X[:, 1] + np.random.randn(100)

    # Custom validation
    if np.any(X < 0) or np.any(y < 0):
        raise NegativeValueError("Dataset contains negative values!")

except NegativeValueError as e:
    logger.error(f"Error: {e}")
    print(e)

else:
    logger.info("Data generated successfully")
    print("Dataset shape:", X.shape, y.shape)

    # ---------------- Train-Test Split ---------------- #
    logger.info("Splitting data into training and testing sets")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    logger.info("Data split successfully")

    # ---------------- Model Training ---------------- #
    logger.info("Training Linear Regression model")
    model = LinearRegression()
    model.fit(X_train, y_train)
    logger.info("Model trained successfully")

    # ---------------- Predictions ---------------- #
    logger.info("Making predictions")
    y_pred = model.predict(X_test)
    logger.info("Predictions made successfully")

    # ---------------- Evaluation ---------------- #
    logger.info("Evaluating model performance")
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)  # use R² instead of accuracy
    logger.info(f"Mean Squared Error: {mse:.4f}")
    logger.info(f"R² Score: {r2:.4f}")

    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")

    logger.info("Project completed successfully")