# Installation

## Requirements

- Python 3.10 or higher
- pip

## Basic Installation

Install the core package from PyPI:

```bash
pip install inflion
```

## Installation with Extras

Inflion has optional dependencies for different features:

### Plotting Support

For visualization features (heatmaps, network graphs, charts):

```bash
pip install inflion[plot]
```

### Embedding Support

For real semantic embeddings using sentence-transformers:

```bash
pip install inflion[embedding]
```

### Full Installation

Install everything:

```bash
pip install inflion[all]
```

## Development Installation

For contributing to Inflion:

```bash
git clone https://github.com/Anarv2104/Inflion.git
cd inflion
pip install -e ".[all,dev]"
```

## Verifying Installation

Test your installation:

```python
from inflion import InfluenceTracker, __version__

print(f"Inflion version: {__version__}")

# Quick test
tracker = InfluenceTracker(use_mock_embedder=True)
result = tracker.track_event(
    sender_id="test_sender",
    receiver_id="test_receiver",
    sender_content="Hello world",
    receiver_content="Hello back",
)
print(f"Installation working! Event tracked: {result['event_id']}")
```

Or via CLI:

```bash
inflion --version
```

## Troubleshooting

### sentence-transformers not found

If you see an ImportError about sentence-transformers:

```bash
pip install sentence-transformers
```

Or use the mock embedder for testing:

```python
tracker = InfluenceTracker(use_mock_embedder=True)
```

### matplotlib not found

For plotting features:

```bash
pip install matplotlib
```

### NumPy version conflicts

If you encounter NumPy version issues:

```bash
pip install "numpy<2"
```
