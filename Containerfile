FROM debian:trixie-slim
RUN apt-get update && apt-get install -y --no-install-recommends texlive-latex-extra latexmk
WORKDIR /src
