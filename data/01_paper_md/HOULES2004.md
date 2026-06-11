**Original article**

# **Evaluation of the ability of the crop model STICS to recommend nitrogen fertilisation rates according to agro-environmental criteria**

Vianney HOULÈSa *, Bruno MARYa , Martine GUÉRIFb, David MAKOWSKIc , Eric JUSTESd

> a INRA, Unité d'Agronomie, rue Fernand Christ, 02007 Laon Cedex, France b INRA, Unité CSE, Domaine St-Paul, Site Agroparc, 84914 Avignon Cedex 9, France c INRA/INA-PG, UMR Agronomie, BP 01, 78850 Thiverval-Grignon, France d INRA, Unité d'Agronomie, Auzeville, BP 27, 31326 Castanet-Tolosan Cedex, France

> > (Received 16 July 2003; accepted 11 March 2004)

**Abstract** – The use of crop models for nitrogen fertiliser management raises several issues. A first problem is to define suitable criteria for optimising nitrogen fertilisation in function of economic, quality and environmental objectives. A second issue is to assess the capacity of the crop model to predict the variables involved in the calculation of the criteria such as grain yield, grain protein content, residual soil mineral nitrogen or nitrogen balance. A third issue is to evaluate the results obtained by applying the decision rules selected by the crop model. The three problems are considered in this paper in the case of winter wheat and the STICS model. Fourteen field experiments with various N fertilisation strategies were used for evaluating the model. STICS predicted grain yield and nitrogen balance more accurately than protein content and soil mineral N at harvest. Among the eight criteria tested for optimising N fertilisation, those using a maximal threshold on nitrogen balance seem to be the most valuable for satisfying agricultural and environmental objectives. Under conditions of environmental constraint, STICS was more efficient than the reference method (AZOBIL) at selecting the optimal nitrogen fertilisation scenario.

**crop model / agro-environmental criteria / evaluation / nitrogen fertilisation**

2. MATERIALS AND METHODS**

This study is organised into three parts. First, we perform a data-based evaluation of several agro-environmental criteria that may be used to select appropriate N fertilisation scenarios from various experimental treatments. At this stage, the criteria, named hereafter as 'decision criteria', are calculated from the measured values at harvest of three variables of agronomic and environmental interest: grain yield, grain protein content and soil mineral nitrogen. Second, the STICS crop model is used to predict the different variables taken into account by the agro-environmental criteria and the predicted values are compared with the observations. Finally, we evaluate the capacity of STICS to select appropriate N fertilisation scenarios.

### **2.1. Field experiments**

The data analysed in this study come from 14 nitrogen fertilisation experiments carried out on winter wheat in several sites in northern France. A description of the main characteristics of these experiments is given in Table I. The nitrogen treatments varied primarily in total N rates and secondarily in splitting schemes. In each site, N rates varied from 0 to a maximum that reached 240 to 400 kg ha–1. The Boigneville experiments were realised during two successive years on 15 locations within a heterogeneous field [24]. In order to limit the influence of this site among the databases used, we retained only three locations per year, chosen from among the most different soils according to their available water reserve. In La Cheppe and La Minière, several N treatments led to the same total N rate but had different types of splitting. In each experiment, a recommended N rate was calculated at the end of winter using the AZOBIL balance-sheet method [26] and was one of the N treatments (Tab. I). These different N rates and splitting patterns represent in this study the different scenarios to be evaluated, from among which the best will have to be selected according to agro-environmental criteria. The Chambry experiments were used in a previous study to estimate some parameters of the STICS model (v5) for the cultivar *Shango* according to the methodology used by Dorsainvil [11].

Three variables of agronomic and environmental interest were measured at harvest: grain yield, *GN* (Mg dry matter ha–1),

grain protein content, *GP* (% of grain dry matter), and soil mineral nitrogen content in the 0–90 cm layer, *SN* (kg N ha–1). The latter measurement was not performed in all treatments (see Tab. I). Mineral nitrogen in soil was extracted with KCl M solution (soil:solution = 1:2) and measured by continuous flow colorimetry. The amounts of ammonium N were always small, so that only nitrate is considered in the results. Grain nitrogen content was measured using the Kjeldahl or Dumas methods and multiplied by 5.7 to obtain grain protein content [12, 17].

### **2.2. Agro-environmental decision criteria**

We defined and compared 8 agro-environmental decision criteria with respect to N fertilisation strategies by taking into account simultaneously the grain yield, the grain protein content (as an indicator of crop quality) and an environmental variable related to the risk of N loss. Each criterion can be characterised by a 'gross margin' (*GM*) and a 'gross income' (*GI*), defined as follows. *GM* (€ ha-1) is the difference between the income associated with grain production and the cost of the N fertiliser applied. It is the same for all criteria and is calculated as follows [28]:

$$GM = \mathbf{g} \left( GP \right) \cdot GY - \mathbf{c} \cdot NR \tag{1}$$

where *NR* is the total nitrogen rate (kg ha–1), *GP* is the grain protein content (%), *GY* is the grain yield (Mg ha–1) obtained for the rate *NR*, *g* is the function (€ Mg–1) that gives the price of wheat versus *GP* and *c* is the cost of the N fertiliser (€ kg–1). Grain prices were set equal to current values used by cooperatives in 2002. We used the following values:

*g(GP)* = 86.25 if *GP* ≤ 9 (2)

*g(GP)* = 86.25 + 3.93 (*GP–*9) if 9 < *GP* ≤ 12.5 (3)

*g(GP)* = 100 if *GP* > 12.5 (4)

*c* = 0.60. (5)

The gross margin, *GM*, represents approximately the variable part of the farmer's income, since EU subsidies may represent about half of the farmer's income. Those are not considered because they are independent of crop production.

The 'gross income', *GI*, is a function of *GM* and a 'penalty function' related to an environmental variable (Tab. II). For some criteria, the penalty function is nil and the environmental constraint is accounted differently (see below). Eight different penalty functions were considered. The penalty function considered in the criteria 1–2 uses the nitrogen balance, *NB* (kg ha–1), defined as the difference between N inputs as fertiliser and N outputs as wheat grains. The CORPEN office1 in France has proposed this balance as a basis for evaluating the risk of nitrogen losses. It is calculated as:

$$NB = NR - 10. \, GY. \, GP\% . \, \text{7.} \tag{6}$$

The N balance is converted into a penalty function using the taxation coefficient α (Tab. II). We considered two values for the parameter, α: 0.23 and 1.50 € kg–1. The first one corre-

**Table II.** Expression of eight agro-environmental criteria for evaluating nitrogen fertilisation strategies. GI = 'gross income', GM = 'gross margin', NB = N balance, SN = soil mineral nitrogen at harvest, TNB = threshold for N balance, TSN = threshold for soil mineral nitrogen at harvest (see definitions in the text).

| Criterion # | Criterion expression | Constraint | Parameter value  |
|-------------|----------------------|------------|------------------|
| 1           | GI = GM – α NB       | –          | α = 0.23 € kg–1  |
| 2           | GI = GM – α NB       | –          | α = 1.50 € kg–1  |
| 3           | GI = GM –<br>β<br>SN | –          | β = 1.00 € kg–1  |
| 4           | GI = GM –<br>SN<br>β | –          | β = 6.00 € kg–1  |
| 5           | GI = GM              | NB < TNB   | TNB = 90 kg ha–1 |
| 6           | GI = GM              | NB < TNB   | TNB = 60 kg ha–1 |
| 7           | GI = GM              | SN < TSN   | TSN = 35 kg ha–1 |
| 8           | GI = GM              | SN < TSN   | TSN = 20 kg ha–1 |

sponds to that proposed in a French project elaborated by the CORPEN, which is a low level of taxation. It can be considered as a reference criterion, not very different from the present situation. The second one is more severe and allows us to study the effect of a higher environmental tax.

A second environmental variable is considered in criteria 3 and 4: the amount of soil mineral nitrogen at harvest (*SN*). This variable is an indicator of the risk of nitrate pollution. It is predicted by crop models such as STICS and can be measured in field experiments. It is converted into a penalty function through the taxation parameter β that has been set either to a low (1 € kg–1) or a high level (6 € kg–1). The low level corresponds approximately to the threshold given by Makowski et al. [28], and the high level is 6 times higher, similarly to the parameter α.

The best N fertilisation strategy using criteria 1–4 is the strategy maximising the gross income. Another approach consists of selecting the strategy maximising the gross margin *GM* and satisfying an environmental constraint. This approach is considered in the criteria 5–8. The constraint is defined by a maximum threshold either on N balance (criteria 5–6) or on soil mineral N at harvest (criteria 7–8). The best strategy with criteria 5–8 is the strategy maximising GM, among all the strategies satisfying the constraint. If no strategy can satisfy the constraint, the strategy giving the lowest value for the environmental variable is selected. Again, two thresholds are considered for each environmental variable: a high one (criteria 5 and 7) and a lower one, thus more severe (criteria 6 and 8). The eight decision criteria were calculated for the different nitrogen fertilisation rates applied in the experiments. The decision criteria were first calculated with the measured values of yield, grain protein content, N balance and soil mineral nitrogen at harvest, and in a second stage, with the values estimated using STICS.

# **2.3. The STICS model**

The STICS model has already been described in several papers [7, 8]. It simulates the water, carbon and nitrogen dynamics in the soil-plant system at a daily time step. It considers the effects of water and nitrogen stress on plant growth and grain yield. The nitrogen balance, *NB*, depends on nitrogen

<sup>1</sup> Comité d'Orientation pour la Réduction de la Pollution des Eaux par les Nitrates, created by the French Ministry of Agriculture.

uptake which is calculated as the result of plant demand and soil supply, the latter being affected by root growth and nitrate concentration in soil layers. Soil mineral nitrogen, *SN*, is the balance between production and consumption processes: N fertilisation and mineralisation, N uptake, N leaching and N losses from fertiliser.

# **2.4. Comparison between observed and simulated values**

We performed two sets of simulations with STICS for each of the 14 experiments. The first set uses the actual climate of the year of the experiment during the whole growing season. The resulting simulations are called 'descriptive simulations'. The second set mimics a situation of real-time selection of a fertilisation strategy: it considers the actual climate until the date of the second nitrogen application (the date at which we want to define the N rate using the model), and then a probable climate up to harvest time. The probable climate was defined by the last thirty years of actual climate at the nearest weather station. The resulting simulations were averaged over the 30 years for each experiment. This second set of simulations is called 'predictive simulations'. From a practical point of view, the predictive simulations are more interesting. However, the comparison of the predictive and descriptive simulations is useful to study the effect of climate uncertainty on the results of the crop model.

Five types of variables are calculated from the STICS simulations for each experiment: grain yield, *GY*, grain protein content, *GP*, soil mineral nitrogen at harvest, *SN*, nitrogen balance, *NB* and gross margin, *GM*. For each variable, observed and simulated values are compared according to the following criteria:

– the root mean square error (RMSE)

$$RMSE = \sqrt{\frac{1}{N} \sum_{i} (Z_i - \hat{Z})^2} \tag{7}$$

where *N* is the number of observations, and *Zi* and represent the observed and simulated variables, respectively. *Zi* ˆ

- the parameters of the linear regression: slope *a*, intercept *b* and determination coefficient r2;
- the decomposition of the mean square error between the systematic mean square error (*RMSEs*) and the unsystematic mean square error (*RMSEu*) [38]:

$$RMSE_{\bar{s}} = \sqrt{\frac{1}{N} \sum_{i} (b + a.Zi - Zi)^2} \tag{8}$$

$$RMSE = \sqrt{\frac{1}{N} \sum_{i} (b + a.Zi - \hat{Z})^2} \,. \tag{9}$$

This decomposition allows us to distinguish between the systematic component of the error, attributed to a bias, and a random error (unsystematic).

The criteria 7–9 are calculated for several variables: *GY, GP, SN* and *NB*.

# **2.5. Evaluation of the capacity of STICS to select satisfactory strategies**

The last type of evaluation consists of assessing the capacity of STICS to identify the best scenario according to a given decision criterion. We adopted, in a simplified way, the method proposed by Antoniadou and Wallach [1] and applied by Makowski and Wallach [27]. For each of the eight decision criteria displayed in Table II and for each of the two sets of simulations, we first compared the scenario selected by STICS (i.e. the scenario corresponding to the minimal N rate that maximises GI) to the best observed scenario determined from the measurements obtained in the experiment. Therefore, we evaluated the consequence of choosing a scenario with STICS by calculating, for each experiment, the difference between the value of the observed decision criterion corresponding to the N rate selected by STICS and that obtained with the true best scenario. We finally examined whether the scenario selected by STICS could satisfy the environmental constraint defined by the criteria 5–8. The same type of evaluation was also performed for the balance-sheet method (AZOBIL). This was possible because each experiment included a treatment corresponding to the AZOBIL recommended rate.

<sup>*</sup> Corresponding author: houles@avignon.inra.fr

| Experiment# | Location    | Soil type               | Year | Cultivar | N fertiliser rates tested (kg ha–1) * | SN** |
|-------------|-------------|-------------------------|------|----------|---------------------------------------|------|
| 1           | Boigneville | Stony loam              | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 2           | Boigneville | Shallow stony loam      | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 3           | Boigneville | Very shallow stony loam | 1998 | Soissons | 0-120-160-200-240                     | Yes  |
| 4           | Boigneville | Shallow stony loam      | 1999 | Soissons | 0-120-160-200-280                     | Yes  |
| 5           | Boigneville | Stony loam              | 1999 | Soissons | 0-140-180-220-300                     | Yes  |
| 6           | Boigneville | Very shallow stony loam | 1999 | Soissons | 0-120-160-200-280                     | Yes  |
| 7           | Thibie      | Chalk                   | 1994 | Forby    | 80-120-160-200-240-280-320            | –    |
| 8           | Thibie      | Chalk                   | 1995 | Apollo   | 0-80-120-160-200-240-280-320          | Yes  |
| 9           | Thibie      | Chalk                   | 1998 | Shango   | 0-100-135-150-200-210-250-300-350-400 | –    |
| 10          | Thibie      | Chalk                   | 1999 | Shango   | 0-100-135-150-200-210-250-300-350-400 | –    |
| 11          | La Minière  | Deep loam               | 2002 | Shango   | 0-110-150-190-230                     | –    |
| 12          | La Cheppe   | Chalk                   | 2002 | Shango   | 0-140-220-300                         | Yes  |
| 13          | Chambry     | Sandy loam              | 2000 | Shango   | 0-60-120-180-240-300                  | –    |
| 14          | Chambry     | Loam                    | 2001 | Shango   | 0-120-160-220-240-280                 | –    |