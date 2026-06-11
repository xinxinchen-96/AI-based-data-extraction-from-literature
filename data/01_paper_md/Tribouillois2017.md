https://doi.org/10.1016/j.eja.2017.12.004>

Received 19 July 2017; Received in revised form 20 November 2017; Accepted 15 December 2017 Available online 23 December 2017

1161-0301/ ©

![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/11610301)

European Journal of Agronomy

![](_page_0_Picture_4.jpeg)

journal homepage: [www.elsevier.com/locate/eja](https://www.elsevier.com/locate/eja)

# Analysis and modeling of cover crop emergence: Accuracy of a static model and the dynamic STICS soil-crop model

![](_page_0_Picture_7.jpeg)

#### Hélène Tribouillois[⁎](#page-0-0) , Julie Constantin[⁎](#page-0-0) , Eric Justes[1](#page-0-1)

INRA, UMR 1248 AGIR, CS 52 627, Université de Toulouse, INPT, 31326 Castanet-Tolosan Cedex, France

# ARTICLE INFO

## 2. Materials and methods

# 2.1. Field experiment

A field experiment was performed in Auzeville, France (43.53°N, 1.58°E), in 2012 to obtain key emergence data of cover crops, such as emergence duration under non-limiting water conditions and maximum percentage of emerged plants. Ten species were studied: white mustard (Sinapis alba), vetch (Vicia sativa and V. benghalensis), bristle oat (Avena strigosa), Italian ryegrass (Lolium multiflorum), crimson clover (Trifolium incarnatum), faba bean (Vicia faba), foxtail millet (Setaria italica), turnip rape (Brassica rapa), forage pea (Pisum sativum) and phacelia (Phacelia tanacetifolia). Plots of 14 m2 were sown on 16 August and irrigated on 17, 20 and 29 August (20 mm each) to optimize emergence without water stress. The sowing density was 100 plants/m2 for white mustard, 110 plants/m2 for vetch, 220 plants/m2 for bristle oat, 550 plants/m2 for Italian ryegrass, 320 plants/m2 for crimson clover, 50 plants/m2 for faba bean, 680 plants/m2 for foxtail millet, 150 plants/m2 for turnip rape, 60 plants/m2 for forage pea and 390 plants/m2 for phacelia. Emerged epicotyls along one linear meter were counted daily until the maximum percentage of emerged plants was reached. Observed data were fitted with a Gompertz function as a function of degree days to obtain continuous dynamics and compare them among species.

# 2.2. Data from previous field experiments

We analyzed emergence dynamics of the ten cover crop species sown under a wide range of soil, climate and sowing conditions at 18 experimental sites across France ([Table 1](#page-2-0)). Experiments lasted for 1–9 years depending on the site, which provided contrasting climate conditions, even for the same site. Cover crops were sown in summer or early autumn at all sites, from 1 August (day of year or DOY 213) to 2 October (DOY 275). Mean sowing depth was 3 cm (range = 1–5 cm). Mean soil moisture on the sowing date in the seedbed layer (0–10 cm) varied from 1.3% (extremely dry) to 25.9%, (close to field capacity), depending on the site and year. Daily mean temperature for 15 days after sowing ranged from 16 to 25 °C, and water input (rainfall + irrigation) within seven days of sowing ranged from 1 to 45 mm, depending on the site ([Table 1](#page-2-0)). Weather data (including air temperature and rainfall) were obtained from an automatic meteorological station inside each experimental site. The cumulative degree days were calculated from sowing (time 0) as the sum of the daily air temperature minus base temperature of each species. Soil properties varied among sites: clay content from 10 to 27%, CaCO3 from 0 to 64% and maximum water holding capacity in the seedbed layer from 13 to 48 mm. Emergence date was determined as the date when epicotyls of at least 80% of the seeds sown were visible at the soil surface. Emergence date was recorded for 53 "situations" (i.e. combinations of site × year × management) for white mustard; 31 for vetch; 20 for bristle oat; 13 for Italian ryegrass; 5 for crimson clover, faba bean, foxtail millet and turnip rape; and 4 for forage pea and phacelia.

# 2.3. Simple static model to predict emergence duration

We used the General Linear Modeling (GLM) statistical procedure to develop a simple static model to predict duration of cover crop emergence. The database of experimental field data was divided into one calibration and one validation dataset ([Table 2](#page-2-1)), each with a similar combination of sites and sowing situations (e.g. dry or wet). We calibrated the model for all ten cover crop species combined to obtain a generic model that can be used for multiple species. In contrast, we validated the model only for the four species with the largest numbers of situations: white mustard, vetch, bristle oat and Italian ryegrass.

We performed the GLM procedure with the "Modern Applied Statistics with S" package in R software (version 2.14.0). Backward stepwise regression based on Akaike's Information Criterion (StepAIC) was used to select variables for the final model. Non-significant (P > 0.05) candidate variables were excluded. Candidate variables for the model included:

- 1) climate variables: water input (rain + irrigation), potential evapotranspiration and the difference between them within 7, 14, 21 and 30 days of sowing; number of consecutive days without significant water input after sowing; and cumulative degree days 14 and 30 days after sowing (°C);
- 2) soil properties: clay content (%), CaCO3 content (%), soil moisture in the seedbed layer (%) at sowing, available soil water in the seedbed layer (mm) at sowing, and wilting point and field capacity of the seedbed layer (%);
- 3) management practice: sowing depth (cm);
- 4) species characteristics: degree days required to emerge without stress (calculated with specific species base temperature), base temperature (°C) and base water potential (MPa) for emergence ([Tribouillois et al., 2016)](#page-8-10).

If not measured, soil moisture in the seedbed at sowing was predicted by STICS based on initial soil moisture measured in the field before sowing and the subsequent daily climate. STICS has been evaluated as accurate for predicting soil moisture in the seedbed ([Constantin et al., 2015a;](#page-8-9) [Coucheney et al., 2015)](#page-8-17). Degree days required to achieve emergence were calculated from the experimental data for each species, using a base temperature of 11 °C for foxtail millet, 1.5 °C for crimson clover and 0 °C for other species [(Tribouillois et al., 2016)](#page-8-10). The species values of this parameter were calculated mostly based on the field experiment of Auzeville 2012, excepted for phacelia, bristle oat, faba bean and white mustard for which the emergence durations

#### <span id="page-2-0"></span>Table 1

Experimental site characteristics in France, climate ( ± 1 standard deviation among years), and cover crop species assessed at each site.

| Site          | Latitude (longitude) (°N<br>(°E)) | No. of<br>years | Total rainfall + irrigation within 7 days of<br>sowing (mm) | Mean daily temperature for 15 days<br>after sowing (°C) |                                |
|---------------|-----------------------------------|-----------------|-------------------------------------------------------------|---------------------------------------------------------|--------------------------------|
| St-Hilaire    | 49.2 (4.5)                        | 1               | 01 ± 0                                                      | 20 ± 0                                                  | Cl/Fa/Mi/Oa/Pe/Ph/Ry/<br>Tu/Ve |
| Montpellier   | 43.6 (3.9)                        | 2               | 02 ± 1                                                      | 20 ± 1                                                  | Mu/Oa/Ve                       |
| Boult         | 49.4 (4.1)                        | 1               | 05 ± 0                                                      | 17 ± 0                                                  | Mu                             |
| Bignan        | 47.9 (−2.8)                       | 3               | 06 ± 2                                                      | 18 ± 1                                                  | Cl/Fa/Mi/Oa/Pe/Ry/Tu/          |
|               |                                   |                 |                                                             |                                                         | Ve                             |
| Estrées-Mons  | 49.9 (3.0)                        | 2               | 06 ± 7                                                      | 16 ± 2                                                  | Mu/Ve                          |
| La-Chapelle   | 47.4 (−1.0)                       | 2               | 11 ± 17                                                     | 19 ± 0                                                  | Mu/Ve                          |
| Vienne-en-Val | 47.8 (2.1)                        | 2               | 13 ± 3                                                      | 17 ± 1                                                  | Mu/Oa/Ve                       |
| Warmeriville  | 49.3 (4.2)                        | 2               | 14 ± 9                                                      | 17 ± 4                                                  | Mu/Ry/Ve                       |
| Chéry         | 49.7 (3.6)                        | 1               | 16 ± 0                                                      | 17 ± 0                                                  | Mu/Oa/Ve                       |
| Somme         | 49.1 (4.7)                        | 1               | 16 ± 0                                                      | 18 ± 0                                                  | Mu                             |
| Sermaise      | 48.5 (2.1)                        | 2               | 16 ± 15                                                     | 16 ± 2                                                  | Mu/Oa/Ve                       |
| Boigneville   | 48.3 (2.4)                        | 6               | 19 ± 16                                                     | 18 ± 1                                                  | Mu/Ry/Ve                       |
| Lyon          | 45.8 (4.8)                        | 1               | 20 ± 0                                                      | 25 ± 0                                                  | Ve                             |
| Orchies       | 50.5 (3.2)                        | 2               | 23 ± 19                                                     | 18 ± 2                                                  | Mu/Oa/Ve                       |
| Auzeville     | 43.5 (1.5)                        | 9               | 24 ± 20                                                     | 20 ± 2                                                  | Cl/Fa/Mi/Mu/Oa/Ph/Pe/          |
|               |                                   |                 |                                                             |                                                         | Ry/Tu/Ve                       |
| Lusignan      | 46.4 (0.1)                        | 4               | 27 ± 36                                                     | 16 ± 2                                                  | Mu/Oa/Ry/Ve                    |
| La Pouëze     | 47.6 (−0.8)                       | 2               | 44 ± 33                                                     | 18 ± 1                                                  | Mu/Oa/Ve                       |
| Colmar        | 48.1 (7.4)                        | 1               | 45 ± 0                                                      | 19 ± 0                                                  | Ry                             |

<span id="page-2-2"></span>* Cl is 'crimson clover', Fa is 'faba bean', Mi is 'foxtail millet', Mu is 'white mustard', Oa is 'bristle oat', Ph is 'phacelia', Pe is 'forage pea', Ry is 'Italian ryegrass', Tu is 'turnip rape' and Ve is 'vetch'.

2.4. Calibration and validation of STICS for cover crop emergence

STICS model simulates emergence duration by taking into account three main factors: temperature, water status of the soil in the seedbed and sowing depth. STICS predicts emergence as three successive processes: 1) seed imbibition, 2) germination and 3) shoot elongation. Temperature, soil moisture and species parameters (i.e. i) sensitivity to water as base water potential, ii) thermal stresses, and iii) shoot elongation) determine the emergence date. The first step is a passive process influenced by the species-specific water potential in the seedbed, which determines seed imbibition. Once seeds are moistened, rootlets emerge from seeds within a few days, as a function of temperature. Each species completes germination once it has accumulated a species-specific number of degree days after sowing. STICS model takes into account the variability of soil temperature according to sowing depth since the germination is function of soil temperature in the seedbed in the model, the seedbed depth being defined as sowing depth + 1 cm. Sensitivity of seed rootlets to soil dryness (drought and base temperature) also

were shorter in other experimental fields of the database (e.g. thermic stress for phacelia…) where we thus calculated the parameter value based on measurements. Base temperatures and water potentials were determined in the laboratory for all species ([Tribouillois et al., 2016](#page-8-10)). Minimum and base temperature represent both the same process (minimal temperature at which species can germinate) but not using the same equation, such as a classical linear equation for base temperature and a non-linear function for the minimum temperature of germination (see [Tribouillois et al., 2016](#page-8-10) for details). The method used for minimum temperature allows a more accurate estimation due to the fact the response of germination to the temperature increase is not linear. We thus chose to use minimum temperatures as base temperatures (instead of the base temperatures themselves). The temperature used to calculate degree days was air temperature, since we did not have measurements of the temperature in the seedbed for all experiments and that the air temperature was close to the seedbed temperature, as shown by [Dorsainvil et al. (2005)](#page-8-7) for cover crop sowing in summer conditions.

### <span id="page-2-1"></span>Table 2

Ranges of site, soil, and weather data for ten species in calibration and validation datasets.

|             | Characteristic                                                                                                                                                                                                              | White<br>mustard                                            | Vetch                                                       | Bristle oat                                                  | Italian ryegrass                                          | Crimson clover, Faba bean Phacelia Forage<br>pea, Foxtail millet, Turnip rape |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------|
| Calibration | Number of situations*<br>Sowing date<br>Initial soil moisture (%)<br>Soil moisture at sowing (%)<br>Rainfall + irrigation within 7 days of sowing<br>(mm)<br>Number of consecutive days without water<br>input after sowing | 14<br>3 Aug–21 Sept<br>7.4–20.3<br>4.6–24.2<br>0–47<br>0–20 | 13<br>1 Aug–23 Sept<br>7.2–22.4<br>1.3–21.9<br>0–58<br>1–32 | 8<br>10 Aug–16 Sept<br>11.2–30.0<br>5.8–24.2<br>1–41<br>1–33 | 8<br>6 Aug–2 Oct<br>10.8–25.9<br>8.9–22.4<br>0–28<br>0–33 | 5<br>10–22 Aug<br>11.2–30.0<br>8.9–24.2<br>1–41<br>1–33                       |
| Validation  | Number of situations*<br>Sowing date<br>Initial soil moisture (%)<br>Soil moisture at sowing (%)<br>Rainfall + irrigation within 7 days of sowing<br>(mm)<br>Number of consecutive days without water<br>input after sowing | 39<br>5 Aug–12 Sept<br>3.7–25.9<br>4.3–25.9<br>0–80<br>0–25 | 18<br>5 Aug–12 Sept<br>4.8–30.0<br>4.4–24.2<br>1–79<br>1–33 | 12<br>5 Aug–12 Sept<br>10.0–19.0<br>4.8–21.6<br>1–80<br>1–22 | 5<br>10–27 Aug<br>11.2–20.7<br>11.0–22.7<br>8–45<br>1–7   | N/A<br>N/A<br>N/A<br>N/A<br>N/A<br>N/A                                        |

<span id="page-2-3"></span>* The number of "situations" (site × year × management) corresponds to the number of simulations.

influences germination. Subsoil plantlet growth begins after germination, as shoots and roots begin to grow; elongation of the former is a logistic function of degree days that may slow down with unsuitable soil moisture. The emergence occurs when elongation is greater than sowing depth. [Brisson et al. (2008)](#page-8-18) describe all processes and equations of STICS. Since STICS does not consider certain biotic and abiotic processes that cause plant density to decrease (e.g. damping-off, low seed germination), sowing density was considered to equal the density of emerged plants measured in the experiments at Auzeville.

For calibrating cover crops in STICS, we first fixed the parameters values for water potential and germination base temperature taken from a previous laboratory study of multiple cover crop species ([Tribouillois et al., 2016](#page-8-10)). Likewise, degree days required for germination were calculated from that study's data. The temperature used to calculate degree days was air temperature as a proxy of seedbed temperature. Root sensitivity to drought and two shoot elongation parameters were mathematically calibrated using the method of [Guillaume](#page-8-19) [et al. (2011)](#page-8-19) as a simplex algorithm adapted to non-smooth functions in the OptimiSTICS tool ([Wallach et al., 2011](#page-8-20)).

STICS was calibrated using the same calibration dataset as that used to develop the static model, representing a wide range of conditions across France. Unlike the static model, STICS was calibrated for each species by considering species-specific parameters. STICS' predicted emergence dates were evaluated using the same validation dataset as that used to evaluate the static model ([Table 2](#page-2-1)). The model was initialized with soil moisture in the seedbed layer and just below (0–10 cm measured on experimental sites on the sowing date) and with the corresponding sowing depth practiced on experimental sites: mean sowing depth of 3 cm (range = 1–5 cm).

#### 2.5. Statistical criteria used for calibration and evaluation

Three statistical criteria – model efficiency (EF), root mean square error (RMSE) and mean deviation (MD) – were calculated to assess the quality of calibration and validation:

$$EF = 1 - \frac{\sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}^2}{\sum_{l=1}^{n} \text{ (
$$O_l - \overline{o}$$
)}^2} \tag{1}$$

$$RMSE = \sqrt{\frac{1}{n}} \sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}^2 \tag{2}$$

$$MD = \frac{1}{n} \sum_{l=1}^{n} \text{ (
$$P_l - O_l$$
)}\tag{3}$$

where n is the number of observations, Oi and Pi are observed and predicted values, respectively, and *o* is the mean of observed values. EF (ranges = −∞ to 1) represents model accuracy relative to the mean of observed data. As it approaches 1, the match between observed and predicted values increases; it becomes negative when the mean of observed values lies closer to observed values than predicted values do. RMSE provides absolute error, while MD provides model deviation from the line x=y. We also calculated the median difference in absolute values between the observed and the predicted values.

No tables found before Methods section.