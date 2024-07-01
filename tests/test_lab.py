# SPDX-License-Identifier: Apache-2.0

# Standard
import re

# Third Party
import click

# First Party
from instructlab import lab
from instructlab.utils import is_macos_with_m_chip


class TestConfig:
    def test_cli_params_hyphenated(self):
        flag_pattern = re.compile("-{1,2}[0-9a-z-]+")
        invalid_flags = []
        for name, cmd in lab.ilab.commands.items():
            for param in cmd.params:
                if not isinstance(param, click.Option):
                    continue
                for opt in param.opts:
                    if not flag_pattern.fullmatch(opt):
                        invalid_flags.append(f"{name} {opt}")
        assert not invalid_flags, "<- these commands are using non-hyphenated params"


def test_llamap_cpp_import():
    # pylint: disable=import-outside-toplevel
    # Third Party
    import llama_cpp

    llama_cpp.llama_backend_init()


def test_import_mlx():
    # smoke test to verify that mlx is always available on Apple Silicon
    # but never on Linux and Intel macOS.
    if is_macos_with_m_chip():
        assert __import__("mlx")
