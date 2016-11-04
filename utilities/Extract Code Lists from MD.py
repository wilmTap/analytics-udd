# A slightly hacky Python script to iterate over markdown files in the working directory and extract the
# embedded HTML tables which contain code lists into a single JSON associative array, which is saved to disk.
# This code is dedicated "in the public domain". No rights reserved. No warranties given, etc.
# Created: Adam Cooper, Tribal, July 4th 2016
#

#html5lib should be installed; dependency of pd.read_html
import pandas as pd
import numpy as np
import os
import json

code_lists = {'en':{}, 'cy':{}}

# NB1 the first column MUST be the code and MUST contain a unique name for the code list.
# NB2 English and Welsh description headers must match pattern (below)
# This fails with a ValueError if there are duplicate values in index_col.
file_names = os.listdir(".")
file_names.sort()
for file_name in file_names:
    if file_name.endswith(".md"):
        try:
            df_list = pd.read_html(file_name, header=0)#, index_col=0)
            #hack the col headings
            for df in df_list:
                df.columns = [c.replace('DESCRIPTION', '').lstrip().rstrip().upper().replace('(ENGLISH)', 'en').replace('(WELSH)', 'cy') for c in df.columns.values]
            for df in df_list:
                index_col = df.columns.values[0]
                if index_col == "CODE":
                    raise Exception("Markdown contains a table header containing the word 'CODE' rather than an attribute name in {}".format(file_name))
                #remove NULL as a code and re-type index (pandas forces cols with NA to np.float64)
				# this could be avoided if the UDD doc didn;t include NULL in code list table
                df.dropna(subset=[index_col], inplace=True)
                if df[index_col].dtype == np.float64:
                    df[index_col] = df[index_col].astype(int).astype(str)
                df.set_index(index_col, inplace=True)
                #
                for lang_code in code_lists.keys():
                    if not (lang_code in df.columns.values):
                        raise Exception("Failed to find column for language {} for attribute {} in file {}.".format(lang_code, index_col, file_name))
                    code_lists[lang_code][df.index.name] = json.loads(df[lang_code].T.to_json())
            print "{} processed\n".format(file_name)
        except ValueError as e:
            print "{} not processed due to: {}\n".format(file_name, e)

# output separate language files
for lang_code in code_lists.keys():
    json_filename = 'udd_codelists_{}.json'.format(lang_code)
    with file(json_filename, 'w') as f:
        json.dump(code_lists[lang_code], f)
        print "saved code list:", json_filename

