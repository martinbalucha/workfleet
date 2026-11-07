.PHONY: test test-unit lint typecheck

test:
	uv run pytest tests/

test-unit:
	uv run pytest tests/unit

lint:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

typecheck:
	uv run pyright