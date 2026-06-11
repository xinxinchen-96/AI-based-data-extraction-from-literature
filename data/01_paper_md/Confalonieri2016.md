Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/03043800)

# Ecological Modelling

journal homepage: [www.elsevier.com/locate/ecolmodel](http://www.elsevier.com/locate/ecolmodel)

![](_page_0_Picture_4.jpeg)

## Quantifying uncertainty in crop model predictions due to the uncertainty in the observations used for calibration

### Roberto Confalonieri a,∗, Simone Bregaglio b, Marco Acutis b

a Università degli Studi di Milano, DEMM, Cassandra Lab, via Celoria 2, 20133 Milan, Italy

b Università degli Studi di Milano, DISAA, Cassandra Lab, via Celoria 2, 20133 Milan, Italy

#### a r t i c l e i n f o

Article history: Received 11 December 2015 Received in revised form 20 February 2016 Accepted 22 February 2016 Available online 9 March 2016

**2. Materials and methods**

#### 2.1. A methodology for quantifying the uncertainty in model predictions due to random errors in observations

Given a series of observations (e.g. state or rate variables measured in different moments), the methodology is based on the generation of a number of possible (virtual) series of observations from the means and standard deviations of the original data. The rationale for generating the series is that – given the meaning of averaging replicated measurements – each of the generated series couldhave beencollected because ofthe uncertainty (repeatability) ofthe method for determining the variable and ofthe heterogeneity among sampled entities. Under the assumption of normality of distributions, the virtual series of observations can be generated using the Latin hypercube sampling (LHS), a type of stratified Monte Carlo sampling technique [(McKay](#page-5-0) et [al.,](#page-5-0) [1979;](#page-5-0) [Iman](#page-5-0) et [al.,](#page-5-0) [1981).](#page-5-0) Given the efficient stratification properties of LHS, a sample size of 10n can be used [(Helton](#page-4-0) [and](#page-4-0) [Davis,](#page-4-0) [2003;](#page-4-0) [Jia](#page-4-0) et [al.,](#page-4-0) [2007),](#page-4-0) with n being the number of observations available in the dataset.

The availability of the generated series allows to perform the calibration by properly accounting for the uncertainty in measured data used for estimating the objective function. For each series of generated observations, indeed, model parameters can be automatically calibrated using an optimization algorithm. To test our methodology, we used a multi start point, bounded (for parameter ranges) version of the downhill simplex method [(Nelder](#page-5-0) [and](#page-5-0) [Mead,](#page-5-0) [1965).](#page-5-0) This optimization algorithm is based on a geometrical concept, named simplex, consisting of N + 1 vertices interconnected by line segments and polygon faces in an N-dimensional parameter hyperspace. The simplex moves through this space according to three basic rules: reflection, contraction, and expansion. Although a variety of optimization algorithms not using derivatives is available in the literature (e.g. [Kirkpatrick](#page-4-0) et [al.,](#page-4-0) [1983;](#page-4-0) [Glover,](#page-4-0) [1986;](#page-4-0) [Dorigo,](#page-4-0) [1992;](#page-4-0) [Matsumoto](#page-4-0) et [al.,](#page-4-0) [2002),](#page-4-0) we used the simplex because of its good performance with respect to the ease of implementation ([Press](#page-5-0) et [al.,](#page-5-0) [2007).](#page-5-0) However, the methodology proposed here can be applied with whatever optimization algorithm.

The distribution of model outputs obtained for the array of calibrations (one for each generated series) allows to analyse the propagation of uncertainty from observations to model predictions.

#### 2.2. An illustrative case study

Datasets used for this study refer to two field experiments carried out in northern Italy in Opera (45◦22 N, 9◦12 E) in 2004 and in Vignate (45◦29 N, 9◦22 E) in 2002; datasets are described in detail by [Confalonieri](#page-4-0) et [al.](#page-4-0) [(2009).](#page-4-0) Two Indica-type cultivars (Gladio in Opera and Sillaro in Vignate) were scatter seeded and grown under flooded conditions in a completely randomized block design with four and three replicates in Opera and Vignate, respectively. Experimental factors where nitrogen (N) fertilization and cultivar in Opera, N fertilization in Vignate. Experimental plots were 35 m2 (7 m × 5 m) in Opera and 30 m2 (10 m × 3 m) in Vignate. For both experiments, N amount was split in two events, i.e. beginning of

### <span id="page-2-0"></span>**Table 1**

Datasets used for the simulation experiments. Data refer to aboveground biomass (AGB, t ha−1).

| Dataset: Opera-2004  |        |       | Dataset: Vignate-2002       |        |       |
|----------------------|--------|-------|-----------------------------|--------|-------|
| Sowing: May 24, 2004 |        |       | Sowing date: April 29, 2002 |        |       |
| Sampling date        | Mean   | S.D.  | Sampling date               | Mean   | S.D.  |
| June 16              | 0.190  | 0.076 | May 31                      | 0.080  | 0.021 |
| June 21              | 0.305  | 0.080 | June 28                     | 3.145  | 0.248 |
| June 24              | 0.381  | 0.089 | July 27                     | 11.920 | 1.201 |
| June 26              | 0.649  | 0.122 | August 2                    | 14.320 | 1.980 |
| June 29              | 1.183  | 0.426 | August 24                   | 15.077 | 1.349 |
| July 8               | 2.829  | 0.732 | October 6                   | 16.716 | 1.247 |
| July 20              | 5.156  | 0.913 |                             |        |       |
| July 23              | 6.335  | 0.997 |                             |        |       |
| July 25              | 6.630  | 1.427 |                             |        |       |
| July 27              | 7.743  | 1.128 |                             |        |       |
| August 3             | 10.253 | 0.847 |                             |        |       |
| October 3            | 13.589 | 0.404 |                             |        |       |

tillering (code 21 of the BBCH scale for rice; [Lancashire](#page-4-0) et [al.,](#page-4-0) [1991)](#page-4-0) and panicle initiation (BBCH code 30) in Opera and pre-sowing and panicle initiation in Vignate. Differences in the N distribution protocol were due to the differences in the soil N content before sowing and to different cultivar requirements. For this study, simulations were carried out under unlimiting conditions for N; thus, data from the treatments that received the highest amount of N (160 kg N ha−1 in Opera, 150 kg N ha−1 in Vignate) were used for both experiments. Soils were loam in Opera and sandy-loam in Vignate. Management allowed keeping the fields disease-, pest- and weed-free.

For both experiments, data on sowing and sampling dates are shown in Table 1, as well as mean and standard deviation of measured aboveground biomass values (AGB, t ha−1).

Data shown in Table 1 were used to generate virtual series of 12 observations for Opera-2004 and of six observations for Vignate-2002. The generated series of observations were used to calibrated the parameters of the rice model WARM (e.g. [Confalonieri](#page-4-0) et [al.,](#page-4-0) [2009,](#page-4-0) [2010),](#page-4-0) used by the European Commission's Joint Research Centre for rice monitoring and yield forecasting. WARM simulates daily biomass accumulation using a net photosynthesis approach, with radiation use efficiency modulated by temperature, senescence, saturation of enzymatic chains, and atmospheric CO2 concentration. Partitioning to storage organs is reproduced by means of a set of beta and quadratic functions, driven by development stage and by the biomass partitioned to leaves at emergence. Green leaf area increase (LAI) is derived from leaf biomass and a dynamic specific leaf area, whereas senescence is simulated as a function of thermal time accumulated by each daily-emitted LAI unit. A micrometeorological module allows using temperature at the meristematic apex for phenological development and cold- and heat-induced spikelet sterility, whereas mid-canopy temperature is used for biomass accumulation and leaf blast infection. Model algorithms are fully described in the seminal literature and in the model documentation [(www.cassandralab.com/applications/2)](http://www.cassandralab.com/applications/2). In this study, the daily time step version of WARM was used. Since the two datasets were collected under unlimiting conditions for water and nutrients, and fields were properly kept weed-, pest- and disease free, simulations were carried out for potential conditions, with driving variables represented by maximum and minimum air daily temperature (◦C) and global solar radiation (MJ m−2 d−1).

Previous studies allowed identifying maximum radiation use efficiency (RUE, g MJ−1) and optimum mean daily temperature for growth (Topt, ◦C) as the parameters with the largest influence on AGB accumulation under the conditions explored in this study [(Confalonieri](#page-4-0) et [al.,](#page-4-0) [2010).](#page-4-0) The range of values allowed for RUE and Topt during calibrations were 2.6–3.2 g MJ−1 and 26–30 ◦C, respectively [(Confalonieri](#page-4-0) et [al.,](#page-4-0) [2010),](#page-4-0) whereas the starting guess to initialize the simplex was 2.9 g MJ−1 and 28 ◦C for RUE and Topt [(Confalonieri](#page-4-0) et [al.,](#page-4-0) [2009).](#page-4-0) The other parameters were set to the model default for European Indica-type cultivars ([Confalonieri](#page-4-0) et [al.,](#page-4-0) [2009).](#page-4-0) The choice of limiting to a minimum the number of calibrated parameters is coherent with what is often suggested in modelling studies (e.g. [Refsgaard,](#page-5-0) [1997;](#page-5-0) [Wallach](#page-5-0) et [al.,](#page-5-0) [2001).](#page-5-0) However, there are no theoretical reasons that prevent applying the proposed procedure to complex systems where several parameters needs to be simultaneously calibrated. The objective function that was minimized was the relative root mean square error (RRMSE, %, from 0 (optimum) to +∞) between measured and observed AGB values.

###

No tables found before Methods section.