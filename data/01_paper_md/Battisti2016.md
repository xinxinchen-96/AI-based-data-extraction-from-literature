Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/03784290)

# Field Crops Research

jour nal home page: [www.elsevier.com/locate/fcr](http://www.elsevier.com/locate/fcr)

## Inter-comparison of performance of soybean crop simulation models and their ensemble in southern Brazil

Rafael Battisti a, Paulo C. Sentelhas a,∗, Kenneth J. Boote b

a Department of Biosystems Engineering, ESALQ, University of São Paulo, Piracicaba, SP, Brazil b Agronomy Department, University of Florida, Gainesville, FL, USA

## a r t i c l e i n f o

Article history: Received 2 May 2016 Received in revised form 2 September 2016 Accepted 4 October 2016 Available online 15 October 2016

**2. Materials and methods**

#### 2.1. Field experiments

The soybean development, growth and yield data were obtained from different sites in Southern Brazil. These data were divided into two sets, with first one used to calibrate the crop models and the secondfor their evaluation[(Table](#page-2-0) 1). For the sites of FredericoWestphalen, RS, Londrina, PR, and Piracicaba, SP, field experiments were carried out during 2013/14, 2014/15 and 2015/16 crop seasons. For Dourados, MS, the results from 2014/15 crop season were obtained from [Comunello](#page-8-0) [(2015),](#page-8-0) while the other results were obtained from experiments conducted by [Fundac¸](#page-8-0) ão [(2015)](#page-8-0) in Naviraí, São Gabriel do Oeste, and Antônio João. Details of the locations, sowing dates and crop water management are presented in [Table](#page-2-0) 1, while in the Supplementary material (Fig. A1) is shown the geographic position of each site and their respective Köppen's climate classification, according to [Alvares](#page-8-0) et [al.](#page-8-0) [(2013).](#page-8-0)

The cultivar used in all field trials was BRS 284, maturity group 6.5, with indeterminate growth habit, and non-transgenic. This cultivar was chosen since it is recommended for the region of this study and for having a high potential yield, similar to the majority of the cultivars grown. In the field experiments, fertilization was applied to sustain crop growth without deficiency and was performed according to soil analysis, by applying mainly P and K and using rhizobium inoculation to improve soybean N fixation. The crop management followed EMBRAPAıs´ recommendations, keeping the crop free of pests and diseases [(EMBRAPA,](#page-8-0) [2013).](#page-8-0)

The row spacing was between 0.45 and 0.50 m, with the plant population between 26 and 32 plants m−2, respectively for highest and lowest latitudes [(EMBRAPA,](#page-8-0) [2013).](#page-8-0) In the most of locations the soybean was cultivated in no-tillage crop system, except for the experiment in Piracicaba in 2013/2014 crop season, where conventional tillage system was used. During 2013/2014 crop season, the field experiments conducted in Piracicaba (C3) and Dourados (E5) had full irrigation, while in Londrina (C2) the irrigation supplied 75% of crop evapotranspiration. For the other experiments, irrigation was used, when required, only after sowing to guarantee the emergence. The irrigation applied in each site is presented in Supplementary materials (Table A1).

### 2.2. Weather and soil data

Soil characteristics and weather data are the main inputs from field experiment in the crop models, as well as information about crop management such as sowing date, irrigation, row spacing, plant population and cultivar, as previously described. For Piracicaba, Londrina, Frederico Westphalen and Dourados the weather data were obtained from National Meteorological Institute weather stations located near each experiment(±100 m), while for the other sites the weather data were also obtained from stations of the National Meteorological Institute, but considering those that were in the same municipality. The following daily weather data were used: maximum and minimum air temperature; relative humidity; wind speed at 2 m; incoming solar radiation; and rainfall. Details about climate variability during field experiments are presented in Supplementary material (Table A1).

The main soil characteristics are presented in [Table](#page-2-0) 2. In the experiment C1, C2, C3, E1, E2, E3 and E5, the data required to build the soil profile were measured in the field experiment. For E4, E6, E7, E8 and E9, the data were obtained from [RADAM-](#page-9-0)Brazil [Project](#page-9-0) [(1974),](#page-9-0) providing information on clay, silt and sand contents, drainage, pH, carbon and nitrogen contents, and using pedo-transfer functions from[Lopes-Assad](#page-8-0) et [al.(2001)](#page-8-0) and[Reichert](#page-9-0) et [al.(2009)to](#page-9-0) estimate the water content on the soil. Following this information, the FAO model only requires total soil water holding capacity for the crop. For the MONICA model, the type of soil was defined based on the clay, silt and sand content and on the modelıs´ soil database. For APSIM, DSSAT and AQUACROP, the soil profiles were created based on the curve number that defines water infiltration [(Soil](#page-9-0) [Conservation](#page-9-0) [Service,](#page-9-0) [1972),](#page-9-0) bulk density, soil saturation, drained upper limit, lower limit and saturated conductivity. Soil analysis was limited to the top 0.50 m, which required extrapolations to a potentially deeper maximum root depth, with each model presenting a different definition for that [(Palosuo](#page-8-0) et [al.,](#page-8-0) [2011).](#page-8-0) As maximum root depth varies according each one of these models, it was one of the parameters adjusted during the calibration process.

#### 2.3. Crop growth and development

For the field experiments identified as C1, C2 and C3 [(Table](#page-2-0) 1), measurements were recorded for total above dry matter, leaf area index and specific leaf area on six dates (at 20 days after emergence, at beginning of flowering, beginning of pod formation, beginning seed formation, full seed and after full maturity). Measurements included grain yield at maturity, harvest index and the date of occurrence of planting, emergence, anthesis, beginning of pod formation, beginning of seed formation and maturity. All this information was used to calibrate the model coefficients. For the evaluation process, the field experiment E1 to E9 data included the yield at maturity and sowing date, while for E1, E2 and E3 the data included only the dates of each crop phase. Details ofthe methodology of these measurements are shown in Supplementary material (Table A2).

#### 2.4. Crop models

Soybean growth and development were simulated by five crop models, as follows: FAO – Agroecological Zone [(Kassam,](#page-8-0) [1977;](#page-8-0) [Doorenbos](#page-8-0) [and](#page-8-0) [Kassam,](#page-8-0) [1994;](#page-8-0) [Rao](#page-8-0) et [al.,](#page-8-0) [1988),](#page-8-0) referred to as FAO; FAO – AQUACROP v. 4.0 [(Steduto](#page-9-0) et [al.,](#page-9-0) [2009;](#page-9-0) [Raes](#page-9-0) et [al.,](#page-9-0) [2012),](#page-9-0) referred to as AQUACROP; Model for Nitrogen and Carbon in Agroecosystems v. 2.11 [(Nendel](#page-8-0) et [al.,](#page-8-0) [2011),](#page-8-0) referred to as MONICA; Crop SystemModel –CROPGRO – Soybeanv. 4.6.1presentinthe software Decision Support System for Agrotechnology Transfer ([Boote](#page-8-0) et [al.,](#page-8-0) [1998,](#page-8-0) [2003;](#page-8-0) [Jones](#page-8-0) et [al.,](#page-8-0) [2003),](#page-8-0) referred to as DSSAT; and Agricultural Production Systems Simulator v. 7.7 [(Robertson](#page-9-0) [and](#page-9-0) [Carberry,](#page-9-0)

## <span id="page-2-0"></span>**Table 1**

Location, crop season, sowing dates, water management, field experiment (FE) and number of yield results (n) for the experimental data used for crop models calibration (C) and evaluation (E), in Southern Brazil.

| FE          | Location                            | Crop Season | Sowing dates                              | Water management              | n  |
|-------------|-------------------------------------|-------------|-------------------------------------------|-------------------------------|----|
| Calibration |                                     |             |                                           |                               |    |
| C1          | Frederico Westphalen, RS; 27◦       | 2013/14     | 01/Oct, 18/Oct, 08/Nov, 25/Nov and 15/Dec | Rainfed                       | 5  |
|             | 21<br>S, 53◦ 23<br>W, 522 m asl     |             |                                           |                               |    |
| C2          | Londrina, PR; −23◦                  | 2013/14     | 10/Oct, 31/Oct, and 19/Nov                | Rainfed and Partial Irrigated | 6  |
|             | 18<br>S, 51◦ 09<br>W, 585 m asl     |             |                                           |                               |    |
| C3          | Piracicaba, SP, 22◦ 43<br>S,        | 2013/14     | 18/Oct, 14/Nov, and 08/Jan                | Rainfed and Full Irrigated    | 6  |
|             | 47◦ 38<br>W, 547 m asl              |             |                                           |                               |    |
|             | Total of data for calibration       |             |                                           |                               | 17 |
| Evaluation  |                                     |             |                                           |                               |    |
| E1          | Frederico Westphalen, RS;           | 2014/15     | 19/Nov and 18/Dec                         | Rainfed                       | 2  |
|             | 27◦ 21<br>S, 53◦ 23<br>W, 522 m asl |             |                                           |                               |    |
| E2          | Piracicaba, SP,                     | 2014/15     | 22/Dec                                    | Rainfed                       | 1  |
| E3          | 22◦ 43<br>S, 47◦ 38<br>W, 547 m asl | 2015/16     | 22/Oct, 19/Nov and 21/Jan                 | Rainfed                       | 3  |
| E4          | Dourados, MS,                       | 2013/14     | 19/Oct and 31/Oct                         | Rainfed                       | 2  |
| E5          | 22◦ 13<br>S, 54◦ 48<br>W, 430 m asl | 2014/15     | 22/Oct                                    | Rainfed and Full Irrigated    | 2  |
| E6          | Naviraí, MS,                        | 2013/14     | 09/Oct and 18/Oct                         | Rainfed                       | 2  |
|             | 23◦ 03<br>S, 54◦ 11<br>W, 362 m asl |             |                                           |                               |    |
| E7          | São Gabriel do Oeste, MS,           | 2013/14     | 14/Oct and 25/Oct                         | Rainfed                       | 2  |
| E8          | 19◦ 23<br>S, 54◦ 33<br>W, 658 m asl | 2014/15     | 20/Oct                                    | Rainfed                       | 1  |
| E9          | Antônio João, MS,                   | 2013/14     | 29/Oct                                    | Rainfed                       | 1  |
|             | 22◦ 11<br>S, 55◦ 56<br>W, 681 m asl |             |                                           |                               |    |
|             | Total of data for evaluation        |             |                                           |                               | 16 |
|             |                                     |             |                                           |                               |    |

#### **Table 2**

Soil types and their main characteristics used for building the soil profiles needed for FAO, MONICA, APSIM, DSSAT and AQUACROP crop models.

| FE         | Soil characteristicsa |        |    |    |    |          |      |      |      |      |      |      |  |  |
|------------|-----------------------|--------|----|----|----|----------|------|------|------|------|------|------|--|--|
|            | CN                    | BD     | S  | C  | Sn | Sat      | FC   | WP   | pH   | C    | N    | MSDa |  |  |
|            |                       | g cm−3 | %  |    |    | cm3 cm−3 |      |      |      | %    |      |      |  |  |
| Alfisols   |                       |        |    |    |    |          |      |      |      |      |      |      |  |  |
| C2; E2; E3 | 73                    | 1.36   | 13 | 56 | 31 | 0.61     | 0.45 | 0.26 | 5.60 | 0.98 | 0.10 | 180  |  |  |
| Oxisols    |                       |        |    |    |    |          |      |      |      |      |      |      |  |  |
| C1; E1     | 81                    | 1.20   | 19 | 66 | 15 | 0.59     | 0.49 | 0.29 | 5.30 | 1.16 | 0.10 | 160  |  |  |
| C3         | 81                    | 1.28   | 13 | 65 | 22 | 0.45     | 0.43 | 0.31 | 5.35 | 1.70 | 0.10 | 230  |  |  |
| E4         | 73                    | 1.45   | 7  | 15 | 78 | 0.40     | 0.16 | 0.08 | 4.90 | 0.62 | 0.05 | 290  |  |  |
| E5; E6     | 73                    | 1.36   | 19 | 66 | 15 | 0.46     | 0.38 | 0.22 | 5.50 | 1.00 | 0.10 | 200  |  |  |
| E7; E8     | 73                    | 1.30   | 37 | 24 | 39 | 0.44     | 0.31 | 0.18 | 5.20 | 1.60 | 0.09 | 160  |  |  |
| E9         | 73                    | 1.45   | 15 | 75 | 10 | 0.46     | 0.38 | 0.24 | 4.80 | 1.48 | 0.16 | 160  |  |  |

a FE: field experiment (Table 1); CN: Runoff curve number; BD: bulk density; S: silt; C: clay; Sn; sand content; Sat: saturation water point; FC: field capacity; WP: wilting point; C: carbon content; N: nitrogen content; MSD: maximum soil depth, which in each crop model was calibrated. For these soils, there were no limiting problems for drainage.

[1998;](#page-9-0) [Keating](#page-9-0) et [al.,](#page-9-0) [2003;](#page-9-0) [Holzworth](#page-9-0) et [al.,](#page-9-0) [2014),](#page-9-0) referred to as APSIM. These crop models were selected based on their international importance, different origins, different approaches and complexity, and mainly by their prior performance for estimating soybean around the world. Detailed information about these crop models are presented in Supplementary material (Table A3).

For running these models, the initial soil water content was defined based on the water balance initiated six months before sowing, considering the prior crop as fallow.

## 2.5. Calibration phases

The crop models were calibrated in three phases, always comparing the estimated with measured data, considering the experiments C1, C2 and C3 (Table 1):

- First phase (uncalibrated): the aim was to evaluate the efficiency of the crop model to simulate the measured results without any calibration using weather data, soil profile, and crop management (sowing date, irrigation, fertilization and initial condition) information from each site. In this phase,the modelsı´ coefficients were those from the defaultfor a cultivar with maturity group 6.5 (BRS 284) or similar.
- Second phase (calibration to life cycle phases): the coefficients associated with crop phenology were calibrated to achieve the lowest RMSE and the highest "d" values between simulated and measured dates of the following crop stages: emergence; beginning of flowering; beginning of pod; beginning of seed formation; and maturity.
- Thirdphase (growthcalibration): cropgrowthcoefficients (above and below the soil) were calibrated for each model to obtain the lowest RMSE and the highest "d" values for the comparison between simulated and measured values. At this phase, the following crop variables were evaluated: yield, total dry matter, leaf area index, specific leaf area, and harvest index. The procedures adopted for growth calibration followed [Hunt](#page-8-0) [and](#page-8-0) [Boote](#page-8-0) [(1998)](#page-8-0) recommendations, which are: 1st total dry matter; 2nd leaf area index and specific leaf area; 3rd total dry matter; 4th seed size and number of seeds; 5th seed dry weight; 6th seed size and shelling percentage. During these steps, the root growth distribution coefficients were adjusted based on the root profile observed by [Pivetta](#page-9-0) et [al.](#page-9-0) [(2011)](#page-9-0) and on model structure, changing the maximum root depth, root distribution along soil profile or maximum root water uptake by soil layer. The calibrated coefficients by model can be found in the Supplementary material (Table A4a and A4b).

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

**Fig. 1.** Observed (lines) and simulated (points) days after soybean sowing for flowering (R1), beginning of pod formation (R3), beginning of grain filling (R5) and maturity (R7), considering different calibrated crop models (a) and root mean square error (RMSE) for R1 and R7 dates in the end of each calibration phase (b).

![](_page_3_Figure_3.jpeg)

**Fig. 2.** Soybean total above-ground biomass (TAGB) measured and simulated by four crop models in the end of the third calibration phase under rainfed (a) and irrigated (b) conditions, in Piracicaba, SP, Brazil, with sowing date of 14/Nov/2013. The bars indicate standard deviation of measured values.

![](_page_3_Figure_5.jpeg)

**Fig. 3.** Relationship between measured and simulated soybean harvestindex, when using coefficients from the end of the third calibration phase for DSSAT and AQUACROP models. The bars indicate standard error of measured values.

For the evaluation phase, the experiments E1 to E9 were used [(Table](#page-2-0) 1). The crop models were run considering the coefficients obtained at the end of the third phase of calibration, and modelsı´ performances were evaluated only for grain yield.

## 2.6. Data analysis

The results obtained by the crop models and their ensemble (average of five models) were compared to measured field experimental data after each calibration phase and the following statistical indices and errors were computed [(Wallach](#page-9-0) et [al.,](#page-9-0) [2006):](#page-9-0) bias; mean absolute error (MAE);Willmott agreementindex (D) [(Willmott](#page-9-0) et [al.,](#page-9-0) [1985);](#page-9-0) root mean square error of prediction (RMSE); coefficient of determination (R2). Dispersion graphics with the relationship between measured and estimated yields were also used, as well as graphics of residual errors versus measured yields.

#

No tables found before Methods section.