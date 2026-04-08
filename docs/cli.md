# CLI Reference

Inflion provides a command-line interface for common operations.

## Installation

The CLI is installed automatically with the package:

```bash
pip install inflion
```

Verify installation:

```bash
inflion --version
```

## Commands

### `inflion init`

Initialize a new Inflion database.

```bash
inflion init [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database (default: `inflion.db`)
- `--config PATH` - Path to JSON config file

**Example:**
```bash
inflion init --db myproject.db
```

### `inflion ingest`

Ingest interactions from a JSONL file.

```bash
inflion ingest INPUT_FILE [OPTIONS]
```

**Arguments:**
- `INPUT_FILE` - Path to JSONL file with interactions

**Options:**
- `--db PATH` - Path to SQLite database (default: `inflion.db`)
- `--mock-embedder` - Use mock embedder (no sentence-transformers required)

**Input Format:**
Each line should be a JSON object:
```json
{"sender_id": "agent_a", "receiver_id": "agent_b", "sender_content": "Hello", "receiver_content": "Hi there"}
```

**Example:**
```bash
inflion ingest interactions.jsonl --db myproject.db --mock-embedder
```

### `inflion summary`

Show summary of tracked interactions.

```bash
inflion summary [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database (default: `inflion.db`)
- `--top-n INT` - Number of top agents to show (default: 10)
- `--json` - Output as JSON

**Example:**
```bash
inflion summary --db myproject.db --top-n 5

# JSON output
inflion summary --db myproject.db --json > summary.json
```

### `inflion export`

Export data to CSV or JSONL.

```bash
inflion export [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database (default: `inflion.db`)
- `-o, --output PATH` - Output file path (required)
- `--format [csv|jsonl]` - Export format (default: csv)

**Example:**
```bash
inflion export --db myproject.db -o data.csv --format csv
inflion export --db myproject.db -o data.jsonl --format jsonl
```

### `inflion plot`

Generate visualizations. Requires matplotlib (`pip install inflion[plot]`).

#### `inflion plot drift`

Plot drift over time.

```bash
inflion plot drift [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database
- `-o, --output PATH` - Output image path (required)

**Example:**
```bash
inflion plot drift --db myproject.db -o drift.png
```

#### `inflion plot heatmap`

Plot influence heatmap.

```bash
inflion plot heatmap [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database
- `-o, --output PATH` - Output image path (required)

**Example:**
```bash
inflion plot heatmap --db myproject.db -o heatmap.png
```

#### `inflion plot influencers`

Plot top influencers bar chart.

```bash
inflion plot influencers [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database
- `-o, --output PATH` - Output image path (required)
- `--top-n INT` - Number of top influencers (default: 10)

**Example:**
```bash
inflion plot influencers --db myproject.db -o top.png --top-n 5
```

#### `inflion plot network`

Plot influence network graph.

```bash
inflion plot network [OPTIONS]
```

**Options:**
- `--db PATH` - Path to SQLite database
- `-o, --output PATH` - Output image path (required)
- `--min-weight FLOAT` - Minimum edge weight to display (default: 0.1)

**Example:**
```bash
inflion plot network --db myproject.db -o network.png --min-weight 0.2
```

## Workflow Example

```bash
# 1. Initialize database
inflion init --db analysis.db

# 2. Prepare your interactions file (interactions.jsonl)
# Each line: {"sender_id": "...", "receiver_id": "...", "sender_content": "...", "receiver_content": "..."}

# 3. Ingest data
inflion ingest interactions.jsonl --db analysis.db

# 4. View summary
inflion summary --db analysis.db

# 5. Export for further analysis
inflion export --db analysis.db -o results.csv

# 6. Generate visualizations
inflion plot heatmap --db analysis.db -o heatmap.png
inflion plot network --db analysis.db -o network.png
inflion plot influencers --db analysis.db -o influencers.png
```

## Configuration File

You can use a JSON config file:

```json
{
  "storage_backend": "sqlite",
  "storage_path": "inflion.db",
  "baseline_window": 10,
  "drift_threshold": 0.3,
  "influence_threshold": 0.5
}
```

Use with:
```bash
inflion init --config config.json
```
