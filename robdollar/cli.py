# -*- coding: utf-8 -*-

"""Console script for robdollar."""

import click
from robdollar import FeatureSelect


@click.command()
@click.option('--verbose', is_flag=True,
              help="Print results to stdout")
@click.option('--path', default='./',
              help="Output file destination")
@click.argument('file', type=click.Path(exists=True))
@click.argument('target', type=str)
def main(verbose, path, target, file):
    """Console script for robdollar."""

    try:
        target = int(target)  # check if columns are integers
    except ValueError:
        pass

    features = FeatureSelect(file, target)

    try:
        features.load_csv()
    except ImportError:
        click.echo("Change seperator to pipe delimited in file")

    features.feature_selection()
    selected_features = features.selected_features
    if len(selected_features) != 0:
        features.df[selected_features].to_csv(path + 'output')

    if verbose:
        click.echo("\nData Quality Report")
        click.echo("---------------------------------------------------------------------")
        click.echo("Total records: {}".format(len(features.df.index)))
        click.echo(features.data_check().sort_values(['unique'], ascending=True).head(10))
        click.echo("\n")
        click.echo("Selected features")
        click.echo("---------------------------------------------------------------------")

        click.echo(features.selected_features)


if __name__ == "__main__":
    main()
