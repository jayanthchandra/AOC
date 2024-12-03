import polars as pl

df = pl.read_csv("1.txt", separator=' ', has_header=False)
df = df.drop('column_2', 'column_3')
df.head()

# Part 1
sorted_df = df.select(
  pl.col('column_1).sort(), 
  pl.col('column_4).sort()
)

result = sorted_df.select((pl.col('column_1') - pl.col('column_4')).abs().sum())
# part 2
count_df = sorted_df.group_by('column_4').len()
count_df = count_df.rename({"column_4": "column_1"})
joined = sorted_df.join(count_df, on="column_1")
result_part2 = joined.select(
    pl.col('column_1') * pl.col('len')
).sum()
         
