# calc-made-easy

*Calculus Made Easy* by Silvanus P. Thompson (2nd edition, Macmillan, 1914)

## Building

Requirements:

- [Dagger CLI](https://docs.dagger.io)
- Docker or Podman

From the repo root:

```sh
dagger call calculus-made-easy pdf export --path=out/calculus-made-easy.pdf
```

## Layout

- `calculus-made-easy.tex`: the book
- `images/*.pdf`: figures
- `.dagger/*`: dagger workspace

## License

The book is in the public domain. See `LICENSE`.

My contributions are covered by the AGPL-3.0 in `COPYING`.
