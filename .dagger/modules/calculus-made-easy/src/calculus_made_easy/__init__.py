from __future__ import annotations

from dagger import function, object_type
from dagger_clients.core import Container, Directory, File, Workspace, core


@object_type
class CalculusMadeEasy:
    source: Directory

    @classmethod
    def create(
        cls,
        ws: Workspace,
    ) -> CalculusMadeEasy:
        return cls(
            source=ws.directory(
                "/",
                exclude=[
                    "**/.dagger",
                    "**/.git",
                ],
                gitignore=True,
            ),
        )

    @function
    def container(self) -> Container:
        return (
            core()
            .container()
            .from_("debian:trixie-slim")
            .with_exec(["apt-get", "update"])
            .with_exec(["apt-get", "install", "-y", "--no-install-recommends", "texlive-latex-extra", "latexmk"])
            .with_directory("/src", self.source)
            .with_workdir("/src")
        )

    @function
    def pdf(self) -> File:
        return self.container().with_exec(["latexmk", "-pdf", "calculus-made-easy.tex"]).file("calculus-made-easy.pdf")
