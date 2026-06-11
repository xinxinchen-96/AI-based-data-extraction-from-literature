# **The distribution of water and nitrogen in the soil-crop system: a simulation study with validation from a winter wheat field trial**

# **R.F.** Grant

*Department of Soil Science, University of Alberta, Edmonton, Alberta, Canada T6G 2E3* 

- *

Methods**

### *Simulation technique*

*Dynamics of soil C and N.* The dynamics of water and nitrogen uptake are simulated as part of a larger submodel for the movements and

transformations of carbon, nitrogen, and phosphorus in organic and inorganic phases in the soil and crop (Fig. 1). These dynamics are based on explicit finite different approximations to partial differential equations describing movement and transformations of C, N, P, O, water and heat through a horizontally layered soil profile on a fixed time step of 1 h. Subsequent discussion of the model will be limited to C and N.

In the soil organic phase, C and N undergo first order decomposition and mineralization from each of four subcomponents of crop residue [5], and three components of manure [11] into soluble C and NH 4 pools. These pools are the substrates for the formation of two pools of microbial biomass of differing activity, through either aerobic [29] or anaerobic [27] processes based on Michaelis-Menten kinetics. Microbial activity is fully coupled to the movement of O in gaseous and soluble forms through the soil profile. The microbial pools undergo first order decomposition [23], releasing some C into the soluble C pool for recycling to the microbial biomass [30] and some into humads, with associated mineralization and fixation of NH 4. Similarly, humads undergo first order hydrolysis [34], with partial solubilization and partial reformation of C and N as humus, again with associated mineralization and fixation of NH 4. Humus also undergoes first order hydrolysis and mineralization.

In the soil inorganic phase, soluble NH 4 may be adsorbed into exchangeable NH 4 [38], volatilized into gaseous NH 3 [8] and nitrified [28] into soluble NO3. When oxygen is deficient at the microbial microsites, soluble NO 3 is used as an alternative electron acceptor for microbial respiration, causing denitrification for which soluble C is the substrate.

Both soluble NH~- and soluble NO~ are fully coupled to submodels for water movement through the soil profile. The vertical movement of each N species i between adjacent layers *(Fv,N, i* in g m -2 h -1) is calculated as the sum of convective and diffusive fluxes:

$$F_{V,N,i} = F_{V,W}C_{N,i} + D_e \,\partial C_{N\varepsilon,i} / \partial z \tag{1}$$

where *Fv, W* = vertical water flux (m 3 m -2 h-l), *Cus,i* = concentration of N in soil water (g m 3), *D e* = effective dispersion-diffusion coefficient of

![](_page_2_Figure_0.jpeg)

*Fig. 1.* Flow diagram for nitrogen cycle in the agroecosystem simulation model, showing processes for nitrogen movement and uptake in the soil profile.

N ion (m 2 h-t), and z = soil depth (m). The flux *Fv, w* is calculated from vertical gradients of soil water potential (4',) and hydraulic conductivity between adjacent soil layers as described elsewhere [17]. The diffusive flux *D e OQv,,jOz* is calculated from vertical gradients of concen-

N flow ~-

tration and effective diffusivity between adjacent layers.

*Uptake of mineral N.* The distribution of root DM growth through a horizontally layered soil profile is calculated recursively from current uptake rates of water and N per unit root surface area in each layer. From this distribution, root length and surface area are calculated from an assumed root radius of 0.15.10-3m, a DM content of 0.075 g g-l, and an internal porosity of 0.10 m 3 m -3 [32]. The radial movement of N to crop roots within each horizontal soil layer *(FR,N, i* in g m -2 h -1) is calculated as the sum of convective and diffusive radial fluxes:

$$F_{R,N,l} = F_{R,W} \mathcal{C}_{Ns,l} + D_e \left\| \mathcal{C}_{Ns,l} / \partial r \right\| \tag{2}$$

where *FR, w* =transpiration flux (m 3 m -2 h-~), calculated from radial gradients of hydraulic potential and conductivity between the soil and cylindrical roots in each soil layer. This calculation involves an iterative convergence solution for the canopy water potential (Oc) at which *X FR, w* for all soil layers equals the canopy transpiration rate *(Fc,w).* The transpiration rate is calculated from hourly meteorological data and from canopy stomatal resistance (r~), itself an indirect function of ~. Within the convergence solution, a value for the root water potential (qJr) of each soil layer is calculated such that FR,v¢ from the soil to the roots, as controlled by the soil-root potential gradient ~,- *Or,* is equal to that from the roots to the canopy, as controlled by the root-canopy potential gradient Or-O~, for each layer. The equations used in the convergence solution are given elsewhere [15].

The diffusive flux *D~ OCNs,i/Or* in Eq. 2 is calculated from radial gradients of concentration and effective diffusivity between the soil and cylindrical roots:

$$\begin{aligned} \,^jD_\epsilon \, \left\| \,^jC_{Ns,i} / \right\| &= \\ &= \left\{ 2\pi D_\epsilon (C_{Ns,i} - C_{Nr,i}) / \ln(r_2/r_1) \right\} \, L_r \end{aligned} \tag{3}$$

where *CN~* = N concentration in the rhizosphere (g m-3), r 2 = mean half-distance between root axes (m) as calculated from root length density *(L d* in m m-3), with a maximum value equal to the mean distance for ion diffusion during each time step as calculated from *De,* and where r 1 = root radius and *L r* = root length per layer (ram 2).

Active uptake of N by crop roots *(UN, ~* in g m -2 h -1) is calculated according to Barber [3]:

$$U_{N,i} = \{U_{N,i \text{ min}} (C_{Nr,i} - C_{Nr,i \text{ min}})\} / $$

$$\{C_{KNr,i} + (C_{Nr,i} - C_{Nr,i \text{ min}})\} \tag{4}$$

where U~,i max = maximum uptake rate at saturating *CNr,i* (gm -2 h -1) calculated as the product of an experimental rate constant (gm --2 root area h -1) and the root surface area *(2vrrlL r*  in m z root area m -2 ground area), *CNr,i* min = minimum *CNr,i* for N uptake (g m -z) and *CKNr,i = (CNr,i -- CNr,i* min) at which *UN, i =*  1/2 *UN, i* max (g m-3) • An Arrhenius equation is used to describe the sensitivity of *UN, ~ max* to temperature [26]. Parameters for Eq. 4 were taken from the experimental data of Barber [3] for both NH2 and NO2.

In order to calculate N uptake, *FR,N, ~* from Eq. 2 is equilibrated with *UN, i* from Eq. 4 by iteratively solving for CNr,~ with a convergence criterion of 0.001. The movement and uptake of soluble P and O are calculated in the same way as those of NH~ and NO 3.

*Storage and assimilation of crop* N. N taken up as either NH 4 or NO~- is stored in an inorganic pool *(Np* in g m -2) from which N is withdrawn according to crop growth requirements calculated from the nitrogen : dry matter ratios *(RN, I)Mo* in g g-l) and the DM growth rates *(dDMo/dt* in g m -2 h 1) of each organ (o):

$$\mathbf{d}N_p/\mathbf{d}t = \sum_i U_{N,i} - \sum_o \left\{ \left( \mathbf{d} DM_o/\mathbf{d}t \right) R_{N, DMo} \right\} \tag{5}$$

If the nitrogen concentration in an inorganic pool *(CN, p* in g(N) g(DM)-I), calculated as *Np/*  {leaf DM + sheath DM + stalk structural DM + root DM}, exceeds a threshold value (set at 0.01 for crop plants), *UN, i* max in Eq. 4 is reduced [37].

The term *dDMo/dt* is calculated from the soluble carbohydrate pool of the crop (Cp in g m -2, stored in the leaves as the primary product of photosynthesis), calculated from leaf and canopy level algorithms [13, 16], and from the maintenance respiration rate *(R m* in g m -2 h-a), the dry matter:carbohydrate (CH20) ratio of organ synthesis *(RDM,CH~Oo* in g g-a) and phenology-dependent partitioning coefficients *(Po)* [14]:

$$\text{d}\,\text{D}\,\text{M}_o/\text{d}\,t = \left(d\text{C}_p/\text{d}t - \text{R}_m\right)P_o\,\text{R}_{DM,\text{CH}_2\text{O}o} \quad (6)$$

If *Np* is less than 2 *{(dDMo/dt ) RN,DMo}* from Eq. 5 (i.e. the N reserves present during a given hour are inadequate to meet N demands during the hour), then *dDMo/dt* is reduced to that enabled by *Np,* such that all Np is withdrawn during the hour:

$$\text{d}D\!M_o/\text{d}t = P_o N_p / \left\{ t \sum_o \left( P_o R_{N,DMo} \right) \right\} \tag{7}$$

where t = time step (1 h).

*Remobilization of crop N.* During the pre- and post-anthesis period, reserves of soluble CH20 and N are accumulated in the stalk for subsequent translocation to the grain, as determined by the balance between crop uptake and grain demand [21]. Under conditions of reduced uptake, or of rapid translocation of CH20 or N, these reserves may decline, under which conditions CH20 and N in the model may be transferred from *Cp* and *Np* to the reserves, such that *Ccp,* calculated as Cp/{leaf DM}, and *CNp* also decline. When *Ccp* declines below a threshold value, additional CH20 may be remobilized to Cp from leaf DM of the simulated crop, with accompanying remobilization of leaf N at current leaf *RN,DM o.* This remobilization is intended to allow the model to reproduce the accelerated leaf DM senescence observed under conditions of rapid translocation of CH20 to the grain [39], as may occur during water deficits. Similarly if *CNp* declines below a threshold value of 1.0.10-3g N g-1 DM [41], additional N may be remobilized to *Np* from leaf N. This remobilization is intended to allow the model to reproduce the accelerated loss of leaf N observed under low N fertilization [40]. Up to 67% of leaf N may be remobilized as simulated amino acids with accompanying remobilization of leaf DM at a *RN,DM o* of 16%, Remaining leaf N may be remobilized with leaf DM only at current leaf *RN,DM o* which is much lower, causing accelerated leaf DM senescence. Additional remobilization of leaf DM may occur if the CH20 production of a leaf is insufficient to meet its maintenance respiration requirement over a 24h period, as may occur in the lower canopy layers. Only 25% of leaf DM is recovered as CP during simulated remobilization of leaf DM, while the rest is lost to crop residue on the soil surface. Remobilization of DM and N occurs first in the lower leaves of the simulated canopy, and proceeds upwards. In the model, remobilization of N proceeds in advance of that of DM, as observed experimentally [21].

Leaf photosynthetic capacity is calculated as the product of RuBP carboxylase activity and superficial N density, assuming a constant relationship between RuBP carboxylase and total leaf N. Reductions in leaf *RN,DM o* arising from remobilization of leaf N cause reductions in superficial N density, such that CO 2 fixation [42] and hence Cp is reduced. In this way, a dynamic balance between Cp and *Np* arises within the simulated crop. Within each hourly time step, Eq. 6 is first calculated for root growth, and then for shoot growth, such that the latter is more sensitive to inadequate Np. Under these conditions, *Ccp* and Cp partitioned to the roots increase, such that root : shoot ratios shift in favour of the roots as observed experimentally [21].

# *Experimental technique*

Winter wheat (cv Arminda) was planted at Bouwing (51°57 ' N, 5°45 ' E) on 21 October, 1982 as part of an N fertilizer response study carried out at three sites over two years. Plant density after emergence was 200m -2. Soil characteristics at the site are presented in Table 1. Data for maximum and minimum temperature, global radiation, vapor pressure, windspeed and rainfall were recorded daily. Data for the distribution of carbon, nitrogen and water through the soil-crop system were collected in the field every two to three weeks from February through July 1983, for three fertilizer treatments (Table 2) ranging from 0.0 (N1) to 16.0 (N3) g N m 2. Experimental methods and results are presented by Groot and Verberne [20].

Recorded data for soil, weather and management were used in the model to reproduce the experimental conditions under which the field data were recorded. Because weather data were collected daily, hourly values used in the model were estimated [14]. Model runs were begun on 1 October 1982, and ended on 1 August 1983. A simulated manure application of 750 g DM m -2

| Layer                            | I    | 2    | 3    | 4    | 5    | 6    | 7    |
|----------------------------------|------|------|------|------|------|------|------|
| Depth to bottom (m)              | 0.10 | 0.20 | 0.30 | 0.40 | 0.60 | 0.80 | 1.00 |
| Sand (%)                         | 2.0  | 2.0  | 2.0  | 3.5  | 4.0  | 4.5  | 4.5  |
| Silt (%)                         | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 |
| Clay (%)                         | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 | 35.0 |
| Organic Matter (%)               | 2.8  | 2.8  | 2.8  | 1.4  | 1.4  | 0.7  | 0.0  |
| Saturated conductivity (mm h -z) | 0.28 | 0.28 | 0.28 | 0.28 | 0.10 | 0.10 | 0.10 |
| VWC at 0.03 MPa (m 3 m 3)        | 0.38 | 0.38 | 0.38 | 0.38 | 0.40 | 0.40 | 0.40 |
| VWC at 1.5 MPa (m 3 m -3)        | 0.17 | 0.17 | 0.17 | 0.17 | 0.18 | 0.18 | 0.18 |
| Bulk Density (Mg m -3)           | 1.35 | 1.35 | 1.35 | 1.40 | 1.40 | 1.35 | 1.35 |

*Table 1.* Physical and chemical characteristics of the clay at Bouwing

*Table 2.* Fertilizer treatments (g m -2) at Bouwing. N1 = lowest level, N2 = intermediate level, and N3 = highest level

|           | Date (ddmmyy) |        |       |  |  |  |
|-----------|---------------|--------|-------|--|--|--|
| Treatment | 130583        | 220683 | total |  |  |  |
| N1        | 0             | 0      | 0     |  |  |  |
| N2        | 6.0           | 0      | 6.0   |  |  |  |
| N3        | 12.0          | 4.0    | 16.0  |  |  |  |

was added to the uppermost soil layer on 1 October 1982 to enable apparent mineralization rates for the soil profile that were consistent with those estimated for these soils [31]. Output from the model was studied at two levels of temporal resolution: (1) hourly, to study the behavior of the algorithms for water and nutrient uptake by the simulated root system, and (2) seasonal, to compare the longer term distributions of carbon, nitrogen and water arising from these algorithms in the model with corresponding distributions recorded in the field experiment.

#

No tables found before Methods section.