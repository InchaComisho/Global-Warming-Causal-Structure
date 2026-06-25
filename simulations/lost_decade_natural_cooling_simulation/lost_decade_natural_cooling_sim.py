"""
Lost Decade Natural Cooling Simulation
======================================
Conceptual counterfactual causal simulation.

Compares observed CO2-centered climate response (2015-2025) against
alternative pathways in which global resources were directed toward
restoring and supplementing Earth's natural cooling functions.

This is an index-based, causal, conceptual model — NOT a precise climate forecast.
Indexes are normalized 0-100. Values are illustrative proxies derived from
publicly documented trends (FAO/FRA forest loss, Global Carbon Budget land sink
anomalies, IPCC AR6 observations) scaled to a common index basis.

Scenarios
---------
A  Observed / historical trajectory (CO2-centered, carbon-credit-centered)
B  CO2-centered mitigation (stronger emission reduction, weak cooling restoration)
C  Natural cooling restoration since 2015 (forest, soil, water-cycle, ocean support)
D  Cooling Credit pathway since 2015 (financial redirection toward physical cooling)

Author: Master / inchacomusho / InchaComisho
Repository: https://github.com/InchaComisho/Global-Warming-Causal-Structure
"""

import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
})

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Time axis ─────────────────────────────────────────────────────────────────
YEARS_HIST = np.arange(2015, 2026)          # 2015-2025 (observed)
YEARS_EXT  = np.arange(2015, 2036)          # 2015-2035 (with projection)
N_HIST = len(YEARS_HIST)
N_EXT  = len(YEARS_EXT)

# ── Palette ───────────────────────────────────────────────────────────────────
COLOR = {
    "A": "#D62728",   # red  — observed
    "B": "#FF7F0E",   # orange — CO2 mitigation
    "C": "#2CA02C",   # green — natural cooling restoration
    "D": "#1F77B4",   # blue  — cooling credit pathway
}
LABEL = {
    "A": "A: Observed (CO₂-centered)",
    "B": "B: CO₂ mitigation (stronger)",
    "C": "C: Natural cooling restoration since 2015",
    "D": "D: Cooling Credit pathway since 2015",
}

# ══════════════════════════════════════════════════════════════════════════════
# Index definitions (0-100 normalized, higher = healthier / worse for heat load)
# ══════════════════════════════════════════════════════════════════════════════

def _lerp(start, end, n):
    """Linear interpolation over n steps."""
    return np.linspace(start, end, n)


def _smooth_lerp(start, end, n, power=0.9):
    """Slightly accelerating trend (convex for decline, concave for recovery)."""
    t = np.linspace(0, 1, n)
    t = t ** power
    return start + (end - start) * t


def build_scenario_data(years):
    n = len(years)
    ext = (n == N_EXT)   # True if we're on the extended axis

    # -- Scenario A: observed / historical --
    A = {
        "forest_cooling_function":       _smooth_lerp(78, 62 if not ext else 52, n),
        "soil_microbe_function":         _smooth_lerp(72, 59 if not ext else 48, n),
        "soil_water_retention":          _smooth_lerp(74, 61 if not ext else 50, n),
        "evapotranspiration_function":   _smooth_lerp(76, 63 if not ext else 52, n),
        "ocean_biological_sink":         _smooth_lerp(80, 69 if not ext else 60, n),
        "vertical_circulation_function": _smooth_lerp(82, 72 if not ext else 63, n),
        "water_phase_transition_cooling":_smooth_lerp(77, 64 if not ext else 53, n),
        "carbon_sink_capacity":          _smooth_lerp(75, 60 if not ext else 49, n),
        "heat_load_index":               _smooth_lerp(40, 68 if not ext else 82, n, power=1.1),
        "cooling_credit_intervention":   _lerp(2, 6 if not ext else 8, n),
        "carbon_credit_strength":        _lerp(15, 42 if not ext else 55, n),
    }

    # -- Scenario B: stronger CO2 mitigation, still weak on cooling restoration --
    B = {
        "forest_cooling_function":       _smooth_lerp(78, 64 if not ext else 55, n),
        "soil_microbe_function":         _smooth_lerp(72, 61 if not ext else 51, n),
        "soil_water_retention":          _smooth_lerp(74, 63 if not ext else 53, n),
        "evapotranspiration_function":   _smooth_lerp(76, 65 if not ext else 55, n),
        "ocean_biological_sink":         _smooth_lerp(80, 71 if not ext else 63, n),
        "vertical_circulation_function": _smooth_lerp(82, 74 if not ext else 66, n),
        "water_phase_transition_cooling":_smooth_lerp(77, 66 if not ext else 56, n),
        "carbon_sink_capacity":          _smooth_lerp(75, 63 if not ext else 53, n),
        "heat_load_index":               _smooth_lerp(40, 61 if not ext else 73, n, power=1.05),
        "cooling_credit_intervention":   _lerp(2, 9 if not ext else 12, n),
        "carbon_credit_strength":        _lerp(15, 58 if not ext else 72, n),
    }

    # -- Scenario C: natural cooling restoration since 2015 --
    C = {
        "forest_cooling_function":       _smooth_lerp(78, 84 if not ext else 90, n, power=0.7),
        "soil_microbe_function":         _smooth_lerp(72, 82 if not ext else 90, n, power=0.7),
        "soil_water_retention":          _smooth_lerp(74, 83 if not ext else 91, n, power=0.7),
        "evapotranspiration_function":   _smooth_lerp(76, 85 if not ext else 92, n, power=0.7),
        "ocean_biological_sink":         _smooth_lerp(80, 82 if not ext else 87, n, power=0.8),
        "vertical_circulation_function": _smooth_lerp(82, 85 if not ext else 90, n, power=0.8),
        "water_phase_transition_cooling":_smooth_lerp(77, 85 if not ext else 92, n, power=0.7),
        "carbon_sink_capacity":          _smooth_lerp(75, 86 if not ext else 93, n, power=0.7),
        "heat_load_index":               _smooth_lerp(40, 50 if not ext else 52, n, power=0.8),
        "cooling_credit_intervention":   _lerp(5, 38 if not ext else 55, n),
        "carbon_credit_strength":        _lerp(15, 28 if not ext else 30, n),
    }

    # -- Scenario D: Cooling Credit pathway since 2015 --
    D = {
        "forest_cooling_function":       _smooth_lerp(78, 88 if not ext else 94, n, power=0.65),
        "soil_microbe_function":         _smooth_lerp(72, 88 if not ext else 95, n, power=0.65),
        "soil_water_retention":          _smooth_lerp(74, 89 if not ext else 96, n, power=0.65),
        "evapotranspiration_function":   _smooth_lerp(76, 90 if not ext else 96, n, power=0.65),
        "ocean_biological_sink":         _smooth_lerp(80, 86 if not ext else 92, n, power=0.7),
        "vertical_circulation_function": _smooth_lerp(82, 88 if not ext else 93, n, power=0.7),
        "water_phase_transition_cooling":_smooth_lerp(77, 90 if not ext else 96, n, power=0.65),
        "carbon_sink_capacity":          _smooth_lerp(75, 91 if not ext else 97, n, power=0.65),
        "heat_load_index":               _smooth_lerp(40, 44 if not ext else 43, n, power=0.5),
        "cooling_credit_intervention":   _lerp(5, 70 if not ext else 88, n),
        "carbon_credit_strength":        _lerp(15, 20 if not ext else 18, n),
    }

    # Derive composite natural_cooling_function index
    cooling_dims = [
        "forest_cooling_function",
        "soil_microbe_function",
        "soil_water_retention",
        "evapotranspiration_function",
        "ocean_biological_sink",
        "vertical_circulation_function",
        "water_phase_transition_cooling",
    ]
    for scen in (A, B, C, D):
        scen["natural_cooling_function"] = np.mean(
            [scen[k] for k in cooling_dims], axis=0
        )

    return A, B, C, D


# ── Build data for both time axes ────────────────────────────────────────────
A_h, B_h, C_h, D_h = build_scenario_data(YEARS_HIST)
A_e, B_e, C_e, D_e = build_scenario_data(YEARS_EXT)

SCENARIOS_HIST = {"A": A_h, "B": B_h, "C": C_h, "D": D_h}
SCENARIOS_EXT  = {"A": A_e, "B": B_e, "C": C_e, "D": D_e}

# ══════════════════════════════════════════════════════════════════════════════
# CSV export
# ══════════════════════════════════════════════════════════════════════════════

def export_csv():
    rows = []
    for sc_key, sc_data in SCENARIOS_EXT.items():
        for i, yr in enumerate(YEARS_EXT):
            row = {"year": int(yr), "scenario": sc_key}
            for col, arr in sc_data.items():
                row[col] = round(float(arr[i]), 2)
            rows.append(row)

    df = pd.DataFrame(rows)
    col_order = (
        ["year", "scenario"]
        + [c for c in df.columns if c not in ("year", "scenario")]
    )
    df = df[col_order]
    path = os.path.join(OUTPUT_DIR, "simulation_results.csv")
    df.to_csv(path, index=False)
    print(f"  OK {path}")
    return df


# ══════════════════════════════════════════════════════════════════════════════
# Shared plotting helpers
# ══════════════════════════════════════════════════════════════════════════════

def _base_fig(title, ylabel, ylim=(30, 105)):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_xlim(YEARS_EXT[0] - 0.3, YEARS_EXT[-1] + 0.3)
    ax.set_ylim(*ylim)
    ax.axvline(2025, color="grey", linewidth=1.2, linestyle=":", alpha=0.7)
    ax.text(2025.2, ylim[1] - 4, "2025\n(projection →)", fontsize=8,
            color="grey", va="top")
    return fig, ax


def _add_legend(ax):
    handles = [
        mpatches.Patch(color=COLOR[k], label=LABEL[k]) for k in ("A", "B", "C", "D")
    ]
    ax.legend(handles=handles, fontsize=8.5, loc="best", framealpha=0.85)


def _save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {path}")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 1 — Carbon sink loss index
# ══════════════════════════════════════════════════════════════════════════════

def plot_carbon_sink_loss():
    fig, ax = _base_fig(
        "Carbon Sink Capacity Index  (0–100, higher = stronger sink)",
        "Carbon Sink Capacity Index",
        ylim=(35, 105),
    )
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["carbon_sink_capacity"], color=COLOR[k],
                linewidth=lw, linestyle=ls, label=LABEL[k])
        ax.annotate(
            f"{sc['carbon_sink_capacity'][-1]:.0f}",
            xy=(YEARS_EXT[-1], sc["carbon_sink_capacity"][-1]),
            xytext=(4, 0), textcoords="offset points",
            fontsize=8, color=COLOR[k], va="center",
        )
    ax.fill_between(
        YEARS_EXT,
        SCENARIOS_EXT["A"]["carbon_sink_capacity"],
        SCENARIOS_EXT["D"]["carbon_sink_capacity"],
        alpha=0.08, color=COLOR["D"],
        label="Lost decade gap (A → D)",
    )
    ax.legend(fontsize=8.5, loc="lower left", framealpha=0.85)
    ax.text(
        0.02, 0.05,
        "Note: Proxy index — not a direct measurement of GtC/yr totals.",
        transform=ax.transAxes, fontsize=7.5, color="grey",
    )
    _save(fig, "carbon_sink_loss_index.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 2 — Natural cooling function index
# ══════════════════════════════════════════════════════════════════════════════

def plot_natural_cooling_function():
    fig, ax = _base_fig(
        "Natural Cooling Function Index  (composite, 0–100)",
        "Natural Cooling Function Index",
        ylim=(38, 100),
    )
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["natural_cooling_function"], color=COLOR[k],
                linewidth=lw, linestyle=ls)
        ax.annotate(
            f"{sc['natural_cooling_function'][-1]:.0f}",
            xy=(YEARS_EXT[-1], sc["natural_cooling_function"][-1]),
            xytext=(4, 0), textcoords="offset points",
            fontsize=8, color=COLOR[k], va="center",
        )
    dims_label = (
        "Composite of: forest evapotranspiration · soil microbes · "
        "soil water retention\nevapotranspiration · ocean biological sink · "
        "vertical circulation · water phase transition"
    )
    ax.text(
        0.02, 0.04, dims_label,
        transform=ax.transAxes, fontsize=7, color="grey",
    )
    _add_legend(ax)
    _save(fig, "natural_cooling_function_index.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 3 — Water phase transition cooling index
# ══════════════════════════════════════════════════════════════════════════════

def plot_water_phase_transition():
    fig, ax = _base_fig(
        "Water Phase Transition Cooling Index  (0–100)",
        "Water Phase Transition Cooling Index",
        ylim=(38, 105),
    )
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["water_phase_transition_cooling"],
                color=COLOR[k], linewidth=lw, linestyle=ls)
        ax.annotate(
            f"{sc['water_phase_transition_cooling'][-1]:.0f}",
            xy=(YEARS_EXT[-1], sc["water_phase_transition_cooling"][-1]),
            xytext=(4, 0), textcoords="offset points",
            fontsize=8, color=COLOR[k], va="center",
        )
    ax.text(
        0.02, 0.04,
        "Includes evaporation · condensation · latent heat transfer · "
        "vegetation/soil water exchange.\nProxy index — not a direct W/m² measurement.",
        transform=ax.transAxes, fontsize=7.5, color="grey",
    )
    _add_legend(ax)
    _save(fig, "water_phase_transition_cooling_index.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 4 — Lost decade counterfactual (multi-panel)
# ══════════════════════════════════════════════════════════════════════════════

def plot_lost_decade_counterfactual():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        "Lost Decade Counterfactual  —  What Could Have Been Different (2015–2035)",
        fontsize=13, fontweight="bold", y=1.01,
    )

    # Left: Natural cooling function
    ax = axes[0]
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["natural_cooling_function"],
                color=COLOR[k], linewidth=lw, linestyle=ls, label=LABEL[k])
    ax.fill_between(
        YEARS_EXT,
        SCENARIOS_EXT["A"]["natural_cooling_function"],
        SCENARIOS_EXT["C"]["natural_cooling_function"],
        alpha=0.12, color=COLOR["C"],
    )
    ax.set_title("Natural Cooling Function Index", fontsize=11)
    ax.set_xlabel("Year"); ax.set_ylabel("Index (0–100)")
    ax.set_ylim(38, 100); ax.set_xlim(2014.7, 2035.3)
    ax.axvline(2025, color="grey", linestyle=":", linewidth=1)
    ax.text(2025.15, 40, "2025 →", fontsize=8, color="grey")
    ax.legend(fontsize=8, framealpha=0.85)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Right: Heat load index
    ax = axes[1]
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["heat_load_index"],
                color=COLOR[k], linewidth=lw, linestyle=ls, label=LABEL[k])
    ax.fill_between(
        YEARS_EXT,
        SCENARIOS_EXT["A"]["heat_load_index"],
        SCENARIOS_EXT["D"]["heat_load_index"],
        alpha=0.12, color=COLOR["D"],
    )
    ax.set_title("Heat Load Accumulation Index", fontsize=11)
    ax.set_xlabel("Year"); ax.set_ylabel("Index (0–100, higher = more heat stored)")
    ax.set_ylim(30, 95); ax.set_xlim(2014.7, 2035.3)
    ax.axvline(2025, color="grey", linestyle=":", linewidth=1)
    ax.text(2025.15, 88, "2025 →", fontsize=8, color="grey")
    ax.legend(fontsize=8, framealpha=0.85)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Gap annotation on right panel
    y_a = SCENARIOS_EXT["A"]["heat_load_index"][-1]
    y_d = SCENARIOS_EXT["D"]["heat_load_index"][-1]
    ax.annotate(
        "", xy=(2034.5, y_d), xytext=(2034.5, y_a),
        arrowprops=dict(arrowstyle="<->", color="purple", lw=1.5),
    )
    ax.text(2034.7, (y_a + y_d) / 2, f"Gap\n{y_a - y_d:.0f} pts",
            fontsize=8, color="purple", va="center")

    fig.tight_layout()
    _save(fig, "lost_decade_counterfactual.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 5 — Carbon Credit vs Cooling Credit
# ══════════════════════════════════════════════════════════════════════════════

def plot_carbon_vs_cooling_credit():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    fig.suptitle(
        "Carbon Credit vs. Cooling Credit — Policy Intervention Strength (2015–2035)",
        fontsize=12, fontweight="bold",
    )

    ax = axes[0]
    ax.set_title("Carbon Credit Strength", fontsize=11)
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k == "B" else 1.8
        ls = "-" if k == "B" else "--"
        ax.plot(YEARS_EXT, sc["carbon_credit_strength"],
                color=COLOR[k], linewidth=lw, linestyle=ls, label=LABEL[k])
    ax.set_xlabel("Year"); ax.set_ylabel("Index (0–100)")
    ax.set_ylim(0, 100); ax.set_xlim(2014.7, 2035.3)
    ax.axvline(2025, color="grey", linestyle=":", linewidth=1)
    ax.legend(fontsize=8, framealpha=0.85)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.text(0.02, 0.96,
            "Carbon Credit: values CO₂ accounting.\nDoes not directly reduce heat load.",
            transform=ax.transAxes, fontsize=8, va="top", color="grey")

    ax = axes[1]
    ax.set_title("Cooling Credit Intervention Strength", fontsize=11)
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.5 if k in ("C", "D") else 1.8
        ls = "-" if k in ("C", "D") else "--"
        ax.plot(YEARS_EXT, sc["cooling_credit_intervention"],
                color=COLOR[k], linewidth=lw, linestyle=ls, label=LABEL[k])
    ax.set_xlabel("Year"); ax.set_ylabel("Index (0–100)")
    ax.set_ylim(0, 100); ax.set_xlim(2014.7, 2035.3)
    ax.axvline(2025, color="grey", linestyle=":", linewidth=1)
    ax.legend(fontsize=8, framealpha=0.85)
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.text(0.02, 0.96,
            "Cooling Credit: rewards measurable physical cooling,\n"
            "water-cycle recovery, soil, forest, marine support.",
            transform=ax.transAxes, fontsize=8, va="top", color="#1F77B4")

    fig.tight_layout()
    _save(fig, "carbon_credit_vs_cooling_credit.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 6 — Heat load gap (detailed)
# ══════════════════════════════════════════════════════════════════════════════

def plot_heat_load_gap():
    fig, ax = _base_fig(
        "Heat Load Accumulation Index  —  Scenario Divergence (2015–2035)",
        "Heat Load Index  (0–100, higher = more accumulated heat)",
        ylim=(28, 98),
    )
    for k, sc in SCENARIOS_EXT.items():
        lw = 2.8 if k in ("A", "D") else 1.8
        ls = "-"
        ax.plot(YEARS_EXT, sc["heat_load_index"],
                color=COLOR[k], linewidth=lw, linestyle=ls, label=LABEL[k])
        ax.annotate(
            f"{sc['heat_load_index'][-1]:.0f}",
            xy=(YEARS_EXT[-1], sc["heat_load_index"][-1]),
            xytext=(4, 0), textcoords="offset points",
            fontsize=8.5, color=COLOR[k], va="center", fontweight="bold",
        )

    # Shade A–D gap
    ax.fill_between(
        YEARS_EXT,
        SCENARIOS_EXT["A"]["heat_load_index"],
        SCENARIOS_EXT["D"]["heat_load_index"],
        alpha=0.1, color="#8B0000", label="Heat load gap (A − D)",
    )

    # Annotate at 2025
    for k in ("A", "D"):
        val = float(np.interp(2025, YEARS_EXT, SCENARIOS_EXT[k]["heat_load_index"]))
        ax.scatter([2025], [val], color=COLOR[k], zorder=5, s=60)
        ax.annotate(
            f"{val:.0f} (2025)",
            xy=(2025, val), xytext=(-55 if k == "A" else 5, 6),
            textcoords="offset points",
            fontsize=8, color=COLOR[k],
            arrowprops=dict(arrowstyle="->", color=COLOR[k], lw=0.8),
        )

    ax.legend(fontsize=8.5, loc="upper left", framealpha=0.85)
    ax.text(
        0.02, 0.04,
        "Higher index = more heat retained in Earth system.\n"
        "Scenario D (Cooling Credit) shows lowest accumulation trajectory.",
        transform=ax.transAxes, fontsize=7.5, color="grey",
    )
    _save(fig, "heat_load_gap.png")


# ══════════════════════════════════════════════════════════════════════════════
# Plot 7 — Causal feedback loop diagram
# ══════════════════════════════════════════════════════════════════════════════

def plot_causal_feedback_loop():
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 13); ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_facecolor("#FAFAFA")
    fig.patch.set_facecolor("#FAFAFA")

    ax.set_title(
        "Causal Feedback Loop — Natural Cooling Function Degradation and Heat Load Spiral",
        fontsize=12, fontweight="bold", pad=16,
    )

    # Node definitions: (x_center, y_center, label, color)
    nodes = [
        (6.5, 8.2,  "Industrial civilization\n& land use change",      "#555555"),
        (2.0, 6.8,  "Forest loss\n& deforestation",                    "#8B4513"),
        (4.2, 5.2,  "Evapotranspiration\n& latent heat loss",          "#228B22"),
        (2.0, 3.6,  "Soil microbe\n& water retention loss",            "#A0522D"),
        (6.5, 6.2,  "CO₂ & GHG\naccumulation",                        "#B22222"),
        (10.5, 6.8, "Ocean biological\n& phytoplankton decline",       "#00688B"),
        (9.0, 5.0,  "Vertical circulation\n& heat distribution loss",  "#4169E1"),
        (6.5, 3.8,  "Water phase transition\ncooling decline",         "#2196F3"),
        (6.5, 2.2,  "Natural cooling\nfunction weakens",               "#E65100"),
        (6.5, 0.8,  "Heat load\naccumulates",                          "#C62828"),
    ]

    box_style = dict(boxstyle="round,pad=0.35", linewidth=1.2)

    node_pos = {}
    for (x, y, lbl, col) in nodes:
        node_pos[lbl] = (x, y)
        fc = col + "22"  # light fill
        bbox = FancyBboxPatch(
            (x - 1.15, y - 0.42), 2.3, 0.84,
            boxstyle="round,pad=0.1", linewidth=1.5,
            edgecolor=col, facecolor=fc, zorder=3,
        )
        ax.add_patch(bbox)
        ax.text(x, y, lbl, ha="center", va="center", fontsize=8,
                fontweight="bold", color=col, zorder=4)

    # Arrows: (from_label, to_label, label_text)
    edges = [
        ("Industrial civilization\n& land use change", "Forest loss\n& deforestation", ""),
        ("Industrial civilization\n& land use change", "CO₂ & GHG\naccumulation", ""),
        ("Industrial civilization\n& land use change", "Ocean biological\n& phytoplankton decline", ""),
        ("Forest loss\n& deforestation", "Evapotranspiration\n& latent heat loss", "↓ cooling"),
        ("Forest loss\n& deforestation", "Soil microbe\n& water retention loss", ""),
        ("Evapotranspiration\n& latent heat loss", "Water phase transition\ncooling decline", ""),
        ("Soil microbe\n& water retention loss", "Water phase transition\ncooling decline", ""),
        ("CO₂ & GHG\naccumulation", "Natural cooling\nfunction weakens", "radiative forcing"),
        ("Ocean biological\n& phytoplankton decline", "Vertical circulation\n& heat distribution loss", ""),
        ("Vertical circulation\n& heat distribution loss", "Water phase transition\ncooling decline", ""),
        ("Water phase transition\ncooling decline", "Natural cooling\nfunction weakens", ""),
        ("Natural cooling\nfunction weakens", "Heat load\naccumulates", "↑ heat retained"),
        ("Heat load\naccumulates", "CO₂ & GHG\naccumulation", "feedback\n(permafrost, ocean)"),
    ]

    def node_center(lbl):
        return node_pos[lbl]

    for (src, dst, elbl) in edges:
        x0, y0 = node_center(src)
        x1, y1 = node_center(dst)
        # Offset slightly from box edges
        dx = x1 - x0; dy = y1 - y0
        norm = max((dx**2 + dy**2) ** 0.5, 0.01)
        shrink = 0.48
        xs = x0 + shrink * dx / norm
        ys = y0 + shrink * dy / norm
        xe = x1 - shrink * dx / norm
        ye = y1 - shrink * dy / norm

        ax.annotate(
            "",
            xy=(xe, ye), xytext=(xs, ys),
            arrowprops=dict(
                arrowstyle="-|>",
                color="#666666",
                lw=1.3,
                connectionstyle="arc3,rad=0.07",
            ),
            zorder=2,
        )
        if elbl:
            mx, my = (xs + xe) / 2, (ys + ye) / 2
            ax.text(mx, my, elbl, fontsize=7, color="#444444",
                    ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.1", fc="white", alpha=0.7, lw=0))

    # Legend / annotation box
    legend_text = (
        "Cooling Credit intervention targets the orange/blue nodes:\n"
        "  → Forest, soil, evapotranspiration, water cycle, marine support\n"
        "  → Directly opposes heat load accumulation\n"
        "Carbon Credit targets only the red CO₂ node."
    )
    ax.text(
        0.01, 0.01, legend_text,
        transform=ax.transAxes, fontsize=8, va="bottom",
        bbox=dict(boxstyle="round", fc="#F0F8FF", ec="#1F77B4", alpha=0.9),
    )

    fig.tight_layout()
    _save(fig, "causal_feedback_loop.png")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print("\nLost Decade Natural Cooling Simulation")
    print("=" * 50)
    print("Generating outputs...\n")

    print("[1/8] Exporting CSV results...")
    export_csv()

    print("[2/8] Carbon sink loss index...")
    plot_carbon_sink_loss()

    print("[3/8] Natural cooling function index...")
    plot_natural_cooling_function()

    print("[4/8] Water phase transition cooling index...")
    plot_water_phase_transition()

    print("[5/8] Lost decade counterfactual...")
    plot_lost_decade_counterfactual()

    print("[6/8] Carbon Credit vs Cooling Credit...")
    plot_carbon_vs_cooling_credit()

    print("[7/8] Heat load gap...")
    plot_heat_load_gap()

    print("[8/8] Causal feedback loop diagram...")
    plot_causal_feedback_loop()

    print("\nAll outputs written to:", OUTPUT_DIR)
    print("\nNOTE: This is a conceptual counterfactual simulation.")
    print("Indexes are illustrative proxies, not measured global totals.")


if __name__ == "__main__":
    main()
