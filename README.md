# Taxlation

Tax legislation translated into Python code.

## Features

- Tax legislation expressed as executable Python code
- Version management of legislation over time
- Audit trail of how legislation is applied

## Packages

Taxlation is organised as a namespace with separate packages:

| Package          | Description                                       |
|------------------|---------------------------------------------------|
| `taxlation`      | Namespace package                                 |
| `taxlation-core` | Shared functionality used across all countries    |
| `taxlation-nl`   | Tax legislation of the Netherlands                |

Install the package for the country you need; 'taxlation-core' is included automatically as a dependency.

```bash
pip install taxlation-nl
```

```python
import taxlation.nl
```

## Requirements

- Python 3.12 or later
