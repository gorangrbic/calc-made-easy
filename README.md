# calc-made-easy

*Calculus Made Easy* by Silvanus P. Thompson (2nd edition, Macmillan, 1914)

## Requirements

- [Dagger CLI](https://docs.dagger.io)
- Docker or Podman

## Building with Dagger

From the repo root:

```sh
dagger call calculus-made-easy pdf export --path=out/calculus-made-easy.pdf
```

Testing cold builds requires pruning, so prune with:

```sh
dagger -m core api call engine local-cache prune
```

## Building with podman

Strip `--no-cache` and `> out/run.log 2>&1` when not testing.

```sh
podman build --no-cache --format docker -t calculus-made-easy -f Containerfile .  && \
podman run --rm --userns=keep-id -v "$PWD":/src calculus-made-easy sh -c 'for i in 1 2 3; do pdflatex -output-directory=out calculus-made-easy.tex; done' \
> out/run.log 2>&1
```

## Layout

- `calculus-made-easy.tex`: the book
- `images/*.pdf`: figures
- `.dagger/*`: dagger workspace
- `Containerfile`: Minimal alpine container

## Security

Used Dockle and Hadolint because google told me to:

```sh
podman save -o ./out/tex-live-image.tar localhost/calculus-made-easy:latest

podman run --rm -v "$PWD"/out:/work docker.io/goodwithtech/dockle:latest --input /work/tex-live-image.tar

podman run --rm -i docker.io/hadolint/hadolint < Containerfile
```

## License

The book is in the public domain. See `LICENSE`.

My contributions are covered by the AGPL-3.0 in `COPYING`.
