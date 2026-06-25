# Model Assumptions — Lost Decade Natural Cooling Simulation

This document details the assumptions, data sources, and methodological choices underlying the simulation.

---

## 1. Index Normalization

All model dimensions use a **normalized 0–100 index scale**.

- **100** represents a fully functional or maximally healthy state of that system dimension.
- **0** represents complete loss of that function.
- No physical unit conversion is performed.
- Values are illustrative proxies, not direct measurements of global totals.

This normalization is intentional. The goal of the model is causal and structural reasoning, not quantitative prediction in specific physical units.

---

## 2. Time Axis

| Period | Status |
|---|---|
| 2015 – 2025 | Historical / observed direction (calibrated to public data trends) |
| 2025 – 2035 | Projection under each scenario (extrapolation, not a forecast) |

The 2025 boundary is the present year in this simulation. Values prior to 2025 are calibrated against directional public data. Values after 2025 are scenario-based extrapolations.

---

## 3. Scenario Definitions

### Scenario A — Observed / Historical

Represents the trajectory broadly consistent with the past decade of global climate response:

- CO₂-centered policy framework (Paris Agreement targets, NDCs)
- Carbon credit and carbon offset market growth
- Insufficient investment in ecological restoration of natural cooling functions
- Continued forest loss (consistent with FAO/FRA global forest area trends)
- Continued soil degradation (consistent with IPCC AR6 land use reports)
- Continued marine productivity decline in affected zones

Cooling function indexes decline at a rate derived from the general directional consensus of:
- FAO Global Forest Resources Assessment reports
- Global Carbon Budget 2022–2024 land sink anomalies
- IPCC AR6 WG1 and WG2 findings on ecosystem degradation

### Scenario B — CO₂-Centered Mitigation (Stronger)

Adds stronger emission reduction relative to Scenario A, but does not significantly increase ecological cooling function restoration:

- Emission reduction rate ~50% faster than Scenario A
- Carbon credit market grows faster
- Natural cooling function restoration remains at near-Scenario-A levels
- Heat load improvement is limited because physical cooling loss continues

### Scenario C — Natural Cooling Restoration since 2015

Assumes that in 2015, global climate policy had added a second track focused on restoring natural cooling functions:

- Forest restoration programs begin at scale (afforestation, reforestation, avoided deforestation)
- Soil health restoration programs begin (organic matter return, mycorrhizal restoration, reduced chemical pesticide use)
- Water-cycle recovery programs begin (watershed restoration, wetland recovery)
- Evapotranspiration enhancement through vegetation diversity recovery
- Urban cooling programs begin (green roofs, urban tree canopy, permeable surfaces)
- Marine biological support (nutrient runoff reduction, coastal ecosystem restoration)
- Atmospheric and oceanic vertical circulation support through surface temperature modulation

The restoration coefficient applied:
- Begins to reverse the decline in 2015 with a concave recovery curve (faster initial gains, gradual leveling)
- Achieves measurable positive change by 2025
- Continues improving through 2035

### Scenario D — Cooling Credit Pathway since 2015

Builds on Scenario C but adds a financial mechanism that systematically redirects investment:

- A Cooling Credit system is established that rewards **measurable physical cooling**, not only carbon accounting
- Financial incentives shift from pure carbon offset markets to cooling function MRV (Measurement, Reporting, Verification)
- Restoration coefficients for all natural cooling dimensions are approximately 15–20% stronger than in Scenario C
- Cooling Credit intervention index rises from near-zero to high levels by 2025
- Carbon Credit strength remains but is partially displaced by Cooling Credit
- Heat load reduction trajectory is the most favorable of all scenarios

---

## 4. Index Construction

### `natural_cooling_function` (composite)

Computed as the **arithmetic mean** of the following seven indexes at each time step:

```
natural_cooling_function = mean(
    forest_cooling_function,
    soil_microbe_function,
    soil_water_retention,
    evapotranspiration_function,
    ocean_biological_sink,
    vertical_circulation_function,
    water_phase_transition_cooling
)
```

Uniform weighting is used because the relative contribution of each dimension to total planetary cooling is not precisely known and varies by geography and season. Uniform weighting avoids unjustified precision.

### `heat_load_index`

Modeled as an accumulation variable. It increases when natural cooling function is low and CO₂ forcing is high. In Scenario A, it follows a slightly super-linear trend. In Scenarios C and D, restoration of natural cooling functions slows and partially reverses the accumulation trajectory.

The heat load index does not represent absolute ocean heat content in Joules or a specific temperature anomaly in Celsius. It is a structural proxy for the direction of heat accumulation.

### `carbon_sink_capacity`

Represents combined terrestrial and marine carbon absorption capacity. It is influenced by:

- Forest area and condition (terrestrial sink)
- Soil organic matter and microbial activity (terrestrial sink)
- Phytoplankton and marine biological productivity (ocean biological pump)

In Scenario A, it declines directionally consistent with the Global Carbon Budget observations of land sink weakening in certain years and regions.

---

## 5. Data Reference Basis

| Dimension | Reference basis (directional only) |
|---|---|
| Forest cooling function | FAO Global Forest Resources Assessment (2015, 2020, 2025); IPCC AR6 WG2 Ch. 2 |
| Soil microbe function | IPCC AR6 WG1 Ch. 5; Lal (2004) soil carbon literature review direction |
| Ocean biological sink | Global Carbon Budget 2022–2024; Friedlingstein et al. land sink anomaly data direction |
| Carbon sink capacity | Global Carbon Budget 2022–2024 |
| Vertical circulation | IPCC AR6 WG1 Ch. 9 ocean heat content and stratification direction |
| Water phase transition | Trenberth et al. global water cycle review direction |

All values are **directional calibration only**. Precise reproduction of any single dataset's numbers is not the goal.

---

## 6. Interpolation Method

Two interpolation functions are used:

- **`_lerp(start, end, n)`**: Simple linear interpolation. Used for policy intervention variables (Cooling Credit, Carbon Credit).
- **`_smooth_lerp(start, end, n, power)`**: Power-law interpolation with adjustable exponent. Used for ecological system variables.
  - For declining variables (power > 1.0): slightly accelerating decline (consistent with tipping-point risk).
  - For recovering variables (power < 1.0): faster initial recovery slowing over time (consistent with ecological restoration dynamics).

No stochastic noise is applied. The model is deterministic and illustrative.

---

## 7. What the Model Does Not Claim

This model does **not** claim:

- That Cooling Credit alone would have stopped warming.
- Precise temperature outcomes in Celsius.
- Precise carbon accounting in GtC/yr.
- That the specific index values are accurate global measurements.
- That the 10-year scenario divergence is the only possible interpretation.
- That Scenario D is achievable without significant political and economic challenge.

The model is a **conceptual tool** for exploring causal structure and the comparative logic of climate response pathways.

---

## 8. Connection to Global Warming Causal Structure

This simulation operationalizes the causal model described in:

> [Global Warming Causal Structure](https://github.com/InchaComisho/Global-Warming-Causal-Structure)
> [Global Warming Causal Structure — GitHub Pages](https://inchacomisho.github.io/Global-Warming-Causal-Structure/)
> [NOTE Article: Causes and Causal Structure of Global Warming](https://note.com/inchacomusho/n/n5b2102ffc1c2)

The causal hypothesis there is:

```text
Industrial civilization expands
→ Forests are cleared, soils degrade, oceans are polluted
→ Evapotranspiration, microbial activity, phytoplankton decline
→ Natural cooling functions weaken across land, ocean, and atmosphere
→ Vertical circulation weakens
→ Heat stagnates more easily in the Earth system
→ Global warming accelerates
```

This simulation translates that hypothesis into four comparable scenarios with time-series indexes, allowing the "lost decade" cost to be visualized.

---

## 9. Connection to Cooling Credit Definition

Cooling Credit as modeled here corresponds to the definition at:

> [Cooling Credit Definition](https://github.com/InchaComisho/Cooling-Credit-Definition)

A Cooling Credit is a credit unit granted to actions that:

- physically reduce heat loads;
- restore natural cooling functions;
- are measurable through MRV;
- contribute to human, civilizational, and ecological resilience.

In the simulation, the `cooling_credit_intervention` index represents the aggregate strength of such a mechanism across the global economy.

---

## 10. Reproducibility

The simulation is fully reproducible from the Python script:

```bash
python lost_decade_natural_cooling_sim.py
```

All parameters and interpolation functions are defined explicitly in the script. No external data files are required to run the model. The CSV and PNG outputs are generated deterministically.

---

## Author

Master / inchacomusho / InchaComisho

---

## License

CC BY 4.0
