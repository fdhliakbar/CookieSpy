# syntax=docker/dockerfile:1
# Stage 1: build wheels (pure runtime deps only)
FROM python:3.12-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=1
WORKDIR /app

# Only install build tooling (no compilers needed for pure-Python deps)
RUN python -m pip install --upgrade pip wheel build

# Copy minimal metadata first for better cache reuse
COPY pyproject.toml ./
COPY README.md ./

# Copy source
COPY src ./src

# Build app wheel (+ its dependencies) into /wheels
RUN pip wheel -w /wheels .

# Stage 2: minimal runtime
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1
WORKDIR /app

# Create non-root user and ensure writable workdir
RUN useradd -m appuser && chown -R appuser:appuser /app

# Install from prebuilt wheels only
COPY --from=builder /wheels /wheels
RUN python -m pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Drop privileges
USER appuser

EXPOSE 5000

# Run the webapp from installed package
CMD ["python", "-m", "cookiespy.webapp"]