# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a logistic regression classifier implemented using scikit-learn.

## Intended Use

This model is intended for binary classification where the goal is to predict the probability of a binary outcome based
on the provided features.

## Training Data

The data comes from the Census Income dataset: https://archive.ics.uci.edu/dataset/20/census+income.

The features in the data are the age, workclass, fnlgt, education, education-num, marital-status, occupation,
relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, and the target is the salary (under
and over 50K a year).

The information about each feature, as well as its types, can be found at the link mentioned above.

Training data can be found at data/train.csv

The evaluation data consists of an 80% of the total data.

## Evaluation Data

Evaluation data can be found at data/test.csv

The evaluation data consists of a 20% of the total data.

## Metrics

Precision: 0.6962025316455697
Recall: 0.24475524475524477
Fbeta: 0.36218250235183447

## Ethical Considerations

The dataset is anonymized and does not contain any identifiable information.

Also note that the dataset is a sample of the Census Income dataset, which might have biases related to race, gender,
and social status. These biases could affect the predictions and lead to unfair outcomes for some groups.

## Caveats and Recommendations

"Extraction was done by Barry Becker from the 1994 Census database. A set of reasonably clean records was extracted
using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0))"

As we can see in this statement from https://archive.ics.uci.edu/dataset/20/census+income, the dataset consists of data
from 1994. We may therefore consider this an outdated sample that may not represent the current statistical
representation of population.

Also consider including more data from other sources as the metrics for this model can improve.
