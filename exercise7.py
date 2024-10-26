from multiprocessing import Pool

def word_count(file_path):

    try:

        with open(file_path, 'r') as file:

            text = file.read()
            word_count = len(text.split())
            return(file_path, word_count)

    except Exception as e:

        return (file_path, f"Error: {str(e)}")

def parallel_word_count(file_paths):

    with Pool() as pool:
        results = pool.map(word_count, file_paths)
        return(dict(results))
