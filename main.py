if __name__ == "__main__":
    from __init__ import *
    import numpy as np
    import pandas as pd

    from Util.DGH import DGH

    df = pd.read_csv(FILE_DATA)

    quasi = df[QUASI_FIELDS]
    quasi = quasi.astype(str)

    dgh = {}

    for q in quasi.columns:
        dgh[q] = DGH(DIR_HIERARCHY + q + POSTFIX + FILE_EXTENSION)    

    precision_metric = 0

    if K > quasi.shape[0] :
        print('k must be smaller than length of data!')
    else :
        while quasi.value_counts()[quasi.value_counts() < K].count() > 0:
            quasi_nunique = []
            for c in quasi.columns:
                quasi_nunique.append([c, quasi[c].nunique()])
            quasi_nunique_df = pd.DataFrame(quasi_nunique, columns=['column_name', 'n_unique' ])

            max_column_name = quasi_nunique_df[quasi_nunique_df.n_unique == quasi_nunique_df.n_unique.max()]['column_name'].values[0]

            for v in quasi[max_column_name].unique():
                status, result = dgh[max_column_name].next_gen(str(v))
                quasi.replace(v, result,inplace=True) 
        
        quasi.to_csv(FILE_RESULT,index = False)

    # Calc precision metric
    for c in QUASI_FIELDS:
        prec = quasi[c].apply(lambda v: dgh[c].height(v)/(dgh[c].max_height-1)).sum()
        precision_metric += prec

    precision_metric = 1 - precision_metric/(quasi.shape[0] * quasi.shape[1])
    print(f'precision metric: {precision_metric}')

