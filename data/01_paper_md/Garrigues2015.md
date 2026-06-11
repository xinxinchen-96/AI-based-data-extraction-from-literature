<span id="page-0-1"></span>Hydrol. Earth Syst. Sci., 19, 3109–3131, 2015 www.hydrol-earth-syst-sci.net/19/3109/2015/ doi:10.5194/hess-19-3109-2015 © Author(s) 2015. CC Attribution 3.0 License.

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

# **Evaluation of land surface model simulations of evapotranspiration over a 12-year crop succession: impact of soil hydraulic and vegetation properties**

**S. Garrigues**[1,2](#page-0-0) **, A. Olioso**[1,2](#page-0-0) **, J. C. Calvet**[3](#page-0-0) **, E. Martin**[3](#page-0-0) **, S. Lafont**[5](#page-0-0) **, S. Moulin**[1,2](#page-0-0) **, A. Chanzy**[1,2](#page-0-0) **, O. Marloie**[4](#page-0-0) **, S. Buis**[1,2](#page-0-0) **, V. Desfonds**[1,2](#page-0-0) **, N. Bertrand**[1,2](#page-0-0) **, and D. Renard**[1,2](#page-0-0)

EMMAH (UMR1114), INRA, Avignon, France Université d'Avignon et des Pays de Vaucluse, UMR1114 – EMMAH, 84000 Avignon, France CNRM-GAME (UMR3589), Météo-France, CNRS, Toulouse, France URFM, INRA, Avignon, France 5 ISPA, INRA, Bordeaux, France

*Correspondence to:* S. Garrigues (sebastien.garrigues@paca.inra.fr)

Received: 8 August 2014 – Published in Hydrol. Earth Syst. Sci. Discuss.: 23 October 2014 Revised: 22 May 2015 – Accepted: 28 May 2015 – Published: 16 July 2015

<span id="page-0-0"></span>**Abstract.** Evapotranspiration has been recognized as one of the most uncertain terms in the surface water balance simulated by land surface models. In this study, the SURFEX/ISBA-A-gs (Interaction Sol–Biosphere– Atmosphere) simulations of evapotranspiration are assessed at the field scale over a 12-year Mediterranean crop succession. The model is evaluated in its standard implementation which relies on the use of the ISBA pedotransfer estimates of the soil properties. The originality of this work consists in explicitly representing the succession of crop cycles and inter-crop bare soil periods in the simulations and assessing its impact on the dynamics of simulated and measured evapotranspiration over a long period of time. The analysis focuses on key parameters which drive the simulation of ET, namely the rooting depth, the soil moisture at saturation, the soil moisture at field capacity and the soil moisture at wilting point. A sensitivity analysis is first conducted to quantify the relative contribution of each parameter on ET simulation over 12 years. The impact of the estimation method used to retrieve the soil parameters (pedotransfer function, laboratory and field methods) on ET is then analysed. The benefit of representing the variations in time of the rooting depth and wilting point is evaluated. Finally, the propagation of uncertainties in the soil parameters on ET simulations is quantified through a Monte Carlo analysis and compared with the uncertainties triggered by the mesophyll conductance which is a key above-ground driver of the stomatal conductance.

This work shows that evapotranspiration mainly results from the soil evaporation when it is continuously simulated over a Mediterranean crop succession. This results in a high sensitivity of simulated evapotranspiration to uncertainties in the soil moisture at field capacity and the soil moisture at saturation, both of which drive the simulation of soil evaporation. Field capacity was proved to be the most influencing parameter on the simulation of evapotranspiration over the crop succession. The evapotranspiration simulated with the standard surface and soil parameters of the model is largely underestimated. The deficit in cumulative evapotranspiration amounts to 24 % over 12 years. The bias in daily daytime evapotranspiration is −0.24 mm day−1 . The ISBA pedotransfer estimates of the soil moisture at saturation and at wilting point are overestimated, which explains most of the evapotranspiration underestimation. The use of field capacity values retrieved from laboratory methods leads to inaccurate simulation of ET due to the lack of representativeness of the soil structure variability at the field scale. The most accurate simulation is achieved with the average values of the soil properties derived from the analysis of field measurements of soil moisture vertical profiles over each crop cycle. The representation of the variations in time of the wilting point and the maximum rooting depth over the crop succession has little impact on the simulation performances. Finally, we show that the uncertainties in the soil parameters can generate substantial uncertainties in ET simulated over 12 years (the 95 % confidence interval represents 23 % of cumulative ET over 12 years). Uncertainties in the mesophyll conductance have lower impact on ET. Measurement random errors explain a large part of the scattering between simulations and measurements at half-hourly timescale. The deficits in simulated ET reported in this work are probably larger due to likely underestimation of ET by eddy-covariance measurements. Other possible model shortcomings include the lack of representation of soil vertical heterogeneity and root profile along with inaccurate energy balance partitioning between the soil and the vegetation at low leaf area index.

## **2 Site and measurements**

#### **2.1 Site characteristics**

The "remote sensing and flux site" of INRA (National Institute of Agronomic Research) Avignon1 (France; 43◦55000.400 N, 4◦52041.000 E (WGS84 system); alt = 32 m a.s.l.) is characterized by a Mediterranean climate with a mean annual temperature of 14 ◦C and a mean annual precipitation of 687 mm. Rainfall mainly occurs in autumn (43 % of yearly rainfall). It is a flat agricultural field oriented north–south in the prevailing wind direction (Fig. 1). The field size is 1.9 ha. In this work, we study a 12-year crop succession from April 2001 to December 2012 (Fig. 2, Table 1). The crop succession consists in a succession of winter arable crops (wheat, peas) and summer arable crops (sorghum, maize, sunflower). Periods between two consecutive crop cycles lasted ∼ 1–1.5 months in the case of a summer crop followed by a winter crop and ∼ 9–10 months in the reverse case. During inter-crop periods, the soil is mostly bare. Limited wheat regrowths occurred over short periods of time. Irrigation is triggered only for summer crops (every 2 years) and concerns the May–July period.

#### **2.2 Field measurements**

Soil moisture, plant characteristics and micrometeorological observations were continuously monitored over the 12-year

<sup>1</sup>[https://www4.paca.inra.fr/emmah_eng/Facilities/](https://www4.paca.inra.fr/emmah_eng/Facilities/In-situ-facilities/Remote-Sensing-Fluxes) [In-situ-facilities/Remote-Sensing-Fluxes](https://www4.paca.inra.fr/emmah_eng/Facilities/In-situ-facilities/Remote-Sensing-Fluxes)

crop succession. A map of the field with the location of the instruments is given in Fig. 1.

# **2.2.1 Soil measurements**

A neutron probe was used to retrieve volumetric soil moisture in three (0–1.90 m) soil profiles with a vertical resolution of 10 cm. To implement the measurements, three neutron probe access tubes, spaced 40 m apart, were installed along a north–south transect located at the centre of the field. A calibration was done for every access tube and soil layer by relating neutron count rates to soil moisture measured by gravimetric method. The average soil moistures at given depth over the soil profiles were then used. The measurements were performed on a weekly basis.

Surface ground heat flux (G) was derived from four heat flux plate measurements located at 5 cm depth. One plate was located along the crop row and the others were equally spaced apart in the inter-row. We accounted for heat storage estimated from temperature and soil moisture measured within the 5 cm layer.

# **2.2.2 Plant measurements**

Plant characteristics (leaf area index (LAI), height, biomass) were monitored over all the crop cycles between April 2001 and December 2012. Canopy height was measured every 10 days using a standard measuring tape. Leaf area index and plant biomass were measured at key crop phenological stages (five to six measurements per crop cycle) using destructive methods and sampling schemes adapted to each crop. LAI was retrieved using a planimeter device and plant biomass was measured using a high-precision scale device. Plant characteristics were measured at four locations in the field (Fig. 2) to sample the within field variability. Average values were recorded. Vegetation height was linearly interpolated on a daily basis. Daily interpolation of LAI was achieved using a functional relationship between LAI and the sum of degree days (Duveiller et al., 2011).

# **2.2.3 Micrometeorological measurements**

Half-hourly observations of air temperature and humidity, wind speed, and atmospheric pressure were continuously monitored at a height of 2 m above the ground or the canopy from a micro-meteorological station located at the centre of the field. Cumulative rainfall was measured from a standard meteorological station located at 150 m apart from the centre of the field. Net radiation (RN) was computed from shortwave and longwave upwelling and downwelling radiations which are measured from a net radiometer device located at the centre of the field and oriented southward.

Sensible (H) and latent (LE) heat fluxes were computed from an eddy-covariance system oriented northward in the prevailing wind direction. The latter was composed of a 3-D sonic anemometer set up in 2001 and of an open-path gas (H2O, CO2) analyser set up in November 2003. The system was monitored following the state-of-the-art guidelines for cropland sites (Rebmann et al., 2012; Moureaux et al., 2012). Fluxes were computed on 30 min intervals using the EDIRE software2 . The flux data processing included spike detection on raw data and standard eddy-covariance corrections (coordinate rotation, density fluctuations, frequency loss). The ECPP3 software (Beziat et al., 2009) was used to discard spurious flux (e.g. friction velocity and footprint controls) and to apply the Foken et al. (2004) quality control tests on the temporal stationarity and the development of turbulence conditions. In this work, only the best quality class of data (Mauder et al., 2013) were used. An additional threshold of 100 W m−2 on the energy balance nonclosure was applied to eradicate very inconsistent fluxes. Direct eddy-covariance measurements of LE are used over the 20 November 2003–18 December 2012 period. They represent 60 % of the period (71 % if we consider only daytime). When no direct measurement of LE was available (2001– 2003 period), LE was estimated as the residue of the energy balance (LE = RN − G − H). Valid direct and indirect LE measurements represent 65 % of the 25 April 2001–18 December 2012 period (77 % of daytime). Cumulative ET in millimetres over a given period of time was computed from LE half-hourly measurements.

# **2.3 Soil properties**

Table 2 presents the values of the soil parameters averaged over the 0–1.2 m soil layer, where most of the root-zone processes occur. The soil moisture at saturation (θs) was derived from soil bulk density measurements performed within the 0–1.2 m layer at different field locations and times over the 12-year period. We used the average value of θs to be representative of the soil structure at the field scale at which the simulations were conducted. The soil moisture at field capacity (θfc) and wilting point (θwp) were retrieved using laboratory or field methods.

- 1. Laboratory method: it consisted in adjusting a Brooks and Corey (1966) retention curve model over soil matric potential (h) and soil water content measured in laboratory. These measurements were obtained from the Richard pressure plate apparatus at matric potentials of −1, −2, −3, −5, −10, −30, −50, −100, and −150 m (Bruckler et al., 2004). They were collected for three soil layers at depths of 0–0.4, 0.4–0.8 and 0.8– 1.2 m. A retention model was adjusted for each soil layer and was used to retrieve θfc and θwp for each soil layer. θwp was computed for h = −150 m. Most studies agree on this definition (Boone et al., 1999; Olioso et
<sup>2</sup>Robert Clement, ©1999, University of Edinburgh, UK, [http:](http://www.geos.ed.ac.uk/abs/research/micromet/EdiRe) [//www.geos.ed.ac.uk/abs/research/micromet/EdiRe.](http://www.geos.ed.ac.uk/abs/research/micromet/EdiRe)

<sup>3</sup>Eddy Covariance Post-Processing, Pierre Béziat, CESBIO, Toulouse, France.

**Table 1.** 2001–2012 crop succession.

| Year | Crop       | Sowing      | Harvest     | Irrigation | Rain  | T    |
|------|------------|-------------|-------------|------------|-------|------|
|      |            | date        | date        | (mm)       | (mm)  | (◦C) |
| 2001 | Maize      | 25 Apr 2001 | 28 Sep 2001 | 375        | 232.0 | 20.7 |
| 2002 | Wheat      | 23 Oct 2001 | 2 Jul 2002  | 0          | 399.0 | 11.6 |
| 2003 | Sunflower1 | 16 Apr 2003 | 26 May 2003 | 40         | 68.0  | 17.1 |
| 2003 | Sunflower  | 2 Jun 2003  | 19 Sep 2003 | 225        | 68.5  | 24.8 |
| 2004 | Wheat      | 7 Nov 2003  | 28 Jun 2004 | 0          | 422.0 | 11.2 |
| 2005 | Peas       | 13 Jan 2005 | 22 Jun 2005 | 100        | 203.5 | 11.9 |
| 2006 | Wheat      | 27 Oct 2005 | 27 Jun 2006 | 20         | 256.0 | 10.7 |
| 2007 | Sorghum    | 10 May 2007 | 16 Oct 2007 | 80         | 168.5 | 20.6 |
| 2008 | Wheat      | 13 Nov 2007 | 1 Jul 2008  | 20         | 502.5 | 11.7 |
| 2009 | Maize2     | 23 Apr 2009 | 15 Jun 2009 | 80         | 110.5 | 19.2 |
| 2009 | Sorghum    | 25 Jun 2009 | 22 Sep 2009 | 245        | 89.0  | 23.6 |
| 2010 | Wheat      | 19 Nov 2009 | 13 Jul 2010 | 0          | 446.5 | 11.6 |
| 2011 | Sorghum    | 22 Apr 2011 | 22 Sep 2011 | 60         | 268.5 | 21.4 |
| 2012 | Wheat      | 19 Oct 2011 | 25 Jun 2012 | 0          | 437.0 | 12.0 |
|      |            |             |             |            |       |      |

The first sunflower in 2003 (1) was stopped and replaced by a new one. The 2009 maize (2) was stopped and replaced by sorghum because the emergence of maize was too heterogeneous. T and rain are the mean temperature and cumulative precipitation, respectively, over the crop cycle.

![](_page_4_Figure_5.jpeg)

**Figure 2.** Illustration of the typical succession of winter and summer crop over the Avignon site and implementation of the crop succession in the simulations. θ and T represent soil moisture and soil temperature transmitted from one sub-simulation to the following one.

al., 2002). For wfc two definitions were used. We estimated θfc at h = −3.3 m, which corresponds to the agronomic definition (Olioso et al., 2002) and for a hydraulic conductivity of K = 0.1 mm day−1 which can be found in hydrological applications (Wetzel and Chang, 1987; Bonne et al., 1999). θwp and θfc estimates were averaged over the 0–1.2 m soil profile and their values are reported in Table 2.

- 2. Field method: θfc and θwp were inferred from field measurements of soil moisture. The time evolution of the root-zone (0–1.2 m) soil moisture was analysed over each crop cycle. Under Mediterranean climate, the rootzone soil moisture generally starts from an upper-level which approximates θfc. It generally reaches a lowerlevel at the end of the growing season which often ap-
proaches θwp. The typical evolution of the root-zone soil moisture over the growing season is illustrated in Fig. 5b for wheat. To be consistent with the previous method, we integrated the soil moisture measurements over the 0–0.4, 0.4–0.8 and 0.8–1.2 m soil layers. θfc and θwp were estimated for each soil layer as the maximum and the minimum, respectively, soil moisture over the growing season. θfc and θwp values were averaged over the 0–1.2 m soil profile for each crop cycle (Table 3). θwp varies from one crop to another, but its mean value is close to the one derived from the retention curve. θfc shows lower temporal variability but its mean value significantly differs from the retention curve estimate.

The maximum rooting depth (Zroot-zone) was estimated from the analysis of the evolution in time of the vertical profiles

**Table 2.** Mean soil properties over the 0–1.2 m soil profile. Density is the soil bulk density. θs is the soil moisture at saturation derived from bulk density measurements. θwp and θfc are the soil moisture at wilting point and field capacity, respectively, derived from laboratory methods for given hydraulic conductivity (K) or matric potential (h) levels. The second and third rows represent the vertical (σV) and the spatiotemporal (σST) variability of these measurements, respectively. NA means not available.

|           | Clay<br>(%) | Sand<br>(%) | Density<br>(g cm−3<br>) | θs<br>(m3 m−3<br>) | θwp<br>(h = −150 m)<br>(m3 m−3<br>) | θfc<br>(h = −3.3 m)<br>(m3 m−3<br>) | θfc<br>0.1 mm day−1<br>(K =<br>)<br>(m3 m−3<br>) |
|-----------|-------------|-------------|-------------------------|--------------------|-------------------------------------|-------------------------------------|--------------------------------------------------|
| Mean      | 33.15       | 13.95       | 1.57                    | 0.390              | 0.170                               | 0.344                               | 0.268                                            |
| σV<br>σST | 0.58<br>NA  | 1.14<br>NA  | 0.16<br>0.05            | 0.056<br>0.019     | 0.011<br>NA                         | 0.021<br>NA                         | 0.027<br>NA                                      |

**Table 3.** Estimates of the rooting depth (Zroot-zone), the soil moisture at field capacity (θfc) and the soil moisture at wilting point (θwp) derived from the time evolution of vertical profiles of fieldmeasured soil moisture. MaxAWC (maximum available soil water capacity; in mm) represents the maximum root-zone water stock available for the crop. When no measurements were available, the mean value (in italic) from a similar crop type was used. The last two rows are the mean and the SD (standard deviation) computed over all crop cycles.

| Crop      | Year | Zroot-zone<br>(m) | θfc<br>(m3 m−3<br>) | θwp<br>(m3 m−3<br>) | MaxAWC<br>(mm) |  |
|-----------|------|-------------------|---------------------|---------------------|----------------|--|
| Maize     | 2001 | 1.45              | 0.320               | 0.174               | 212            |  |
| Wheat     | 2002 | 1.55              | 0.314               | 0.126               | 291            |  |
| Sunflower | 2003 | 1.80              | 0.311               | 0.209               | 184            |  |
| Wheat     | 2004 | 1.65              | 0.314               | 0.183               | 216            |  |
| Peas      | 2005 | 1.00              | 0.308               | 0.218               | 90.0           |  |
| Wheat     | 2006 | 1.85              | 0.309               | 0.179               | 241            |  |
| Sorghum   | 2007 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2008 | 1.00              | 0.279               | 0.202               | 77.0           |  |
| Maize     | 2009 | 1.45              | 0.320               | 0.174               | 212            |  |
| Sorghum   | 2009 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2010 | 1.75              | 0.327               | 0.182               | 254            |  |
| Sorghum   | 2011 | 1.65              | 0.306               | 0.183               | 203            |  |
| Wheat     | 2012 | 1.50              | 0.309               | 0.174               | 203            |  |
| Mean      |      | 1.50              | 0.310               | 0.184               | 189            |  |
| SD        |      | 0.30              | 0.012               | 0.025               | 56.0           |  |

of soil moisture field measurements over the growing season of each crop period. Zroot-zone was approximated by the depth at which the soil moisture change in time vanished (Table 3). We assumed that at a given depth, the time variations in soil moisture due to the vertical diffusion and gravitational drainage were smaller than those generated by the plant water uptake (Olioso et al., 2002). This is a reasonable hypothesis for low hydraulic conductivity soil as the one under study. The Zroot-zone = 1.85 m obtained for wheat in 2006 can be related to the dryness of the crop period (256 mm of rain). The shallower Zroot-zone = 1.0 m obtained for wheat in 2008 can be related to the wetness of the crop period (500 mm of rain).

#### **3 The ISBA-A-gs model**

#### **3.1 Model description**

The ISBA model (Noilhan and Planton, 1989; Noilhan and Mahfouf, 1996) is developed at the CNRM (National Centre for Meteorological Research)/Météo France within the SUR-FEX surface modelling platform (Masson et al., 2013). In this study, we used the version 6.1 of SURFEX. ISBA relies on a single surface energy budget of a soil–vegetation composite. The surface temperature is simulated using the Bhumralkar (1975) and Blackadar (1976) force restore scheme for heat transfers. A horizontal soil/snow/ice/vegetation surface partitioning is used to simulate the evapotranspiration. The soil water transfers are simulated using a force-restore scheme adapted from Deardoff (1977) with three reservoirs: the superficial layer of thickness dsurf = 0.01 m designed to regulate the soil evaporation, the root zone which extends from the surface to the depth Zroot-zone and the deep reservoir which extends from the base of the root zone to the total soil depth. The force restore coefficients were parameterized as a function of the soil hydrodynamic properties which were derived from the Brooks and Corey (1966) retention model. θfc and θwp are defined for K = 0.1 mm day−1 and for h = −150 m, respectively. The soil parameters are derived from clay and sand fractions using the ISBA pedotransfer functions. The latter were built upon on the Clapp and Hornberger (1978) soil texture classification using statistical multiple regressions (Noilhan and Laccarère, 1994). The forcerestore equations and coefficient formulas are given in Boone et al. (1999). Regarding the vegetation processes, we used the A-gs version of ISBA (Calvet et al., 1998, 2008). A-gs is a coupled stomatal conductance–photosynthesis scheme. It uses a CO2 responsive parametrization of photosynthesis based on the model of Goudriaan et al. (1985) and modified by Jacobs et al. (1996). It computes the stomatal conductance as a function of the net assimilation of CO2. The CO2 mesophyll conductance at a leaf temperature of 25◦ (gm) is the main tunable parameter of the A-gs scheme (Calvet et al., 1998, 2012). It represents the response curve of the lightsaturated net rate of CO2 assimilation to the internal CO2

concentration. The simulation of the plant response to water stress (Calvet, 2000; Calvet et al., 2012) is mainly driven by the maximum root-zone water stock available for the plant (MaxAWC) which is defined by

$$\text{MaxAWC} = Z_{\text{root-zone}} \left( \theta_{\text{fc}} - \theta_{\text{wp}} \right) . \tag{1}$$

The model is parametrized through 12 generic land surface patches using the ECOCLIMAP-II database which provides the ISBA surface parameters for ∼ 273 distinct land cover types over Europe (Faroux et al., 2013).

#### **3.2 Model implementation at the Avignon site**

The simulations were conducted at the field scale. ISBA-Ags was run at a 5 min time step and 30 min outputs of the state variables were analysed. Continuous simulations were performed from 25 April 2001 up to 18 December 2012. The 12 year period was split into sub-simulations corresponding to crop and inter-crop periods (Fig. 2). The simulation was initialized once on 25 April 2001 using in situ soil temperature and soil moisture measurements for each soil layer. To ensure the continuity between two contiguous sub-simulations, each sub-simulation was initialized using the simulated soil moisture and soil temperature of the last time step of the previous sub-simulation. The C3 crop patch was used to represent wheat, pea and sunflower crops. The C4 crop patch was used for maize and sorghum crops. Inter-crop periods were represented by the bare soil patch. ISBA-A-gs was driven by local meteorological observations. It was forced by in situ LAI and vegetation height measurements averaged over 10 days. Crop irrigation was not simulated by the model and the actual amount of irrigation water was added to the local rainfall. The simulations were designed to be representative of the field scale. The values of the in situ soil and vegetation parameters used in the simulations correspond to the field average.

No tables found before Methods section.