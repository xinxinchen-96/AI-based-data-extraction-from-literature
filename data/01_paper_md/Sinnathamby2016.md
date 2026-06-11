![](_page_0_Picture_1.jpeg)

Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/03783774)

# Agricultural Water Management

![](_page_0_Picture_4.jpeg)

jour nal home page: [www.elsevier.com/locate/agwat](http://www.elsevier.com/locate/agwat)

# Field-scale calibration of crop-yield parameters in the Soil and Water Assessment Tool (SWAT)

![](_page_0_Picture_7.jpeg)

# Sumathy Sinnathambya, Kyle R. Douglas-Mankina,∗, Collin Craige b

a Biological and Agricultural Engineering, Kansas State University, 147 Seaton Hall, Manhattan, KS 66506-2906, United States b Biosystems and Agricultural Engineering, Oklahoma State University, 111 Agricultural Hall, Stillwater, OK 74078-6016, United States

# a r t i c l e i n f o

Article history: Received 4 May 2016 Received in revised form 26 September 2016 Accepted 30 October 2016 Available online 5 November 2016

**2. Materials and methods**

# 2.1. Model description

The Soil and Water Assessment Tool (SWAT) ver. 2005 is a physically based, watershed scale, continuous simulation model developed by the USDA Agricultural Research Service (ARS)[(Arnold](#page-7-0) et [al.,](#page-7-0) [1998;](#page-7-0) [Neitsch](#page-7-0) et [al.,](#page-7-0) [2004,](#page-7-0) [2005)](#page-7-0) and extensively used throughoutthe world [(Gassman](#page-8-0) et [al.,](#page-8-0) [2007;](#page-8-0) [Douglas-Mankin](#page-8-0) et [al.,](#page-8-0) [2010a;](#page-8-0) [Tuppad](#page-8-0) et [al.,](#page-8-0) [2011;](#page-8-0) [Arnold](#page-8-0) et [al.,](#page-8-0) [2012).](#page-8-0) It is capable of simulating crop growth, soil water, surface water, and groundwater movement as well as sediment and nutrienttransportfor both large and small scales [(Luo](#page-8-0) et [al.,](#page-8-0) [2008).](#page-8-0) The model is often used to examine the effects of agricultural practices on water quality because of its ability to represent numerous management practices, including fertilizer, tillage, crop rotations, irrigation, and drainage ([Arabi](#page-7-0) et [al.,](#page-7-0) [2008;](#page-7-0) [Gassman](#page-7-0) et [al.,](#page-7-0) [2007;](#page-7-0) [Douglas-Mankin](#page-7-0) et [al.,](#page-7-0) [2010a).](#page-7-0) SWAT has been used in many locations within Kansas, ranging from field scale [(Anand](#page-7-0) et [al.,](#page-7-0) [2007;](#page-7-0) [Maski](#page-7-0) et [al.,](#page-7-0) [2008;](#page-7-0) [Douglas-](#page-7-0)Mankin et [al.,](#page-7-0) [2010b)](#page-7-0) to watershed scale ([Parajuli](#page-8-0) et [al.,](#page-8-0) [2009a,b,c;](#page-8-0) [Tuppad](#page-8-0) et [al.,](#page-8-0) [2010a,b;](#page-8-0) [Daggupati](#page-8-0) et [al.,](#page-8-0) [2011;](#page-8-0) [Nejadhashemi](#page-8-0) et [al.,](#page-8-0) [2011;](#page-8-0) [Sheshukov](#page-8-0) et [al.,](#page-8-0) [2011a,b,c;](#page-8-0) [Lee](#page-8-0) [and](#page-8-0) [Douglas-Mankin,](#page-8-0) [2011;](#page-8-0) [Gali](#page-8-0) et [al.,](#page-8-0) [2012;](#page-8-0) [Douglas-Mankin](#page-8-0) et [al.,](#page-8-0) [2013),](#page-8-0) and in many other study regions ([Gassman](#page-8-0) et [al.,](#page-8-0) [2007;](#page-8-0) [Douglas-Mankin](#page-8-0) et [al.,](#page-8-0) [2010a;](#page-8-0) [Tuppad](#page-8-0) et [al.,](#page-8-0) [2011).](#page-8-0) The incorporation of a large number of agricultural practices and structures, enhances its ability to model crop yields [(Douglas-Mankin](#page-7-0) et [al.,](#page-7-0) [2010a).](#page-7-0)

Plant growth in SWAT is simulated using a simplified version of the generic crop growth model from EPIC ([Williams](#page-8-0) et [al.,](#page-8-0) [1984](#page-8-0) [Williams,](#page-8-0) [1995),](#page-8-0) as described in [Neitsch](#page-8-0) et [al.](#page-8-0) [(2005).](#page-8-0) Total plant biomass is incremented daily based on an atmospheric-CO2-dependent radiation use efficiency applied to intercepted photosynthetically active radiation. This potential biomass accumulation is attenuated by the maximum among several possible limiting plant stresses (water, temperature, N, or P) [(Luo](#page-8-0) et [al.,](#page-8-0) [2008).](#page-8-0) Leaf area index (LAI), green leaf area per unitland area, is also incremented daily on the basis of accumulated potential heat units (PHUs), and is also attenuated by a plant-stress factor. LAI increases until a crop-specific maximum LAI is achieved, then remains constant until onset of senscence, after which it declines linearly to zero at harvest. Similarly, canopy height increases until a cropspecific maximum is reached, but it remains at this height through the remainder of the growing season. Root biomass is incremented daily as a fraction of total plant biomass ranging from 0.4 at emergence to 0.2 at maturity according to accumulated PHUs (users may also input root fractions in crop.dat). Root depth for annual crops is incremented daily accoring to accumulated PHUs until maximum root depth for that crop is achieved. Harvested crop yield is simulated as a fraction, defined by a harvest index, of either total or above-ground biomass at the time of harvest, to account for harvested grain (only) or plant biomass, depending on the crop.

## 2.2. Study areas

This study used field-level crop yield and management data from two research field sites [(Fig.](#page-2-0) 1) to calibrate and validate the SWAT model and crop sub-model parameters.

# 2.2.1. Site RK

Site RK (Riley County, Kansas) used crop grain yield data for corn (Zea mays) and grain sorghum (Sorghum bicolor) from 1999 to 2008 and sweet sorghum (Sorghum bicolor (L.) Moench) from 2007 to 2010 [(KSU-AES-CES,](#page-8-0) [1999–2008a,b;](#page-8-0) [Propheter,](#page-8-0) [2009;](#page-8-0) Dr. Scott Staggenborg, 2011, personal communication) from Northeastern Kansas field plots with silt loam soils for calibration. The three fields vary from 1.7 to 3.1 ha (4.1 to 7.8 ac). Corn was alternated annually with soybeans on fields with 3.0% average slope and soil KS-1614050-1 (Ivan and Kennebec silt loams, hydrologic soil group B) on odd years and, during even years, on 1.3% average slope and soil KS-1617170-1 (Reading silt loam, hydrologic soil group B). Grain sorghum was grown on the same fields with corn, so the same soil types were used. A similar rotation method was implemented, alternating with soybeans every year, with grain sorghum on KS-1614050-1 in odd years and KS-1617170-1 in even

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

**Fig. 1.** (a) Locations of two study areas: Cedar Creek Watershed, Riley County, KS (Site RK) and Lower Golf Creek Watershed, Texas County, OK (Site TO). Areal image maps with studied fields (b) Sites RK within North Agronomy Fields and (c) Site TO.

**Table 1** Site RK (Riley County, KS) plant (PLNT) and harvest (HVST) dates and nitrogren and phosphorus fertilizer (FERT) application amounts (kg/ha) for corn, grain sorghum, and sweet sorghum.

| Corn    |         |          |         | Grain Sorghum |          |         | Sweet Sorghum |          |  |
|---------|---------|----------|---------|---------------|----------|---------|---------------|----------|--|
| PLNT    | HVST    | FERT     | PLNT    | HVST          | FERT     | PLNT    | HVST          | FERT     |  |
| 5/3/99  | 9/17/99 | 168N-00P | 5/26/99 | 10/6/99       | 168N-00P | 5/21/07 | 10/25/07      | 168N-67P |  |
| 4/21/00 | 9/6/00  | 146N-00P | 5/10/00 | 9/15/00       | 146N-34P | 5/21/08 | 10/3/08       | 179N-0P  |  |
| 4/17/01 | 9/11/01 | 146N-00P | 5/14/01 | 9/28/01       | 146N-34P | 5/29/09 | 10/5/09       | 179N-0P  |  |
| 4/12/02 | 9/9/02  | 134N-00P | 5/21/02 | 9/30/02       | 151N-56P | 5/24/10 | 10/1/10       | 179N-0P  |  |
| 4/14/03 | 9/8/03  | 134N-00P | 5/13/03 | 9/24/03       | 151N-67P |         |               |          |  |
| 4/14/04 | 9/16/04 | 146N-00P | 5/24/04 | 10/16/04      | 146N-34P |         |               |          |  |
| 4/16/05 | 9/19/05 | 146N-30P | 5/24/05 | 9/27/05       | 146N-34P |         |               |          |  |
| 4/13/06 | 9/15/06 | 146N-30P | 5/18/06 | 9/28/06       | 146N-34P |         |               |          |  |
| 4/23/07 | 9/17/07 | 134N-00P | 5/11/07 | 9/29/07       | 146N-34P |         |               |          |  |
| 4/23/08 | 10/1/08 | 101N-00P | 5/16/08 | 9/25/08       | 146N-34P |         |               |          |  |

years. Sweet sorghum was grown also using a rotation with soybeans on areas with the same soil type as corn and grain sorghum. Management practices were obtained for each crop, including fertilization, planting, harvest (Table 1), and tillage dates and practices. Field cultivator tillage was applied for corn 3 months before planting, 22 days after planting, and 1 month prior to next year soybean rotation. For grain and sweet sorghum, generic no-till mixing characteristics (25 mm mixing depth, 5% mixing efficiency) were applied in SWAT. Herbicides were used on crops but were not included in management practices, because pest or pesticide impacts were not modeled. No irrigation was used during the study period. Time-based management operations were used instead of the default method, which used the fraction of PHU.

The research fields were within the 4,800-ha Cedar Creek–Big BlueWatershed(HUC102702050705),RileyCounty,Kansas (Fig. 1). Land-use distribution in this watershed was 32% hay/pasture, 23% residential area, 16% deciduous forest, 11% soybeans and 8% corn [(USGS,](#page-8-0) [1992).](#page-8-0) Soil was predominantly hydrologic group C followed by group B [(USDA,](#page-8-0) [2011).](#page-8-0) The watershed was delineated into 31 subwatersheds with SWAT 2005 using a 10-m resolution digital elevation model (DEM) from National Elevation Dataset [(USGS,](#page-8-0) [2010).](#page-8-0) Land-use data were derived from the 2010 National Agricultural Statistics Service (NASS) Cropland Data Layer at 30-m resolution [(Mueller](#page-8-0) [and](#page-8-0) [Seffrin,](#page-8-0) [2006)](#page-8-0) and soil data derived from Soil Survey Geographic Database (SSURGO) data [(USDA,](#page-8-0) [2011)](#page-8-0) processed for input to SWAT using a utility developed by [Sheshukov](#page-8-0) et [al.](#page-8-0) [(2011b).](#page-8-0) Slope classes were calculated using the DEM. A total of 3,126 HRUs, each representing specific combinations of soil, slope, and land-use, were generated from these data. The 2 HRUs with soil, slope, and land-use characteristics corresponding to the research fields was used for this analysis.

Weather data, including precipitation, temperature, wind speed, humidity and solar radiation, were obtained from the National Climatic Data Center [(NCDC,](#page-8-0) [2011)](#page-8-0) and collected at a station approximately 1.9 km south ofthe study fields for 1989 to 2008 (Fig. 1b). Potential evapotranspiration (PET) was calculated using the Hargreaves method [(Hargreaves](#page-8-0) [and](#page-8-0) [Samani,](#page-8-0) [1985).](#page-8-0) Daily curve number calculation method used plant evapotranspiration rather than available moisture capacity to adjust antecedent soil moisture condition. These changes to basin-level initial setup were based on a previous study in north-east Kansas ([Sheshukov](#page-8-0) et [al.,](#page-8-0) [2013).](#page-8-0)

#### 2.2.2. Site TO

Site TO (Texas County, Oklahoma) used crop yield data for corn and grain sorghum([OCES,](#page-8-0) [2006,](#page-8-0) [2007,](#page-8-0) [2008,](#page-8-0) [2009,](#page-8-0) [2010)f](#page-8-0)romOklahoma State University grain sorghum and corn performance trials at the Joe Webb Farm and the Oklahoma Panhandle Research and Extension Center (OPREC) field plots to validate corn and grain sorghum calibration results from Site RK. The three fields range from 18 to 63 ha (44.5 to 155.7 ac). Corn and grain sorghum were each grown continuously on fields with 0.9% average slope and OK139Rc-5 soil (Richfield clay loam soil, hydrologic soil group D). The corn plots were irrigated in April (with 76.2 mm), May (76.2 mm),June (152.4 mm),July (152.4 mm) andAugust(50.8 mm) and well fertilized, whereas the grain sorghum plots were not irrigated and had only a small amount of fertilizer applied (Table 2). Management operations used in Lower Golf Creek watershed are given in Table 2. Strip-tillage was carried out before every planting. These fields were within the 12,767.1-ha Lower Golf Creek Watershed [(Fig.](#page-2-0) 1). Watershed land cover was comprised of 51% rangeland/openarea, 23% wheat, 8%general agriculture, 6%corn, 5% grain sorghum, and 5% residential areas, with the remainder comprised of miscellaneous crops [(USGS,](#page-8-0) [1992).](#page-8-0) Hydrologic soil groups D and B were the dominant soil types, with a Richfield clay loam (group D) covering 46.7% of the watershed [(USDA,](#page-8-0) [2011).](#page-8-0) Similar data were used as in Site RK, including 30-m DEM, NASS land-use, and SSURGO soils data. Two HRUs were selected for analysis, one each for corn and grain sorghum. These HRUs had substantially different characteristics (different hydrologic soil group and slope) from those selected for corn and grain sorghum calibration at Site RK.

Weather data were obtained from the Oklahoma Mesonet for 1999–2010 ([http://www.mesonet.org)](http://www.mesonet.org) and included precipitation, maximum and minimum temperature, relative humidity, solar radiation and wind speed. The weather station was located within the watershed approximately 4 km southwest of the study sites. The Hargreaves method (for PET) and the plant evapotranspiration option (for curve number) were selected.

#### 2.3. Calibration and validation

Four plant parameters and five soil/hydrologic parameters were adjusted for HRUs that contained the study field sites to calibrate the crop yields for corn, grain sorghum, and sweet sorghum. These were based on the authors' experience with application of SWAT and its crop submodel and consistent with sensitivity analysis of SWAT by [Nair](#page-8-0) et [al.](#page-8-0) [(2011)](#page-8-0) and [Trybula](#page-8-0) et [al.](#page-8-0) [(2015),](#page-8-0) and values used in calibration in other published studies [(Baumgart,](#page-7-0) [2005;](#page-7-0) [Hu](#page-7-0) et [al.,](#page-7-0) [2007;](#page-7-0) [Neitsch](#page-7-0) et [al.,](#page-7-0) [2005;](#page-7-0) [Ng](#page-7-0) et [al.,](#page-7-0) [2010).](#page-7-0) [Trybula](#page-8-0) et [al.](#page-8-0) [(2015)](#page-8-0) found radiation use efficiency (BIO E), base temperature

#### **Table 2**

Site TO (Texas County, OK) plant (PLNT) and harvest (HVST) dates, and nitrogen and phosphorus fertilizer (FERT) application amounts (kg/ha) for corn and grain sorghum.

| Corn    |         |          | Grain Sorghum |          |        |
|---------|---------|----------|---------------|----------|--------|
| PLNT    | HVST    | FERT     | PLNT          | HVST     | FERT   |
| 4/12/06 | 9/20/06 | 258N-56P | 6/7/06        | 11/17/06 | 56N-6P |
| 4/24/07 | 9/7/07  | 258N-56P | 5/31/07       | 9/20/07  | 56N-6P |
| 4/15/08 | 10/1/07 | 258N-56P | 6/24/08       | 11/6/08  | 56N-6P |
| 4/22/09 | 9/24/09 | 258N-56P | 6/23/09       | 11/3/09  | 56N-6P |
| 4/14/10 | 9/21/10 | 258N-56P | 6/2/10        | 10/29/10 | 56N-6P |

(T BASE), optimum temperature (T OPT), the point in the growing season when LAI declines (DLAI), and the N fraction of harvested biomass (CNYLD) to be the most sensitive SWAT crop submodel parameters for simulations biomass yield, and base temperature (T BASE) and maximum potential leaf area index (BLAI) for simulation of water yield. [Nair](#page-8-0) et [al.](#page-8-0) [(2011)](#page-8-0) determined the most sensitive parameters for crop submodel calibration were BIO E, harvest index for optimal growing condition (HVSTI, fraction of above-ground biomass removed during harvest), BLAI, and the fraction of N in plant at emergence (BN1), half maturity (BN2), and maturity (BN3). Thus, the plant parameters modified in this study included HVSTI, lower harvest index (WYSF, HVSTI under highly water stressed conditions), BIO E, and BLAI. Other sensitive parameters (T BASE, BN1, BN2, BN3, BP1, BP2, BP3) were modified from grain sorghum parameters a priori following [Perkins](#page-8-0) et [al.](#page-8-0) [(2011),](#page-8-0) [Propheter](#page-8-0) [(2009),](#page-8-0) and [BAE](#page-7-0) [(2006).](#page-7-0) The remaining crop parameters were applied directly from those used for grain sorghum in SWAT.

The soil/hydrologic parameters included soil evaporation compensation factor (ESCO), plant uptake compensation factor (EPCO), soil available water capacity (SOL AWC), biological mixing efficiency (BIOMIX), and the nitrate percolation coefficient (NPERCO). These parameters were adjusted to improve the yield results based on SWAT water stress and nutrient stress calculations. The ranges of values for ESCO and EPCO were chosen based on unpublished flow calibration done by the authors for Irish Creek, Black Vermillion watershed, which is located approximately 45 km northeast of the study watershed. Ranges for the other parameters were set based on extensive experience by the authors in calibrating SWAT for other watersheds in the study region and were fixed for both study Sites RK and TO.

Corn and grain sorghum annual grain yields were calibrated at Site RK using model results from 1999 to 2008 with a 2-year (1997–1998) model warm-up period. The model was calibrated for each crop individually using four plant parameters (BIO E, HVSTI,WYSF, andBLAI)followedby soil andhydrologicparameters. Resulting annual yield simulations were compared to the observed annual grain yields from individual study plots using Nash-Sutcliffe efficiency (NSE)[(NashandSutcliffe,](#page-8-0) [1970),](#page-8-0)percent bias (PBIAS), and RMSE-observations standard deviation ratio (RSR) [(Moriasi](#page-8-0) et [al.,](#page-8-0) [2007,](#page-8-0) [2015).](#page-8-0) Final calibration values represent the best possible NSE and PBIAS.

Sweet sorghum yield was calibrated at Site RK using model results from 2007 to 2010 with a 3-year (2004–2006) model warmup period. Growth parameters were set based upon work done by [Perkins](#page-8-0) et [al.](#page-8-0) [(2011),](#page-8-0) [Propheter](#page-8-0) [(2009)](#page-8-0) and Oklahoma State University [(BAE,](#page-7-0) [2006)](#page-7-0) for most parameters ([Table](#page-4-0) 3). As with corn and grain sorghum, four plant parameters were used for sweet sorghum yield calibration. These parameters were tested over ranges consistent with prior sweet sorghum literature [(Perkins](#page-8-0) et [al.,](#page-8-0) [2011:](#page-8-0) BIO E = 55, HVSTI = 0.98, and WYSF = 0.98; [BAE,](#page-7-0) [2006:](#page-7-0) BIO E = 39, HVSTI = 0.90, WYSF = 0.90, and BLAI = 6). Both harvest indexes (WYSF, HVSTI) were tested over the upper end of index range (0.90 to 1.00) to represent hand-harvesting methods used to collect these above-ground biomass yield data [(Perkins,](#page-8-0) [2012).](#page-8-0) The BIO E value was tested from 39 to 59, and BLAI was tested from 5 to 6. Each parameter was changed individually, and resulting biomass yield simulations were compared to the actual annual biomass yields from individual study plots, as described for corn and grain sorghum.

Corn and grain sorghum yields were validated at Site TO using model results from 2006 to 2010 with a 2-year (2004–2005) model warm-up period. Parameters from the Site RK calibrated model were used except where Site TO site-specific data existed (such as precipitation, temperature and management practices given in Table 2). Crop growth parameters were unadjusted.

#### <span id="page-4-0"></span>**Table 3**

Sweet sorghum calibrated SWAT crop parameter values.

| Name      | Parameter Description                                                                 | Grain Sorghum | Sweet Sorghum |
|-----------|---------------------------------------------------------------------------------------|---------------|---------------|
|           | Values calibrated for Sweet Sorghum (Tested over given range)                         |               |               |
| BIO E     | Radiation use efficiency (10−1 g/MJ) (Range: 39–50)                                   | 33.5          | 50            |
| BLAI      | Max. leaf area index (Range: 5–6)                                                     | 3 (5)a        | 6             |
| HVSTI     | Harvest index (Range: 0.90–1.00)                                                      | 0.45 (0.46)a  | 1.0b          |
| WSYF      | Lower limit of harvest index (Range: 0.90–1.00)                                       | 0.25 (0.35)a  | 1.0b          |
|           | Values modified from Grain Sorghum (Perkins et al., 2011; Propheter, 2009; BAE, 2006) |               |               |
| T BASE    | Base temperature needed for plant growth                                              | 11            | 10            |
| BN1       | Fraction of N in plant at emergence                                                   | 0.044         | 0.018         |
| BN2       | Fraction of N in plant at ½ maturity                                                  | 0.0164        | 0.0093        |
| BN3       | Fraction of N in plant at maturity                                                    | 0.0128        | 0.0051        |
| BP1       | Fraction of P in plant at emergence                                                   | 0.006         | 0.002         |
| BP2       | Fraction of P in plant at ½ maturity                                                  | 0.0022        | 0.001         |
| BP3       | Fraction of P in plant at maturity                                                    | 0.0018        | 0.0003        |
|           | Values adopted from Grain Sorghum without adjustment                                  |               |               |
| RDMX      | Max. root depth                                                                       | 2             | 2             |
| FRGRW1    | Fraction of growing season at 1st point on optimal leaf area development curve        | 0.15          | 0.15          |
| LAIMX1    | Fraction of BLAI at 1st point on optimal leaf area development curve                  | 0.05          | 0.05          |
| FRGRW2    | Fraction of growing season at 2nd point on optimal leaf area development curve        | 0.5           | 0.5           |
| LAIMX2    | Fraction of BLAI at 2nd point on optimal leaf area development curve                  | 0.95          | 0.95          |
| WAVP      | Decline in RUE per unit increase in vapor pressure deficit (VPD)                      | 8.5           | 8.5           |
| DLAI      | Fraction of growing season when leaf area starts declining                            | 0.64          | 0.64          |
| T OPT     | Optimal temperature for plant growth                                                  | 30            | 30            |
| BIOEHI    | Radiation use efficiency at elevated CO2                                              | 36            | 36            |
| USLE C    | Min. value of USLE C factor applicable to land cover                                  | 0.2           | 0.2           |
| GSI       | Max. stomatal conductance in drought conditions                                       | 0.005         | 0.005         |
| VPDFR     | VPD at FRGMAX                                                                         | 4             | 4             |
| FRGMAX    | Fraction of max. stomatal conductance achievable at high VPD                          | 0.75          | 0.75          |
| CNYLD     | Fraction of N in harvested biomass                                                    | 0.0199        | 0.0199        |
| CPYLD     | Fraction of P in harvested biomass                                                    | 0.0032        | 0.0032        |
| CO2HI     | Elevated CO2 atmospheric concentration                                                | 660           | 660           |
| CHTMX     | Maximum canopy height                                                                 | 3.5           | 3.5           |
| RSDCO PL  | Plant residue decomposition coefficient                                               | 0.05          | 0.05          |
| BM DIEOFF | Biomass die-off fraction                                                              | 0.1           | 0.1           |

a Calibrated values (from this study, below) in parentheses.

b Harvest index of 1.0 (i.e., harvested 100% of above-ground biomass) was artifact of plot-scale research study conditions.

###

No tables found before Methods section.