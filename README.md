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

## Building with podman

```sh
podman build -t calculus-made-easy -f Containerfile .
podman run --rm -v "$PWD":/src calculus-made-easy latexmk -pdf -outdir=out calculus-made-easy.tex
```

## Layout

- `calculus-made-easy.tex`: the book
- `images/*.pdf`: figures
- `.dagger/*`: dagger workspace

## License

The book is in the public domain. See `LICENSE`.

My contributions are covered by the AGPL-3.0 in `COPYING`.
