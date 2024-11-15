rule all:
    input:
        "output_with_sampling_lines.tsv",  # Output from sampling_lines rule
        "sample_rescaled.bed.gz",
        "sample_rescaled.hist",
        "rescale_to_reference.png"

rule normalised_freq:
    input:
        "sample_X_merged.bed.gz"
    output:
        "query_file.tsv"
    shell:
        "zcat {input} | python frequency_calc.py  > {output}" 

rule merge_files:
    input:
        reference="reference.hist",
        query="query_file.tsv"
    output:
        "merged_query_reference.tsv"
    shell:
        """
        join -1 1 -2 1 reference.hist query_file.tsv | \
        awk '{{print $1, $3, $4, $2}}' > {output}
        """

rule calculate_difference:
    input:
        merged="merged_query_reference.tsv"
    output:
        "max_difference.txt"
    shell:
        """
        awk 'NR>1 {{diff=$4-$3; if(NR==2 || diff > max){{max=diff; line=$0;}}}}
        END{{print line > "{output}"}}' {input.merged}
        """

rule sampling_lines:
    input:
        difference="merged_query_reference.tsv",
        max_diff="max_difference.txt"
    output:
        "output_with_sampling_lines.tsv"
    shell:
        """
        max_diff=$(awk '{{print $4}}' {input.max_diff})  
        fragment_count=$(awk '{{print $2}}' {input.max_diff}) 
        awk -v max_diff="$max_diff" -v fragment_count="$fragment_count" 'BEGIN{{OFS="\t"}}
        NR==1{{print $0, "Sampling_Lines"}}
        NR>1{{sampling_lines=int(($4/max_diff) * fragment_count); print $0, sampling_lines}}
        ' {input.difference} > {output}
        """ 

rule subsample:
    input:
        bed="sample_X_merged.bed.gz",
        lines="output_with_sampling_lines.tsv"
    output:
        shuffled=temp("sample_shuffled.bed.gz"),
        rescaled="sample_rescaled.bed.gz"
    shell:
        """
        # Step 1: Shuffle the BED file and gzip the output
        zcat {input.bed} | shuf | gzip > {output.shuffled}
        
        # Step 2: Pass the shuffled BED file to the Python rescaling script
        zcat {output.shuffled} | python rescaling.py | gzip > {output.rescaled}
        """

rule rescaled_hist:
    input:
        "sample_rescaled.bed.gz"
    output:
        "sample_rescaled.hist"
    shell:
        "zcat {input} | python frequency_cal.py | sort -k1,1n > {output}" 
    
rule generate_plot:
    input:
        reference="reference.hist",
        query="query_file.tsv",
        sample_rescaled="sample_rescaled.hist"
    output:
        "rescale_to_reference.png"
    shell:
        """
        python plot_rescale.py {input.reference} {input.query} {input.sample_rescaled} {output}
        """      
