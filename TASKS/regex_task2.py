import logging

import pandas as pd
import re

logger = logging.getLogger(__name__)

START_REGEX = r'(\d+\s*\.?\d*)\s'
MID_REGEX = r'(?:x|×|by)\s'
LAST_REGEX = r'(\d+(?:.|,)?\d*\s*)x?\s*(\d\.?\d)?\s'
LL_REGEX = r"(cm|in)\)?\s?(?:$|\()"


def clean_val(dim):
    return float(dim.replace(",", "."))


def main():
    # used single regex for all the strings (Bonus)
    dims_regex = rf"{START_REGEX}*{MID_REGEX}*{LAST_REGEX}*{LL_REGEX}"

    final_df = pd.DataFrame()
    dim_df = pd.read_csv("Data_Engineer_test/candidateEvalData/dim_df_correct.csv")

    for rowIndex, row in dim_df.iterrows():
        unit = 'cm'
        groups = []
        dims = dict()

        for group in re.search(dims_regex, row["rawDim"]).groups():
            if group:
                groups.append(group)

        try:
            dims['height'], dims['width'], unit = clean_val(groups[0]), clean_val(groups[1]), groups[2]
            if len(groups) == 4:
                dims['depth'] = clean_val(groups[2])
                unit = groups[3]
            else:
                dims['depth'] = None  # same as NaN
        except IndexError as er:
            logger.warning(f"Regex not handled for this: {row['rawDim']}")

        # converting h & w to cms
        if "in" in unit:
            dims['height'] = dims['height'] * 2.54
            dims['width'] = dims['width'] * 2.54

        final_df = final_df.append(dims, ignore_index=True)

    print(final_df.head(10))


if __name__ == "__main__":
    main()
