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
            .from_("ghcr.io/gorangrbic/calculus-made-easy:latest")
            .with_directory("/src", self.source, owner="tex")
            .with_workdir("/src/book")
        )

    @function
    def pdf(self) -> File:
        return (
            self.container()
            .with_exec(["pdflatex", "calculus-made-easy.tex"])
            .with_exec(["pdflatex", "calculus-made-easy.tex"])
            .with_exec(["pdflatex", "calculus-made-easy.tex"])
            .file("calculus-made-easy.pdf")
        )
