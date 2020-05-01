# Paper: Efficient Pairwise Annotation of Argument Quality

This is the data and code for the paper Efficient Pairwise Annotation of Argument Quality.

Lukas Gienapp, Benno Stein, Matthias Hagen and Martin Potthast

    @InProceedings{gienapp:2020,
        author =              {Gienapp, Lukas and Stein, Benno and Hagen, Matthias and Potthast, Martin},
        booktitle =           {The 58th annual meeting of the Association for Computational Linguistics (ACL) },
        month =               jul,
        publisher =           {ACL},
        site =                {Seattle, USA},
        title =               {{Efficient Pairwise Annotation of Argument Quality}},
        year =                2020
    }
-----------------------------------------------
## Webis-ArgQuality-20 Corpus
The Webis-ArgQuality-20 corpus consists of two sets of data: a processed version, where for each annotated argument, a scalar value for each argument quality dimension is derived; and the raw annotation data, providing the individual paired comparison labels. The structure of both datasets is described below. 

### [Processed Data](./Webis-ArgQuality-20-Full)
The dataset is split into three different tables. Each key represents a column name, with details about the contained data in the explanation field. Primary keys are marked in **bold**. If a combined key is used, all entries that the combined key is composed of are marked. Foreign keys that can be used to reference other tables are marked in *italics*.
###### Argument Dataset
| Key                 | Explanation                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------|
| ***Topic ID***      | Unique identifier for the topic context the item was judged in                                    |
| **Argument ID**     | Unique identifier for the item in regards to the discussion it is part of                         |
| **Discussion ID**   | Unique identifier of the discussion the item is part of                                           |
| Is Argument?        | Boolean value, indicating wether the item is an argument, or not                                  |
| Stance              | Denotes the stance of the item, can be Pro, Con or Not specified                                  |
| Relevance           | Relevance score, z-normalised  																	  |
| Logical Quality     | Logical quality score, z-normalised     														  |
| Rhetorical Quality  | Rhetorical quality score, z-normalised     														  |
| Dialectical Quality | Dialectical quality score, z-normalised     													  |
| Combined Quality 	  | Combined quality score, z-normalised     													 	  |
| Premise             | Text of the items' premise                                                                        |
| Text Length         | Word Count of the premise                                                                         |

###### Ranking Dataset
| Key               | Explanation                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| ***Topic ID***    | Unique identifier for the topic context                                       |
| **Model**         | Name of the model the ranking this entry stems from was obtained with         |
| **Rank**          | The rank of the argument in the respective engines ranking                    |
| *Argument ID*     | Unique identifier for the argument in regards to the discussion it is part of |
| *Discussion ID*   | Unique identifier of the discussion the argument is part of                   |

###### Topic Dataset
| Key                       | Explanation                                                       |
|---------------------------|-------------------------------------------------------------------|
| ***Topic ID***            | Unique identifier for the topic                                   |
| Category                  | Thematical category the topic belongs to                          |
| Long Query                | Long query, used as input for the retrieval models                |
| Short Query               | Shortened form of the query                						|

### [Raw Data](./Webis-ArgQuality-20-Raw)
Individual comparisons for argument quality are given in a dedicated table each. Relevance annotations are included as well. Each key represents a column name, with details about the contained data in the explanation field. Primary keys are marked in **bold**. If a combined key is used, all entries that the combined key is composed of are marked. Foreign keys that can be used to reference other tables are marked in *italics*.

###### Quality Annotations

| Key                       | Explanation                                                           |
|---------------------------|-----------------------------------------------------------------------|
| ***Argument ID A***       | Unique identifier for argument A in regards to the discussion it is part of |
| ***Discussion ID A***     | Unique identifier of the discussion argument A is part of                   |
| ***Argument ID B***       | Unique identifier for argument B in regards to the discussion it is part of |
| ***Discussion ID B***     | Unique identifier of the discussion argument B is part of                   |
| Comparison                | Denotes the direction of the comparison; can be "A" if argument A is better, "B" if argument B is better, of "Tie", if both arguments are equal.                   |

###### Relevance Annotations
| Key                       | Explanation                                                           |
|---------------------------|-----------------------------------------------------------------------|
| ***Task ID***             | ID of the annotation task this annotation was part of. |
| ***Argument ID***         | Unique identifier for the argument in regards to the discussion it is part of |
| ***Discussion ID***       | Unique identifier of the discussion the argument is part of                   |
| Relevance                 | Denotes the relevance of this argument with regards to the topic on a scale of 0 (low) to 4 (high). -2 is used to mark irrelevant text. |
| Is Argument?              | Boolean value, indicating wether the item is an argument, or not        |

### [Model Implementation](./Webis-ArgQuality-20-Model)
A Python implementation is included. See code comments for additional implementation details. Also, an example describing the usage of the model is given, and can be applied to the `Webis-ArgQuality-20-Raw`data to derive the processed version.
