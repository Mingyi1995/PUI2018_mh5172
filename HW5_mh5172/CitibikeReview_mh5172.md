# CitibikeReview_mh5172

### Null Hypothesis
You bring up an interesting null hypothesis, and expressed it proporly in both words and formula.

### Data you selected
The data you selected supports your hypothesis well, however, I think it is better if you can exclude those data not in the time you focus on. In this way, your plot will be more clear. Moreover, the data of total amount of young and old riders in 7pm - 3pm are supposed to be calculated and plotted.

### According to reading: Relative Risk/ Odds Ratio
According to the reading material, as the data set is paired, and the young/ old riders is categorical, we should use relative risk or odds ratio to test.

#### [Relative Risk](https://en.wikipedia.org/wiki/Risk_ratio)
Risk ratio is used in the statistical analysis of the data of experimental, cohort and cross-sectional studies, to estimate the strength of the association between treatments or risk factors, and outcome. For example, it is used to compare the risk of an adverse outcome when receiving a medical treatment versus no treatment (or placebo), or when exposed to an environmental risk factor versus not exposed.

Assuming the causal effect between the exposure and the outcome, values of RR can be interpreted as follows:

RR = 1 means that exposure does not affect the outcome;
RR < 1 means that the risk of the outcome is decreased by the exposure;
RR > 1 means that the risk of the outcome is increased by the exposure.

#### [Odds Ratio](https://en.wikipedia.org/wiki/Odds_ratio)
In statistics, the odds ratio (OR) is one of three main ways to quantify how strongly the presence or absence of property A is associated with the presence or absence of property B in a given population. If each individual in a population either does or does not have a property "A" (e.g. "high blood pressure"), and also either does or does not have a property "B" (e.g. "moderate alcohol consumption") where both properties are appropriately defined, then a ratio can be formed which quantitatively describes the association between the presence/absence of "A" (high blood pressure) and the presence/absence of "B" (moderate alcohol consumption) for individuals in the population. This ratio is the odds ratio (OR) and can be computed following these steps:

For a given individual that has "B", compute the odds that the same individual has "A".
For a given individual that does not have "B", compute the odds that the same individual has "A".
Divide the odds from step 1 by the odds from step 2 to obtain the odds ratio (OR).
### According to slides: Z-test/ Chi-Square
#### [Z-Test](https://en.wikipedia.org/wiki/Z-test)
A Z-test is any statistical test for which the distribution of the test statistic under the null hypothesis can be approximated by a normal distribution. Because of the central limit theorem, many test statistics are approximately normally distributed for large samples. For each significance level, the Z-test has a single critical value (for example, 1.96 for 5% two tailed) which makes it more convenient than the Student's t-test which has separate critical values for each sample size. Therefore, many statistical tests can be conveniently performed as approximate Z-tests if the sample size is large or the population variance is known. If the population variance is unknown (and therefore has to be estimated from the sample itself) and the sample size is not large (n < 30), the Student's t-test may be more appropriate.

In this case, we can regard young and older riders as two sample, and use Z-Test to calculate the difference between those two samples is significant or not.

#### [Chi-Square](https://en.wikipedia.org/wiki/Z-test)
The chi-squared test is used to determine whether there is a significant difference between the expected frequencies and the observed frequencies in one or more categories.

In this case, we should calculate the expected frequencies of young and old riders in night. And assume that the ratio of night riders among young and old group is the same.
