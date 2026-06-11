Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/03784290)

# Field Crops Research

jour nal homepage: [www.elsevier.com/locate/fcr](http://www.elsevier.com/locate/fcr)

# Assessing crop model improvements through comparison of sorghum (sorghum bicolor L. moench) simulation models: A case study of West African varieties

![](_page_0_Picture_5.jpeg)

F.M Akinseyea,b,∗, M. Adamb,e, S.O Agelec, M.P. Hoffmannd, P.C.S Traore b, A.M. Whitbreadd,f

a Department of Meteorology and Climate Science, Federal University of Technology, PMB 704, Akure, Ondo State, Nigeria

b International Crops Research Institute for the Semi-Arid Tropics (ICRISAT), WCA Region, Bamako, Mali

c Department of Crop, Soil and Pest Management, Federal University of Technology, PMB 704, Akure, Ondo State, Nigeria d Crop Production Systems in the Tropics, Georg-August-Universität Göttingen, Grisebachstraße 6, 37077 Göttingen, Germany

e CIRAD- UMR AGAP, Avenue Agropolis, 34398 Montpellier Cedex 5, France

f International Crops Research Institute for the Semi-Arid Tropics (ICRISAT) Patancheru 502324, Andhra Pradesh, India

# a r t i c l e i n f o

Article history: Received 26 July 2014 Received in revised form 13 October 2016 Accepted 21 October 2016 Available online 3 November 2016

**2. Materials and methods**

Extensive literature is available describing APSIM ([Holzworth](#page-12-0) et [al.,](#page-12-0) [2014),](#page-12-0) DSSAT [(Jones](#page-12-0) et [al.,](#page-12-0) [2003;](#page-12-0) White et al., 2015) and SAMARA ([Dingkuhn](#page-12-0) et [al.,](#page-12-0) [2011).](#page-12-0) The following section highlights only the main differences in model design related to this study.

### 2.1. Model design differences

### 2.1.1. Phenology

the main difference between APSIM-DSSAT vs. SAMARA resides in the way photoperiod is taken into account. For APSIM and DDSAT it is a linear relation expressed with the critical PP and the slope of the curve, to extent the thermal time to flag leaf initiation. SAMARA implements the model 'impatience' ([Dingkuhn](#page-12-0) et [al.,](#page-12-0) [2008)](#page-12-0) using the concept of threshold-lowering that vary with plant age. It implements decreasing day length requirements during the photoperiod sensitive phase. As the photoperiod sensitive phase progresses, the requirement of day length to trigger flowering is decreased.

### 2.1.2. Leaf development

though all models used the concept of phyllochron and specific leaf area, Samara adds to this by a more detailed description of plant morphology, including size and time of appearance of organ cohorts (leaves,tillers, internodes) and their senescence. It does not simulate individual organs but bases crop growth and development on the definition of the potential organ size adjusted according to source and sink relations.

### 2.1.3. Biomass production

is driven by intercepted light in all models. However, SAMARA calculates gross primary production first, and then steps down to potential net primary production by estimating daily respiration demand. APSIM and DSSAT use a simple RUE concept which takes respiration losses implicitly into account. In APSIM, RUE is based on global radiation while DSSAT on Photosynthetic Active Radiation (PAR). In APSIM on a daily basis, two estimates of the daily biomass production are calculated, one limited by available water for transpiration, and the other limited by radiation. The minimum of these two estimates is the actual biomass production for the day. The main differences between APSIM and DSSAT lie on the biomass partitioning. DSSAT available assimilates are distributed to stem, leaf, root and grain (pod) according to the development stage, with priorities to the different organs according to the development stage. For APSIM the partitioning is directly linked to thermal time through partitioning coefficients. Samara partitioning of biomass to organs is based on source sink relation. Since aggregate supply can be greater or smaller than aggregate demand, growth can be source or sink limited. An inter-organ competition factor controls organs size, and feedbacks on growth and senescence processes.

### 2.2. Calibration data

### 2.2.1. Site

The experimental data used for model calibration were collected from an on-station field trial during 2013 growing season at the International Crops Research Institute for the Semi-Arid Tropics (ICRISAT), Bamako, Mali Republic (12.520N and −8.070W). Daily climatic condition was monitored during 2013 growing season using automatic weather station (AWS) installed within the station (<500 m to the experimental site). The data observed include rainfall, solar radiation, maximum and minimum temperature, relative humidity, and wind speed and direction. Long-term (1970–2010) daily climatic records were obtained to establish comparison with the cropping year at the station. The record shows that 2013 total rainfall (1190 mm) was a little above the long-term average (1970–2010) and classified as a wet year. The analysis of monthly rainfall at the station indicates a distinct mono-modal pattern with the peak amount in August and varied between May and October ([Fig.](#page-2-0) 1). Over 50% of the total rainfall was received in the month of July and August, while both minimum and maximum temperatures decrease uniformly throughout the growing season.

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

**Fig. 1.** Comparison of the long-term (1970–2010) monthly rainfall, minimum air temperature and maximum air temperature and cropping year 2013.

#### **Table 1**

Comparison of growing season climatological indices for long- term (1970–2010) period and cropping year (2013) which include onset date of growing season (OGS), cessation date of growing season (CGP), Length of growing season (LGP), number of rainy days (NRD), total growing season rainfall (GSR), average minimum temperature(T min) and maximum temperature (T max), average solar radiation (Srad),Day length (DL minimum and maximum) at the study site.

| Parameters        | 1970–2010 | St.dev | 2013   |
|-------------------|-----------|--------|--------|
| OGS               | 02-Jun    | 7      | 09-Jun |
| CGS               | 20-Oct    | 9      | 05-Nov |
| LGP (days)        | 141       | 19     | 149    |
| NRD (days)        | 60        | 7      | 64     |
| GSR (mm)          | 906.7     | 46.7   | 1179   |
| ◦<br>Tmin (<br>C) | 21.6      | 2.0    | 21.3   |
| T max (◦C)        | 35.5      | 3.2    | 35.5   |
| Srad (MJ/m2)      | 24.7      | 2.2    | 18.7   |
| DL min (Hr)       |           |        | 11.26  |
| DL max (Hr)       |           |        | 13.15  |
|                   |           |        |        |

NB: St.dev means standard deviation.

To further define the climatology of the station/area (Table 1), the onset date of growing season was computed after [Omotosho](#page-12-0) et [al.](#page-12-0) [(2000),](#page-12-0) while cessation of rainy season was computed after [Traoré](#page-12-0) et [al.](#page-12-0) [(2000).](#page-12-0) Average monthly air temperature varies from 26.2 ◦C to 32.3 ◦C; average solar radiation observed was 18.7 MJ/m2/day. Also, growing season astronomical day length varies from 11 h 15 min to 12 h 45 min and civil daylength from 12 h 10 min to 13 h 38 min.

The soil of the experimental plot is a well-drained, sandy loam (55% sand, 35% silt, and 20% clay), soil organic carbon content was low (0.24%) and associated with this, total N was measured as 225 mg/kg. High available phosphorus (Bray-I) of 94.5 mg/kg can be traced to a long history of P fertilizer use on the station, with a 2.47 cmol/kg CEC and a pH water of 5.3. Parameters in APSIM related to water dynamics such as runoff curve number and evaporation terms were defined as [Probert](#page-12-0) et [al.](#page-12-0) [(1998)](#page-12-0) and [Hoffmann](#page-12-0) et [al.](#page-12-0) [(2016).](#page-12-0)

### 2.2.2. Experiment

The experimental protocol was designed to observe crop phenology, morphology and above ground dry matter dynamics, yield and yield components under non-limited water and nutrient supply. The experiment had variety (four) and sowing date (three) as treatments in a randomized complete block design (RCBD) with four replications. The varieties CSM63E, CSM335, Fadda and IS15401 were selected in this study for their contrasting phenology and morphology as well as their responses to photoperiod. The duration of their crop growing cycle varies from early to late maturity and characterized as Guinea landrace plant group [(Harlan](#page-12-0) [and](#page-12-0) [de](#page-12-0) [Wet,](#page-12-0) [1972).](#page-12-0) Their geographical origin emerged from both Mali and Burkina Faso. Variety CSM63E-locally named "Jakumbe" is early (85–100days) maturing of intermediate height type, producing relatively low biomass, and having low PPS. Variety CSM335 otherwise called "Tieble" is a traditional local variety with medium physiological maturity ranging from 105 to 135 days, intermediate plant height, high biomass, low grain and moderate PPS. Variety Fadda is an improved hybrid, medium maturity days (100–135), high-yielding dual purposes (biomass and grain), intermediate plant height and also moderate PPS. IS15401 also called Soumalemba is a late maturity variety varied from 100 to 155 days, improved traditional tall variety, high-yielding dual purposes (biomass and grain), and high PPS.

The varieties were sown on June 14 representing early planting date (PD 1), July 9 representing medium planting date (PD 2) and August 5 representing late planting date (PD 3) respectively. These sowing dates covered the widest range of farmer's sowing window for sorghum in the Sudano-Sahelian zone. Plant population was 67,000 hills/ha (0.75 m between rows and 0.20 m between hills), which was achieved by thinning to 1plant/hill, 15 days after planting (DAP). The crop was fertilized using 100 kg/ha of di-ammonium phosphate at sowing and 50 kg/ha of Urea (46%N) at 40 days after planting. Insecticides were used according to local recommendations and weeding was done manually. Each plot was 8 by 5.25 m and contained seven rows. The outer two rows were excluded from sampling in order to prevent border effect on the measurements.

Leaf area index (LAI) and above-ground biomass (separated into leaf, stem and panicle) were sampled within three rows at 1 m2 per sampling time, every 15 days interval, beginning from 25DAP for PD 1, 27 DAP for PD 2 and 30 DAP for PD 3 until grain filling stage. The samples were oven dried at 72 ◦C for 72 h. At maturity, harvest was done on 4 m2 area within each plot for the determination of final biomass and grain yield. The fresh weights of these samples were taken and thereafter sub-sample of 20% of the total harvested leaves and stems together with the total harvested panicles grain were oven-dried at 72 ◦C for 72 h. Phenology and leaf development were recorded as emergence, 50% flag leaf date, 50% flowering and maturity dates, total leaf number (TLN).

### 2.2.3. Calculation of derived parameters

Additional parameters for calibration were calculated as follows:

<span id="page-3-0"></span>Daily growing degree-days (GDD, ◦C day) were calculated as [(Streck,](#page-12-0) [2002):](#page-12-0)

$$\text{GDD} = \langle \text{T}_{\text{mean}} - \text{T}_{\text{b}} \rangle / \text{day} \tag{1}$$

Where Tb is the base temperature, assumed 11 ◦C as found in most literature for sorghum [(Folliard](#page-12-0) et [al.,](#page-12-0) [2004;](#page-12-0) [Clerget](#page-12-0) et [al.,](#page-12-0) [2004)](#page-12-0) and Tmean is the daily mean temperature. The accumulated growing degree-days from planting (AGDD) was calculated by adding up the GDD values, i.e. AGDD = -GDD.

Phyllochron was calculated for each variety on the late planting date (PD 3) because the late sowing had the least effect of photoperiod on the appeared leaf. Phyllochron value was derived from the linear regression between the number of leaves produced and the thermal time in each sampled period. The thermal time (◦C) necessary for the appearance of a leaf is equal to 1/b, where b is the slope of the regression.

The coefficient of light extinction was computed from measurements made with a LAI-2000 plant canopy analyzer. The fraction of radiation intercepted was calculated by multiplying the instrument output DIFN (Diffuse Not Intercepted) by a value of 0.94 assuming only 6% of visible light reflected by green canopy [(Dingkuhn](#page-12-0) et [al.,](#page-12-0) [1999).](#page-12-0) Light extinction coefficient Kdf is then calculated inverting Lambert-Beer's law as:

$$\mathbf{K_{df}} = -\ln(\mathbf{O.94PAR_{transmitted}}) \ast \mathbf{LAl^{-1}} \tag{2}$$

Representative values of Kdf for the four varieties at different development stages were in both cases derived by regressing of ln(PARtransmitted)vs. LAI [(Dingkuhn](#page-12-0) et [al.,](#page-12-0) [1999).](#page-12-0) Radiation Use Efficiency (RUE) was calculated as the slope of the linear regression between values of above ground biomass and cumulated APAR – Absorbed photosynthetically active radiation (calculated using Eq. (3)) ([Sinclair](#page-12-0) [and](#page-12-0) [Muchow,](#page-12-0) [1999).](#page-12-0) The Photosynthetic Active Radiation (PAR) was calculated from daily solar radiation (SR; obtained from weather station records during growing period), assuming that PAR comprised 45% of SR [(Howell](#page-12-0) et [al.,](#page-12-0) [1983).](#page-12-0) Meanwhile, daily fAPAR time series was estimated by Lambert-Beer formula using the k values in Lambert- Beer's law

$$\mathsf{APAR}_{\mathsf{d}} = \mathsf{PAR}_{\mathsf{d}} \times f \mathsf{APAR}_{\mathsf{d}} \tag{3}$$

In the equation the subscript letter d refers to the daily value and fAPARd = 1-exp−k*LAI.

# 2.3. Validation data

For model validation we used the results of field experiments carried out between 2000 and 2008 for two locations (Bamako and Cinzana, Mali). The details ofthese experiments have been reported by [Clerget](#page-12-0) et [al.](#page-12-0) [(2004,](#page-12-0) [2007,](#page-12-0) [2008).](#page-12-0) The agronomic practices and relevant observations used for this study are presented in [Table](#page-4-0) 2.

# 2.4. Calibration and evaluation of the models

First we calibrated the models by matching observed results from the 2013 field experiment with model outputs. Within this process we used the derived parameter for parameterization of the models. The calibration procedure followed four phases which include phenology, morphology, above-ground biomass and grain yield. Thereafter, we used the additional data set to validate the models independently. For calibration and validation, we assessed the goodness-of-fit between model simulated and observed values of yield and above-ground biomass as well as phenological events. Model-estimated (simulated) were compared with observed using the following listed statistics;

1. Root mean square error (RMSE):

$$\text{RMSE} = \{ \mathbf{n}^{-1} \boldsymbol{\Sigma} (\text{simulated} - \text{observed})^2 \}^{0.5} \tag{4}$$

2. The normalized root mean square error (NRMSE) express in percent, calculated according to [Loague](#page-12-0) [and](#page-12-0) [Green](#page-12-0) [(1991)](#page-12-0) with Eq. (4)

$$\text{NRMSE} = \left[ \text{n}^{-1} \Sigma (\text{simulated} - \text{observed})^2 \right]^{0.5} \text{X} \frac{100}{M} \tag{5}$$

M is the mean of the observed variable. NRMSE gives a measure (%) of the relative difference of simulated versus observed data. The simulation is considered excellent with a NRMSE less than 10%, good if the NRMSE is greater than 10% and less than 20%, fair if the NRMSE is greater than 20% and less than 30% and poor ifthe NRMSE is greater than 30% [(Jamieson](#page-12-0) et [al.,](#page-12-0) [1991).](#page-12-0)

3. Linear regression(1:1) plot was takenas anindicator to inform whether the models under- or overestimated measured yields, i.e. the direction and magnitude of bias.

4. Additionally, for comparison, the traditional R2 regression statistic (least-squares coefficient of determination) was calculated though it does not take into account model bias, which is central when assessing the performance of simulation models.

# 2.4.1. Sensitivity analysis

A sensitivity analysis was carried out on the three models used (APSIM, DSSAT and Samara) from the data used for calibration. Five (5) model parameters were changed by adding or subtracting 10% to the calibrated values and the effect on the flowering date, maximum LAI, final above ground biomass (AGB) and grain yield were calculated. Similar to [Zuidema](#page-12-0) et [al.](#page-12-0) [(2005),](#page-12-0) such an analysis will identify parameters that have a strong influence on modelled output, in this case sorghum production, and therefore need to be estimated accurately.

No tables found before Methods section.