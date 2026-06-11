https://doi.org/10.1016/j.eja.2022.126501>

Available online 22 March 2022 1161-0301/©

![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](www.sciencedirect.com/science/journal/11610301) 

European Journal of Agronomy

![](_page_0_Picture_4.jpeg)

journal homepage: [www.elsevier.com/locate/eja](https://www.elsevier.com/locate/eja)

# Assimilating leaf area index data into a sugarcane process-based crop model for improving yield estimation

![](_page_0_Picture_7.jpeg)

Izael Martins Fattori Junior a,* , Murilo dos Santos Vianna b , Fabio ´ Ricardo Marin a

a *University of Sao* ˜ *Paulo, "Luiz de Queiroz" College of Agriculture (Esalq), Piracicaba, SP, Brazil* b *Institute of Crop Science and Resource Conservation (INRES), University of Bonn, Bonn 53111, Germany* 

## ARTICLE INFO

*

**2. Material and methods**

## *2.1. Field experiments description*

In total, we used a dataset of 22 experiments described in [Table 1](#page-2-0). Experiments 1–3 were conducted at the College of Agriculture "Luiz de Queiroz" (Esalq) of University of Sao ˜ Paulo (USP) in Piracicaba, Brazil (Lat. 22◦41′ 55′′ S, long. 47◦38′ 34′′ W, alt. 540 m a.m.s.l.). Chopped stalks of the RB867515 cultivar (Exps. 1 and 2) were used for planting 13–15 buds m− 1 at 1.4 m row spacing down to a depth of 0.2 m. Experiment 3 was conducted in the first ratoon of experiment 1 (sugarcane re-growth). Agricultural practices were adopted to represent high-yield farming systems and to ensure the crop was free from pests, diseases, and nutritional stress. The climate is characterized by a hot and humid summer with dry winter (Cwa - Koppen ¨ classification), and the soil of the three experiments is classified as Typic Hapludox. For these experiments, daily solar radiation, maximum and minimum air temperature, rainfall, wind speed, and relative air humidity were collected adjacent to the experiment site using an automatic weather station. The experimental area was irrigated by a center-pivot. The water balance was monitored to manage the water applications and ensure crops were not exposed to water stress throughout the growing cycle; for these, irrigation was triggered every time the soil moisture reached 80% of the total available soil water. Five locations were randomly selected at the beginning of each season, where LAI samples were taken with an LAI-2200 instrument (LI-COR Bioscience), following user manual recommendations for row crops ([Gonçalves et al., 2020)](#page-10-0). LAI measurements were taken in a frequency of 5–20 days in experiments 1–3. Stalk fresh yield (SFY, Mg ha− 1 ) was measured only at the end of the crop season by mechanical harvesting for the three experiments. Experiments 1 and 2 during the crop season suffered from lodging, after heavy rain events and after the crop reaches a high SFY and stalks height. This caused changes in LAI during the season and accelerate the decrease in LAI at the late stage.

We also used experimental data of previous studies (Experiments 4–22, [Table 1](#page-2-0)) conducted in a diversity of environments and using different cultivars ([Marin et al., 2015, 2011; Suguitani, 2006; Vianna](#page-11-0)  [et al., 2020)](#page-11-0), and following a similar protocol of the experiments 1–3 above described. Experiments 4–15 had the LAI sampled 1–7 times during the crop season, and SFY sampled only at the end of the crop

## <span id="page-2-0"></span>**Table 1**

|  | Description of experimental datasets used in the simulations. Only experiments 16–22 were used for model calibration. |  |  |
|--|-----------------------------------------------------------------------------------------------------------------------|--|--|
|--|-----------------------------------------------------------------------------------------------------------------------|--|--|

| Experiment<br>Number | Location                                      | Planting<br>date       | Harvest<br>date        | Planting<br>Type      | Weather†                 | Soil‡                      | Water<br>treatment | Variety  | Ref.          |
|----------------------|-----------------------------------------------|------------------------|------------------------|-----------------------|--------------------------|----------------------------|--------------------|----------|---------------|
| 1                    | Piracicaba/SP 22◦41' S,<br>47◦38'W, 560 m     | 10/05/<br>2018         | 11/30/<br>2019         | Plant                 | 21.6 ◦C, 1230<br>mm, CWa | Typic<br>Hapludox          | Irrigated          | RB867515 | ¥             |
| 2                    |                                               | 11/06/                 | 11/30/                 | Plant                 |                          | Typic                      | Irrigated          | RB867515 |               |
| 3                    |                                               | 2018<br>11/31/         | 2019<br>11/04/         | 1st                   |                          |                            | Irrigated          | RB867515 |               |
| 4                    |                                               | 2019<br>10/29/         | 2020<br>07/15/         | Ratoon*<br>Plant      |                          |                            | Irrigated          | R570     | Suguitani     |
| 5                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | R570     | (2006)        |
| 6                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | RB72454  |               |
| 7                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | RB72454  |               |
| 8                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | SP832847 |               |
| 9                    |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | SP832847 |               |
| 10                   |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Irrigated          | NCo376   |               |
| 11                   |                                               | 2004<br>10/29/         | 2005<br>07/15/         | Plant                 |                          |                            | Rainfed            | NCo376   |               |
| 12                   | Aparecida do Taboado/MS                       | 2004<br>07/01/         | 2005<br>09/08/         | Plant                 | 23.5 ◦C, 1560            | Typic                      | Rainfed            | RB867515 | Marin et al.  |
|                      | 20◦05 S, 51◦18′<br>W, 335 m                   | 2006                   | 2007                   |                       | mm, Aw                   | Hapludox<br>Typic          |                    |          | (2015)        |
| 13                   | Colina/SP 20◦25′<br>S,<br>48◦19′<br>W, 590 m  | 02/10/<br>2004         | 06/15/<br>2005         | Plant                 | 22.8 ◦C, 1363<br>mm, Cwa | Typic<br>Hapludox          | Rainfed            | RB867515 |               |
| 14                   | Olimpia/SP 20◦26′<br>S,<br>48◦32′<br>W, 500 m | 02/10/<br>2004         | 06/15/<br>2005         | Plant                 | 23.3 ◦C, 1349<br>mm, Cwa | Typic<br>Typic<br>Hapludox | Rainfed            | RB867515 |               |
| 15                   | Coruripe/AL 10◦07′<br>S,                      | 08/16/                 | 09/15/                 | Plant                 | 21.6 ◦C, 1401            | Typic<br>Fragiudult        | Rainfed            | RB867515 |               |
| 16                   | 36◦10'W, 16 m<br>Piracicaba/SP 22◦41' S,      | 2005<br>12/06/         | 2006<br>10/15/         | Plant                 | mm, As<br>21.6 ◦C, 1230  | Typic<br>Typic             | Irrigated          | RB867515 | Vianna et al. |
| 17                   | 47◦38'W, 560 m                                | 2012<br>10/15/         | 2013<br>07/15/         | 1st                   | mm, CWa                  | Hapludox<br>Typic          | Irrigated          | RB867515 | (2020)        |
| 18                   |                                               | 2013<br>10/15/         | 2014<br>07/15/         | Ratoon*<br>1st Ratoon |                          |                            | Irrigated          | RB867515 |               |
| 19                   |                                               | 2013<br>07/15/         | 2014<br>06/08/         | 2nd                   |                          |                            | Irrigated          | RB867515 |               |
| 20                   |                                               | 2014<br>07/15/         | 2015<br>06/08/         | Ratoon*<br>2nd        |                          |                            | Irrigated          | RB867515 |               |
| 21                   |                                               | 2014<br>06/08/         | 2015<br>06/08/         | Ratoon<br>3rd         |                          |                            | Irrigated          | RB867515 |               |
| 22                   |                                               | 2015<br>06/08/<br>2015 | 2016<br>06/08/<br>2016 | Ratoon*<br>3rd Ratoon |                          |                            | Irrigated          | RB867515 |               |

† Respectively: mean annual temperature, annual total rainfall, Koeppen Classification.

‡ U.S. Soil Taxonomy.

¥ Experimental data collected for this study and not previously published.

* With mulch cover.

season. The experiments 16–22 were only used for DS calibrations and had tiller population, stalk diameter, stalk height, LAI, SFY, stalk, and leaf dry mass, and sucrose content on fresh cane basis (POL) obtained by regular sampling ([Vianna et al., 2020](#page-11-0)).

Soil characteristics and management practices such as planting and harvesting dates, row spacing, mulch cover and irrigation applications (mm d− 1 ) on each site were prescribed to the model as input information. Also, for experiments 3, 17, 19 and 21 a total of 12 Mg ha− 1 of green cane straw were considered for simulations. All other experiments were conducted at bare soil conditions.

The experiments 1–3 and 16–22 had the LAI sampled with the LAI-2200 and LAI-2000 respectively, which had an accuracy of 4%, according to the user manual ([Gonçalves et al., 2020)](#page-10-0). The other experiments had their LAI sampled with different sensors and methodology ([Marin et al., 2015, 2011; Suguitani, 2006)](#page-11-0); to maintain the response of the DA methods with the DS, we assumed the same accuracy for all observations.

# *2.2. Brief description of DSSAT/SAMUCA and calibration process*

The SAMUCA model is a PBM firstly developed by [Marin and Jones](#page-11-0)  [(2014)](#page-11-0), which is capable to simulate the growth and development of sugarcane crop, implementing an algorithm to describe processes related to phenology, canopy development, tillering, biomass accumulation, root growth, and water stress ([Marin et al., 2017](#page-11-0)). [Vianna et al.](#page-11-0)  [(2020)](#page-11-0) improved the SAMUCA model by including recent scientific findings on sugarcane growth at phytomer level, canopy assimilation, and tillering. In this new version, the model was adapted to operate the one-dimensional "tipping bucket" soil water balance and to incorporate the soil temperature to account for the trash blanket effect on sugarcane growth and water use. This presented a superior performance compared with the previous version and was comparable to other widely used PBMs for sugarcane. For this study, we used the SAMUCA model incorporated into the Decision Support System for Agrotechnology Transfer (DSSAT) platform version 4.8 [(Jones et al., 2003; Hoogenboom](#page-11-0) 

[et al., 2019; Vianna et al., 2020)](#page-11-0), namely DSSAT/SAMUCA (DS).

The model was calibrated for cultivar RB867515 by [Vianna at al.](#page-11-0)  [(2020),](#page-11-0) using experiments 16–22. A routine was designed to find crop parameters that minimize simulation errors by means of the RMSE ([Wallach et al., 2018)](#page-11-0). To avoid unrealistic parameters estimation, the constrained BFGS ("Broyden–Fletcher–Goldfarb–Shanno") optimization method ([Byrd et al., 1996)](#page-10-0) was employed assigning plausible range of parameters based on field observation and literature. To adapt the plant-module of SAMUCA within the soil-plant-atmosphere framework of DSSAT, the root growth parameters SRLMAX (Specific Root Length at Root Front), SRLMIN (Specific Root Length at Inner Roots Profile), and DSHOOT_EXT (Below ground shoots expansion rate) were re-calibrated (Table S1). The procedure was performed by eye-fitting using the same set of observations employed by [Vianna et al. (2020)](#page-11-0) (experiments 16–22) for which we obtained similar performance (Table S2).

#### *2.3. Description of data assimilation procedure*

Three different updating methods of DA were investigated in this study: EnKF, ES, and WM, which are described below. Also, standard DS simulations without DA were performed, which are thereafter called open-loop (OP) simulations. For each DA, the ability to deal with LAI assimilation and their performance with DS simulations were assessed, by comparing the simulation results of SFY at the end of the crop cycle. Therefore, the DS was adapted to read an input file with a new estimated vector of state variables at any time, regardless of the method. When new LAI values were assimilated by DS, the leaf area and dry weight were also updated at phytomer and field level to ensure the consistency of canopy representation.

## *2.3.1. Ensemble Kalman filter method*

The EnKF employs an analytic solution based on two related sources of information, in this case: PBM's outputs and field observations. These are synthesized to provide a better estimation, with lower variance. For that, the EnKF assumes that the observed data can be related to the state variable *xt* (LAI in the case of this study) at time *t* as shown in Eq. (1):

$$\mathbf{y} = \mathbf{H}\mathbf{x}_t + \mathbf{e} \tag{1}$$

where y is the observations vector; *H* is the observation operator that relates to *y*; *ε* is a Gaussian random error vector with a mean of zero and observation error covariance *R*. Also, the forecast of *xt* at *t* = *k* is Gaussian with mean *xf t*=*k* and error covariance *Pf t*=*k*. Under these assumptions, the estimated state and error covariance (*P*) are updated as:

$$\mathbf{x}_{r=k}^{\mu} = \begin{array}{c} \mathbf{x}_{r=k}^{\circ} + \mathbf{K}(\mathbf{y}_{r=k} \quad -H\mathbf{x}_{r=k}^{\circ}) \end{array} \tag{2}$$

$$P_{t=k}^{*} = \quad (I - KH)P_{t=k}^{\ell} \tag{3}$$

where *t* is the time index; *k* is the time of the observed data; *f* represents the prior state (called forecast) and *a* is the posterior state (called analysis); *I* is the identity matrix; and *K* represents the Kalman gain calculated by Eq. (4):

$$\mathbf{K} = \quad \quad P_{t=k}^{\zeta} H^T \left( H P_{t=k}^{\zeta} H^T + \mathcal{R}_{t=k} \right)^{-1} \tag{4}$$

The EnKF forecast and analysis error covariance *Pf* come directly from an ensemble of the model simulations:

$$P^{\ell}H^{T} = \left(N_{\pi} - 1\right)^{-1} \sum_{n=1}^{N_{\pi}} \left(\mathbf{x}_{n}^{\ell} - \overline{\mathbf{x}}^{\ell}\right) \left(H\mathbf{x}_{n}^{\ell} - H\overline{\mathbf{x}}^{\ell}\right)^{T} \tag{5}$$

where *Ne* is the number of ensemble members, *n* is a running index for an ensemble member, and *xf* are the ensemble mean calculated as:

$$\overline{\mathbf{x}}' = \quad N_{\mathbf{e}}^{-1} \sum_{n=1}^{N_{\mathbf{e}}} \mathbf{x}_{n}' \tag{6}$$

In our study, we only used the LAI retrieved from ground

measurements as a state variable for DA methods. Thus, *H* can be taken as an identity matrix (*H* = 1), with that we can rewrite the Eqs. (2), (4) and (5) as Eqs. (7)–(9).

$$\mathbf{x}_{r=k}^{\boldsymbol{\mu}} = \mathbf{x}_{r=k}^{\boldsymbol{\ell}} + \mathbf{K} \left( \mathbf{y}_{r=k} - \mathbf{x}_{r=k}^{\boldsymbol{\ell}} \right) \tag{7}$$

$$K = \quad P_{t=k}^{\ell} \left( P_{t=k}^{\ell} + R_{t=k} \right)^{-1} \tag{8}$$

$$P^{\ell} = \quad \left(N_r - 1\right)^{-1} \sum_{n=1}^{N_r} \left(\mathfrak{x}_n^{\ell} - \quad \mathfrak{x}^{\ell}\right) \left(\mathfrak{x}_n^{\ell} - \quad \mathfrak{x}^{\ell}\right)^T \tag{9}$$

In EnKF, the observed data are perturbed with the Monte Carlo approach to generate an ensemble, based on the data uncertainty represented by the variance. When used together with PBMs, there are two methods to generate the ensemble members ([Zhuo et al., 2019)](#page-12-0): the first method adds a Gaussian perturbation to the PBM state variables output. The second, add a Gaussian perturbation to the model input parameters.

In this study, we used the second method to generate the ensemble members. Thus, we selected the most sensitive parameters to LAI based on a sensitivity analysis, using the Fourier amplitude sensitivity test (FAST) ([Cukier et al., 1973; Saltelli et al., 1999)](#page-10-0) from the SALlib library (<https://salib.readthedocs.io/en/latest/index.html>). These were MAXGL (maximum number of green leaves a tiller can hold), MLA (maximum leaf area), PLASTOCHRON (thermal time required for the appearance of one new phytomer), INIT_LF_AREA (initial leaf area of first appeared leaf), and MID_TT_LF_GRO (thermal time where leaves can achieve half of its maximum biomass) (Table S1). These parameters were then perturbed to generate an ensemble (40 members), with a gaussian distribution and an uncertainty level of 10% before the simulation starts, as recommended for [Ines et al. (2013)](#page-11-0) and [Curnel et al.](#page-10-0)  [(2011)](#page-10-0) to optimize the time of the simulation and model accuracy.

After generating the set of parameters, DS runs until the first observed LAI is available. At this point, we calculated in sequence *K* and the vector *xa t*=*k* (Eqs. (7) and (8)), that was considered the optimal estimation of LAI. This step also included small inflation of 1.5 for LAI in ensemble members, in the case of their variability becoming too low ([Ines et al., 2013)](#page-11-0). This step ensured that the observations were not systematically rejected during assimilation. After that, the estimated LAI is stored in an input file for the next simulations, and runs were re-initialized until the next observations became available.

# *2.3.2. Ensemble smoother method*

The ES has the same assumptions and equations as the EnKF. The difference between them is the number of assimilations. The ES assimilates all observed data at once, regardless of the acquisition time. Thus, the DS predicted all the state variables until the end of the simulations, using 40 ensemble members and considering the parameter perturbation procedure. At the prediction step, the DS output is then compared with all observations. For each observation, the Eqs. (7)–(9) were applied, and the term *xa t*=*k* was estimated. Thereafter, the DS was reinitialized and the *xa t*=*k* was assimilated at each time, which reduces the number of model re-initialization and made it easier to couple with any program that was not created to DA adaptation, like the majority of PBM ([Lee et al., 2016; Yu et al., 2020](#page-11-0)).

# *2.3.3. Weighted mean method*

The WM methodology follows the approach proposed by [Tewes et al.](#page-11-0)  [(2020a),](#page-11-0) which assumes that the PBMs OP ensemble simulation runs from the beginning to the end of the crop growing cycle. One or a few members of the PBMs simulations that were close to the observed variable receive a greater weight for the state vector estimation.

The same crop parameters used for EnKF and ES were used to create the ensemble members in this method. However, different from the other DA, a uniform distribution is assumed to create the 40 sets of parameters, and the maximum and the minimum values of the distribution range were assumed to be ± 10% of the selected parameters <span id="page-4-0"></span>mean value (Table S1). After the ensemble simulations run, a Python script reads the output file of the DS and performs the WM calculation as follows.

To predict the state *X*̂(*t*) of the system, we used the weighted mean of the ensemble *Xi*(*t*):

$$\widehat{X}(t) = \begin{array}{c} \frac{\sum_{i=1}^{N} \boldsymbol{w}_{i}(t)X_{i}(t)}{\sum_{i=1}^{N} \boldsymbol{w}_{i}(t)} \end{array} \tag{10}$$

where each weight *w* of ensemble member *i* at day *t* is calculated as follow:

$$\rho_i(t) = P(O(t_k)|X_i(t_k)) \quad \text{for} \quad t_k \quad \le t \quad \le \quad t_{k+1} \tag{11}$$

where *P* is the likelihood from that the observational *O* at time *tk* approximates the simulated value. The observational error was assumed as a normal distribution, where *O*(*tk*) is mean and *σk* the standard deviation of the distribution. Thus, we applied the following equation for the calculation of the likelihood *P*:

$$P(O(t_k)|X_i(t_k)\ ) = \frac{1}{\sqrt{2\pi\sigma_k^2}} \exp\left(-\frac{\left(h(\left(t_k\right)) - \quad O(t_k)\right)^2}{\sigma_k^2}\right) \tag{12}$$

where *h* mapped the states to the observational variables.

The calculated weights for the first observation were then propagated until the next observation, and they were also used to calculate the weighted mean of other state variables. For example, the SFY retrieved from the simulation members that have LAI closer to the observations will receive more weight. When a new observation is available, the weighted mean is recalculated, and when observations were outside the ensemble members, the entire weights were given to the closest member. Contrary to other existing DA updating methods, no state variables are updated during the simulation runs. Therefore, observations are used to select the output simulations' members of the PBM, not change the state variable directly in the PBM, during the run, which is common for the other DA methods.

## *2.4. Data analysis*

The performance of each DA was evaluated by comparing simulated and observed SFY by using root mean squared error (RMSE) and coefficient of determination (R2 ). We also compared each DA with OP simulation to select the best approach for each experiment. It should be noted that we used the absolute error (AE) to compare the SFY at the end of the crop cycles for each experiment. To quantify if and how much each DA method reduced the SFY simulation error, the difference between the AE of three DA methods against the AE of OP simulations is calculated. Negative differences between DA and OP error, indicate better performance in DA method than the OP simulation.

## *2.5. Effect of genotype-specific calibration on DA methods*

The DS model was previously calibrated and evaluated for the RB867515 cultivar, with experiments 16–22 ([Table 1)](#page-2-0). This cultivar is one of the main Brazilian cultivars present in more than 20% of sugarcane plantations in Brazil [(Vianna et al., 2020](#page-11-0)); and which is also present in seven of the fifteen field experiments not utilized in the calibration procedure [(Table 1)](#page-2-0). The remaining experiments (4–11) used four different cultivars, where three were also commonly planted in Brazil (R570, RB72454, and SP832847). The NCo376 is one of the main South African cultivars for which the DSSAT/Canegro model was extensively tested ([Marin et al., 2011; Singels et al., 2008)](#page-11-0).

Therefore, this analysis aimed to investigate the influence of assimilating data from different genotypes but considering fixed crop parameters previously calibrated for the RB867515 cultivar. For that, we performed simulations for OP and three DA methods (EnKF, ES, and

WM) using the same calibration for all experiments (Table S1). The effect of employing genotype-specific calibration was then evaluated by grouping the experiments by cultivar type and comparing the RMSE of the cultivar group with the calibrated cultivar (RB867515). This resulted in two groups of experiments: (i) the experiments with cultivar RB867515, considering in this group only those not directly used for calibration (1–3 and 12–15); (ii) the experiments with different cultivars, with no genotype-specific calibration. These results provide practical information to whether PBMs must be calibrated prior to being used with DA methods across cultivars, and what is the level of uncertainty of this procedure.

## *2.6. Effect of the number and timing of observations on DA methods*

To assess the impact of number and timing of LAI observations on the performance of SFY simulations, we ran a simulation experiment omitting and prescribing LAI observations to DA methods at different combinations of crop developmental stages. We divided the crop cycle in three main stages: stage 1 – early stage of development from planting to the maximum number of tillers; stage 2 – medium stage of development from a maximum number of tillers to the maximum LAI; and stage 3 – late stage of development from maximum LAI to harvest. Seven study cases scenarios were tested (Table 2) considering these three stages. Cases 1–3 assimilated LAI observations from only one specific stage. For verifying the relationship between crop stages, we performed study cases 4–6, which grouped LAI observations two at a time. Finally, we simulated DAs considering all observations (Case 7). For this analysis, we only used experiments 1 and 2 ([Table 1](#page-2-0)), because they presented enough observations in each stage, different from the other experiments. For each stage of development, we used only four observations, to maintain the same number of observations for all stages (Table S3).

#

No tables found before Methods section.