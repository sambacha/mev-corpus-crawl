# -*- coding:utf-8 -*-
import os

exception = []
for folder in os.listdir("./"):
    if folder.startswith("0x"):
        file_path = "./" + folder + "/function_normalized_tokens"
        # file_path = './' + folder + '/statement_normalized_tokens'
        # file_path = './' + folder + '/contract_normalized_tokens'
        if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
            exception.append(folder)
            print folder
        else:
            continue

print len(exception)

"""
for folder in os.listdir('./'):
    if folder.startswith('0x'):
        print folder
        for fname in os.listdir('./' + folder + '/'):
            # print fname
            current_dir = './' + str(folder) + '/'
            if fname.startswith('source_tokens'):
                os.rename(current_dir + fname, current_dir + 'contract_tokens' )
            elif fname.startswith('normalized_tokens'):
                os.rename(current_dir + fname, current_dir + 'contract_normalized_tokens' )
            elif fname.startswith('statement_tokens_context'):
                os.rename(current_dir + fname, current_dir + 'statement_tokens' )
            elif fname.startswith('statement_context_normalized_tokens'):
                os.rename(current_dir + fname, current_dir + 'statement_normalized_tokens' )
    # break
"""
