# Snakemake Workflow: Rescaling and Plotting Histograms

This Snakemake workflow processes genomic fragment data and generates histograms and plots for comparison. The workflow involves calculating normalized fragment frequencies, merging data, calculating differences, and rescaling the data. Finally, it generates a plot comparing the rescaled data with the reference and query data.

## Workflow Overview

The workflow consists of the following steps:
1. **Normalize frequencies** of fragments from a BED file.
2. **Merge** reference and query histograms for comparison.
3. **Calculate differences** between reference and query distributions.
4. **Sample lines** based on the calculated differences.
5. **Rescale** the input data using a subsampling approach.
6. **Generate a plot** comparing reference, query, and rescaled histograms.

### Rules Overview

1. **`normalised_freq`**: Calculates normalized frequencies from the input BED file (`sample_X_merged.bed.gz`) and saves them as `query_file.tsv`.
2. **`merge_files`**: Merges `reference.hist` and `query_file.tsv` into a single file (`merged_query_reference.tsv`).
3. **`calculate_difference`**: Computes the maximum difference between the reference and query distributions and saves the result in `max_difference.txt`.
4. **`sampling_lines`**: Calculates the number of sampling lines for each fragment length and outputs `output_with_sampling_lines.tsv`.
5. **`subsample`**: Shuffles and resamples the input BED file and generates a rescaled version (`sample_rescaled.bed.gz`).
6. **`rescaled_hist`**: Generates a histogram for the rescaled data (`sample_rescaled.hist`).
7. **`generate_plot`**: Uses the `plot_rescale.py` script to generate a plot (`rescale_to_reference.png`) comparing the reference, query, and rescaled histograms.

## How to Run
snakemake -s rescaling_to_reference.smk --cores 1
