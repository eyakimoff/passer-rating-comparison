# Passer Rating Analysis: Traditional vs. Refined Formulas

This project explores and compares the effectiveness of two passer rating formulas: the traditional formula and a refined version that removes the thresholds present in the traditional calculation. By analyzing game data, the project evaluates how well each formula predicts game outcomes and highlights key differences in their performance. Additionally, it provides insights into individual player performance and showcases the top all-time performances using both formulas.

---

## Overview

The passer rating formulas are widely used metrics for evaluating quarterback performance in football. This project aims to:

1. Compare the predictive performance of the **traditional passer rating formula** and a **refined formula** that eliminates thresholds.
2. Analyze individual player performance using both formulas.
3. Identify the all-time best game performances based on each formula.

---

## Features

-   **Model Evaluation**: Compare the accuracy, precision, recall, and confusion matrices of both formulas.
-   **Player Analysis**: View individual player game data and assess their performance using each formula.
-   **Top Performances**: Explore the best all-time performances according to each formula.
-   **Visualizations**: Examine ROC curves and AUC values for deeper insights into model performance.

---

## Key Findings

### Model Performance Summary

#### Traditional Rating Model:

-   **Accuracy**: 0.71 (71% of predictions are correct).
-   **Precision**:
    -   For losses (0): 0.71
    -   For wins (1): 0.70
-   **Recall**:
    -   For losses (0): 0.72
    -   For wins (1): 0.69
-   **Confusion Matrix**:

    $$
    \begin{bmatrix}
    TN = 1019 & FP = 390 \\
    FN = 439 & TP = 971
    \end{bmatrix}
    $$

---

#### Refined Rating Model:

-   **Accuracy**: 0.66 (slightly lower than the traditional model).
-   **Precision**:
    -   For losses (0): 0.65
    -   For wins (1): 0.69
-   **Recall**:
    -   For losses (0): 0.73
    -   For wins (1): 0.60
-   **Confusion Matrix**:

    $$
    \begin{bmatrix}
    TN = 1023 & FP = 386 \\
    FN = 559 & TP = 851
    \end{bmatrix}
    $$

---

### Key Observations

1. **Traditional Rating Model Performs Slightly Better**:

    The accuracy of the traditional model is 71%, compared to 66% for the refined model.

    - Recall for wins (69%) is significantly higher than the refined model (60%).
    - The traditional rating model misses fewer actual wins, with 439 false negatives vs. 559 in the refined model.

2. **Refined Rating Model Is Better at Identifying Losses**:

    - The refined model has a higher recall for losses (73%), which correctly predicts more actual losses than the traditional model (72%).
      However, this comes at the cost of lower win recall (60%), meaning it struggles to classify wins correctly.

3. **Impact of Confusion Matrix Differences**:

    - The refined model has more false negatives (559 vs. 439), meaning it misclassifies a higher number of actual wins as losses.
    - The traditional model maintains a more balanced tradeoff between identifying wins and losses.

### ROC Curve and AUC

-   **Traditional Model AUC**: Expected to be higher, indicating better performance in distinguishing wins and losses.
-   **Refined Model AUC**: Expected to be lower, reflecting its difficulty in identifying wins accurately.

### Conclusion

The traditional passer rating remains a stronger predictor of winning games, with a higher correlation to game outcomes and better overall accuracy. The refined passer rating prioritizes identifying poor performances and losses, but its harsh penalties may overcorrect and reduce its effectiveness in predicting wins.

If the goal is predicting game outcomes, the traditional model is preferable. However, the refined model offers a different perspective on quarterback performance, emphasizing mistakes and underperformance more heavily. Further refinements could help balance its evaluation of both strong and weak performances.

---

## Visualizations

The project includes interactive visualizations to explore:

-   **ROC Curves**: Compare the AUC values of both formulas.
-   **Top Performances**: Visualize all-time great games ranked by each formula.
-   **Individual Player Analysis**: Assess player performance trends over time.

---

## How It Works

1. **Data Collection**:

    - Retrieves live and historical game data using APIs (e.g., Yahoo Finance API for football data).
    - Processes quarterback performance statistics.

2. **Formulas Adjustment (Below)**

3. **Machine Learning Evaluation**:

    - Models are evaluated using metrics such as accuracy, precision, recall, and AUC to measure their predictive ability.

4. **Interactive Streamlit App**:

    - Explore the findings through a user-friendly interface.

## Passer Rating Formula

The passer rating formula is defined as follows:

$a = \left( \frac{\text{CMP}}{\text{ATT}} - 0.3 \right) \times 5$

$b = \left( \frac{\text{YDS}}{\text{ATT}} - 3 \right) \times 0.25$

$c = \left( \frac{\text{TD}}{\text{ATT}} \right) \times 20$

$d = 2.375 - \left( \frac{\text{INT}}{\text{ATT}} \times 25 \right)$

Where:

-   **ATT** = Number of passing attempts
-   **CMP** = Number of completions
-   **YDS** = Passing yards
-   **TD** = Touchdown passes
-   **INT** = Interceptions

If the result of any calculation is greater than **2.375**, it is set to **2.375**. If the result is a negative number, it is set to **0**.

The overall passer rating is then calculated as:

$\text{Passer Rating} = \left( \frac{a + b + c + d}{6} \right) \times 100$

## Refined Passer Rating Formula

**Refined Formula**:
A modified version that removes thresholds and the completion percentage component to allow continuous evaluation of performance.
The refined passer rating formula is defined as follows:

$b = \left( \frac{\text{YDS}}{\text{ATT}} - 3 \right) \times 0.25$

$c = \left( \frac{\text{TD}}{\text{ATT}} \right) \times 20$

$d = 2.375 - \left( \frac{\text{INT}}{\text{ATT}} \times 25 \right)$

Where:

-   **ATT** = Number of passing attempts
-   **YDS** = Passing yards
-   **TD** = Touchdown passes
-   **INT** = Interceptions

$\text{Passer Rating} = \left( \frac{b + c + d}{6} \right) \times 100$

---

## Contact

For questions or feedback, feel free to reach out:

-   **GitHub**: [eyakimoff](https://github.com/yourusername)
-   **LinkedIn**: [Eric Yakimoff](https://www.linkedin.com/in/eric-yakimoff-3537981a3/)
