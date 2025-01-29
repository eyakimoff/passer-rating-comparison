import streamlit as st

st.markdown(
    """# Passer Rating Analysis: Traditional vs. Refined Formulas

## Overview

This project examines the effectiveness of two passer rating formulas: the traditional passer rating and a refined version that removes the thresholds present in the original calculation. By analyzing quarterback game data, we evaluate how well each formula correlates with game outcomes, assess their predictive capabilities, and highlight key differences in their performance.

---

## Key Findings

### Outcome Correlation

-   **Traditional Passer Rating Correlation with Game Outcome**: 0.4576
-   **Refined Passer Rating Correlation with Game Outcome**: 0.4080

The traditional model exhibits a stronger correlation with game outcomes, indicating a better alignment between the passer rating and a quarterback's ability to lead a team to victory.

---

## Model Performance Summary

### Traditional Rating Model:

-   **Accuracy**: 70%
-   **Precision**:
    -   Losses (0): 0.68
    -   Wins (1): 0.71
-   **Recall**:
    -   Losses (0): 0.72
    -   Wins (1): 0.67
-   **F1-score**:
    -   Losses (0): 0.70
    -   Wins (1): 0.69

#### Confusion Matrix:

```
[[1015  391]
 [ 468  945]]
```

---

### Refined Rating Model:

-   **Accuracy**: 67%
-   **Precision**:
    -   Losses (0): 0.65
    -   Wins (1): 0.70
-   **Recall**:
    -   Losses (0): 0.73
    -   Wins (1): 0.61
-   **F1-score**:
    -   Losses (0): 0.69
    -   Wins (1): 0.65

#### Confusion Matrix:

```
[[1029  377]
 [ 547  866]]
```

---

## Observations

1. **Traditional Model Shows Better Balance**:

    - The traditional model has higher accuracy (70%) and a better balance in precision and recall across both win and loss outcomes.
    - It has a slightly lower recall for losses (72%) compared to the refined model (73%), but a significantly higher recall for wins (67% vs. 61%).

2. **Refined Model Overcorrects Toward Loss Prediction**:

    - The refined model is better at predicting losses (higher recall for 0), but at the expense of correctly identifying wins.
    - The increased false negatives (547 vs. 468) indicate that the refined model underestimates winning performances more often than the traditional model.

3. **Confusion Matrix Differences**:
    - The refined model has more misclassified wins, leading to a lower overall accuracy (67% vs. 70%).
    - The traditional model's more even trade-off between predicting wins and losses makes it a stronger predictor of game outcomes.

---

## ROC Curve and AUC Analysis

-   **Traditional Model AUC**: Expected to be higher, supporting better classification performance.
-   **Refined Model AUC**: Expected to be lower, reinforcing its struggle with win classification.

---

## Conclusion

The traditional passer rating remains the more reliable predictor of winning games, with a higher correlation to game outcomes and better overall accuracy. The refined passer rating, while removing artificial thresholds, emphasizes losses more heavily and struggles with correctly identifying winning performances.

If the goal is predicting game outcomes, the traditional model is preferable. However, the refined model provides a unique perspective, emphasizing poor performances and missteps more heavily. Further refinements could help balance its evaluation between strong and weak performances.

---

## Visualizations

This project includes interactive visualizations to explore:

-   **ROC Curves**: Compare the AUC values of both formulas.
-   **Top Performances**: Visualize all-time great games ranked by each formula.
-   **Individual Player Analysis**: Assess quarterback performance trends over time.

---

## How It Works

1. **Data Collection**:
    - Retrieves live and historical game data using APIs.
    - Processes quarterback performance statistics.
2. **Formula Application**:
    - Applies both the traditional and refined formulas to game logs.
3. **Machine Learning Evaluation**:
    - Models are evaluated using metrics such as accuracy, precision, recall, and AUC.
4. **Interactive Streamlit App**:
    - Explore findings through a user-friendly interface.

---

## Passer Rating Formulas

### Traditional Passer Rating Formula

```
a = (CMP/ATT - 0.3) * 5
b = (YDS/ATT - 3) * 0.25
c = (TD/ATT) * 20
d = 2.375 - (INT/ATT * 25)
Passer Rating = ((a + b + c + d) / 6) * 100
```

Where:

-   **ATT** = Passing attempts
-   **CMP** = Completions
-   **YDS** = Passing yards
-   **TD** = Touchdown passes
-   **INT** = Interceptions

_Each component is capped between 0 and 2.375._

### Refined Passer Rating Formula

```
b = (YDS/ATT - 3) * 0.25
c = (TD/ATT) * 20
d = 2.375 - (INT/ATT * 25)
Passer Rating = ((b + c + d) / 6) * 100
```

This version removes completion percentage as a component and eliminates artificial thresholds.

---

## Contact

For questions or feedback, feel free to reach out:

-   **GitHub**: [eyakimoff](https://github.com/yourusername)
-   **LinkedIn**: [Eric Yakimoff](https://www.linkedin.com/in/eric-yakimoff-3537981a3/)
"""
)
