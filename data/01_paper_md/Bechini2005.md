![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

Environmental Modelling & Software 21 (2006) 1042e1054

[www.elsevier.com/locate/envsoft](http://www.elsevier.com/locate/envsoft)

# Parameterization of a crop growth and development simulation model at sub-model components level. An example for winter wheat (Triticum aestivum L.)

Luca Bechini a, *, Stefano Bocchi a , Tommaso Maggiore a , Roberto Confalonieri b

a Department of Crop Science, Section of Agronomy, University of Milano, Via Celoria 2, 20133 Milano, Italy b Institute for the Protection and Security of the Citizen, Joint Research Centre of the European Commission, AGRIFISH Unit, MARS-STAT Sector, TP 268 e 21020 Ispra (VA), Italy

> Received 2 June 2004; received in revised form 5 May 2005; accepted 9 May 2005 Available online 18 July 2005

#### Abstract

Dynamic simulation models are frequently used for assessing agronomic and environmental effects of different management practices, under various pedo-climatic conditions. CropSyst is a suitable cropping systems simulation model for such applications. However, available CropSyst crop parameters for winter wheat, one of the most important cereals in the world, are limited. In this work we show that it is possible to parameterize separate sub-model components by using existing experimental data and literature. The experiments, carried out in northern Italy between 1986 and 2001, quantified the dynamics of aboveground biomass (AGB),

plant nitrogen (N) concentration (PNC) and N uptake (UPTK) by means of periodical measurements.

The relative root mean square error (calculated by dividing the root mean square error by the average of observations) obtained after model calibration and validation on an independent data set was, respectively, in the range 9e30% and 17e32% for AGB, 10% and 6e40% for PNC, 8e28% and 9e24% for UPTK. AGB was frequently underestimated. Despite the limited accuracy of simulations, we argue that calibrated crop parameters are adequate for scenario analysis as most differences between years and fertilization levels were reproduced by the model and final AGB and cumulative UPTK were also correctly simulated. 2005 Elsevier Ltd. All rights reserved.

2. Material and methods

# 2.1. Experimental data

Experimental data were collected in 4 experiments (Table 1 and 2) carried out between 1986 and 2002 in Table 1

| sets<br>data<br>The                   | this<br>in<br>used               | work                                   |                                |                          |                                                                                            |                                                                                                                                            |            |                       |                      |                                                       |
|---------------------------------------|----------------------------------|----------------------------------------|--------------------------------|--------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------|----------------------|-------------------------------------------------------|
| Experiment<br>no.                     | Location                         | longitude,<br>Latitude,<br>altitude    | Years                          | Sowing<br>date           | Treatments                                                                                 | Experimental<br>design                                                                                                                     | Replicates | Measured<br>variables | samples<br>of<br>No. | size<br>Sample                                        |
| 1                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e1987<br>e1988<br>1986<br>1987 | 20/10/1986<br>25/10/1987 | )<br>1<br>ha<br>levels<br>N<br>140,<br>kg<br>N<br>210<br>(0,<br>3                          | block<br>randomized<br>Complete                                                                                                            | 3          | AGBc<br>PNCd          | 6                    | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 2                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e1990<br>e1991<br>1989<br>1990 | 02/11/1989<br>16/11/1990 |                                                                                            | species;<br>cultivars)<br>(plot:<br>Split-plot<br>subplot:                                                                                 | 4          | AGBc<br>PNCd          | 15<br>16             | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 3                                     | Lodi                             | a.s.l.<br>4519#N,<br>928#E,<br>m<br>80 | e1997<br>1996                  | 14/10/1996               |                                                                                            | species;<br>cultivars)<br>(plot:<br>Split-plot<br>subplot:                                                                                 | 3          | AGBc<br>PNCd          | 8                    | m)<br>linear<br>1.0<br>!<br>m<br>(0.18<br>m2<br>0.180 |
| 4                                     | Lodigiano<br>Angelo<br>S.        | a.s.l.<br>4515#N,<br>922#E,<br>m<br>73 | e2002<br>2001                  | 16/11/2001               | 40,<br>0,<br>)<br>1<br>!<br>ha<br>100a<br>levels<br>N<br>kg<br>50,<br>N<br>80b<br>(0,<br>9 | fertilization;<br>fertilization;<br>cultivars)<br>top-dressing<br>preseeding<br>esplit-plot<br>sub-subplot:<br>subplot:<br>(plot:<br>Split | 3          | AGBc                  | 5                    | m)<br>linear<br>1.2<br>!<br>m<br>(0.18<br>m2<br>0.216 |
| Top-dressing<br>Pre-seeding<br>a<br>b | fertilization.<br>fertilization. |                                        |                                |                          |                                                                                            |                                                                                                                                            |            |                       |                      |                                                       |

c AGB d PNC

Z plant nitrogen

Z

aboveground

 biomass. concentration.

Table 2 Characteristics of the soils

| Experiment | Location  | Years     | Soil<br>layer (m) | Sand<br>(g kg<br>1<br>) | Clay<br>(g kg<br>1<br>) | Silt<br>(g kg<br>1<br>) | pH (water) | C.E.C.a<br>(cmol kg<br>1<br>) | SOMb<br>(g kg<br>1<br>) |
|------------|-----------|-----------|-------------------|-------------------------|-------------------------|-------------------------|------------|-------------------------------|-------------------------|
| 1          | S. Angelo | 1986e1987 | 0.00e0.40         | 550                     | 30                      | 420                     | 6.2        | 10.0                          | 26                      |
|            |           |           | 0.40e0.60         | 580                     | 20                      | 400                     |            |                               | 18                      |
|            |           |           | 0.60e0.80         | 540                     | 30                      | 430                     |            |                               | 15                      |
|            |           |           | 0.80e1.00         | 550                     | 30                      | 420                     |            |                               | 14                      |
| 1          | S. Angelo | 1987e1988 | 0.00e0.20         | 630                     | 40                      | 330                     | 6.7        | 13.0                          | 15                      |
|            |           |           | 0.20e0.40         | 650                     | 40                      | 310                     |            |                               | 15                      |
|            |           |           | 0.40e0.60         | 700                     | 40                      | 260                     |            |                               | 9                       |
|            |           |           | 0.60e0.80         | 600                     | 50                      | 350                     |            |                               | 8                       |
|            |           |           | 0.80e1.00         | 540                     | 30                      | 130                     |            |                               | 6                       |
| 2          | S. Angelo | 1989e1990 | 0.00e0.20         | 540                     | 90                      | 370                     | 5.9        | 12.0                          | 18                      |
|            |           |           | 0.20e0.40         | 670                     | 160                     | 170                     |            |                               | 17                      |
|            |           |           | 0.40e0.60         | 580                     | 20                      | 400                     |            |                               | 11                      |
|            |           |           | 0.60e0.80         | 540                     | 30                      | 430                     |            |                               | 9                       |
|            |           |           | 0.80e1.00         | 550                     | 30                      | 420                     |            |                               | 8                       |
| 2          | S. Angelo | 1990e1991 | 0.00e0.20         | 700                     | 50                      | 250                     | 6.7        | 10.9                          | 11                      |
|            |           |           | 0.20e0.40         | 710                     | 80                      | 210                     |            |                               | 7                       |
|            |           |           | 0.40e0.60         | 620                     | 50                      | 330                     |            |                               | 10                      |
|            |           |           | 0.60e0.80         | 550                     | 30                      | 420                     |            |                               | 8                       |
|            |           |           | 0.80e1.00         | 520                     | 20                      | 460                     |            |                               | 5                       |
| 3          | Lodi      | 1996e1997 | 0.00e0.30         | 720                     | 100                     | 180                     | 6.5        | 10.0                          | 15                      |
|            |           |           | 0.30e0.50         | 650                     | 130                     | 220                     |            |                               | 13                      |
|            |           |           | 0.50e1.00         | 540                     | 190                     | 270                     |            |                               | 10                      |
| 4          | S. Angelo | 2001e2002 | 0.00e0.20         | 690                     | 150                     | 160                     | 6.4        | 9.0                           | 13                      |
|            |           |           | 0.20e0.40         | 650                     | 150                     | 200                     |            |                               | 15                      |
|            |           |           | 0.40e0.60         | 550                     | 40                      | 410                     |            |                               | 11                      |
|            |           |           | 0.60e0.80         | 520                     | 20                      | 460                     |            |                               | 6                       |
|            |           |           | 0.80e1.00         | 540                     | 30                      | 430                     |            |                               | 7                       |

a C.E.C. Z cation exchange capacity. b SOM Z soil organic matter.

2 locations in northern Italy. This area is characterized by a moderate continental climate, with a mean annual temperature of about 13 C; the absolute minimum temperature occurs between January and February and the absolute maximum between July and August. Total precipitation (about 800 mm year-1 ) is relatively well distributed and the average wind speed is about 1.5 m s-1 .

For all the experiments considered, the soils had high phosphorus and low potassium content. Daily meteorological data (rainfall, maximum and minimum air temperatures, global solar radiation) were collected with automatic weather stations near the fields. Plant samples were dried in oven at 70 C (until constant weight) to determine the aboveground biomass (AGB).

The first experiment was carried out with the aim of verifying the effects of nitrogen (N) fertilization on winter wheat (cv. Gemini) growth. The second experiment had the purpose of describing the spring dynamics of biomass accumulation and forage quality of five species [winter wheat, Italian ryegrass (Lolium multiflorum Lam.), barley (Hordeum vulgare L.), rye (Secale cereale L.), triticale (Triticum ! Secale)]. Two cultivars were used for each species (Pandas and Centauro for wheat). AGB samples were collected every 10 days until head emergence [Decimal Code (DC) 55], every 3 days between earing and late milk maturity (DC77) and every 10 days between late milk maturity and physiological maturity (DC89). The third experiment was conducted to study the spring dynamics of forage quality and biomass accumulation of winter wheat, barley and Italian ryegrass. Two cultivars were grown for each species (Eridano and Soissons for wheat). The fourth experiment was carried out to compare the effects of N fertilization on the growth of three wheat cultivars (Guadalupe, Enesco and Eureka). In this experiment, aboveground plant biomass accumulation was measured only for the optimal N treatment. Plant sample size for AGB measurements was determined by using the following method. An elementary sub-sample size (S ) was chosen (0.20 linear m Z 0.036 m2 ). Nine biomass samples of size aS (with a integer from 2 to 10) were weighted, recording separately the values for each elementary sub-sample. For each sample the mean weight of the a sub-samples and its standard deviation were calculated. The means and the standard deviations were plotted against a. The minimum sample size for the experiment corresponded to the value of a with stable means and reasonably low standard deviations.

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

Fig. 1. Plant nitrogen concentration versus accumulated aboveground biomass: data used in this study for calibration and validation, and comparison between the maximum, critical and minimum nitrogen dilution curves proposed by [Justes et al. (1994)](#page-12-0) and calculated by CropSyst with our parameters set.

Overall, 80 average measurements of AGB and 75 of plant N concentration (PNC) were available in the data set (Fig. 1), covering a wide range of growth stages, biomasses and N concentrations. The experimental data were analyzed with the software CoLiDaTa [(Confalonieri](#page-11-0) [and Scaglia, 2002)](#page-11-0), which automatically applies many statistical tests for the validation of analytical data. In particular, the Grubbs's test ([Grubbs, 1969; ISO 5725-2,](#page-12-0) [1994)](#page-12-0) was used to discard outliers.

#### 2.2. Simulation model

CropSyst ([Sto¨ckle et al., 2003)](#page-12-0) is a multi-year, multicrop, daily time step cropping systems simulation model developed to evaluate the effects of different pedoclimatic and management conditions on crop growth and on environmental impact.

Crop development is simulated through thermal time accumulation, by computing the growing degree days (GDDs), using Tb (base temperature; C) as a lower threshold and Tcutoff ( C; optimum temperature for thermal time accumulation) as an upper threshold. Photoperiodical effects for long-day plants between emergence and flowering are implemented by multiplying GDDs by fphoto, a dimensionless variable: fphotoZ L - Lif- = Lins - Lif- where L is daylength (h), Lif (h) is daylength to inhibit flowering (no development occurs when daylength is below Lif), Lins (h) is daylength for insensitivity (above Lins the maximum development rate occurs). fphoto equals 0 below Lif and 1 above Lins.

The potential daily AGB production (AGBP) is calculated as the minimum of the values computed with Eqs. (1) and (2) proposed, respectively, by [Tanner and](#page-12-0) [Sinclair (1983)](#page-12-0) and by [Monteith (1977)](#page-12-0):

$$\text{AGB}_{\text{PT}} = \frac{K_{\text{BT}} T_{\text{P}}}{\text{VPD}} \tag{1}$$

where AGBPT (kg m-2 day-1 ) is the crop potential transpiration-dependent biomass production, TP (kg m-2 day-1 ) is crop potential transpiration, VPD (kPa) is the daytime mean atmospheric vapor pressure deficit and KBT (kPa kg kg-1 ) is a biomass-transpiration coefficient, which corresponds to the water use efficiency (WUE: aboveground biomass accumulated/water transpired) multiplied by the VPD.

$$\text{AGB}_{\text{iPAR}} = \text{RUE} \times \text{iPAR} \times T_{\text{lim}} \tag{2}$$

where AGBiPAR (kg m-2 day-1 ) is the intercepted PARdependent biomass production, RUEPAR (kg MJ-1 ) is the PAR use efficiency, iPAR (MJ m-2 day-1 ) is the daily amount of crop-intercepted photosynthetically active radiation and Tlim is a factor which describes the effect of temperature on radiation-dependent biomass accumulation, calculated as:

$$T_{\rm lim} = \begin{cases} 0 & T_{\rm m} < T_{\rm b} \\ \frac{T_{\rm m} - T_{\rm b}}{T_{\rm opt} - T_{\rm b}} & T_{\rm b} \le T_{\rm m} \le T_{\rm opt} \\ 1 & T_{\rm m} > T_{\rm opt} \end{cases} \tag{3}$$

where Tm ( C) is the average air daily temperature and Topt ( C) is the optimum temperature for growth.

The Eq. (2) is necessary because of the instability of Eq. (1) at low values of VPD. Water and nitrogen limitations are then applied to AGBP to calculate actual daily AGB production. Water limited growth (AGBT) is calculated by multiplying AGBP for the ratio of actual to potential transpiration; subsequently, actual daily AGB production is calculated by applying the concept <span id="page-4-0"></span>of critical nitrogen concentration [(Sto¨ckle and Debaeke,](#page-12-0) [1997](#page-12-0)) to AGBT.

Leaf area growth is calculated on the basis of Eq. (4):

$$\text{LAI} = \frac{\text{SLA} \times \text{AGB}}{\text{l} + p \times \text{AGB}} \tag{4}$$

where LAI (m2 m-2 ) is the green leaf area index, AGB is the accumulated aboveground biomass (kg m-2 ), SLA (m2 kg-1 ) is the mean of specific leaf area values measured at early growth stages and p is an empirical partitioning coefficient.

CropSyst uses the following equations to identify the maximum, critical and minimum nitrogen concentrations from emergence to flowering for the aboveground part of the plant:

$$N_{\text{max}} = \min\left(N_{\text{max}_{\text{\textd}}}, a_{\text{max}} \mathbf{AGB}^{-\delta}\right) \tag{5}$$

$$N_{\rm crit} = \min\left(0.8N_{\rm max_{\varepsilon}}, a_{\rm crit} \text{AGB}^{-\delta}\right) \tag{6}$$

$$N_{\rm min} = \min\left(0.4N_{\rm max_c}, a_{\rm min} \text{AGB}^{-b}\right) \tag{7}$$

where

$$a_{\text{max}} = \frac{N_{\text{max}_{\mathbf{e}}}}{2^{-b}} \tag{8}$$

$$a_{\rm crit} = \frac{0.8N_{\rm max_c}}{1.5^{-b}} \tag{9}$$

$$a_{\rm min} = \frac{0.4N_{\rm max_c}}{0.S^{-b}}\tag{10}$$

and Nmax, Ncrit and Nmin (%) are, respectively, the plant maximum, critical and minimum nitrogen concentrations; Nmaxe (%) is the plant maximum nitrogen concentration during early growth, AGB (kg ha-1 ) is the aboveground plant biomass; amax, acrit, amin represent thresholds at which plant nitrogen concentrations begin to decrease, and b Z 0.4. For the period between flowering and physiological maturity, maximum and minimum nitrogen concentrations decrease linearly to ''maximum nitrogen concentration at maturity'' (Nmaxm ) and ''minimum nitrogen concentration at maturity'' (Nminm ) input parameters.

#### 2.3. Model parameterization and validation

CropSyst version 3.02.23 (January 8, 2002) was used. Potential evapotranspiration was calculated by using the PriestleyeTaylor equation; the default value used (1.26) was already applied in the same area for rice simulation ([Confalonieri and Bocchi, in press)](#page-11-0); the aridity factor was set to 0.030 (default). Soil water redistribution was simulated with the cascade sub-model.

Due to the relatively limited amount of available data, calibration of crop parameters was carried out without distinctions among cultivars. Far from being correct for a subsequent experimental application of CropSyst, this approach is in our opinion coherent with the purpose of deriving a set of crop parameters for scenario simulations at species level.

Data from the second and fourth experiments were used for the calibration of crop parameters, while data from the first and third were used for validation. During the first experiment, cultivar Gemini was grown; for the second, data collected for Centauro and Pandas cultivars were averaged, as in the third experiment for the cultivars Soissons and Eridano; for the fourth experiment, only data collected for the cultivar Eureka were used. We were not interested in specifically calibrating most of the crop N parameters, because an extensive work on N dilution curves for winter wheat has been already carried out by [Justes et al. (1994):](#page-12-0) for this reason, we included only non-N limited treatments in the calibration data set. All experiments fulfilled this requirement; the second experiment was chosen for calibration because it is the one with the highest number of AGB measurements; experiment no. 3 was used for validation, having measurements of PNC, while no. 4 was used for calibration (no measurements of PNC available). Nitrogen simulation was activated for all the simulations, using the parameterization of nitrogen transformations set up by [Confalonieri et al. (2001)](#page-11-0) on similar soils.

The calibration of crop parameters was carried out separately for each simulation module, i.e. crop phenology (thermal time, photoperiod) and crop growth (water- and radiation-dependent growth, nitrogendependent growth). We underline that CropSyst is not a modular simulator, but we reproduced simple model components in a spreadsheet, to calculate specific rate equations outside the model. This procedure was intended to avoid problems derived from a ''blackbox'' calibration (carried out on the whole simulation model) where the error in one parameter value could be compensated by errors in other parameter values and, despite reasonable simulation results, the parameterization obtained could be inaccurate and unrealistic.

## 2.3.1. Crop development e thermal time and photoperiod modules

With two exceptions, all the parameters were calibrated on the basis of our experimental data set. Thermal time required for emergence was taken from literature, because we did not have recorded emergence dates; phenologic sensitivity to water stress was left to the default value because our data set did not include situations that allowed calibration of this parameter. Tb, Tcutoff, Lif and Lins were calibrated using the Microsoft

Excel Solver ([Flystra et al., 1998)](#page-11-0), such that the coefficient of variation (CV) among the GDDs required from emergence to flowering and from emergence to physiological maturity, was minimized (following [Bonhomme et al., 1994)](#page-11-0).

## 2.3.2. Crop growth e water- and radiation-dependent growth modules

From our experience and a previous sensitivity analysis carried out with the same model [(Confalonieri](#page-11-0) [and Bechini, 2004)](#page-11-0), we decided, for the less important parameters, to set several of them at their default values and to take others from literature. We calibrated RUEPAR, by isolating the calculation of radiationdependent biomass from the calculation of transpirationdependent biomass. To do this, because CropSyst is not a modular model, we decided to separately reproduce the two sub-models for the calculation of AGBiPAR and AGBPT, by calculating Eqs. (1) and (2) in a spreadsheet. These equations were used to simulate daily AGB accumulation for the period between the closed canopy stage (full radiation interception) and flowering: in this period, AGBiPAR depends only on solar radiation, RUEPAR and air temperature. Because CropSyst uses the minimum of AGBiPAR and AGBPT as the potential daily AGB production, the periods in which AGBiPAR was lower than AGBPT were selected. The Microsoft Excel Solver was then used to calibrate RUEPAR, with the objective of minimizing the difference between measured and calculated AGB increments. We further improved the goodness of simulations for the whole crop growing period by calibrating KBT, SLA, Topt, leaf duration and p, within reasonable ranges drawn from the literature.

# 2.3.3. Crop growth e N-dependent growth module

In accordance with Eq. [(9)](#page-4-0), Nmaxe was calculated as acrit/0.8, with acrit Z 4.4% (critical N concentration during early stages, with AGB ! 1.55 t DM ha-1 ; [Justes](#page-12-0) [et al., 1994)](#page-12-0). Moreover, Nminm was set as the minimum concentration reached with AGB of 14 t DM ha-1 ([Justes et al., 1994)](#page-12-0). Nmaxm was calibrated by using our experimental data. We further calibrated the empirical parameters ''N uptake adjustment'' and ''N availability adjustment'' to reduce the errors in the simulations of PNC.

The agreement between measured and simulated values of accumulated AGB, PNC and accumulated UPTK was expressed by using several of the indices proposed by [Loague and Green (1991)](#page-12-0) and recently reviewed by [Fila et al. (2003):](#page-11-0) the relative root mean square error (RRMSE, ranges from 0 to CN, optimum Z 0%), the coefficient of determination (CD, ranges from 0 to CN, optimum Z 1, indicates whether the model reproduces the trend of measured values or not), the modelling efficiency (EF, ranges from -N to 1, optimum Z 1, if positive, indicates that the model is a better predictor than the average of measured values), the coefficient of residual mass (CRM, ranges from -N to CN, optimum Z 0, if positive indicates model underestimation). The parameters of the linear regression equation between measured and predicted values were also calculated with the least squares method; because these data are not independent ([Donatelli et al.,](#page-11-0) [2003)](#page-11-0), no conclusions were drawn about their statistical significance.

No tables found before Methods section.