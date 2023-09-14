def join_two_tables_and_filter(df1, df2, on = None, how = None, filter_cond = None):
    '''
    Explain:
        This Function will join two tables and use a filter condition if available.

    Input:
        df1: Left side of the join. Expect Dataframe.
        df2: Right side of the join. Expect Dataframe.
        on: A condition for the join. Expect condition.
        how: Must be one of inner, cross, outer,full, full_outer, left, left_outer, right, right_outer,left_semi, and left_anti.
        filter_cond: A filtering condition. Expect condition.

    Output: 
        A Dataframe.
    '''

    # Join
    df = df1.join(df2, on, how)

    # Filter
    if filter_cond is not None:
        df = df.filter(filter_cond)

    return df
