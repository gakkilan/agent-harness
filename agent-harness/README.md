# Agent Harness

Standard AI Agent testing and evaluation environment.

## Directory Structure

```
agent-harness/
├── config/              # Configuration files
│   └── opencode.json    # Agent settings
├── tests/               # Test cases
│   ├── unit/           # Unit tests
│   ├── integration/    # Integration tests
│   └── benchmarks/     # Performance benchmarks
├── agents/             # Custom agent definitions
├── fixtures/           # Test data
│   ├── code-samples/   # Code examples
│   └── mock-data/      # Mock data files
├── scripts/            # Utility scripts
│   └── run-tests.sh    # Test runner
└── results/            # Test output
    └── reports/        # Generated reports
```

## Usage

### Run All Tests

```bash
cd agent-harness
./scripts/run-tests.sh
```

### Run Specific Test

```bash
# Unit test
opencode run "$(cat tests/unit/test-code-generation.md)"

# Integration test
opencode run "$(cat tests/integration/test-api-integration.md)"
```

### Add New Test

1. Create markdown file in appropriate directory
2. Follow existing test format
3. Run tests to verify

## Configuration

Edit `config/opencode.json` to customize:
- Model settings
- Agent definitions
- Skill paths
- Tool permissions

## Skills Integration

This harness uses your installed skills from:
`~/.config/opencode/skills/`

Available skills:
- superpowers (14 skills)
- ui-ux-pro-max (7 skills)
- sanyuan-skills (5 skills)
- web-access (1 skill)
- skill-creator (1 skill)

## License

MIT
