# BINF-3121_Final_Project
---
Ann Loraine and Diego Lopez <br/>
2023-12-09 <br/>
Let's see what the MUTE and SPEECHLESS bait, CATCHES <br/>
---
------------------------------------------------------------------------

## Introduction

This project is a continuation from Ann Loraine findings that two genes
were found to have a correlation coefficient of 0.49 that are required
to form stomata in the leaves of Arabidopsis thaliana plants:

The pair is:

-   [AT5G53210](https://www.arabidopsis.org/servlets/TairObject?name=AT5G53210&type=locus)
    (gene symbol SPEECHLESS)
-   [AT3G06120](https://www.arabidopsis.org/servlets/TairObject?name=AT3G06120&type=locus)
    (gene symbol MUTE)

These genes are involved in the same processes and such genes typically
exhibit similar expression patterns, which enables us to identify other
genes involved the same process.

In this Markdown, we use a large expression data set to answer the
question:

-   Are any more genes involved in stomatal formation and can we
    identify those genes?

Since the two genes have a relativly strong correlation coefficient of
0.49. We can compare expression of MUTE and SPEECHLESS to other genes in
the genome, and identify those genes, if any, that are highly correlated
with both MUTE and SPEECHLESS and therefore would be likely candidates
for genes involved in stomatal formation.

TLDR: This pair of genes should help us find genes are are involved in,
and required for, formation of stomata during leaf development. Let's
find out if it can!

------------------------------------------------------------------------

### About the data

The data were taken from the Gene Expression Omnibus and processed by
Ann Loraine. Data files were downloaded from GEO and re-processed using
algorithms standard in the field.

Data are available from the following publicly accessible URL:

``` {r}
data_file_url = "https://uncc.instructure.com/courses/176579/files/18867927/download"
```

------------------------------------------------------------------------

## Results

Download the data file to our local computer:

``` {r}
fname="expression_data.txt.gz"
if (!file.exists(fname)) {
  download.file(data_file_url,fname,mode="wb")
}
```

Note that on Windows systems, we need `mode` to be set to `wb` to ensure
that the file will be available for reading in the next step.

Read the data file into memory:

``` {r}
df = read.table(fname, header = T, sep = "\t")
```

The data frame contains `r ncol(df)` columns and `r nrow(df)` rows.

Rows are named for Arabidopsis gene names. The column names correspond
to individual samples from the Gene Expression Omnibus. Each row
contains expression values for the gene in that row. This sounds rather
complex, let's try to mine the data.

------------------------------------------------------------------------

## Compute Correlation Coefficients:

Compute Pearson's correlation coefficients between the expression of
MUTE and SPEECHLESS with all other genes in the dataset.
`{r correlation_coefficients_results} # Compute Pearson's correlation coefficients cor_matrix <- cor(df)`
We can now refer to cor_matrix when visualizing the correlation of MUTE
and SPEECHLESS to the rest of the data. \*\*\* \### Visualize
Correlation Coefficients Distribution:

Let's create a histogram showing the distribution of Pearson's
correlation coefficients across all 500 samples.

To begin lets put the genes MUTE and SPEECHLESS into their own
variables.

``` {r}
mute <- "AT3G06120"  
speechless <- "AT5G53210"  
```

Using the gene names we can begin extracting the correlation
coefficients for the genes MUTE and SPEECHLESS from the correlation
matrix.

``` {r}
cor_mute <- cor_matrix[mute, drop = FALSE]
cor_speechless <- cor_matrix[speechless, drop = FALSE]
```

The drop = FALSE argument makes sure that the result is a data frame
instead of a vector.

Finally we can print out the data.

``` {r}
cor_mute
cor_speechless
```

Hmm that doesn't seem to be working...lets try somthing else.

------------------------------------------------------------------------

## Results

Correlation Coefficients The correlation coefficients between MUTE and
other genes, as well as SPEECHLESS and other genes, were computed using
Pearson's correlation method. Here are the results:

We first create the vector for the histogram:
`{r } cor_vector <- as.vector(cor_matrix)`

Now we can declare the histogram like so:
`{r } hist(cor_vector, main = "Distribution of Pearson's Correlation Coefficients",      xlab = "Correlation Coefficient", ylab = "Frequency", col = "red", border = "black", breaks = 40)`

The histogram above shows the distribution of how strongly each gene
correlates with MUTE and SPEECHLESS across all samples. Genes with
higher absolute correlation coefficients indicate stronger correlation
with MUTE or SPEECHLESS.

It appears we have a large amount of strong candidate genes that are
above a 0.5 correlation!

Great that worked! Lets try to isolate those candidate genes...

------------------------------------------------------------------------

## Highly Correlated Genes

Based on the correlation threshold of 0.5, lets try to show which of the
genes are identified as highly correlated with both MUTE and SPEECHLESS:

We'll start by saving the threshold to a variable
`{r } threshold <- 0.5`

Next, we can use the absolute values of both the correlaction
coefficients for the MUTE and SPEECHLESS genes. The absolute value of
the correlation coefficient for the two genes must greater than the
threshold.

We can use greater than (\>) with the and (&) symbols to create the
logic all in one line like so:

`{r } highly_correlated_genes <-names(which(abs(cor_mute) > threshold & abs(cor_speechless) > threshold))`

Now let's print the result!

`{r } highly_correlated_genes`

Well, that didn't work...hmm I wonder what happened?

------------------------------------------------------------------------

## Discussion

The analysis was supposed to identify a set of genes that are highly
correlated with both MUTE and SPEECHLESS but was rather unsuccessful.
Those genes would be potential candidates for further investigation, as
they may play a role in the stomatal.

The next steps in this study would involve exploring the biological
functions of identified candidate genes (if we could have isolated
them), then conducting more experiments to discover their role in
stomatal development.

------------------------------------------------------------------------

## Conclusion

In conclusion, the exploration of gene expression data did reveal many
highly correlated genes with the stomatal formation using the bait genes
MUTE and SPEECHLESS. However, due to a roadblock in my understanding of
how to mine the data, we were unable to produce a subset to continue our
research

-   There is still that can be done to further research and find those
    genes that aid in stomatal development.

-   The use of MUTE and SPEECHLESS as bait genes has proven effective in
    identifying some strong correlation for genes (from the histogram).
    I am sure a different approach could uncover what genes are most
    strongly correlated to the bait genes.
