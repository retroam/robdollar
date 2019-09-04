#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `robdollar` package."""


import unittest
from click.testing import CliRunner

from robdollar import cli


class TestRobdollar(unittest.TestCase):
    """Tests for `robdollar` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_load_df(self):
        """Test dataframe load"""

    def test_data_check(self):
        """Test dataframe check"""

    def test_feature_selection(self):
        """Test feature selection"""


    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'robdollar.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
