import pandas as pd

# Load the TSV file into a Pandas DataFrame
df = pd.read_csv('/home/jaelliott/MatheisonLab/pg-gan/independent_study_work/population_data/igsr_samples.tsv', sep='\t')
df = df[['Biosample ID', 'Population code']]

print(df.columns)
print(df.head)

# Saving this new and smaller DataFrame to a TSV
df.to_csv('output.tsv', sep='\t', index=False)
