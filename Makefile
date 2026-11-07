.PHONY: test test-unit lint quality-check

test:
	uv run pytest tests/

test-unit:
	uv run pytest tests/unit

lint:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

quality-check:
	uv run pyright
	uv run lint-imports