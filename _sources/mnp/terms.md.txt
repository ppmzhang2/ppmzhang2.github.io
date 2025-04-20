---
title: Terminology
---

# Terminology

This is a non-exhaustive list of terms and acronyms used in papers
{cite}`mnp_alan_2022_s43017_022_00292_`
{cite}`mnp_harb_2023_3c00164_`
{cite}`mnp_leusch_2022_120984_`
on microplastics and nanoplastics (MnP) in the ocean-atmosphere system.

## Microplastic / Nanoplastic

- **MP**: microplastics, particles 1 $\mu m$ to 5 $mm$ in diameter.

- **NP**: nanoplastics, plastic particles smaller than 1 $\mu m$ in diameter.

- **MnP**: micro(nano)plastics, collective term for all particles $\le$ 5 $mm$, including MPs and NPs.

- **Primary MnP**: Intentionally manufactured micro/nano-sized plastics.

- **Secondary MnP**: Plastics formed by degradation of larger items.

## Flux

{#rec-lod}

- **LOD**: Limit of Detection, smallest detectable concentration.

{#rec-loq}

- **LOQ**: Limit of Quantification, smallest quantifiable concentration.

- **SSA**: Sea Spray Aerosol, aerosol particles ejected into the atmosphere when air bubbles formed by breaking waves burst at the ocean surface.

- **SML**: Surface Microlayer, the uppermost ~1000 µm of the ocean surface where floating MNP like PE accumulate.

- **MART**: Marine Aerosol Reference Tank, to simulate SSA production and measure MNP aerosolization.

- $[\text{MNP}]_{\text{air}}$ or $[\text{MNP}]_{\text{water}}$: Airborne or Waterborne MNP Concentration, number of MNP particles per unit volume of air or water

  - Units: particles $m^{-3}$ (alternatively particles $L^{-1}$)

- $U_{10}$: Wind speed at 10 m height, standard reference wind speed used in ocean-atmosphere modeling

  - Units: $m \cdot s^{-1}$

- $E_f$: Emission Factor, empirical coefficient relating water MNP concentration to emission flux

  - Units: $m^{3} \cdot m^{-2} \cdot s^{-1}$
  - Values vary by particle size and type (e.g., $10^{-9} - 10^{-8}$ for typical MnPs)

- $Q$: Volumetric flow rate of incoming or outgoing air

  - Units: $m^3 \cdot s^{-1}$

- $\mathcal{C}$: Particle number concentration of MnP

  - Units: particles $m^{-3}$

- $E$: Emission Rate

  - Definition: Total number of MNP particles emitted per second
  - In the MART setup, the change in concentration of particles in the air over
    time can be written as:

    $$
    \frac{d\mathcal{C}}{dt} =
    Q_{\text{in}} \cdot \mathcal{C}_{\text{in}} -
    Q_{\text{out}} \cdot \mathcal{C}_{\text{out}} + E - L
    $$

    Where:

    - $\mathcal{C}$ = particle concentration in the chamber (air)
    - $Q_{\text{in}}$ = air inflow rate
    - $\mathcal{C}_{\text{in}}$ = particle concentration in inflow air
    - $Q_{\text{out}}$ = air outflow rate
    - $\mathcal{C}_{\text{out}}$ = particle concentration in outflow air
    - $L$ = loss of particles (e.g., deposition on walls; often neglected in basic cases)

  - When steady state is reached, i.e., the particle concentration in the chamber becomes constant over time:

    $$
    \frac{d\mathcal{C}}{dt} = 0
    $$

    Also assume:

    - Clean air inflow: $\mathcal{C}_{\text{in}} = 0$
    - Losses are negligible: $L \approx 0$

    So the mass balance simplifies to:

    $$
    E = Q_{\text{out}} \cdot \mathcal{C}_{\text{out}}
    $$

  - Units: particles $s^{-1}$

- $F$: Emission Flux

  - Definition: Number of MNP particles emitted per unit area per unit time
  - Formula:

    $$
    F(U_{10}, \mathcal{C}) = (3.84 \times 10^{-6} \cdot U_{10}^{-3.41}) \cdot (E_f \cdot \mathcal{C})
    $$

  - Units: particles $m^{-2} \cdot s^{-1}$
  - Note that $3.84 \times 10^{-6} \cdot U_{10}^{-3.41}$ is a **dimensionless coefficient**.

- $AF$: Aerosolization Factor

  - Definition: Ratio of MNP concentration in air to that in water
  - Formula:

    $$
    AF = \frac{[\text{MNP}]_{\text{air}}}{[\text{MNP}]_{\text{water}}}
    $$

  - Dimensionless (ratio of concentrations)

## Aerosol

{#rec-aerosol-mode}

- **Aerosol Size Modes**: grouped log-normal size distributions, each has a characteristic size range and composition:

  - _Nucleation Mode_

    - Diameter < 5 nm
    - Represents the smallest aerosols (e.g., newly formed sulfate particles).
    - No microplastics allowed due to their larger size.

  - _Aitken Mode_

    - Diameter ~5–50 nm
    - Small particles that can grow via condensation/coagulation.
    - Subdivided into soluble and insoluble.

  - _Accumulation Mode_

    - Diameter ~50-250/500 nm
    - Intermediate-size aerosols where particles tend to "accumulate."
    - Important for cloud formation and light scattering.

  - _Coarse Mode_

    - Diameter >250 nm
    - Larger particles that deposit faster.
    - Includes both soluble and insoluble variants.

  - _Super-Coarse Mode_

    - Diameter >2500 nm
    - Largest particles (like microplastic fibres).
    - Only insoluble; no soluble version exists in the model.

{#rec-mnp-particle-types}

- **MnP Particle Types**

  - _Fragment_:

    - Small broken-down pieces of plastic; emitted across all insoluble modes (except nucleation).

  - _Fibre_:

    - Thread-like plastic particles (e.g., from textiles); emitted only into the super-coarse insoluble mode.
    - Currently modeled as spheres, which underrepresents their atmospheric behavior.

{#rec-ccn}

- **CCN**: Cloud Condensation Nuclei

  - Particles that can initiate cloud droplet formation when in the soluble mode and in the presence of supersaturation.

- **AOD**: Aerosol Optical Depth

  - A measure of how much aerosol particles in the atmosphere block or scatter sunlight.

- **CDNC**: Cloud Droplet Number Concentration

  - The number of cloud droplets per unit volume of air, influenced by aerosol concentration and type.

- **Radiative Effects**:

  - The influence of particles on Earth's energy balance via scattering or absorbing radiation.

Back to {doc}`index`.

```{disqus}

```
