from __future__ import annotations

from dagger import function, object_type
from dagger_clients.core import Container, Directory, File, Workspace


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
            self.source
            .docker_build(dockerfile="Containerfile")
            .with_directory("/src", self.source)
        )

    @function
    def pdf(self) -> File:
        return (
            self.container()
            .with_exec(["latexmk", "-pdf", "calculus-made-easy.tex"])
            .file("calculus-made-easy.pdf")
        )
