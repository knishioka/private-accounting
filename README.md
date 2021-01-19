# private-accounting
## Overview

Automation scripts for private accounting.

## Build Image

```bash
docker build -t accounting .
```

## Quick Start

```bash
cp .env.sample .env
```

```bash
docker run --rm --env-file=.env -it -v $(pwd):/usr/src/app accounting bash
```
