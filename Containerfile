FROM alpine:3.24.4 AS builder
RUN apk upgrade --no-cache && apk add --no-cache perl=5.42.3-r0 wget=1.25.0-r3 ca-certificates=20261020-r0 gnupg=2.4.9-r1
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN mkdir /tmp/install-tl \
 && wget -qO- https://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz | tar xz -C /tmp/install-tl --strip-components=1 \
 && /tmp/install-tl/install-tl --repository=https://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet --scheme=infraonly --texdir=/opt/texlive --no-doc-install --no-src-install --no-interaction
ENV PATH=/opt/texlive/bin/x86_64-linuxmusl:$PATH
RUN tlmgr install latex-bin amsmath amsfonts tools graphics footmisc bigfoot wrapfig fancyhdr geometry hyperref etoolbox ec cm-super tex4ebook luaxml extractbb

FROM alpine:3.24.4
COPY --from=builder /opt/texlive /opt/texlive
ENV PATH=/opt/texlive/bin/x86_64-linuxmusl:$PATH
RUN apk add --no-cache ghostscript=10.08.0-r0 zip=3.0-r13 && adduser -D tex
USER 1000
WORKDIR /src
