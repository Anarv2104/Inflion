<p align="center">
  <img src="https://img.shields.io/badge/Inflion-AI%20Influence%20Measurement-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyek0xMiAyMGMtNC40MSAwLTgtMy41OS04LThzMy41OS04IDgtOCA4IDMuNTkgOCA4LTMuNTkgOC04IDh6Ii8+PC9zdmc+" alt="Inflion">
</p>

<h1 align="center">Inflion</h1>

> **Note:** This project was previously released as **TraceIQ**. It has been renamed to **Inflion** starting with `v0.1.0`. The API and behavior are unchanged.

<p align="center">
  <strong>
Inflion is a Python library for measuring cross-agent influence in multi-agent AI systems,
providing reproducible metrics for semantic drift, propagation risk, and reasoning stability.
</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/inflion/"><img src="https://img.shields.io/pypi/v/inflion.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/inflion/"><img src="https://img.shields.io/pypi/pyversions/inflion.svg" alt="Python versions"></a>
  <a href="https://pypi.org/project/inflion/"><img src="https://img.shields.io/pypi/l/inflion.svg" alt="License"></a>
  <a href="https://pepy.tech/project/inflion"><img src="https://static.pepy.tech/badge/inflion" alt="Downloads"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-example">Quick Start</a> •
  <a href="#scientific-contributions">Science</a> •
  <a href="#documentation">Docs</a> •
  <a href="#citation">Cite</a>
</p>

---

## The Problem

Modern AI systems increasingly operate through interaction: agents collaborate, critique, retrieve, plan, and self-modify through communication with other agents.

Yet we lack scientific tools to answer fundamental questions:

> - **How much did one agent influence another?**
> - **Did incorrect reasoning propagate through the system?**
> - **When does collaboration become instability?**
> - **How can influence be measured reproducibly and rigorously?**

**Inflion** introduces a formal measurement framework for studying influence propagation in autonomous multi-agent AI systems.

---

## Scientific Contributions

Inflion provides three core measurement primitives:

### 1. Influence Quotient (IQx)

A quantitative metric measuring **semantic drift** in an agent's output caused by prior agent messages.

```
IQx = Drift_L2 / (Baseline_Median + ε)
```

IQx estimates how much reasoning changed due to interaction, enabling measurement of cross-agent cognitive influence.

### 2. Propagation Risk (PR)

A network-level metric estimating how influence spreads across an agent graph using **spectral radius analysis**.

```
PR = max(|eigenvalues(Adjacency_Matrix)|)
```

PR provides early detection of unstable influence propagation and cascading reasoning errors.

### 3. Reproducible Influence Experiments

Inflion includes CI-safe experimental pipelines evaluating:

- ✓ Hint injection and misinformation propagation
- ✓ Influence stability across agent chains
- ✓ Cold-start detection behavior
- ✓ Mitigation policy effectiveness

These experiments support ongoing research into multi-agent AI safety and **Contagious Intelligence**.

---

## Where Inflion Fits in AI Research

Modern AI tooling focuses on different layers of the stack:

| Tool | What It Measures |
|------|------------------|
| **TensorBoard** | Model training metrics |
| **Weights & Biases** | Experiment tracking |
| **LangSmith / Prompt tools** | Prompt execution traces |
| **Inflion** | Cross-agent influence and reasoning propagation |

Inflion introduces a missing instrumentation layer:
**measurement of cognitive influence between autonomous AI agents.**

As multi-agent systems become standard in RAG, planning, robotics, and orchestration,
understanding *how agents influence each other* becomes as critical as measuring accuracy.

---

## Why Inflion Exists

Autonomous AI systems are evolving from isolated models into **collaborative agent networks**.

However, we currently lack standardized methods to measure:

| Challenge | Description |
|-----------|-------------|
| **Cross-agent reasoning influence** | How does one agent's output change another's behavior? |
| **Error propagation** | Do mistakes cascade through agent pipelines? |
| **Stability** | Is collaborative reasoning stable or chaotic? |
| **Safety risks** | What are the emergent risks in multi-agent systems? |

Inflion was built as a **scientific instrument** for studying emergent behavior in distributed intelligence.

> **Inflion is not a dashboard. It is not a monitoring SaaS.**
>
> Inflion is **measurement infrastructure** for multi-agent cognition research.

---

## Research Vision

Inflion is measurement infrastructure for multi-agent AI systems.

As AI shifts from isolated models to collaborative agent networks, system behavior emerges from interactions between models—not from a single model alone. While we can measure accuracy, latency, and loss, we currently lack tools to quantify how reasoning propagates across agents.

Inflion provides reproducible metrics and structured tracking for cross-agent influence, reasoning drift, and propagation dynamics. The goal is not monitoring dashboards, but scientific instrumentation for studying distributed AI cognition.

If collaborative AI becomes the dominant computing paradigm, measuring influence between agents will be as fundamental as measuring model performance.

---

## Features

| Feature | Description |
|---------|-------------|
| 📊 **Influence Tracking** | Track influence between agent interactions |
| 🎯 **Semantic Drift** | Measure drift using embedding similarity |
| 🌐 **Propagation Risk** | Estimate network-level influence spread |
| ⚡ **Anomaly Detection** | Quantile-calibrated alerting system |
| 🧊 **Cold-Start Handling** | Statistical validation during warm-up |
| 🔬 **Research Pipelines** | CI-safe reproducible experiments |
| 🔌 **Integration Ready** | Templates for RAG and multi-agent orchestration |

---

## Installation

**Core library** (lightweight, no heavy ML dependencies):

```bash
pip install inflion
```

**With real embedding models:**

```bash
pip install "inflion[embedding]"
```

**With research plotting tools:**

```bash
pip install "inflion[research]"
```

**Full installation:**

```bash
pip install "inflion[embedding,research]"
```

---

## Real-World Use Cases

Inflion is designed for real multi-agent AI systems:

- **Evaluate RAG hallucination propagation**
  Measure whether incorrect retrieval contaminates downstream reasoning.

- **Audit autonomous agent pipelines**
  Track which agents influence critical decisions in planning systems.

- **Study collaborative reasoning stability**
  Detect when agent feedback loops amplify errors.

- **AI governance and accountability**
  Build audit trails showing how decisions evolved across agents.

- **Research on Contagious Intelligence**
  Quantify cognitive transfer between AI systems in controlled experiments.

Inflion acts as a **measurement microscope** for studying distributed AI cognition.

---

## Quick Example

```python
from inflion import InfluenceTracker

tracker = InfluenceTracker(use_mock_embedder=True)

result = tracker.track_event(
    sender_id="agent_a",
    receiver_id="agent_b",
    sender_content="We should switch to renewable energy.",
    receiver_content="Good point. Renewables are the future."
)

print("Drift:", result["drift_l2_state"])
print("IQx:", result["IQx"])
print("Alert:", result["alert"])

tracker.close()
```

**Output:**
```
Drift: 0.847
IQx: 1.23
Alert: False
```

---

## What Inflion Outputs

Each tracked interaction returns structured metrics you can log, visualize, or audit:

- `drift_l2_state` — semantic drift magnitude
- `IQx` — normalized influence score
- `alert` — anomaly signal (calibrated)
- `valid` — whether baseline is stabilized
- `receiver_state` — receiver baseline summary

---

## Research Applications

Inflion has been evaluated on synthetic multi-agent benchmarks
and integrated into experimental LLM pipelines involving chained,
retrieval-augmented, and tool-using agents.

The framework enables reproducible studies of:

- Influence propagation across agent graphs
- Stability of collaborative reasoning loops
- Detection of misleading hint injection
- Mitigation policy effectiveness
- Cold-start behavior in autonomous agents

All experiments are reproducible through CI-safe pipelines
that generate structured `summary.json` artifacts for verification.

---

## Integration Patterns

Inflion works with common agent architectures:

| Pattern | Description |
|---------|-------------|
| **LLM-only agents** | Track message → response influence |
| **RAG systems** | Include retrieved context in receiver input |
| **Tool-using agents** | Track tool output influence |
| **Memory agents** | Track before/after memory state |
| **Multi-agent orchestrators** | Full conversation influence graphs |

---

## What Inflion Is NOT

| Limitation | Explanation |
|------------|-------------|
| **Not causal inference** | Metrics measure correlation, not proven causation |
| **Not intent detection** | Cannot determine manipulation intent |
| **Not semantic understanding** | Measures embedding-level drift |
| **Not a production security system** | Research measurement tool |
| **Not plug-and-play safety** | Thresholds require calibration per environment |

---

## Research Context

Inflion supports research into:

- 🔬 AI-to-AI influence modeling
- 🧬 Contagious Intelligence hypothesis
- ⚖️ Multi-agent reasoning stability
- 🛡️ Autonomous system safety
- 🧠 Distributed cognition in AI systems

Detailed metric definitions and implementation notes
are available in the project documentation.

---

## Documentation

| Document | Description |
|----------|-------------|
| [Metrics](https://github.com/Anarv2104/Inflion/blob/main/docs/metrics.md) | Metric definitions and formulas |
| [Integration](https://github.com/Anarv2104/Inflion/blob/main/docs/integration.md) | Integration patterns |
| [CLI Reference](https://github.com/Anarv2104/Inflion/blob/main/docs/cli.md) | Command-line interface |
| [Configuration](https://github.com/Anarv2104/Inflion/blob/main/docs/configuration.md) | TrackerConfig options |
| [Architecture](https://github.com/Anarv2104/Inflion/blob/main/docs/architecture.md) | System design |
| [Theory](https://github.com/Anarv2104/Inflion/blob/main/docs/THEORY.md) | Mathematical foundations |
| [Experiments](https://github.com/Anarv2104/Inflion/tree/main/experiments) | Research testbed |

**CLI Help:** `inflion --help`

---

## Reproducibility & CI

Inflion experiments are **CI-safe**:

- ✅ Quick mode never hard-fails CI
- ✅ Proof mode enforces strict statistical validation
- ✅ Artifacts upload even on failures
- ✅ Experiments produce structured outputs

This ensures reproducible research pipelines.

---

## Contributing

Contributions welcome! See
[CONTRIBUTING.md](https://github.com/Anarv2104/Inflion/blob/main/CONTRIBUTING.md)

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/amazing-feature

# 3. Run tests and linter
pytest
ruff check src/ tests/

# 4. Submit a Pull Request
```

---

## Citation

If you use Inflion in your research, please cite:

```bibtex
@software{inflion,
  title = {Inflion: Measuring AI-to-AI Influence in Multi-Agent Systems},
  author = {Vasavada, Anarv and Contributors},
  year = {2026},
  url = {https://github.com/Anarv2104/Inflion}
}
```

---

## License

Inflion is open-source under the MIT License, enabling academic and commercial use with minimal restrictions.

See the full license text at:
https://github.com/Anarv2104/Inflion/blob/main/LICENSE

---

<p align="center">
  <a href="https://github.com/Anarv2104/Inflion">
    <img src="https://img.shields.io/badge/GitHub-Source%20Code-24292e?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://pypi.org/project/inflion/">
    <img src="https://img.shields.io/badge/PyPI-Install%20Package-3776AB?style=for-the-badge&logo=pypi&logoColor=white">
  </a>
  <a href="https://github.com/Anarv2104/Inflion/tree/main/docs">
    <img src="https://img.shields.io/badge/Docs-Technical%20Documentation-6A0DAD?style=for-the-badge&logo=readthedocs&logoColor=white">
  </a>
  <a href="https://github.com/Anarv2104/Inflion/issues">
    <img src="https://img.shields.io/badge/Community-Report%20Issues-D73A49?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>
