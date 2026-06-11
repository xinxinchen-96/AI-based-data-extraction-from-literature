[Journal of Hydrology 546 (2017) 166–178](http://dx.doi.org/10.1016/j.jhydrol.2016.12.049)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/00221694)

Journal of Hydrology

journal homepage: [www.elsevier.com/locate/jhydrol](http://www.elsevier.com/locate/jhydrol)

Research papers

# Estimation of available water capacity components of two-layered soils using crop model inversion: Effect of crop type and water regime

![](_page_0_Picture_6.jpeg)

K. Sreelash a,b,c,d , Samuel Buis a,⇑ , M. Sekhar b,d , Laurent Ruiz b,d,e,f , Sat Kumar Tomer b,d,g , Martine Guérif a

aUMR EMMAH, INRA, UAPV, F-84 914 Avignon, France

b Indo-French Cell for Water Sciences, Indian Institute of Science, IRD, Bangalore, India

cNational Centre for Earth Science Studies, Thiruvananthapuram, India

dDepartment of Civil Engineering, Indian Institute of Science, Bangalore, India

e INRA, UMR 1069 SAS, AGROCAMPUS OUEST, F-35000 Rennes, France

f GET, CNRS, UPS, IRD, CNES, 31400 Toulouse, France

g Aapah Innovations Private Limited, Hyderabad 500 032, India

## article info

Article history: Received 21 March 2016 Received in revised form 22 December 2016 Accepted 24 December 2016 Available online 27 December 2016 This manuscript was handled by Tim McVicar Editor-in-Chief, with the assistance

of Yongqiang Zhang, Associate Editor

## 2. Materials and methods

## 2.1. Site information

The experimental catchment of Berambadi (84 km2 ) is located in the Kabini river basin in South India (AMBHAS Site, [www.amb](http://www.ambhas.com)[has.com](http://www.ambhas.com), long term environmental observatory BVET [http://bvet.](http://bvet.obs-mip.fr) [obs-mip.fr](http://bvet.obs-mip.fr); [Braun et al., 2009; Ruiz et al., 2010; Violette et al.,](#page-11-0) [2010](#page-11-0)). It is intensively used for agro-hydrological, remote sensing and hydrological investigations [(Kumar et al., 2009)](#page-11-0). The land is used for agriculture and the crops are mostly rainfed or irrigated with groundwater. We used a total of 60 crop/soil/climate situations covering 4 crops across 3 years from May 2011 to Dec 2013 and 42 agricultural plots each approximately 1 ha in size, monitored for soil moisture and crop growth. Among them, 15 <span id="page-2-0"></span>crop/soil/climate situations from 12 plots were used for the calibration of STICS plant parameters (see Section 2.4). The inversions were performed on 45 crop/soil/climate situations from 33 plots. The results presented in the following will only concern the situations/plots used for the inversions.

The 4 crops studied have distinct characteristics (Table 1). Turmeric is an irrigated 8 months crop (May–December) while the 3 others are rainfed crops grown over 4 months (May to August for sunflower and sorghum and September–December for maize).

The climate is tropical semi-arid, dominated by south-west monsoon with a mean annual rainfall of 800 mm (coefficient of variation 0.28), and an annual Potential Evapotranspiration (PET Penman Method, [Penman, 1948)](#page-12-0) of 1100 mm (coefficient of variation 0.05), computed over 2005–2015. Daily records of air humidity, wind velocity, maximum and minimum air temperatures, precipitation and global radiation were obtained from an automatic weather station (CIMEL, type ENERCO 407 AVKP) and a meteorological flux tower (Astra Microwave, India) located in the study area. Measurements from the closest station were considered for each plot.

For the study period, the amount and distribution of rainfall and (Rain + Irrigation)/PET ratio varied across years and cropping seasons [(Table 2](#page-3-0)). This led to a varying degree of crop water stress experienced by the crops. 2012 was relatively dry as compared to 2011 and 2013 which can be classified as ʻnormal years'.

#### 2.2. Crops: management and LAI measurements

Information on management activities such as date and dose of sowing, fertilizing, irrigation and date of harvest were obtained during field visits. Sowing dates (expressed as day of the year) vary between 130 to 150 for sunflower and sorghum, between 110 and 124 for turmeric and between 250 and 262 for maize. Fertilizer is applied once at the beginning of the season, the quantity varying between 20 to 30 kg N/ha for sunflower, 30–50 kg N/ha for sorghum, 100–200 kg N/ha for turmeric and 25–50 kg N/ha for maize.

LAI was measured using a CI-202 Portable Leaf Area meter (CID Bioscience) and a LAI-2000 Plant Canopy Analyzer (LI-COR) every 10 days in 2011 and 2012, and every 20 days in 2013, concurrently with soil moisture measurements (see next section). Three measurements of LAI were taken in one representative sample area of 2 m2 and the mean value was used as representative of the plot.

Time series of LAI [(Fig. 1)](#page-3-0) obtained by interpolation of the measurements using a parametric growth curve approach [(Baret, 1986)](#page-11-0) revealed a large variability resulting mainly from interactions between crop, climate and soil type. It provides the basis for the determination of root zone soil water content properties from crop model inversion.

## 2.3. Soils: pedology, soil moisture measurements, reference AWC parameters values

Soils in the studied area are roughly classified as red soils (Alfisols, FAO) or black soils (Vertisols, FAO). According to the 1:50,000 scale soil map of the area prepared by Karnataka State Remote Sensing Application Center (KSRSAC), six categories are considered based on the particle size distribution of the top layer: Clay and Clay Loam for vertisols, Gravelly Loam Sand, Loamy Sand, Sandy Clay Loam and Sandy Loam for Alfisols. Sandy Clay Loam is the major soil class, covering 50% of the area. The soil is gravelly sandy loam at the hill slopes, sandy loam and sandy clay loam in the plains and clay loam and clay in the valley.

Surface soil moisture (SSM; typically from 0 to 10 cm deep) used for model inversion was measured with a ML2x Theta Probe Soil Moisture Sensor (Delta-T devices, sampling volume: 2.5 cm diameter, 6 cm long) and the mean of 3 measurements used as representative of each field plot. Additionally three soil samples per plot were collected for gravimetric soil moisture measurements. Theta Probe devices were calibrated twice a year using the gravimetric measurements: once during period of low soil moisture (before the start of the cropping season) and other during period of high soil moisture (during or at the end of the first cropping season). Profiles of soil moisture - used to determine in situ soil hydraulic properties – were also measured using soil moisture sensors (Trime-FM Field Portable TDR Meter, IMKO Micromodultechnik GmbH, sampling volume: 15 cm diameter, 18 cm long). The measurements were made at an increment of 10 cm from surface up to 1 m deep for shallow soils and up to 2 m for deeper soils. Both surface and profile soil moisture were measured throughout the year at a frequency of 10 days in 2011 to 2012 and 20 days in 2013. To capture the extreme values of soil moisture in both dry and wet conditions, surface and profile soil moisture were measured daily for a 30 days period once in October 2011 and once in August 2013.

To compare the estimated values of soil properties retrieved from model inversion to 'observed values', water content at field capacity (hFC), wilting point (hWP) and soil depth (DL) were determined from in situ measurements on the monitored plots [(Table 3)](#page-3-0). As proposed by [Hunt et al. (2009)](#page-11-0) and [Martinez-Fernandez et al.](#page-12-0) [(2015),](#page-12-0) hFC and hWP were inferred from long term soil moisture data: hFC as the 'minimum of maximum value' of the layer soil moisture in the growing season, while discarding soil moisture data immediately after a rainfall event (or irrigation event), and hWP as the '5th percentile of the minimum values' of the layer soil moisture in the growing season. Our time series of soil moisture exhibited alternate wetting and drying cycles, thus capturing both maximum and minimum soil water content. Bulk density was determined as the ratio of volumetric soil moisture (from TDR measurements) to gravimetric soil moisture (measured on soil samples). The depth of soil layers was determined by soil augering. The depth of soil from surface to weathering zone varied from 70 cm to 150 cm and was independent of the soil type.

## 2.4. Model and parameters

The STICS crop model [(Brisson et al., 1998; Coucheney et al.,](#page-11-0) [2015](#page-11-0)) is a daily time-step model which simulates the functioning of a soil-crop system over a single or several successive crop cycles. It has been successfully used for spatial applications and coupled with hydrological models at the catchment scale [(Beaujouan](#page-11-0) [et al., 2001](#page-11-0)). The upper boundary conditions are governed by standard climatic variables (radiation, maximum and minimum air temperatures, rainfall, potential evapotranspiration) and the lower boundary condition is the soil/sub-soil interface. We used the Pen-

Table 1

Monitored plots and vegetation measurements from 2011 to 2013. (LAI – Leaf Area Index; SSM – Surface Soil Moisture).

| Crop      | Number of situations monitored | Growing season        | Average length of the growing period | Avg. number of LAI/SSM Observations per situation |
|-----------|--------------------------------|-----------------------|--------------------------------------|---------------------------------------------------|
| Turmeric  | 17                             | May to December       | 240 days                             | 10                                                |
| Sunflower | 11                             | May to August         | 110 days                             | 8                                                 |
| Sorghum   | 9                              | May to August         | 110 days                             | 8                                                 |
| Maize     | 8                              | September to December | 100 days                             | 7                                                 |

#### <span id="page-3-0"></span>Table 2

Cumulated Rain, Potential Evapotranspiration (PET Penman Method, [Penman, 1948](#page-12-0)), Irrigation and (Rain + Irrigation)/PET ratio over the corresponding growing season for turmeric, sunflower, sorghum and maize crops for 2011, 2012 and 2013 in the Berambadi catchment.

| Variable                | 2011 |      | 2012    |      |      |         | 2013 |      |         |
|-------------------------|------|------|---------|------|------|---------|------|------|---------|
|                         | S1   | S2   | S1 + S2 | S1   | S2   | S1 + S2 | S1   | S2   | S1 + S2 |
| Rain (mm)               | 520  | 321  | 841     | 302  | 282  | 584     | 557  | 301  | 858     |
| Irrigation (mm)         | 0    | 0    | 170     | 0    | 0    | 165     | 0    | 0    | 90      |
| PET (mm)                | 347  | 351  | 698     | 366  | 341  | 707     | 342  | 344  | 686     |
| (Rain + Irrigation)/PET | 1.50 | 0.91 | 1.45    | 0.83 | 0.83 | 1.06    | 1.63 | 0.88 | 1.38    |

S1 - Season-1: May to August (sunflower and sorghum).

S2 - Season-2: September to December (maize).

S1 + S2: May to December (turmeric).

![](_page_3_Figure_7.jpeg)

Fig. 1. LAI curves for (a) sunflower, (b) sorghum, (c) turmeric and (d) maize showing the variability of LAI between plots and crops. Abcissa represents time expressed in Thermal Degree Days (summation of air temperature above a crop-specific base temperature) from sowing to maturity.

#### Table 3

Range of observed values of Field Capacity and Wilting Point obtained from long term soil moisture observations (2011–2014) and AWC (computed using Eq. [(1)](#page-4-0)) for different soil types in the 33 plots. Field Capacity and Wilting Point values are presented in gravimetric unit, the unit used in the model STICS.

| Soil type/parameter | No of plots | Soil moisture at field capacity hFC (g/g) | Soil moisture at wilting point hWP (g/g) | Available water content AWC (mm) |
|---------------------|-------------|-------------------------------------------|------------------------------------------|----------------------------------|
| Sandy Loam          | 11          | 14.0–19.5                                 | 4.5–7.5                                  | 127.0–215.0                      |
| Sandy Clay Loam     | 15          | 17.5–23.5                                 | 6.5–11.0                                 | 139.0–231.0                      |
| Clay Loam           | 7           | 22.5–30.0                                 | 10.5–12.5                                | 129.0–198.0                      |

man method to calculate potential evapotranspiration (PET; [Penman, 1948)](#page-12-0). Crops are described by their LAI, above-ground biomass and nitrogen content and the number and biomass of harvested organs. The main processes described are carbon assimilation and allocation to different organs and water and nitrogen balances (for detailed description, see [Brisson et al., 1998, 2008)](#page-11-0).

The different components of actual evapotranspiration (ET) are calculated from the potential evapotranspiration: soil evaporation (Es), plant transpiration (Tp) and evaporation from the water intercepted by the foliage that contributes to reducing the evaporative demand at the plant level. For Es, two stages are considered following rainfall: a first stage where the soil evaporates at the potential rate, and a second stage where evaporation is lower and decreases according to climate and type of soil. Crop water requirements (or maximum transpiration) are determined according to a crop coefficient approach which is well adapted to the crops considered herein [(Brisson et al., 1998, 2008)](#page-11-0). The actual plant transpiration Tp is based on the water physically available in the soil and the capacity of the plant to extract it, due to its root characteristics, corresponding to the concept of AWC (amount of water between field capacity hFC and wilting point hWP). The ratio of actual transpiration to maximal transpiration, is a bilinear function of the amount of water available in the rooting zone (with a minimum value of 0 when the soil water content is equal to hWP and a maximum value equal to (hFC-hWP)). The soil water content regarded as being the threshold between the maximal transpiration stage and the reduced transpiration stage depends on root density, stomatal functioning of the plant and climatic demand. Water stress indices are derived from those calculations and affect transpiration and different components of plant growth.

The soil is considered as a reservoir and is defined as a succession of up to five homogeneous layers characterized each by its retention capacity characteristics (hFC and hWP, bulk density and thickness). Water transfer downwards in the soil microporosity is <span id="page-4-0"></span>simulated on a one-dimensional regular mesh discretized per 1 cm step with a functional reservoir type model according to the tipping bucket concept. Incoming water fills the layers by downward flow, assuming that the upper limit of each single reservoir corresponds to the layer's field capacity.

The STICS model contains about 200 input parameters which are related to the characteristics of the plant, soil and crop management activities. The plant parameters for sunflower, sorghum, turmeric and maize related to leaf growth, biomass, yield, and root growth were calibrated with the OptimiSTICS software ([Buis](#page-11-0) [et al., 2011](#page-11-0)), using all the available data on a restricted number of plots that were therefore not used for inversions. With the calibrated model, the crop specific parameters can be assumed constant for the given crop for the study area. The parameters related to the agricultural practices (sowing dates, fertilization dates and doses, irrigation dates and doses and harvest dates) were set in accordance with the information collected from farmers.

In order to reduce the number of soil parameters to be potentially estimated, we adopted the simplified representation of the soil proposed by [Varella et al. (2010a):](#page-12-0) a surface layer and a second layer mainly representing the root zone. The first layer depth was set at 10 cm which is compatible both with our field measurements of SSM and the order of magnitude of SSM retrievals from radar remote sensing ([Jackson et al., 1995; Baghdadi and Zribi,](#page-11-0) [2006)](#page-11-0) for further applications at larger scale. Here we considered only the permanent soil properties related to water storage and transfers in the soil and restricted the estimation to five parameters: soil moisture at field capacity (hFC) and wilting point (hWP) of both layers and thickness of the second layer (DL2) (Table 4). These parameters describe the AWC (expressed in mm) of each layer which determines maximum water storage and available water for plant uptake as follow:

$$\mathbf{A}\mathbf{W}\mathbf{C} = (\theta_{\mathbf{f}\mathbf{C}} - \theta_{\mathbf{W}\mathbf{P}}) \cdot \mathbf{B}\mathbf{D} \cdot \mathbf{D}_{\mathbf{L}} \cdot \mathbf{1}\mathbf{0}^{-1} \tag{1}$$

where BD is the bulk density (g/cm3 ) and DL is the thickness (cm) of the layer.

These parameters influence also other processes such as soil evaporation, carbon and nitrogen cycle in the soil [(Brisson et al.,](#page-11-0) [2008)](#page-11-0). They are involved separately in some of these processes which bring independent constraints for their estimation. The soil input parameters non-estimated in the inversion process were obtained from local soil maps, soil experiments and standard values for soil classes (details are provided in Appendix-A).

## 2.5. Inversion method

Generalized Likelihood Uncertainty Estimation (GLUE) approach is an informal Bayesian method using prior information of parameter values for estimating model parameters [(Beven and](#page-11-0) [Binley, 1992; Makowski et al., 2002)](#page-11-0). Based on Monte Carlo simulation, GLUE transforms the problem of searching an optimal parameter set into searching sets of parameter values which would produce reliable simulations of the variables of interest ([Aronica](#page-11-0) [et al., 2002](#page-11-0)). GLUE based approaches have been successfully applied to hydrological models (e.g. [Li et al., 2010)](#page-11-0) and dynamic

## crop models [(Makowski et al., 2004; Guérif et al., 2006; Varella](#page-11-0) [et al., 2010a, 2010b; Sreelash et al., 2012)](#page-11-0).

Sets of parameters values are randomly chosen in a prior distribution representing the potential parameter space. These sets are then used in model simulations, which produce multiple sets of values of output variables of interest. These outputs are compared with measured values with an appropriate likelihood measure. The parameters values corresponding to the highest likelihoods are called acceptable or ''behavioural" values. The size of this ensemble is defined as a proportion of the total number of parameters values: the acceptable sample rate (ASR). The behavioural values are then used to determine the estimates of the parameters and their uncertainty bounds.

Prior information was defined here as independent uniform distributions whose bounds are the minimum and maximum of the observed values measured on a wide set of 60 plots (larger than the 33 considered in this study) in different soil types of the Berambadi catchment (Table 4). These lower and upper bounds of the parameters were decreased/increased by 10% to account for any errors in the measured soil moisture. The parameters sets were sampled in the prior distributions using Latin Hypercube Sampling (LHS; [McKay et al., 1979)](#page-12-0). An initial sample of size 20,000 was produced and then filtered to remove parameter combinations which were considered as not reasonable. The sampled combinations in which (hFC1 hWP1) 6 7.0 g/g and (hFC2 hWP2) 6 7.0 g/g were removed since these situations were never observed in the field experimental data. The simulations were carried out for the 9500 remaining samples.

We used the sum of absolute errors (SAE), proposed by [Brazier](#page-11-0) [et al. (2000)](#page-11-0) as the likelihood metric. SAE was calculated for each variable considered in the inversion for each model run as,

$$\mathbf{SAE}_i^k = \sum_{j=1}^{M_i} |\hat{\mathbf{y}}_{ij}^k - \mathbf{y}_{ij}| \tag{2}$$

where SAEk i is the sum of absolute errors for parameter set k, with k = 1 to N (N being the number of sets), variable i, with i = 1 to n (n being the total number of variables considered), and measurement date j, with j = 1 to Mi (Mi being the total measurements dates for the variable i), y^k i;j is the simulated value of variable i at date j for the parameter set k and yi;j is the measured value of variable i at date j.

Observations used to estimate soil parameters were made of a combination of two STICS output variables: SSM and LAI. On average, 10 observations of LAI and SSM were used in case of turmeric plots and 7 observations in the case of sunflower, sorghum and maize plots [(Table 1)](#page-2-0). The SAE values of SSM and LAI were normalized (RSAE) to take into account their varying units and magnitudes (Eq. (3)). We used a combined likelihood function by assigning weights to RSAE of LAI and SSM so as to take into account in an appropriate way the relative influence of these variables (Eq. [(4)](#page-5-0)). Based on the results of preliminary experiments carried out to study the influence of each variable on the parameter estimation (not reported here), we set w1 to 0.4 and w2 to 0.6.

Table 4

| The soil parameters of STICS model selected for estimation along with their initial ranges of values used as prior information. |  |  |  |
|---------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|---------------------------------------------------------------------------------------------------------------------------------|--|--|--|

| Parameter (name in STICS) | Definition                                 | Unit | Initial Range |
|---------------------------|--------------------------------------------|------|---------------|
| hFC1 (HCC(1))             | Water content at field capacity of layer 1 | g/g  | 10–32         |
| hFC2 (HCC(2))             | Water content at field capacity of layer 2 | g/g  | 10–32         |
| hWP1 (HMINF(1))           | Water content at wilting point of layer 1  | g/g  | 5–15          |
| hWP2 (HMINF(2))           | Water content at wilting point of layer 2  | g/g  | 5–15          |
| DL2 (EPC(2))              | Thickness of layer 2                       | cm   | 70–150        |

<span id="page-5-0"></span>
$$R\text{SAE}_i^k = \frac{\text{SAE}_i^k}{\sum_{k=1}^N \text{SAE}_i^k} \tag{3}$$

$$\text{CL}^k = \left(\text{w}_1 \ast \text{RSA}_{\text{LAl}}^k + \text{w}_2 \ast \text{RSA}_{\text{SSM}}^k\right)^{-1} \tag{4}$$

where w1 þ w2 ¼ 1.

ASR was set to 4% based on these preliminary experiments. The medians of the behavioural values were taken as the estimates of the parameters.

#### 2.6. Statistical criteria for assessing inversion performance

Several criteria are used for assessing the performance of the inversion process:

For each parameter and each inversion situation, a relative absolute error (RAE) was computed, based on the difference between estimated and observed values:

$$RAE_{i,p} = \text{abs}\left(\frac{\left(\chi_{i,p}^{\text{obs}} - \bar{\chi}_{i,p}^{\text{post}}\right)}{\chi_{i,p}^{\text{obs}}}\right) \tag{5}$$

where xobs i;p is the observed value of the soil parameter xi for a given plot p and xpost i;p is the corresponding value of the estimate obtained from the GLUE method.

A mean absolute error (MRAE) was computed as the mean of RAE of a given parameter xi for the different plots.

$$\text{MRAE}_{i} = \frac{1}{\mathcal{P}} \sum_{p=1}^{p} \text{RAE}_{i,p} \tag{6}$$

A relative error (REi) was used to quantify the improvement brought by the inversion process with respect to prior information. REi was computed here as the ratio of the MRAE calculated for the estimated parameter xpost i to that calculated for the prior information xprior i .

$$RE_i = \frac{\text{MRAE}(\bar{\mathbf{x}}_i^{\text{post}})}{\text{MRAE}(\bar{\mathbf{x}}_i^{\text{prior}})} \tag{7}$$

REi quantifies the improvement (REi < 1) or degradation (REi P 1) in the estimate of parameter xi with respect to prior information [(Varella et al., 2010a)](#page-12-0).

As an alternative to RE, the information brought by the inversion process in the parameter estimate was also assessed, for each parameter and each inversion situation, by comparing the standard deviation of the prior and posterior parameter distributions, using a normalized standard deviation given in Eq. (8):

$$
\sigma_{\text{norm}_{i,p}} = \frac{\sigma_{\text{s}^{\text{sout}}_{i,p}}}{\sigma_{\text{s}^{\text{stor}}_{i,p}}} \tag{8}
$$

rnormi;p quantifies the reduction (rnormi;p < 1Þ or increase (rnormi;p > 1Þ in the uncertainty of the estimate of parameter xi with respect to this of its prior information.

## 2.7. Sensitivity analysis

We performed a sensitivity analysis to assess the information content of LAI and SSM observations for estimating AWC components [(Varella et al., 2010a](#page-12-0)). Sobol' main sensitivity indices [(Saltelli et al., 2008](#page-12-0)), which measure the part of variance of simulated outputs explained by the parameters independently from each other, were estimated using the EASI (effective algorithm for computing global sensitivity indices) method [(Plischke, 2010](#page-12-0)). The main advantage of this method is that it does not require any specific numerical experiment design for the estimation of the indices. They have thus been computed at no extra cost using all the simulations performed for the model inversions. Nonnormalized Sobol' indices were used (i.e. Sobol' indices multiplied by the total variance of SSM/LAI) to visualize the variance explained by each parameter and not ʻjust' the proportion of total variance they explain.

No tables found before Methods section.